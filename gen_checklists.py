"""
gen_checklists.py

Generates one self-contained editorial checklist per chapter, under PROCESS v4
(Decisions 75 to 81, 2026-09-30, `AIOM_Process_v4_Proposal_v1.0.md`). Each file
holds the whole process: the steps in order, what every gate checks, who owns
each step, and space for findings.

THE STEP LABELS ARE KEPT FROM v3 ON PURPOSE, AND THE NUMBERS ARE THEREFORE OUT
OF ORDER. Every tool binds a check to the label of the step that claims it:
`chapter_check.py` binds W14 to "Stage 3", voicecheck to "Stage 4", the print
render to "Stage 5", the web build to "Gate G2" and continuity to "Gate G3", and
`snapshot.py`, `web_build.py` and `amend.py` read the lock from "Stage 9". Each
v4 step takes the label whose check it owns, so none of those tools changed.
v3 Stages 1, 2 and 7 are retired: 1 and 2 merged into the review, which is
"Stage 4" because it owns voicecheck, and 7 merged into the one fact check,
"Stage 3". `reopen.py` reads step order from the checklist, so the order below
is what it resets through.

Chapters 1 and 2 are locked under Processes v2 and v3 and are never regenerated.

Usage:
    python3 gen_checklists.py 3            # write Chapter 3's checklist
    python3 gen_checklists.py 3 4 5        # several
    python3 gen_checklists.py 3 --force    # overwrite, DESTROYING its ticks
    python3 gen_checklists.py 3 --stdout   # print, write nothing
"""

import argparse
import glob
import os
import sys

DRAFTS = "Drafts"

# Locked under an earlier process. A completed unit keeps the process it was
# completed under.
LOCKED_UNDER_EARLIER_PROCESS = {1, 2}

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

