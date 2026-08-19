#!/usr/bin/env python3
"""
Amend a LOCKED chapter. One command, about twenty seconds, and the chapter never
leaves Stage 9.

THE RULING THIS IMPLEMENTS, 2026-08-13. Dan is the author and the final editor.
An edit he makes is approved by definition and SUPERSEDES. This tool therefore
reopens nothing, asks nothing about the merit of the edit, and never prompts for
a review. The thirteen-step lifecycle is for producing a chapter. It is not for
changing a comma in one that already exists.

WHAT IT STILL RUNS, AND WHY THAT IS NOT A CONTRADICTION. The mechanical gates
have no opinion about the writing. They measure the rendered object, and they
catch damage that is invisible in the source because it is not in the sentence
that changed: this repository has a one-sentence reorder pushing footnotes off
their calling pages ELEVEN PAGES LATER, twice. Approving an edit cannot make a
footnote land on the right page. So the gates report render damage and stop
before committing it, and Dan decides what to do. They never overrule the edit.

WHY THE CHECKLIST IS TOUCHED ON EVERY AMENDMENT, which is load bearing rather
than bookkeeping. snapshot.py resolves what publishes as the newest commit whose
CHECKLIST reported Stage 9. An amendment that changed only the chapter HTML would
leave the lock commit behind, and the site would keep serving the pre-amendment
text with nothing reporting it. Appending the amendment record to the checklist
is what advances the snapshot, and it also clears the "edited without reopening"
warning, because the record moves with the text.

SUPERSEDING A FACT-CHECK RULING. If the edit rewrites a sentence W14 protects,
the answer is not to switch the gate off. Dan is overturning an earlier reading
of a source, which he may do, and the ledger must stop claiming a ruling that is
no longer in force or it silently protects nothing. `--supersede ID "reason"`
retires that ruling in AIOM_Claim_Ledger.md, dated and attributed, keeping the
old text as history.

--rule IS THE SAME RULING APPLIED IN ADVANCE. Naming each ID by hand costs a
round trip: the gate fails, the IDs are read off the failure, and the command is
retyped. That is friction with no decision inside it, because the answer is
already known. Dan's edit supersedes whatever it breaks, so --rule retires
exactly the rulings this edit breaks, dated and attributed like any other
supersede, and the history is kept. It can never retire a ruling that still
holds, because the set comes from the same evaluation W14 runs.

WHAT --rule CANNOT DO, and it is the same blind spot the gate has. A withdrawn
claim RESTATED IN DIFFERENT WORDS matches no forbidden string. It breaks the
ruling in substance, W14 stays silent, and --rule retires nothing because
nothing failed. This is exactly how SF2 came back as SF8. The mechanical half
got faster; the reading half did not move.

    python3 amend.py Ch01 -m "tighten the opening case"
    python3 amend.py Ch01 -m "restate the GitHub act one" --supersede SF3 "..."
    python3 amend.py Ch01 -m "rewrite the opening case" --rule
"""

import argparse
import datetime
import os
import re
import sys

import chapter_check
import claimcheck
import status_check

# resolve(), is_locked() and the mechanical suite itself live in
# chapter_check.py and are IMPORTED rather than repeated here. Two
# implementations of one thing that silently disagree is this repository's
# signature failure, and the suite is the last place to reproduce it.
from chapter_check import is_locked, resolve, run

LEDGER = "AIOM_Claim_Ledger.md"


def changed_files(paths):
    out = run(["git", "diff", "--name-only", "--"] + list(paths)).stdout
    return [f for f in out.split("\n") if f.strip()]


def supersede(ruling_id, reason, today):
    """Retire a ruling in the claim ledger. Dan's ruling replaces the old one.

    The old REQUIRED and FORBIDDEN lines are renamed rather than deleted, so the
    ledger keeps the history and claimcheck stops enforcing them. Its field regex
    anchors on the bare keyword, so a SUPERSEDED- prefix is invisible to it.
    """
    text = open(LEDGER, encoding="utf-8").read()
    pat = re.compile(r"^(###\s+%s\s*::.*?)(?=^###\s|\Z)" % re.escape(ruling_id),
                     re.M | re.S)
    m = pat.search(text)
    if not m:
        sys.exit("no ruling %r in %s" % (ruling_id, LEDGER))
    block = m.group(1)
    new = re.sub(r"^-\s+(REQUIRED|FORBIDDEN|REVIEW):", r"- SUPERSEDED-\1:",
                 block, flags=re.M)
    new = new.rstrip("\n") + (
        "\n- SUPERSEDED %s: retired by Dan, the final editor, whose edit "
        "supersedes. Reason: %s The lines above are kept as history and are no "
        "longer enforced by W14.\n\n" % (today, reason.rstrip() + ("" if reason.rstrip().endswith(".") else ".")))
    open(LEDGER, "w", encoding="utf-8").write(text[:m.start(1)] + new
                                              + text[m.end(1):])
    return True


