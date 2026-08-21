#!/usr/bin/env python3
"""
chapter_check.py

The mechanical suite, run on ANY chapter, locked or in flight. Decision 69.

WHAT THIS IS FOR. A passed step is a claim about the chapter: when Stage 4
passes, the chapter claims voicecheck is clean; when G2 passes, it claims fifteen
gates are green. Those claims were verified once, by hand, at the moment the step
was ticked, and then nothing re-tested them until a person remembered to look.
Chapter 1's 2026-08-08 reopen records the consequence in its own grounds:
status_check.py "reporting 8 of 13 had been false since round 1 landed". Nothing
was broken in the tooling. Nobody had asked it.

THE CHAPTER'S OWN CHECKLIST DECIDES WHAT BINDS, AND THIS IS THE WHOLE DESIGN.
A check FAILS the run only once the chapter has passed the step that owns it.
Before that it still runs and still prints, but it cannot fail anything. So a
half-drafted chapter with no provenance line and four of six slots does not sit
red for a fortnight, which would train everyone to ignore the suite and reproduce
the exact failure this is meant to prevent. Red is never the normal state,
because red means a tick is currently lying.

This adds no standard. Every check here was already ruled, already written and
already run by hand at a checkpoint. What is new is that they now run at the
commit that breaks them rather than at the next time somebody looks, which makes
this an enforcement of the scoped re-run matrix rather than a new gate.

WHAT IT CANNOT DO. Two of G2's eighteen boxes are MANUAL: figure geometry read
against a raster, and the rasterized page-level visual review. Gaps G-I and G-II
add more reading. This runner never ticks those and never stays silent about
them: when the text has moved under a passed G2 it says so and names them stale,
following the snapshot divergence warning's precedent of reporting rather than
failing. It takes a G2 re-run from eighteen boxes to two. It cannot take it to
zero.

amend.py calls this module rather than carrying its own copy of the suite. Two
implementations of one thing that silently disagree is this repository's
signature failure, and a second copy of the checks would be that failure in the
one place whose job is detecting it.

Usage:
    python3 chapter_check.py Ch02              # one chapter, by id or path
    python3 chapter_check.py --all             # every chapter under Drafts/
    python3 chapter_check.py Ch02 --no-print   # skip the print render
    python3 chapter_check.py Ch02 --strict     # fail on reporting checks too
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys

import claimcheck
import status_check

# (key, label, the step whose PASS makes this check binding, builder)
#
# The owner is the step that CLAIMS the check. Stage 3 rules the claims the
# ledger holds, so W14 binds from there. Stage 4 owns voicecheck. Stage 5 is the
# first step to read a rendered page, so the print render and its fifteen gates
# bind from there rather than from G2. G2 owns the web build, which gates the
# same artifact family. G3 owns continuity.
SUITE = [
    ("W14",        "W14  claim preservation",   "Stage 3"),
    ("voicecheck", "voicecheck, mechanical",    "Stage 4"),
    ("print",      "print render + 15 gates",   "Stage 5"),
    ("web",        "web build + gates",         "Gate G2"),
    ("G3",         "G3   continuity",           "Gate G3"),
    ("registry",   "registry objects",          "Gate G1"),
    ("record",     "checklist self-consistency", None),   # None: always binds
]

MANUAL_BOXES = [
    "G2 MANUAL, figure geometry against a raster",
    "G2 MANUAL, rasterized page-level visual review",
    "Gap G-I, a floated callout colliding with a block panel",
    "Gap G-II, a stranded head GROUP, which gate 14 cannot see",
]


def run(cmd, **kw):
    return subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True,
                          text=True, **kw)


def resolve(target):
    """(chapter_html, checklist, chapter_id) from 'Ch01' or a path."""
    if os.path.isfile(target):
        chdir = os.path.dirname(os.path.dirname(os.path.abspath(target)))
        live = target
    else:
        hits = glob.glob(os.path.join("Drafts", target + "*"))
        if not hits:
            sys.exit("no chapter directory matching %r under Drafts/" % target)
        chdir = hits[0]
        stage0 = os.path.join(chdir, "00_Stage0_Draft")
        cands = [p for p in glob.glob(os.path.join(stage0, "*.html"))
                 if not os.path.basename(p).startswith(("DRAFT-", "_"))
                 and not p.endswith(".print.html")]
        if len(cands) != 1:
            sys.exit("expected exactly one live text in %s, found %d"
                     % (stage0, len(cands)))
        live = cands[0]
    cl = sorted(glob.glob(os.path.join(chdir, "AIOM_Ch*_Checklist*.md")))
    if not cl:
        sys.exit("no checklist in %s" % chdir)
    return live, cl[-1], claimcheck.chapter_id_for(live)


def passed_steps(checklist):
    """{step id: date} for every step this checklist reports as passed."""
    return {s["id"]: s.get("date", "")
            for s in status_check.parse(checklist) if s["status"]}


def is_locked(checklist):
    return "Stage 9" in passed_steps(checklist)


def text_moved_since(live, when):
    """Has the live text changed since the date a step was ticked?

    Two ways it can have: an uncommitted edit sitting in the tree, or a commit
    dated after the tick. Day granularity is all the checklist records, so a
    same-day edit after a same-day tick reads as unmoved. That is the direction
    to err in: this drives a warning, and a warning that cries wolf is ignored.
    """
    r = run(["git", "status", "--porcelain", "--", live])
    if r.stdout.strip():
        return True
    r = run(["git", "log", "-1", "--format=%ad", "--date=short", "--", live])
    last = r.stdout.strip()
    return bool(last and when and last > when)


def build_commands(live, chapter, locked, no_print, checklist):
    """The command for each check, or None where the check is skipped."""
    cmds = {
        "W14":        ["python3", "claimcheck.py", live],
        "voicecheck": ["python3", "voicecheck.py", live],
        "G3":         ["python3", "continuity.py", live,
                       "--chapter", str(int(chapter.replace("Ch", "")))],
        "record":     ["python3", "status_check.py", checklist],
        # Owned by G1 because whether a chapter renders a real, CERTIFIED object
        # under the registry's own name is structural, and G1 runs right after
        # the draft, so a drafter finds out immediately rather than at G2.
        "registry":   ["python3", "registry.py", "--check",
                       chapter],
    }

    if no_print:
        cmds["print"] = None
    else:
        # AIOM_build.py sets base_url to the input file's OWN directory, so a
        # build in place under Drafts/ loses AIOM_book.css and fonts/ and
        # reports dozens of false defects. The copy to the root is the remedy
        # CLAUDE.md section 5 prescribes; the caller removes it afterwards.
        cmds["print"] = ["python3", "AIOM_build.py", "_check_build.html",
                         "--out", "build/%s-check.pdf" % chapter]

    if locked:
        # The published snapshot is the last lock, so --from-worktree is what
        # tests the text in hand rather than the text it replaces.
        cmds["web"] = ["python3", "web_build.py", "--site", "--from-worktree",
                       "--out", "build/web-check"]
    else:
        # A site build SKIPS an unlocked chapter (gate W2 refuses it), so it
        # would report a clean pass having never read this chapter at all.
        # --preview is the unlocked path: noindex, local only.
        cmds["web"] = ["python3", "web_build.py", live, "--preview",
                       "--out", "build/web-preview"]
    return cmds


def suite(live, checklist, chapter, no_print=False, quiet=False):
    """Run the suite. Returns (results, stale) where results is a list of
    dicts with key, label, ok, out and binds."""
    done = passed_steps(checklist)
    locked = "Stage 9" in done
    cmds = build_commands(live, chapter, locked, no_print, checklist)

    tmp = "_check_build.html"
    if cmds.get("print"):
        os.makedirs("build", exist_ok=True)
        shutil.copy(live, tmp)

    results = []
    try:
        for key, label, owner in SUITE:
            cmd = cmds.get(key)
            binds = owner is None or owner in done
            if cmd is None:
                continue
            r = run(cmd)
            ok = r.returncode == 0
            results.append({"key": key, "label": label, "ok": ok,
                            "out": r.stdout + r.stderr, "binds": binds,
                            "owner": owner})
            if not quiet:
                mark = "pass" if ok else "FAIL"
                if not binds:
                    note = "  (reporting, %s not passed)" % owner
                elif not ok:
                    note = "  <- %s claims this" % owner if owner else ""
                else:
                    note = ""
                print("  %-28s %s%s" % (label, mark, note))
    finally:
        for f in (tmp, tmp.replace(".html", ".print.html")):
            if os.path.exists(f):
                os.remove(f)

    stale = []
    if "Gate G2" in done and text_moved_since(live, done.get("Gate G2", "")):
        stale = list(MANUAL_BOXES)
    return results, stale


def report(results, stale, strict=False):
    """Print the failures and the stale manual boxes. Returns an exit code."""
    binding = [r for r in results if not r["ok"] and (r["binds"] or strict)]
    advisory = [r for r in results if not r["ok"] and not r["binds"] and not strict]

    if stale:
        print("\n  WARNING, and this runner cannot close it:")
        print("  the text has moved since G2 was ticked, so these are STALE.")
        for m in stale:
            print("    - %s" % m)
        print("  They need a human read. This is a report, not a failure.")

    for r in advisory:
        print("\n  %s failed but does not bind yet (%s has not passed)."
              % (r["label"].strip(), r["owner"]))

    if not binding:
        return 0

    print("\n" + "=" * 70)
    print("A PASSED STEP'S CLAIM IS NO LONGER TRUE.")
    print("=" * 70)
    for r in binding:
        who = r["owner"] or "the checklist"
        print("\n%s, claimed by %s:" % (r["key"], who))
        lines = [l for l in r["out"].split("\n")
                 if "FAIL" in l or "fail" in l.lower()]
        for l in (lines or r["out"].split("\n"))[-12:]:
            if l.strip():
                print("   " + l.strip()[:140])
    print("\nEither the edit is wrong, or the step needs reopening. "
          "See the scoped\nre-run matrix in CLAUDE.md section 8.")
    return 1


def check_one(target, no_print=False, strict=False):
    live, checklist, chapter = resolve(target)
    done = passed_steps(checklist)
    state = "LOCKED" if "Stage 9" in done else "%d step(s) passed" % len(done)
    print("\n%s  (%s)" % (chapter, state))
    print("  live text  %s" % live)
    results, stale = suite(live, checklist, chapter, no_print=no_print)
    return report(results, stale, strict=strict)


def main():
    ap = argparse.ArgumentParser(description="The mechanical suite, on any "
                                             "chapter, locked or in flight.")
    ap.add_argument("chapter", nargs="?", help="ChNN, or a path to the live text")
    ap.add_argument("--all", action="store_true",
                    help="every chapter under Drafts/ that has a live text")
    ap.add_argument("--no-print", action="store_true",
                    help="skip the print render and its fifteen gates")
    ap.add_argument("--strict", action="store_true",
                    help="fail on reporting checks too, whatever the checklist "
                         "claims")
    a = ap.parse_args()

    if not os.path.exists("web_templates/chapter.html.j2"):
        sys.exit("chapter_check.py must run from the repository root")
    if not a.chapter and not a.all:
        ap.error("give a chapter, or --all")

    if a.all:
        targets = []
        for d in sorted(glob.glob("Drafts/Ch*")):
            stage0 = os.path.join(d, "00_Stage0_Draft")
            live = [p for p in glob.glob(os.path.join(stage0, "*.html"))
                    if not os.path.basename(p).startswith(("DRAFT-", "_"))
                    and not p.endswith(".print.html")]
            if live:
                targets.append(live[0])
        if not targets:
            print("no chapter under Drafts/ has a live text yet. Nothing to "
                  "check, which is not a failure.")
            return 0
    else:
        targets = [a.chapter]

    codes = [check_one(t, no_print=a.no_print, strict=a.strict) for t in targets]
    bad = sum(1 for c in codes if c)
    print("\n%d chapter(s) checked, %d with a broken claim." % (len(codes), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
