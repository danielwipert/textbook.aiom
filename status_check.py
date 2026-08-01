#!/usr/bin/env python3
"""status_check.py  |  chapter lifecycle status consistency gate

The per-chapter checklist is the single source of truth for lifecycle status,
and within it the "Status: [x]" checkbox on each step is authoritative. This
gate reads a checklist, prints that one authoritative status table (so no one
has to guess which document is right), and fails on the structural drift that
is easy to introduce by hand and safe to detect:

  1. A gate or stage marked passed while one of its own sub-checkboxes is still
     open and carries no exception note. This is the class of error that let a
     gate read "passed" while an item under it was unaddressed.
  2. A checkbox and its date disagreeing (passed with no date, or a date with
     no check).
  3. A step marked passed with no findings recorded at all.

It deliberately does not infer status from the narrative findings text, because
those are histories that mix revert and pass language and cannot be parsed
reliably. Status lives in exactly one place, the checkbox; CLAUDE.md section 10
and the Workplan tracker must mirror the table this prints.

Usage:
    python3 status_check.py Drafts/Ch01_The_Category_Error/AIOM_Ch01_Checklist_v6.md
    python3 status_check.py            # every AIOM_Ch*_Checklist*.md under Drafts/
"""
import glob
import os
import re
import sys

STEP_RE = re.compile(r"^## (Stage \d+|Gate G\d+)\.\s*(.+)$")
STATUS_RE = re.compile(r"^Status:\s*\[( |x)\]\s*Date cleared:\s*(.*)$")
SUBBOX_RE = re.compile(r"^- \[( |x)\]\s*(.+)$")
# a sub-item may be left open on a passed step only if it is labelled a known
# exception: a coverage gap, a manual eyeball, or a first-pass note
EXCEPTION_RE = re.compile(r"\b(gap|manual|eyeball|first-pass|do before|"
                          r"not automated|sign-off)\b", re.I)


def parse(path):
    steps, cur = [], None
    for ln in open(path, encoding="utf-8").read().split("\n"):
        m = STEP_RE.match(ln)
        if m:
            cur = {"id": m.group(1), "name": m.group(2).strip(),
                   "status": None, "date": "", "subboxes": [], "findings": []}
            steps.append(cur)
            continue
        if cur is None:
            continue
        s = STATUS_RE.match(ln)
        if s and cur["status"] is None:
            cur["status"], cur["date"] = (s.group(1) == "x"), s.group(2).strip()
            continue
        b = SUBBOX_RE.match(ln)
        if b:
            cur["subboxes"].append((b.group(1) == "x", b.group(2).strip()))
            continue
        if cur["status"] is not None:
            cur["findings"].append(ln)
    return steps


def check(path):
    steps = parse(path)
    fails, warns = [], []
    print(f"\n=== {os.path.basename(path)} ===")
    print(f"{'STEP':<9} {'NAME':<26} {'STATUS':<8} DATE")
    for st in steps:
        passed = st["status"]
        print(f"{st['id']:<9} {st['name'][:26]:<26} "
              f"{'passed' if passed else 'open':<8} {st['date']}")
        findings = "\n".join(st["findings"]).strip()
        if passed:
            for done, label in st["subboxes"]:
                if not done and not EXCEPTION_RE.search(label):
                    fails.append(f"{st['id']}: marked passed but sub-item is "
                                 f"open with no exception note: {label[:48]}")
            if not st["date"]:
                warns.append(f"{st['id']}: marked passed but has no date")
            if not findings:
                warns.append(f"{st['id']}: marked passed with no findings")
        else:
            if st["date"]:
                warns.append(f"{st['id']}: not passed but carries a date")
    for w in warns:
        print("  WARN  " + w)
    for f in fails:
        print("  FAIL  " + f)
    passed_n = sum(1 for s in steps if s["status"])
    print(f"  {passed_n}/{len(steps)} steps passed")
    return not fails


def main():
    args = sys.argv[1:] or sorted(
        glob.glob("Drafts/**/AIOM_Ch*_Checklist*.md", recursive=True))
    if not args:
        print("no checklist given and none found under Drafts/")
        return 1
    ok = all(check(p) for p in args)
    print("\nSTATUS " + ("CONSISTENT" if ok else "INCONSISTENT"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
