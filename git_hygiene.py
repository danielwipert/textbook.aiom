#!/usr/bin/env python3
"""
git_hygiene.py  |  is any work stranded, and is the tree fit to hand over?

Written 2026-08-12, after four sessions worked Chapter 1 in three days without
seeing each other and produced three disagreeing records of one chapter. The
cost was a whole session of file management instead of drafting. This script
exists so that never costs a session again.

Run it BEFORE any merge and BEFORE closing a session. It answers one question:
is there work anywhere that `main` does not have?

WHY A HAND-ROLLED SWEEP IS NOT ENOUGH, and the reason this is a script rather
than a snippet in HANDOFF.md. The container clones with `fetch --depth 50`. In a
shallow clone the common ancestor of an older branch is BEYOND THE BOUNDARY, so
`git merge-base` fails and `git rev-list origin/main..<branch>` counts the
branch's ENTIRE history instead of its unmerged part. On 2026-08-12 that made
seven dead branches look like 137 stranded commits, and the same reading after
`--unshallow` showed the true figure was 24 across three branches. FOUR OF THE
SEVEN WERE FULLY MERGED AND THE SHALLOW COUNT SAID OTHERWISE. A sweep that does
not deepen first reports noise as danger, which is worse than not running it:
it burns the reader's trust in the check.

So this script deepens first, every time, and says so.

    python3 git_hygiene.py             # report
    python3 git_hygiene.py --deep      # also list files unique to each branch

Exit codes: 0 clean, 1 stranded work found, 2 the working tree is not clean.
"""
import subprocess
import sys


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        return ""
    return r.stdout.strip()


def unshallow():
    """Deepen before measuring. See the docstring: a shallow clone lies."""
    if git("rev-parse", "--is-shallow-repository") == "true":
        print("Clone is SHALLOW. Deepening before measuring, because a shallow")
        print("clone reports merged branches as stranded.\n")
        subprocess.run(["git", "fetch", "--unshallow", "--all"],
                       capture_output=True, text=True)
    subprocess.run(["git", "fetch", "--all", "--prune"],
                   capture_output=True, text=True)


def branches():
    out = git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin")
    return [b for b in out.splitlines() if b and not b.endswith("/HEAD")]


def main():
    deep = "--deep" in sys.argv
    unshallow()

    rc = 0
    dirty = git("status", "--porcelain")
    print("WORKING TREE")
    if dirty:
        print("  NOT CLEAN. Commit or stash before merging or handing over:")
        for line in dirty.splitlines()[:20]:
            print(f"    {line}")
        rc = 2
    else:
        print("  clean")

    head = git("rev-parse", "--abbrev-ref", "HEAD")
    ahead = git("rev-list", "--count", "origin/main..HEAD")
    behind = git("rev-list", "--count", "HEAD..origin/main")
    print(f"\nCURRENT BRANCH  {head}")
    print(f"  ahead of main {ahead}, behind main {behind}")
    if behind != "0":
        print("  main HAS COMMITS YOU DO NOT. Read them before merging;")
        print("  a force push here would destroy them.")

    stranded, merged = [], []
    for b in branches():
        n = git("rev-list", "--count", f"origin/main..{b}")
        if n and n != "0":
            stranded.append((b, int(n)))
        else:
            merged.append(b)

    print(f"\nBRANCHES WITH WORK MAIN DOES NOT HAVE  ({len(stranded)})")
    if not stranded:
        print("  none. Nothing is stranded.")
    for b, n in sorted(stranded, key=lambda x: -x[1]):
        last = git("log", "-1", "--format=%ad", "--date=short", b)
        print(f"  {b:48} +{n:<4} last {last}")
        if deep:
            base = git("merge-base", "origin/main", b)
            if base:
                names = git("diff", "--name-status", base, b)
                new = [l.split("\t", 1)[1] for l in names.splitlines()
                       if l.startswith("A")]
                for f in new[:12]:
                    exists = subprocess.run(
                        ["git", "cat-file", "-e", f"origin/main:{f}"],
                        capture_output=True).returncode == 0
                    if not exists:
                        print(f"       ONLY HERE: {f}")
    if stranded:
        rc = rc or 1

    # origin/main is trivially merged into itself, and deleting the branch you
    # are standing on is never safe. Both were listed as deletable on the first
    # run of this script, which is the kind of suggestion a tired reader acts on.
    protected = {"origin/main", f"origin/{head}"}
    merged = [b for b in merged if b not in protected]

    print(f"\nFULLY MERGED INTO MAIN, SAFE TO DELETE  ({len(merged)})")
    for b in merged:
        print(f"  {b}")
    if merged:
        print("\n  Delete them with:")
        print("    " + " ".join("git push origin --delete "
                                + b.split("/", 1)[1] for b in merged[:1]))
        print("  or all at once:")
        names = " ".join(b.split("/", 1)[1] for b in merged)
        print(f"    git push origin --delete {names}")

    print("\n" + "=" * 68)
    if rc == 0:
        print("CLEAN. Nothing stranded, tree committed.")
    elif rc == 2:
        print("WORKING TREE NOT CLEAN. Fix that first.")
    else:
        print("STRANDED WORK EXISTS. Do not retire a branch until main has it.")
        print("Re-run with --deep to see which files live ONLY on a branch.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
