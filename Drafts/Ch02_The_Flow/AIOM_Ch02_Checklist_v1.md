# Chapter 2: The Flow

Editorial checklist.

Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

Stages run in order. A chapter is not Locked until every stage above has
passed. Stages 6, 7, and 8 are all external and may be run in one sitting.
Stage 1 may not be batched with them: it runs early or it is worthless.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every stage: no em dashes; every empirical claim cited or
cut; six-slot skeleton without exception; theorems are the only chapter
anchoring callouts; the seven craft criteria in AIOM_Prose_Standard_v2.0.md
bind from Stage 0 forward, not from Stage 4.

---

## Stage 0. Draft

Owner: Claude

Status: [x]        Date cleared: 2026-08-21

> Against the chapter outline and the fixed six-slot skeleton. Sources verified live with an access date; no archival (Decision 48). The craft standard binds here, not only at Stage 4: read AIOM_Prose_Standard_v2.0.md before drafting. Craft caught at Stage 4 is a rewrite; craft applied at Stage 0 is free.

- [x] Drafted against the SEVEN craft criteria in AIOM_Prose_Standard_v2.0.md, read BEFORE drafting rather than after. The voice is Concrete Management Prose

Findings:

---

Findings:

- **STAGE 0 CLOSED 2026-08-21.** 6,872 words, inside the Decision 33 band. Drafted
  against `AIOM_Prose_Standard_v2.0.md` from the first sentence rather than
  repaired at Stage 4, which is what Decision 71 requires and what Chapter 1 could
  not have.
- **The second-model bias review ran before this tick, not after**, under Dan's
  ruling of 2026-08-21, because the opening case is about the drafting vendor's own
  product. Nine of ten findings were accepted and applied. The record is
  `AIOM_Ch02_bias_review_record.md`.
- **BR5 was the most valuable finding and it was not about the vendor.** The craft
  section diagnosed the usage flow as managed on adoption percentages while section
  2.2 sets the test as request volume. The diagnostic failed its own standard on its
  first worked example. Corrected.
- **The markup did not match the design system and the print render is what caught
  it.** The draft used bare `<h2>` for teaching sections and slot labels for the
  summary and key terms, where Chapter 1 uses `h3.section` with a `num` span,
  `h3.tail-head`, `h3.keyterms-head`, and five slot labels. Converted to the
  Chapter 1 convention before G1.

## Gate G1. Structural gate

Owner: Claude

Status: [x]        Date cleared: 2026-08-21

> Mechanical. Runs before Dan sees the chapter, so no reading time is spent on a draft with a defect a script could find.

- [x] All six slots present, in order, correctly headed
- [x] Opening case carries a provenance line under its title
- [x] Every exit competency assigned to this chapter is addressed
- [x] Every registry ID cited resolves in AIOM_Registry_Manifest.json AND is certified (Decision 72): run registry.py --check
- [x] Tier rules hold: one theorem callout, lemmas by ID, propositions by ID
- [x] Every empirical claim carries a citation; every source carries an access date (Decision 48, no archival)
- [x] Every Slot 5 key term appears defined in the body
- [x] Zero em dashes
- [x] Word count inside the chapter target band
- [x] Gloss-less lemmas carry a book-authored gloss, marked as such

Findings:

---

Findings:

- **G1 IS NOT CLEARED. Nine of ten boxes pass; one cannot be ticked by Claude and
  it is the access-date box.** Recorded 2026-08-21.
- **G1.1 six slots, in order:** pass. Opening case, teaching body, craft section,
  chapter summary, key terms, discussion questions and problems, in that order,
  with five slot labels matching Chapter 1.
- **G1.2 provenance line:** pass, and it states that figures come from press
  reporting of a paywalled primary and are pending verification.
- **G1.3 competencies:** pass. C2 is served by the three-flow mapping and worked
  problem P1; C3 by section 2.6 and the derived consequence.
- **G1.4 registry:** pass. `registry.py --check` resolves THM-004 in the pinned
  manifest, confirms it is certified, and confirms the panel renders the registry
  name character for character.
- **G1.5 tier rules:** pass. One theorem callout, no lemmas or propositions cited.
- **G1.6 access dates: FAIL, AND THE REASON IS STRUCTURAL RATHER THAN AN
  OVERSIGHT.** Decision 48 requires every source verified live with an access date.
  All four entries carry `accessed: null` because **no source in this chapter has
  been read by anyone.** The case was found by WebSearch, which returns summaries;
  `WebFetch` and `curl` are blocked by the egress proxy, re-confirmed against
  fortune.com on 2026-08-21. Claude cannot supply an access date without
  fabricating one. **This box is Dan's or it waits for Stage 3.**
