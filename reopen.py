#!/usr/bin/env python3
"""reopen.py  |  reopen a chapter at a stage, without destroying its history

CLAUDE.md section 8: "A reopen after Stage 9 re-runs every step from the one
that owns the change." That rule had no mechanism. Reopening by hand means
editing thirteen status markers and trusting that none was missed, which is the
class of error status_check.py exists to catch and cannot catch here, because a
marker left ticked by accident looks exactly like a marker ticked on purpose.

What this does, for every step from the reopen point forward:

  1. Resets the status marker to [ ] and clears its date.
  2. Resets every sub-checkbox to [ ].
  3. Moves the existing findings into a dated ARCHIVED FINDINGS block, kept in
     place and clearly marked superseded. Findings are the record of what was
     examined and why it was ruled; destroying them destroys the audit trail.
  4. Writes a reopen record at the top of the checklist saying what was
     reopened, when, and on what grounds.

Steps BEFORE the reopen point are not touched. gen_checklists.py --force is not
a substitute: it overwrites ticks, writes to checklists/ rather than the
chapter folder, and would fork a live checklist.

Usage:
    python3 reopen.py <checklist.md> --from "Stage 2" --reason "..." --dry-run
    python3 reopen.py <checklist.md> --from "Stage 0" --reason "..."
"""
import argparse
import os
import re
import sys

STEP_RE = re.compile(r"^## (Stage \d+|Gate G\d+)\.\s*(.+)$")
STATUS_RE = re.compile(r"^Status:\s*\[( |x|~|!)\]\s*Date cleared:\s*(.*)$")
SUBBOX_RE = re.compile(r"^- \[( |x)\]\s*(.+)$")

# Document order, so "from Stage 2" can mean "Stage 2 and everything after it"
# including the gates interleaved between stages.
ORDER = ["Stage 0", "Gate G1", "Stage 1", "Stage 2", "Stage 3", "Stage 4",
         "Stage 5", "Gate G2", "Stage 6", "Stage 7", "Gate G3", "Stage 8",
         "Stage 9"]


def parse_steps(lines):
    """Line ranges per step, in document order."""
    steps, cur = [], None
    for i, ln in enumerate(lines):
        m = STEP_RE.match(ln)
        if m:
            if cur:
                cur["end"] = i
            cur = {"id": m.group(1), "name": m.group(2).strip(),
                   "start": i, "end": len(lines)}
            steps.append(cur)
    return steps


def reopen(path, from_step, reason, date, dry):
    if from_step not in ORDER:
        print(f"unknown step {from_step!r}; expected one of: "
              + ", ".join(ORDER))
        return 1

    lines = open(path, encoding="utf-8").read().split("\n")
    steps = parse_steps(lines)
    if not steps:
        print(f"no steps found in {path}; is this a chapter checklist?")
        return 1

    cutoff = ORDER.index(from_step)
    affected = [s for s in steps
                if s["id"] in ORDER and ORDER.index(s["id"]) >= cutoff]
    if not affected:
        print(f"nothing at or after {from_step}")
        return 1

    out = list(lines)
    touched = []

    for step in affected:
        lo, hi = step["start"], step["end"]
        was_passed = False
        status_at = None
        sub_reset = 0
        findings_at = None

        for i in range(lo, hi):
            s = STATUS_RE.match(out[i])
            if s and status_at is None:
                status_at = i
                was_passed = s.group(1) != " "
                continue
            b = SUBBOX_RE.match(out[i])
            if b:
                if b.group(1) == "x":
                    sub_reset += 1
                out[i] = f"- [ ] {b.group(2)}"
                continue
            if out[i].strip() == "Findings:" and findings_at is None:
                findings_at = i

        if status_at is None:
            continue

        # Only steps that had actually recorded something need an archive
        # block. An untouched step is reset silently.
        if was_passed and findings_at is not None:
            body = "\n".join(out[findings_at + 1:hi]).strip()
            if body:
                archive = [
                    "",
                    f"ARCHIVED {date}, superseded by the reopen at "
                    f"{from_step}. The record below describes a version of the "
                    "chapter that no longer exists. It is kept because it "
                    "states what was examined and how it was ruled, which the "
                    "re-run should not have to rediscover. It is NOT evidence "
                    "that this step has passed.",
                    "",
                ]
                out[findings_at + 1:hi] = archive + [body, ""]

        out[status_at] = "Status: [ ]        Date cleared: "
        touched.append((step["id"], step["name"], was_passed, sub_reset))
        # Line numbers shifted; re-parse for the next step.
        steps = parse_steps(out)
        remaining = {s["id"]: s for s in steps}
        for a in affected:
            if a["id"] in remaining:
                a["start"] = remaining[a["id"]]["start"]
                a["end"] = remaining[a["id"]]["end"]

    record = [
        "",
        f"## REOPENED {date}: {from_step} and everything after it",
        "",
        f"Grounds: {reason}",
        "",
        f"Every step from {from_step} forward is reset to not-run. Their "
        "sub-checkboxes are cleared and their findings are archived in place, "
        "marked superseded. Steps before the reopen point are untouched and "
        "keep their passes.",
        "",
        "Reopened by `reopen.py`. Per CLAUDE.md section 8, a reopen re-runs "
        "every step from the one that owns the change, and no chapter is "
        "Locked until every step is complete again.",
        "",
        "| Step | Name | Was | Sub-boxes cleared |",
        "|---|---|---|---|",
    ]
    for sid, name, was_passed, n in touched:
        record.append(f"| {sid} | {name} | "
                      f"{'passed' if was_passed else 'not run'} | {n} |")
    record += ["", "---"]

    # Insert the record after the checklist title block, before the first step.
    first = parse_steps(out)[0]["start"]
    out[first:first] = record

    text = "\n".join(out)
    if dry:
        print(f"DRY RUN, nothing written to {path}\n")
        print("\n".join(record))
        return 0

    open(path, "w", encoding="utf-8").write(text)
    print(f"reopened {os.path.basename(path)} at {from_step}: "
          f"{len(touched)} steps reset")
    for sid, name, was_passed, n in touched:
        print(f"  {sid:<9} {name[:30]:<30} "
              f"{'was passed' if was_passed else 'was not run':<12} "
              f"{n} sub-boxes cleared")
    print("\nRun status_check.py to confirm the resulting state.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("checklist")
    ap.add_argument("--from", dest="from_step", required=True,
                    help='e.g. "Stage 0", "Stage 2", "Gate G2"')
    ap.add_argument("--reason", required=True,
                    help="why the chapter is being reopened; goes in the record")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD, defaults to today")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    date = args.date
    if date is None:
        import datetime
        date = datetime.date.today().isoformat()

    return reopen(args.checklist, args.from_step, args.reason, date,
                  args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