# (id, name, owner, note, [gate checks]), in PROCESS v4 order.
STAGES = [
    ("0", "Plan and draft", "Claude; Dan approves the plan (sitting 1)",
     "v4 step 1 and 2. A one-page plan comes FIRST (Decision 77) and Dan "
     "approves it before a word is drafted, because a structural question is "
     "cheapest before the prose exists. Then Claude drafts against the fixed "
     "six-slot skeleton, with the craft standard binding from here, and clears "
     "the frequency sweep before anyone reads the draft (Decision 78). Sources "
     "verified live with an access date; no archival (Decision 48).", [
         "Plan written, one page, in 00_Stage0_Draft: opening case and its "
         "source, teaching sections, craft artifact, registry objects rendered, "
         "continuity promises paid and made, and a source for every empirical "
         "claim the chapter intends to make",
         "Dan approved the plan (sitting 1)",
         "Drafted against the SEVEN craft criteria in "
         "AIOM_Prose_Standard_v2.0.md, read BEFORE drafting rather than after. "
         "The voice is Concrete Management Prose",
         "Frequency sweep cleared (Decision 78): `freqsweep.py` lists every "
         "frequency sentence and each is cited, rewritten as a formal "
         "conditional, or cut, or kept as qualification for Dan to rule; the "
         "dispositions go in the review package",
     ]),

    ("G1", "Structural gate", "Claude",
     "Mechanical. Runs before Dan sees the chapter, so no reading time is "
     "spent on a draft with a defect a script could find.", [
         "All six slots present, in order, correctly headed",
         "Opening case carries a provenance line under its title",
         "Every exit competency assigned to this chapter is addressed",
         "Every registry ID cited resolves in AIOM_Registry_Manifest.json AND "
         "is certified (Decision 72): run registry.py --check",
         "Tier rules hold: one theorem callout, lemmas by ID, propositions by ID",
         "Every empirical claim carries a citation; every source carries an access date (Decision 48, no archival)",
         "Every Slot 5 key term appears defined in the body",
         "Zero em dashes",
         "Word count inside the chapter target band",
         "Gloss-less lemmas carry a book-authored gloss, marked as such",
         "voicecheck.py mechanical bans clean before anyone reads the draft",
     ]),

    ("4", "Review", "Claude; second model reads independently; Dan rules (sitting 2)",
     "v4 step 3, Decision 77. ONE pass replacing v3 Stages 1, 2 and 4: "
     "structure against AIOM_Structure_v1.md and AIOM_Exit_Competencies_v1.md, "
     "teaching quality, and voice and craft against AIOM_Prose_Standard_v2.0.md. "
     "Labelled Stage 4 because it owns voicecheck. Read ADVERSARIALLY: for each "
     "competency and each criterion quote the WEAKEST evidence and rule it, "
     "reading the per-section table rather than the chapter average. ONE "
     "second-model package carries the three questions as separate sections, "
     "read without Claude's findings, and is BUILT BEFORE the sitting "
     "(Decision 81). Claude applies what is not a judgment call and hands Dan "
     "ONE decision list; Dan rules every finding, Claude rules none, and the "
     "ruled list is applied in ONE commit.", [
         "Structure: every slot serves the chapter's stated purpose in "
         "AIOM_Structure_v1.md",
         "Structure: every assigned exit competency is DELIVERED, not merely "
         "discussed: a reader could perform it",
         "Structure: the anchor theorem is the right one and is load-bearing "
         "in the argument rather than decorative",
         "Structure: ledger obligations met, no earlier chapter's term "
         "redefined, promises owed are paid, nothing belonging to a later "
         "chapter front-run",
         "Teaching: clarity, pacing, cognitive load, example fitness and "
         "transitions carry the target reader without a stall",
         "C1 concrete particular: every abstraction carrying argumentative "
         "weight is anchored to a named, specific instance",
         "C2 context and stakes: every mechanism states the conditions that "
         "made it available and what it settles, not only what it does",
         "C3 claim first: the main point of a paragraph is visible in its "
         "first sentence or two, qualifications subordinate, no throat "
         "clearing",
         "C4 deliberate rhythm: sentence length varies, mostly 12 to 24 "
         "words, a short sentence after a long explanation, no long stretch "
         "at a uniform length",
         "C5 paragraph close: paragraphs end on the load-bearing clause, not a "
         "trailing qualifier and not a cross-reference",
         "C6 the guard holds in BOTH directions: no hero or villain framing, "
         "no populist register, no character-driven causation where a "
         "structural account is available, and no false sophistication, no "
         "abstraction where an ordinary word serves, no aphorism standing in "
         "for an explanation",
         "C7 business reality first: no paragraph opens on a framework, "
         "category or conceptual distinction where a business statement is "
         "available, and every coined term arrives after the mechanism it "
         "names",
         "Second-model package (one, three sections) returned and its findings "
         "recorded, one line each",
         "Dan has ruled every finding (sitting 2), applied in one commit",
     ]),

    ("6", "Author pass", "Dan",
     "v4 step 4, Decision 75. Dan's own pass and rewrite, in Word, through "
     "`copyedit_export.py` and `copyedit_import.py`. It sits BEFORE the fact "
     "check so that every step after it checks the text Dan wants: on Chapter "
     "2 this pass changed 104 of 195 blocks after three checks had run. "
     "Includes the whole-chapter read the old Stage 8 was.", [
         "Unedited export round-trips at zero reported changes before the "
         "pair is trusted on this chapter",
         "Dan's pass imported; every block the importer refused resolved by "
         "hand",
         "After import, `voicecheck.py`, `claimcheck.py` and `freqsweep.py` "
         "re-run, and every new hit fixed or put to Dan",
     ]),

    ("3", "Fact check", "Dan, external (sitting 3)",
     "v4 step 5, Decision 76. ONE external fact check replacing v3 Stages 3 "
     "and 7, on a fresh RENDER of the post-author-pass text, never the HTML. "
     "Two checks run in parallel on different prompts: A reads the sources, "
     "B reads only the render. THE CHECKER MUST HAVE WEB ACCESS: Chapter 2's "
     "first checker could not read, and its work was redone. Labelled Stage 3 "
     "because it owns W14. Rulings go into the register notes, with the "
     "condition that would reverse them, and into AIOM_Claim_Ledger.md.", [
         "Packet built with `factcheck_packet.py` against a fresh render, "
         "BEFORE the sitting",
         "Check A (reads the sources, web access confirmed) returned",
         "Check B (reads only the render) returned",
         "Dan has ruled both sets in one sitting (sitting 3); register notes "
         "and AIOM_Claim_Ledger.md updated; applied in one commit",
         "Any empirical claim added after this check carries a source before "
         "lock (standing rule 2)",
     ]),

    ("5", "Design review", "Claude",
     "v4 step 6, with G2 and G3 in the same session. Once, after the text is "
     "final, NEVER EARLY: Chapter 2 ran it early and ran it twice. Rasterize "
     "EVERY page and read it at the size it ships at: figures, callout "
     "placement, page fill, slot openings, running heads, key-term register, "
     "against the locked design system.", []),

    ("G2", "Production gate", "Claude",
     "Mechanical, run on the rendered PDF by AIOM_build.py. The boxes below "
     "mirror the fifteen numbered gates the tool prints, one for one, so a "
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
         "Ledger updated at lock (continuity.py --update), glosses written by hand. DO BEFORE ticking Stage 9: this is a Stage 9 action listed here for visibility, not a G3 check, and it stays open while G3 passes.",
     ]),

    ("8", "Sign-off", "Dan (sitting 4)",
     "v4 step 7. Claude sends the render plus a short diff of everything that "
     "changed since the author pass. Dan approves the whole, or names ONE "
     "structural reason and the chapter returns to the step that owns it. The "
     "full read already happened in the author pass.", []),

    ("9", "Locked", "Claude",
     "Frozen. Continuity ledger committed. After lock the only path is "
     "`amend.py` (CLAUDE.md section 8).", []),
]

