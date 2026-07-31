"""
gen_checklists.py

Generates one self-contained editorial checklist per chapter. Each file holds
the whole process: the stages in order, what every gate checks, who owns each
stage, and space for findings. Nothing else needs to exist alongside it.

Run this once. After that you tick the files by hand. Only rerun it if the
process itself changes, and note that --force overwrites your ticks.

Usage:
    python3 gen_checklists.py            # generate any missing checklists
    python3 gen_checklists.py --force    # overwrite everything
"""

import argparse
import os

OUTDIR = "checklists"

CHAPTERS = [
    (1, "The Category Error"),
    (2, "The Flow"),
    (3, "A Science and Its Discipline"),
    (4, "The Playing Field"),
    (5, "The Anatomy of Cost"),
    (6, "The Nature of Value"),
    (7, "Sourcing"),
    (8, "Metering"),
    (9, "Attribution"),
    (10, "Planning and Budgeting"),
    (11, "Allocation and Routing"),
    (12, "The Value Boundary"),
    (13, "Diagnosis and Maturity"),
    (14, "The Organized Buyer"),
    (15, "Standing Up the Discipline"),
]

# (id, name, owner, note, [gate checks])
STAGES = [
    ("0", "Draft", "Claude",
     "Against the chapter outline and the fixed six-slot skeleton. "
     "Sources verified live with an access date; no archival (Decision 48).", []),

    ("G1", "Structural gate", "Claude",
     "Mechanical. Runs before Dan sees the chapter, so no reading time is "
     "spent on a draft with a defect a script could find.", [
         "All six slots present, in order, correctly headed",
         "Opening case carries a provenance line under its title",
         "Every exit competency assigned to this chapter is addressed",
         "Every registry ID cited resolves against Locked Registry v1.3",
         "Tier rules hold: one theorem callout, lemmas by ID, propositions by ID",
         "Every empirical claim carries a citation; every source carries an access date (Decision 48, no archival)",
         "Every Slot 5 key term appears defined in the body",
         "Zero em dashes",
         "Word count inside the chapter target band",
         "Gloss-less lemmas carry a book-authored gloss, marked as such",
     ]),

    ("1", "Content review", "Dan",
     "Is this the right chapter, not is it true. Read against the outline and "
     "the competency map. Structural findings only, no line edits.", []),

    ("2", "Source and fact check 1", "Dan",
     "Every empirical claim traced to primary source. Runs before voice and "
     "design so corrections do not churn later polish.", []),

    ("3", "Voice check", "Claude",
     "Magisterial register: third person, no contractions, no em dashes, no "
     "rhetorical questions outside discussion prompts, no hedging. Also checks "
     "over-explanation below the reader baseline and under-explanation above it.",
     []),

    ("4", "Design review", "Claude",
     "Blocked until D0 closes. Layout, figures, typography, running heads, "
     "callout placement, key-term register, against the locked design system.",
     []),

    ("G2", "Production gate", "Claude",
     "Mechanical, run on the rendered PDF.", [
         "Renders under WeasyPrint without error or warning",
         "Zero overflow: all character bounds inside the text block",
         "Running heads correct and correctly sided on every page",
         "All figures present, numbered, captioned, referenced in text",
         "Figure geometry validated by pixel sampling",
         "Callout placement correct: no splits, ordering correct after place.py",
         "Footnotes on correct pages, numbering sequential and unbroken",
         "Key-term register renders with correct rule and tint alternation",
         "No widows, no orphans, no section head stranded at a page foot",
         "Rasterized visual sample reviewed at page level",
     ]),

    ("5", "Copy edit", "Dan",
     "Line level, on prose that has stopped moving. Decision 24 places this "
     "late. Revisit the placement after Chapter 4.", []),

    ("6", "Final fact check 2", "Dan",
     "Narrower than stage 2. Targets what changed since it, confirming nothing "
     "broke in revision.", []),

    ("G3", "Continuity gate", "Claude",
     "Mechanical, against the running continuity ledger. Catches chapter to "
     "chapter drift here rather than at manuscript integration, where the fix "
     "would mean reopening a locked chapter.", [
         "No term redefined that an earlier chapter already owns",
         "Every forward reference assigned to this chapter is paid",
         "Every forward reference this chapter makes is logged",
         "Northmoor figures diffed against generator output",
         "Registry IDs logged; recurring glosses worded identically",
         "Maturity ladder language consistent with the locked five-stage model",
         "Founding Question references match the canonical table exactly",
         "Ledger updated on lock",
     ]),

    ("7", "Final read", "Dan",
     "The chapter read whole, typeset, at reading pace, in one sitting. Pass or "
     "fail on the whole, per Decision 30. No lists of small fixes. A failure "
     "names one structural reason and the chapter returns to the stage that "
     "owns it.", []),

    ("8", "Locked", "Claude",
     "Frozen. Continuity ledger committed. No change without an explicit "
     "reopen, which re-runs every stage from the one that owns the change.", []),
]

PREAMBLE = """Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

Stages run in order. A chapter is not Locked until every stage above has
passed. Stages 5, 6, and 7 are all external and may be run in one sitting.
Stage 1 may not be batched with them: it runs early or it is worthless.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every stage: no em dashes; every empirical claim cited or
cut; six-slot skeleton without exception; theorems are the only chapter
anchoring callouts."""


def render(number, title):
    out = [f"# Chapter {number}: {title}", "", "Editorial checklist.", "",
           PREAMBLE, "", "---", ""]

    for sid, name, owner, note, checks in STAGES:
        label = f"Stage {sid}" if not sid.startswith("G") else f"Gate {sid}"
        out.append(f"## {label}. {name}")
        out.append("")
        out.append(f"Owner: {owner}")
        out.append("")
        out.append("Status: [ ]        Date cleared: ")
        out.append("")
        out.append(f"> {note}")
        out.append("")
        if checks:
            for c in checks:
                out.append(f"- [ ] {c}")
            out.append("")
        out.append("Findings:")
        out.append("")
        out.append("---")
        out.append("")

    out.append("## Chapter notes")
    out.append("")
    out.append("Open items, deferrals, and anything a later chapter needs to know.")
    out.append("")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true",
                        help="overwrite existing checklists, destroying ticks")
    args = parser.parse_args()

    os.makedirs(OUTDIR, exist_ok=True)
    written = skipped = 0

    for number, title in CHAPTERS:
        path = os.path.join(OUTDIR, f"AIOM_Ch{number:02d}_Checklist.md")
        if os.path.exists(path) and not args.force:
            skipped += 1
            continue
        with open(path, "w") as f:
            f.write(render(number, title))
        written += 1

    print(f"written: {written}   skipped: {skipped}")
    print(f"location: {os.path.abspath(OUTDIR)}")


if __name__ == "__main__":
    main()
