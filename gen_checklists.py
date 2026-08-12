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
     "Sources verified live with an access date; no archival (Decision 48). "
     "The craft standard binds here, not only at Stage 4: read "
     "AIOM_Voice_and_Craft_v1.md before drafting. Craft caught at Stage 4 is "
     "a rewrite; craft applied at Stage 0 is free.", [
         "Drafted against the six craft criteria "
         "(AIOM_Voice_and_Craft_v1.md), read before drafting rather than after",
     ]),

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

    ("2", "Developmental edit", "Claude",
     "Teaching quality, held early so its line edits do not churn fact check, "
     "voice, design, and production. Clarity, pacing, cognitive load, example "
     "fitness, transitions, and whether the argument carries the target reader "
     "without a stall. Claude runs a fresh critical pass; Dan gut-checks with a "
     "second model and rules.", []),

    ("3", "Source and fact check 1", "Dan",
     "Every empirical claim traced to primary source. Runs after the "
     "developmental edit, so it checks prose that has stopped moving.", []),

    ("4", "Voice and craft check", "Claude",
     "Two halves. The mechanical half is voicecheck.py: magisterial register, "
     "third person, no contractions, no em dashes, no rhetorical questions "
     "outside discussion prompts, no hedging, plus over-explanation below the "
     "reader baseline and under-explanation above it. The judgment half is the "
     "six craft criteria below, read against AIOM_Voice_and_Craft_v1.md. "
     "voicecheck.py also prints advisory craft metrics proxying C1, C3, C4, and "
     "C5; the metrics inform the read and never decide it. C2 and C6 have no "
     "proxy and are enforced by reading alone. Read ADVERSARIALLY and by "
     "section: for each criterion quote the WEAKEST passage in the chapter "
     "and rule it, rather than asking whether the criterion is met. Read the "
     "per-section table, never the chapter average alone. Record a finding "
     "per criterion; 'met' is not a finding. Dan gut-checks the craft read "
     "with a second model and rules, as at Stage 2; the reusable verification "
     "prompt travels in the Chapter 1 checklist.", [
         "C1 concrete particular: every abstraction carrying argumentative "
         "weight is anchored to a named, specific instance",
         "C2 context and stakes: every mechanism states the conditions that "
         "made it available and what it settles, not only what it does",
         "C3 front-loaded sentences: findings lead, qualifications "
         "subordinate, no throat-clearing openers",
         "C4 deliberate rhythm: sentence length varies, no long stretch at a "
         "uniform length",
         "C5 paragraph close: paragraphs end on the load-bearing clause, not a "
         "trailing qualifier",
         "C6 the guard holds: no hero or villain framing, no populist "
         "register, no character-driven causation where a structural account "
         "is available",
     ]),

    ("5", "Design review", "Claude",
     "Blocked until D0 closes. Layout, figures, typography, running heads, "
     "callout placement, key-term register, against the locked design system.",
     []),

    ("G2", "Production gate", "Claude",
     "Mechanical, run on the rendered PDF by AIOM_build.py. The boxes below "
     "mirror the fourteen numbered gates the tool prints, one for one, so a "
     "box cannot claim a check the tool does not perform. That drift is real: "
     "until 2026-08-05 this list claimed figure validation, widow and orphan "
     "detection, and a bottom-margin check that AIOM_build.py never ran, and "
     "those boxes were ticked by hand. Run `pip install -r requirements.txt` "
     "first; the build refuses to start without its toolchain. Two boxes are "
     "marked MANUAL: they are not automated, a human must look, and they are "
     "labelled so an open box is recorded rather than silently accepted.", [
         "Renders under WeasyPrint without error or warning",
         "Gate 1, zero right-margin overflow",
         "Gate 2, zero em and en dashes in the rendered text",
         "Gate 3, running heads and folios correct and correctly sided",
         "Gate 4, callout placement: no splits, ordering correct after place.py",
         "Gate 5, font faces: expected set only, none stray inside SVG",
         "Gate 6, key-term register renders with correct rule and tint alternation",
         "Gate 7, opening-case provenance line present on page 1",
         "Gate 8, footnotes on the calling page, numbering sequential",
         "Gate 9, dated evidence boxes labelled and ruled",
         "Gate 10, problem labels present with their titles",
         "Gate 11, theorem panel intact, labelled, ruled, not split",
         "Gate 12, figures captioned, numbered in order, each referenced in text",
         "Gate 13, no text below the bottom margin, folio excluded",
         "Gate 14, no widows, no orphans, no section head stranded at a page foot",
         "Gate 15, typographic marks: zero straight quotes or apostrophes",
         "MANUAL, not automated: figure geometry checked by eyeball against a "
         "raster, since SVG rx renders as curve paths and does not appear in "
         "pdfplumber rects",
         "MANUAL, not automated: rasterized page-level visual review "
         "(pdftoppm -png -r 150), read by a human",
     ]),

    ("6", "Copy edit", "Dan",
     "Line level, on prose that has stopped moving. Decision 24 places this "
     "late. Revisit the placement after Chapter 4.", []),

    ("7", "Final fact check 2", "Dan",
     "Narrower than stage 2. Targets what changed since it, confirming nothing "
     "broke in revision.", []),

    ("G3", "Continuity gate", "Claude",
     "Mechanical, against the running continuity ledger. Catches chapter to "
     "chapter drift here rather than at manuscript integration, where the fix "
     "would mean reopening a locked chapter. Run "
     "`python3 continuity.py <chapter.html> --chapter N`. The ledger is the "
     "authority: when a chapter and the ledger disagree the gate fails and Dan "
     "rules, and the gate never edits the ledger to make itself pass. At Stage "
     "9, and only then, `--update` appends this chapter's terms, forward "
     "references, and registry objects, and `--pay N` marks promises the "
     "chapter has now kept.", [
         "Check 1, no term redefined that an earlier chapter already owns",
         "Check 2, every forward reference this chapter makes is logged",
         "Check 3, every forward reference assigned to this chapter is paid",
         "Check 4, registry IDs logged; recurring glosses worded identically",
         "Check 5, Founding Question references match the canonical table exactly",
         "Check 6, maturity ladder language consistent with the locked five stages",
         "Check 7, Northmoor figures diffed against generator output",
         "Ledger updated at lock (continuity.py --update), glosses written by hand",
     ]),

    ("8", "Final read", "Dan",
     "The chapter read whole, typeset, at reading pace, in one sitting. Pass or "
     "fail on the whole, per Decision 30. No lists of small fixes. A failure "
     "names one structural reason and the chapter returns to the stage that "
     "owns it.", []),

    ("9", "Locked", "Claude",
     "Frozen. Continuity ledger committed. No change without an explicit "
     "reopen, which re-runs every stage from the one that owns the change.", []),
]

PREAMBLE = """Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

Stages run in order. A chapter is not Locked until every stage above has
passed. Stages 6, 7, and 8 are all external and may be run in one sitting.
Stage 1 may not be batched with them: it runs early or it is worthless.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every stage: no em dashes; every empirical claim cited or
cut; six-slot skeleton without exception; theorems are the only chapter
anchoring callouts; the six craft criteria in AIOM_Voice_and_Craft_v1.md bind
from Stage 0 forward, not from Stage 4."""


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
