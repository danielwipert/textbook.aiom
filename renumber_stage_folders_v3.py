#!/usr/bin/env python3
"""
renumber_stage_folders_v3.py

One-time Process v2 to v3 stage-folder migration, Decision 68. Sibling of
renumber_stage_folders.py, which did v1 to v2 on 2026-08-05 and is kept for the
same reason this will be: a migration nobody can audit is a migration nobody can
trust.

Process v3 moves Stage 5 and Gate G2 to sit after Stage 7, so that the two reads
of a rendered page happen once, on text nothing further will move. No stage is
renamed and no stage is renumbered. Only four folder PREFIXES change, and they
change as a cycle, which is why this renames through temporary names rather than
in place.

    06_Stage5_Design_Review        -> 08_Stage5_Design_Review
    07_G2_Production_Gate          -> 09_G2_Production_Gate
    08_Stage6_Copy_Edit            -> 06_Stage6_Copy_Edit
    09_Stage7_Final_Fact_Check_2   -> 07_Stage7_Final_Fact_Check_2

CHAPTER 1 IS DELIBERATELY EXCLUDED AND THAT IS THE POINT OF THIS SCRIPT HAVING A
SKIP LIST AT ALL. It is LOCKED under Process v2 and its checklist records its
steps in v2 order. Renumbering its folders would leave the folders disagreeing
with the record beside them, which is the shape of defect this repository keeps
paying for. A completed unit keeps the process it was completed under, exactly as
dated records keep their v1 numbers.

Usage:
    python3 renumber_stage_folders_v3.py --dry-run   # show what would move
    python3 renumber_stage_folders_v3.py             # move it, through git mv
"""

import argparse
import os
import subprocess
import sys

DRAFTS = "Drafts"

# (from, to), applied as a cycle through temporary names.
MOVES = [
    ("06_Stage5_Design_Review",      "08_Stage5_Design_Review"),
    ("07_G2_Production_Gate",        "09_G2_Production_Gate"),
    ("08_Stage6_Copy_Edit",          "06_Stage6_Copy_Edit"),
    ("09_Stage7_Final_Fact_Check_2", "07_Stage7_Final_Fact_Check_2"),
]

# Locked under Process v2. See the docstring.
SKIP = ["Ch01_The_Category_Error"]


def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(args), r.stderr.strip()))


def migrate(unit, dry):
    root = os.path.join(DRAFTS, unit)
    present = [a for a, _ in MOVES if os.path.isdir(os.path.join(root, a))]
    if not present:
        return 0
    if len(present) != len(MOVES):
        print("  %s: expected %d stage folders to move, found %d. SKIPPED, "
              "inspect by hand." % (unit, len(MOVES), len(present)))
        return 0

    if dry:
        for a, b in MOVES:
            print("  %s: %s -> %s" % (unit, a, b))
        return len(MOVES)

    # Through temporary names, because the four prefixes form a cycle and a
    # direct rename would collide with a folder that has not moved yet.
    for a, _ in MOVES:
        git("mv", os.path.join(root, a), os.path.join(root, "_mig_" + a))
    for a, b in MOVES:
        git("mv", os.path.join(root, "_mig_" + a), os.path.join(root, b))
    print("  %s: 4 folders renumbered" % unit)
    return len(MOVES)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if not os.path.isdir(DRAFTS):
        sys.exit("run this from the repository root")

    units = sorted(d for d in os.listdir(DRAFTS)
                   if os.path.isdir(os.path.join(DRAFTS, d)))
    moved = 0
    for u in units:
        if u in SKIP:
            print("  %s: SKIPPED, locked under Process v2" % u)
            continue
        moved += migrate(u, a.dry_run)

    print("\n%s: %d folder moves across %d units."
          % ("would move" if a.dry_run else "moved", moved,
             len(units) - len(SKIP)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