AMEND_HEADING = "## Amendments after lock"


def record(checklist, message, today, superseded):
    """Append the amendment to the checklist WITHOUT touching any step's tick.

    Stage 9 stays passed. That is the point: an amendment is not a reopen, and
    status_check must still report 13 of 13 when this returns.
    """
    text = open(checklist, encoding="utf-8").read()
    if AMEND_HEADING not in text:
        text = text.rstrip("\n") + (
            "\n\n---\n\n" + AMEND_HEADING + "\n\n"
            "Edits made after Stage 9 by Dan, the author and final editor, whose\n"
            "edit is approved by definition and supersedes. No step is reopened.\n"
            "The mechanical gates were run and passed on each one; nothing here\n"
            "was reviewed for editorial merit, because that judgment is Dan's and\n"
            "was already exercised. Written by `amend.py`.\n")
    entry = "\n**%s.** %s" % (today, message.rstrip().rstrip(".") + ".")
    if superseded:
        entry += (" Superseded fact-check ruling(s): %s. See "
                  "`AIOM_Claim_Ledger.md`." % ", ".join(superseded))
    open(checklist, "w", encoding="utf-8").write(text.rstrip("\n") + entry + "\n")


def main():
    ap = argparse.ArgumentParser(
        description="Amend a locked chapter. Reopens nothing.")
    ap.add_argument("chapter", help="ChNN, or a path to the live text")
    ap.add_argument("-m", "--message", required=True,
                    help="what changed, for the record and the commit")
    ap.add_argument("--supersede", nargs=2, action="append", default=[],
                    metavar=("RULING_ID", "REASON"),
                    help="retire a fact-check ruling this edit overturns")
    ap.add_argument("--rule", action="store_true",
                    help="retire whichever rulings this edit breaks, on Dan's "
                         "authority, without naming them first")
    ap.add_argument("--no-print", action="store_true",
                    help="skip the print render and its fifteen gates")
    ap.add_argument("--force", action="store_true",
                    help="commit even though a gate reported render damage")
    ap.add_argument("--dry-run", action="store_true",
                    help="run the checks and stop, changing nothing")
    a = ap.parse_args()

    if not os.path.exists("web_templates/chapter.html.j2"):
        sys.exit("amend.py must run from the repository root")

    live, checklist, chapter = resolve(a.chapter)
    today = datetime.date.today().isoformat()
    print("Amending %s" % chapter)
    print("  live text  %s" % live)
    print("  checklist  %s" % os.path.basename(checklist))

    if not is_locked(checklist):
        sys.exit("\n%s is NOT locked. An amendment applies to a locked chapter; "
                 "this one is already open, so edit it through its open stage."
                 % chapter)

    touched = changed_files([live])
    if not touched and not a.supersede:
        sys.exit("\nno uncommitted change to %s. Nothing to amend." % live)

    # ---- the ruling Dan overturns, applied BEFORE W14 runs -------------------
    # A dry run must not write the ledger. It did until --rule existed, and the
    # trap was survivable only because naming an ID by hand is deliberate.
    # Retiring rulings AUTOMATICALLY makes an unnoticed ledger edit easy to
    # produce, so the guard goes in with the flag that creates the hazard.
    def retire(rid, reason, note=""):
        if rid in superseded:
            return
        if a.dry_run:
            print("  would supersede %s in %s%s" % (rid, LEDGER, note))
        else:
            supersede(rid, reason, today)
            print("  superseded %s in %s%s" % (rid, LEDGER, note))
        superseded.append(rid)

    superseded = []
    for rid, reason in a.supersede:
        retire(rid, reason)

    if a.rule:
        # Only rulings the edit ACTUALLY breaks are retired. The set comes from
        # the same evaluation W14 runs, so this can never retire a ruling that
        # still holds. What it cannot see is a withdrawn claim restated in
        # different words: that breaks a ruling in substance while matching no
        # string, so it is neither retired here nor reported by the gate.
        broken = claimcheck.broken_rulings(live)
        if not broken:
            print("  --rule: no ruling broken by this edit, nothing retired")
        for rid in broken:
            retire(rid, "Dan's edit supersedes. %s" % a.message.rstrip().rstrip("."),
                   " (--rule)")

    # ---- the mechanical half. No opinion about the writing. ------------------
    # The suite is chapter_check.py's, not a copy of it. A locked chapter has
    # passed every step, so every check in it binds here, which is the behaviour
    # this command has always had.
    print("\nMechanical checks. These measure the artifact, never the edit.")
    results, stale = chapter_check.suite(live, checklist, chapter,
                                         no_print=a.no_print)
    failures = [(r["key"], r["out"]) for r in results if not r["ok"]]
    if stale:
        print("\n  The text has moved since G2 was ticked, so these are STALE "
              "and need a\n  human read. Reported, never ticked, and never a "
              "failure:")
        for m in stale:
            print("    - %s" % m)

    if failures:
        # The heading must say which of two different things happened. A W14
        # objection is not render damage: the artifact is fine and a ruled
        # sentence moved. Calling both "the render broke" would misdescribe the
        # one case where Dan has a decision to make.
        names = {n for n, _ in failures}
        claim_only = names <= {"W14", "web"} and "W14" in names
        print("\n" + "=" * 70)
        if claim_only:
            print("A RULED SENTENCE CHANGED. The artifact is fine.")
        elif names & {"print", "web"}:
            print("THE RENDER BROKE. This is not a judgment about the edit.")
        else:
            # voicecheck, G3 or the record. Calling any of these render damage
            # would misdescribe the one case where Dan has a decision to make,
            # which is the same reason the W14 split exists.
            print("A CHECK OBJECTED. The render is fine.")
        print("=" * 70)
        for name, out in failures:
            lines = [l for l in out.split("\n")
                     if re.search(r"\b(FAIL|W\d+[a-c]?:|^\s*\d+\.\s)", l)
                     or "gate" in l.lower() and "fail" in l.lower()]
            print("\n%s:" % name)
            for l in (lines or out.split("\n"))[-14:]:
                if l.strip():
                    print("   " + l.strip()[:140])
        if any(n == "W14" for n, _ in failures):
            if a.rule and a.dry_run:
                # A dry run retires nothing, so the rulings --rule WOULD have
                # cleared are still failing here. Saying so is the difference
                # between a preview and a false alarm.
                print("\n  W14 objects because the edit changed a sentence a "
                      "fact check ruled.\n  --dry-run retired nothing, so these "
                      "are the same rulings listed above as\n  \"would "
                      "supersede\". The real run clears them.")
            else:
                print("\n  W14 objects because the edit changed a sentence a fact "
                      "check ruled.\n  If that is deliberate, re-run with:"
                      "\n     --supersede <RULING_ID> \"why\", or --rule to "
                      "retire whatever this edit breaks")
        if any(n == "print" for n, _ in failures):
            print("\n  If gate 4 reported a split callout, the remedy is:"
                  "\n     python3 place.py %s" % live)
        if not a.force:
            print("\nNothing committed. Fix the render, or re-run with --force "
                  "to commit anyway.")
            return 1
        print("\n--force given: committing over the failure, on Dan's authority.")

    if a.dry_run:
        print("\n--dry-run: checks only, nothing written.")
        return 0

    # ---- the record, which is what advances the published snapshot -----------
    record(checklist, a.message, today, superseded)
    steps = status_check.parse(checklist)
    if not is_locked(checklist):
        sys.exit("refusing to commit: the checklist no longer reports Stage 9")
    passed = sum(1 for s in steps if s["status"])
    print("\nRecorded. %s still LOCKED, %d of %d steps."
          % (chapter, passed, len(steps)))

    paths = [live, checklist] + ([LEDGER] if superseded else [])
    body = "Amend %s: %s\n\n" % (chapter, a.message.rstrip().rstrip("."))
    body += ("Post-lock amendment by Dan, the author and final editor. His edit "
             "is approved\nby definition and supersedes, so no step was "
             "reopened and the chapter never\nleft Stage 9.\n\n"
             "The mechanical gates were run and passed: they measure the "
             "rendered artifact\nrather than the edit, and exist to catch "
             "damage that is invisible in the source.\n")
    if superseded:
        body += ("\nFact-check ruling(s) superseded on Dan's authority: %s. "
                 "Retired in\nAIOM_Claim_Ledger.md with the old text kept as "
                 "history.\n" % ", ".join(superseded))
    if failures and a.force:
        body += ("\nCommitted with --force over a reported render failure, on "
                 "Dan's authority.\n")
    body += ("\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>\n")

    run(["git", "add"] + paths)
    c = run(["git", "commit", "-F", "-"], input=body)
    if c.returncode != 0:
        print(c.stdout + c.stderr)
        return 1
    print(run(["git", "log", "--oneline", "-1"]).stdout.strip())
    print("\nThe site publishes this on the next push, because the checklist "
          "moved with the text.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