- **G1.7 key terms defined in the body:** pass, after a fix. "Three-flow mapping"
  was a key term whose exact phrase never appeared in the body; the craft section
  now introduces it in bold.
- **G1.8 zero em dashes:** pass, confirmed in the render as well as the source.
- **G1.9 word band:** pass, 6,872 against 6,500 to 7,500.
- **G1.10 gloss-less lemmas:** not applicable, no lemmas cited.
- **THE PRINT RENDER PASSES ALL FIFTEEN GATES**, which is not a G1 requirement and
  is recorded because it was run: gate 12 caught a captioned but unreferenced
  Figure 2.1, and gate 15 caught straight marks that `voicecheck` could not see
  because they entered through footnotes generated from the register. Both fixed.
  **A source-side check is not a render-side check**, which this repository already
  knew and this chapter demonstrated again.

**G1 CLEARED 2026-08-21, after Dan supplied what Claude could not.**

- **G1.6 is now satisfied on all four entries, by two different routes.** Dan
  accessed the Forbes and Fortune articles on 2026-08-21 and both entries carry
  that date. `mit-nanda-2025` is non-perishable, and the Chapter 1 convention is
  that a fixed document needs no access date; its location remains a Stage 3 task.
- **`uber-2026-adoption` HAS NO ACCESS DATE BECAUSE IT NO LONGER CITES A
  DOCUMENT, and that is the ruling rather than a gap.** The February and March
  adoption percentages appeared across outlets with consistent values and no
  consistent attribution, which is repetition rather than corroboration. Dan ruled
  the fallback wording on 2026-08-21: **the figures came out rather than a citation
  being invented to hold them.** The chapter now says "about a third" and "a large
  majority", and the share of committed code is characterized rather than
  quantified. The reversing condition is in the register: a named source, read and
  dated, would license restoring the figures.
- **THE FALLBACK BROKE THE RENDER, WHICH IS WHY IT WAS RE-RUN RATHER THAN
  REASONED ABOUT.** Lengthening one register title and one citation gloss grew
  footnote 4 enough to push footnote 5 off its calling page, two pages away. Both
  strings were shortened, the long-form reasoning stayed in the register note where
  it belongs and is never published, and all fifteen gates pass. This is the
  coupling CLAUDE.md records from Chapter 1 appearing in Chapter 2 on its first
  edit.

## Stage 1. Content review

Owner: Dan

Status: [ ]        Date cleared: 

> Is this the right chapter, not is it true. Read against the outline and the competency map. Structural findings only, no line edits.

Findings:

---

## Stage 2. Developmental edit

Owner: Claude

Status: [ ]        Date cleared: 

> Teaching quality, held early so its line edits do not churn fact check, voice, design, and production. Clarity, pacing, cognitive load, example fitness, transitions, and whether the argument carries the target reader without a stall. Claude runs a fresh critical pass; Dan gut-checks with a second model and rules.

Findings:

---

## Stage 3. Source and fact check 1

Owner: Dan

Status: [ ]        Date cleared: 

> Every empirical claim traced to primary source. Runs after the developmental edit, so it checks prose that has stopped moving.

Findings:

---

## Stage 4. Voice and craft check

Owner: Claude

Status: [ ]        Date cleared: 

> Two halves. The mechanical half is voicecheck.py: third person, no contractions, no em dashes, no rhetorical questions outside discussion prompts, no hedging, plus over-explanation below the reader baseline and under-explanation above it. The judgment half is the SEVEN craft criteria below, read against AIOM_Prose_Standard_v2.0.md, which is the one prose standard and whose voice is called Concrete Management Prose. voicecheck.py also prints advisory craft metrics proxying C1, C3, C4, and C5; the metrics inform the read and never decide it. C2 and C7 have no proxy and are enforced by reading alone. Read ADVERSARIALLY and by section: for each criterion quote the WEAKEST passage in the chapter and rule it, rather than asking whether the criterion is met. Read the per-section table, never the chapter average alone. Record a finding per criterion; 'met' is not a finding. Dan gut-checks the craft read with a second model and rules, as at Stage 2; the reusable verification prompt travels in the Chapter 1 checklist.

- [ ] C1 concrete particular: every abstraction carrying argumentative weight is anchored to a named, specific instance
- [ ] C2 context and stakes: every mechanism states the conditions that made it available and what it settles, not only what it does
- [ ] C3 claim first: the main point of a paragraph is visible in its first sentence or two, qualifications subordinate, no throat clearing
- [ ] C4 deliberate rhythm: sentence length varies, mostly 12 to 24 words, a short sentence after a long explanation, no long stretch at a uniform length
- [ ] C5 paragraph close: paragraphs end on the load-bearing clause, not a trailing qualifier and not a cross-reference
- [ ] C6 the guard holds in BOTH directions: no hero or villain framing, no populist register, no character-driven causation where a structural account is available, and no false sophistication, no abstraction where an ordinary word serves, no aphorism standing in for an explanation
- [ ] C7 business reality first: no paragraph opens on a framework, category or conceptual distinction where a business statement is available, and every coined term arrives after the mechanism it names