PREAMBLE = """Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

PROCESS v4 (Decisions 75 to 81). Seven steps and FOUR sittings for Dan: plan
approval, review rulings, fact-check rulings, sign-off, plus his author pass.
Steps run in the order below. The Stage numbers are LABELS kept from v3 so the
tools bind unchanged; they are not the order.

| v4 step | Label here | Dan |
|---|---|---|
| 1 Plan, 2 Draft self-checked | Stage 0, Gate G1 | sitting 1, approve plan |
| 3 Review | Stage 4 | sitting 2, rule one list |
| 4 Author pass | Stage 6 | his pass, in Word |
| 5 Fact check | Stage 3 | sitting 3, rule A and B |
| 6 Production | Stage 5, Gate G2, Gate G3 | none |
| 7 Sign-off and lock | Stage 8, Stage 9 | sitting 4 |

Findings are ONE LINE EACH (Decision 81): ID, what, Dan's ruling, commit. The
reasoning goes in the commit message. The next package is built before the
sitting it serves. Tooling is FROZEN while this chapter is in flight (Decision
79): a non-blocking tool defect goes on the fix-between-chapters list in
HANDOFF.md.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every step: no em dashes; every empirical claim cited,
rewritten as a formal conditional, or cut; six-slot skeleton without exception;
theorems are the only chapter anchoring callouts; the seven craft criteria in
AIOM_Prose_Standard_v2.0.md bind from Stage 0 forward."""


def render(number, title):
    out = [f"# Chapter {number}: {title}", "", "Editorial checklist, Process v4.", "",
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


def target(number):
    hits = glob.glob(os.path.join(DRAFTS, "Ch%02d_*" % number))
    if len(hits) != 1:
        sys.exit("expected one Drafts/Ch%02d_* directory, found %d"
                 % (number, len(hits)))
    return os.path.join(hits[0], "AIOM_Ch%02d_Checklist_v1.md" % number)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("chapters", nargs="+", type=int)
    parser.add_argument("--force", action="store_true",
                        help="overwrite an existing checklist, destroying ticks")
    parser.add_argument("--stdout", action="store_true",
                        help="print the checklist and write nothing")
    args = parser.parse_args()
    titles = dict(CHAPTERS)

    for n in args.chapters:
        if n not in titles:
            sys.exit("no chapter %d" % n)
        if n in LOCKED_UNDER_EARLIER_PROCESS:
            sys.exit("Chapter %d is locked under an earlier process and is "
                     "never regenerated" % n)
        text = render(n, titles[n])
        if args.stdout:
            print(text)
            continue
        path = target(n)
        existing = glob.glob(os.path.join(os.path.dirname(path),
                                          "AIOM_Ch*_Checklist*.md"))
        if existing and not args.force:
            print("skipped, exists: %s" % existing[0])
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print("written: %s" % path)


if __name__ == "__main__":
    main()
