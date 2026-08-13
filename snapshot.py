#!/usr/bin/env python3
"""
Lock snapshots. What the site publishes is the last LOCKED state of each chapter,
never the working tree.

WHY THIS EXISTS. Before it, reopening a locked chapter broke the whole site
build: `web_build.py --site` failed with "W10: no locked chapter found", CI went
red, and nothing else could deploy until the chapter re-locked. That makes an
edit to a published chapter an event rather than a Tuesday, which is backwards
for a book whose author revises continuously. Ruled 2026-08-13: the working tree
and the published site are decoupled, and the site keeps serving the old snapshot
SILENTLY while a revision is in flight.

WHERE THE SNAPSHOT COMES FROM, and why it is derived rather than stored. Two
alternatives were rejected.

A committed `published/` copy of each chapter would duplicate the chapter text
inside the repository, which is precisely the Decision 50 hazard: two files
holding one chapter, free to disagree, with no gate able to hold them together
because they are SUPPOSED to differ while a revision is open.

An explicit `ch01-locked-v1` tag written at lock time can be FORGOTTEN, and a
forgotten tag publishes a stale chapter with nothing reporting it.

So the snapshot is derived from the record that already exists and is already
enforced: the chapter's checklist. The newest commit whose version of that
checklist reported Stage 9 passed IS the lock. It cannot be forgotten, it needs
no new artifact, and git already stores every byte.

THE HOLE THIS LEAVES, stated rather than hidden. If a locked chapter's text is
edited without reopening its checklist, the checklist still says Stage 9 while
the text has moved. The snapshot is still correct (it serves the locked text),
but the working tree now disagrees with what the record claims. `divergence()`
reports that, loudly, on every build. It is deliberately NOT a build failure,
because failing would reintroduce the exact coupling this file removes.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

import status_check


def _git(*args, check=True):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def _reports_locked(blob_text):
    """Does this checklist TEXT report Stage 9 passed?

    status_check.parse takes a path, so the blob is written to a temp file
    rather than reimplementing the parser. Reimplementing it is how a second
    answer to a single-sourced question gets created.
    """
    fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False,
                                     encoding="utf-8")
    try:
        fh.write(blob_text)
        fh.close()
        steps = status_check.parse(fh.name)
    except Exception:
        return False
    finally:
        os.unlink(fh.name)
    lock = next((s for s in steps if s["id"] == "Stage 9"), None)
    return bool(lock and lock["status"])


def lock_commit(checklist_path):
    """(sha, date) of the newest commit whose checklist reported Stage 9.

    Returns None if the chapter has never locked. Only commits that MODIFIED the
    checklist are considered, which is correct: between two such commits the
    reported status cannot have changed.
    """
    rel = os.path.relpath(os.path.abspath(checklist_path), os.getcwd())
    log = _git("log", "--format=%H %ad", "--date=short", "--", rel).strip()
    if not log:
        return None
    for line in log.split("\n"):
        sha, date = line.split(" ", 1)
        try:
            blob = _git("show", "%s:%s" % (sha, rel))
        except RuntimeError:
            continue
        if _reports_locked(blob):
            return sha, date.strip()
    return None


def _files_at(sha, dirpath):
    rel = os.path.relpath(os.path.abspath(dirpath), os.getcwd())
    out = _git("ls-tree", "-r", "--name-only", sha, "--", rel).strip()
    return [l for l in out.split("\n") if l]


def materialize(drafts_root, out_dir):
    """Write every chapter's LOCKED state into out_dir, mirroring Drafts/.

    The tree it writes is shaped exactly like Drafts/, so discovery, gate W2,
    the checklist lookup and claimcheck's chapter-id inference all keep working
    unchanged against it. That is the whole reason this is a tree rather than a
    set of in-memory strings: the alternative was threading snapshot content
    through every path-dependent call in web_build.py.

    Returns (chapters, notes): chapters is [(sha, date, chapter_dir_name)] for
    each chapter that has ever locked, notes is human-readable lines for the
    build log.
    """
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir, exist_ok=True)
    chapters, notes = [], []

    for name in sorted(os.listdir(drafts_root)):
        chdir = os.path.join(drafts_root, name)
        if not os.path.isdir(chdir) or not re.match(r"Ch\d+", name):
            continue
        found = sorted(f for f in os.listdir(chdir)
                       if re.match(r"AIOM_Ch\d+_Checklist.*\.md$", f))
        if not found:
            notes.append("%s: no checklist, skipped" % name)
            continue
        checklist = os.path.join(chdir, found[-1])
        lock = lock_commit(checklist)
        if lock is None:
            notes.append("%s: never locked, not published" % name)
            continue
        sha, date = lock
        for rel in _files_at(sha, chdir):
            dst = os.path.join(out_dir, os.path.relpath(rel, drafts_root))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            blob = subprocess.run(["git", "show", "%s:%s" % (sha, rel)],
                                  capture_output=True)
            if blob.returncode:
                continue
            with open(dst, "wb") as fh:
                fh.write(blob.stdout)
        chapters.append((sha, date, name))
        notes.append("%s: publishing the lock of %s (%s)" % (name, date, sha[:10]))
    return chapters, notes


def divergence(drafts_root, chapters):
    """Chapters whose working tree differs from the snapshot being published.

    Two shapes, and only one is a problem.

    A chapter whose checklist has been REOPENED is expected to differ; that is
    what a revision in flight looks like and it is reported as ordinary news.

    A chapter whose checklist still reports Stage 9 while its text has moved is
    a record that has stopped being true, because an edit to a locked chapter is
    supposed to reopen it. Reported as a WARNING rather than a failure, on the
    2026-08-13 ruling that the site keeps serving silently.
    """
    out = []
    for sha, _date, name in chapters:
        chdir = os.path.join(drafts_root, name)
        rel = os.path.relpath(os.path.abspath(chdir), os.getcwd())
        diff = subprocess.run(
            ["git", "diff", "--name-only", sha, "--", rel],
            capture_output=True, text=True).stdout.strip()
        if not diff:
            continue
        found = sorted(f for f in os.listdir(chdir)
                       if re.match(r"AIOM_Ch\d+_Checklist.*\.md$", f))
        still_locked = False
        if found:
            try:
                steps = status_check.parse(os.path.join(chdir, found[-1]))
                lock = next((s for s in steps if s["id"] == "Stage 9"), None)
                still_locked = bool(lock and lock["status"])
            except Exception:
                pass
        changed = [f for f in diff.split("\n") if f]
        out.append((name, still_locked, changed))
    return out


def main(argv):
    root = argv[1] if len(argv) > 1 else "Drafts"
    out = "build/_snapshots"
    chapters, notes = materialize(root, out)
    print("lock snapshots, from %s" % root)
    for n in notes:
        print("  " + n)
    if not chapters:
        print("\nNO CHAPTER HAS EVER LOCKED. Nothing would publish.")
        return 1
    div = divergence(root, chapters)
    if div:
        print()
        for name, still_locked, changed in div:
            if still_locked:
                print("  WARNING %s: text has changed since it locked, but its "
                      "checklist still reports Stage 9. An edit to a locked "
                      "chapter should reopen it." % name)
            else:
                print("  %s: revision in flight, %d file(s) differ from the "
                      "published lock" % (name, len(changed)))
    print("\n%d chapter(s) would publish" % len(chapters))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
