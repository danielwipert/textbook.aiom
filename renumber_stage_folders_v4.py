#!/usr/bin/env python3
"""
renumber_stage_folders_v4.py

One-time Process v3 to v4 stage-folder migration, Decisions 75 to 81. Sibling of
renumber_stage_folders.py (v1 to v2) and renumber_stage_folders_v3.py (v2 to v3),
kept for the same reason they are: a migration nobody can audit is a migration
nobody can trust.

v4 has ten checklist steps where v3 had thirteen. v3 Stages 1, 2 and 7 are
retired (merged into the review and the one fact check), so their folders go,
and the rest are renumbered into v4 order. The Stage labels are unchanged, as in
the checklist, so a folder still names the step it belongs to.

    00_Stage0_Draft             stays    (tools hardcode this path)
    01_G1_Structural_Gate       stays
    02_Stage4_Review            new      (was Stages 1, 2, 4)
    03_Stage6_Author_Pass       new      (was Stage 6, copy edit)
    04_Stage3_Fact_Check        new      (was Stages 3 and 7)
    05_Stage5_Design_Review
    06_G2_Production_Gate
    07_G3_Continuity_Gate
    08_Stage8_Sign_Off
    09_Stage9_Locked

IT REFUSES ANY UNIT WHOSE STAGE FOLDERS HOLD ANYTHING BUT A .gitkeep. A folder
with work in it belongs to a chapter in flight, and deleting it is not a
migration. Chapters 1 and 2 are skipped by name: they are locked under Processes
v2 and v3, and a completed unit keeps the process it was completed under.

Usage:
    python3 renumber_stage_folders_v4.py --dry-run
    python3 renumber_stage_folders_v4.py
"""
import argparse
import os
import subprocess
import sys

DRAFTS = "Drafts"
SKIP = ["Ch01_The_Category_Error", "Ch02_The_Flow"]
KEEP = {"00_Stage0_Draft", "01_G1_Structural_Gate"}
V4 = [
    "00_Stage0_Draft",
    "01_G1_Structural_Gate",
    "02_Stage4_Review",
    "03_Stage6_Author_Pass",
    "04_Stage3_Fact_Check",
    "05_Stage5_Design_Review",
    "06_G2_Production_Gate",
    "07_G3_Continuity_Gate",
    "08_Stage8_Sign_Off",
    "09_Stage9_Locked",
]


def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(args), r.stderr.strip()))


def migrate(unit, dry):
    root = os.path.join(DRAFTS, unit)
    old = sorted(d for d in os.listdir(root)
                 if os.path.isdir(os.path.join(root, d)))
    if old == V4:
        print("  %s: already v4" % unit)
        return
    for d in old:
        for f in os.listdir(os.path.join(root, d)):
            if f != ".gitkeep":
                print("  %s: %s holds %s. REFUSED, inspect by hand."
                      % (unit, d, f))
                return
    drop = [d for d in old if d not in KEEP]
    add = [d for d in V4 if d not in KEEP]
    if dry:
        print("  %s: remove %d empty folders, create %d" % (unit, len(drop), len(add)))
        return
    for d in drop:
        git("rm", "-q", os.path.join(root, d, ".gitkeep"))
        if os.path.isdir(os.path.join(root, d)):
            os.rmdir(os.path.join(root, d))
    for d in add:
        os.makedirs(os.path.join(root, d), exist_ok=True)
        keep = os.path.join(root, d, ".gitkeep")
        open(keep, "w").close()
        git("add", keep)
    print("  %s: migrated to v4" % unit)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    for unit in sorted(os.listdir(DRAFTS)):
        if unit in SKIP or not os.path.isdir(os.path.join(DRAFTS, unit)):
            continue
        migrate(unit, a.dry_run)


if __name__ == "__main__":
    main()