Findings:

---

## Stage 6. Copy edit

Owner: Dan

Status: [ ]        Date cleared: 

> Line level, on prose that has stopped moving. Decision 24 places this late. Revisit the placement after Chapter 4.

Findings:

---

## Stage 7. Final fact check 2

Owner: Dan

Status: [ ]        Date cleared: 

> Narrower than stage 2. Targets what changed since it, confirming nothing broke in revision.

Findings:

---

## Stage 5. Design review

Owner: Claude

Status: [ ]        Date cleared: 

> Blocked until D0 closes. Layout, figures, typography, running heads, callout placement, key-term register, against the locked design system.

Findings:

---

## Gate G2. Production gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, run on the rendered PDF by AIOM_build.py. The boxes below mirror the fifteen numbered gates the tool prints, one for one, so a box cannot claim a check the tool does not perform. That drift is real: until 2026-08-05 this list claimed figure validation, widow and orphan detection, and a bottom-margin check that AIOM_build.py never ran, and those boxes were ticked by hand. Run `pip install -r requirements.txt` first; the build refuses to start without its toolchain. Two boxes are marked MANUAL: they are not automated, a human must look, and they are labelled so an open box is recorded rather than silently accepted.

- [ ] Renders under WeasyPrint without error or warning
- [ ] Gate 1, zero right-margin overflow
- [ ] Gate 2, zero em and en dashes in the rendered text
- [ ] Gate 3, running heads and folios correct and correctly sided
- [ ] Gate 4, callout placement: no splits, ordering correct after place.py
- [ ] Gate 5, font faces: expected set only, none stray inside SVG
- [ ] Gate 6, key-term register renders with correct rule and tint alternation
- [ ] Gate 7, opening-case provenance line present on page 1
- [ ] Gate 8, footnotes on the calling page, numbering sequential
- [ ] Gate 9, dated evidence boxes labelled and ruled
- [ ] Gate 10, problem labels present with their titles
- [ ] Gate 11, theorem panel intact, labelled, ruled, not split
- [ ] Gate 12, figures captioned, numbered in order, each referenced in text
- [ ] Gate 13, no text below the bottom margin, folio excluded
- [ ] Gate 14, no widows, no orphans, no section head stranded at a page foot
- [ ] Gate 15, typographic marks: zero straight quotes or apostrophes
- [ ] MANUAL, not automated: figure geometry checked by eyeball against a raster, since SVG rx renders as curve paths and does not appear in pdfplumber rects
- [ ] MANUAL, not automated: rasterized page-level visual review (pdftoppm -png -r 150), read by a human

Findings:

---

## Gate G3. Continuity gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, against the running continuity ledger. Catches chapter to chapter drift here rather than at manuscript integration, where the fix would mean reopening a locked chapter. Run `python3 continuity.py <chapter.html> --chapter N`. The ledger is the authority: when a chapter and the ledger disagree the gate fails and Dan rules, and the gate never edits the ledger to make itself pass. At Stage 9, and only then, `--update` appends this chapter's terms, forward references, and registry objects, and `--pay N` marks promises the chapter has now kept.

- [ ] Check 1, no term redefined that an earlier chapter already owns
- [ ] Check 2, every forward reference this chapter makes is logged
- [ ] Check 3, every forward reference assigned to this chapter is paid
- [ ] Check 4, registry IDs logged; recurring glosses worded identically
- [ ] Check 5, Founding Question references match the canonical table exactly
- [ ] Check 6, maturity ladder language consistent with the locked five stages
- [ ] Check 7, Northmoor figures diffed against generator output
- [ ] Ledger updated at lock (continuity.py --update), glosses written by hand. DO BEFORE ticking Stage 9: this is a Stage 9 action listed here for visibility, not a G3 check, and it stays open while G3 passes.

Findings:

---

## Stage 8. Final read

Owner: Dan

Status: [ ]        Date cleared: 

> The chapter read whole, typeset, at reading pace, in one sitting. Pass or fail on the whole, per Decision 30. No lists of small fixes. A failure names one structural reason and the chapter returns to the stage that owns it.

Findings:

---

## Stage 9. Locked

Owner: Claude

Status: [ ]        Date cleared: 

> Frozen. Continuity ledger committed. No change without an explicit reopen, which re-runs every stage from the one that owns the change.

Findings:

---

## Chapter notes

Open items, deferrals, and anything a later chapter needs to know.
