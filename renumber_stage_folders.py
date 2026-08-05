#!/usr/bin/env python3
"""renumber_stage_folders.py  |  one-time Process v1 to v2 folder migration

Every chapter and part-case folder under Drafts/ carries stage folders named
against Process v1. The live process is v2 (CLAUDE.md section 8), so the names
lie: 04_Stage3_Voice_Check when voice is Stage 4, 05_Stage4_Design_Review when
design is Stage 5. A drafter filing an artifact by folder name files it under
the wrong stage.

v2 also added the developmental edit at Stage 2, which has no folder at all.

Renames descending so no rename collides with a name not yet vacated. Uses
git mv, so history follows. Idempotent: a unit already migrated is skipped.

Usage:
    python3 renumber_stage_folders.py --dry-run
    python3 renumber_stage_folders.py
"""
import argparse
import os
import subprocess
import sys

ROOT = "Drafts"

# (old name, new name), in the order they must be applied. Descending by new
# number, so each target slot is free when its rename runs.
RENAMES = [
    ("11_Stage8_Locked",              "12_Stage9_Locked"),
    ("10_Stage7_Final_Read",          "11_Stage8_Final_Read"),
    ("09_G3_Continuity_Gate",         "10_G3_Continuity_Gate"),
    ("08_Stage6_Final_Fact_Check_2",  "09_Stage7_Final_Fact_Check_2"),
    ("07_Stage5_Copy_Edit",           "08_Stage6_Copy_Edit"),
    ("06_G2_Production_Gate",         "07_G2_Production_Gate"),
    ("05_Stage4_Design_Review",       "06_Stage5_Design_Review"),
    ("04_Stage3_Voice_Check",         "05_Stage4_Voice_And_Craft_Check"),
    ("03_Stage2_Source_Fact_Check_1", "04_Stage3_Source_Fact_Check_1"),
]

# Added by Process v2. Created empty, with a .gitkeep so it survives commit.
NEW_DIRS = ["03_Stage2_Developmental_Edit"]

# Unchanged under v2, listed so the expected set is complete and auditable.
UNCHANGED = ["00_Stage0_Draft", "01_G1_Structural_Gate",
             "02_Stage1_Content_Review"]


def units():
    return sorted(d for d in os.listdir(ROOT)
                  if os.path.isdir(os.path.join(ROOT, d)))


def run(cmd, dry):
    if dry:
        print("      would run: " + " ".join(cmd))
        return True
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(f"      ERROR: {r.stderr.strip()}")
        return False
    return True


def migrate(unit, dry):
    base = os.path.join(ROOT, unit)
    moved = created = 0
    for old, new in RENAMES:
        src, dst = os.path.join(base, old), os.path.join(base, new)
        if not os.path.isdir(src):
            continue
        if os.path.exists(dst):
            print(f"      SKIP {old}: {new} already exists")
            continue
        if run(["git", "mv", src, dst], dry):
            moved += 1
    for d in NEW_DIRS:
        path = os.path.join(base, d)
        if os.path.isdir(path):
            continue
        if dry:
            print(f"      would create: {path}")
            created += 1
            continue
        os.makedirs(path, exist_ok=True)
        open(os.path.join(path, ".gitkeep"), "w").close()
        created += 1
    return moved, created


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(ROOT):
        print(f"no {ROOT}/ directory; run from the repository root")
        return 1

    total_moved = total_created = 0
    for unit in units():
        moved, created = migrate(unit, args.dry_run)
        if moved or created:
            print(f"  {unit}: {moved} renamed, {created} created")
            total_moved += moved
            total_created += created
        else:
            print(f"  {unit}: already on v2 numbering")

    print(f"\n{total_moved} folders renamed, {total_created} created"
          + ("  (dry run, nothing written)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
