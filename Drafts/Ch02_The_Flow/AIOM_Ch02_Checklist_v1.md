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

Owner: Claude; second model checks; Dan rules

Status: [x]        Date cleared: 2026-08-24

> Is this the right chapter, not is it true. Read against AIOM_Structure_v1.md and AIOM_Exit_Competencies_v1.md. Structural findings only, no line edits and no fact checking: Stages 3 and 7 own truth and Stages 2 and 4 own prose. REASSIGNED FROM DAN TO CLAUDE, Decision 73: the work is comparison against two fixed documents, which needs no author and cost Dan hours. WHAT REPLACES HIM IS THE SECOND MODEL, NOT NOTHING. A chapter judged by the model that drafted it is self-marking, and the bias review of 2026-08-21 proved the cost: its most useful finding, BR5, was a STRUCTURAL one that Claude had not seen in its own work. Read ADVERSARIALLY: for each competency quote the WEAKEST evidence in the chapter and rule it, rather than asking whether the competency is met. Dan rules every finding; Claude rules none.

- [x] Every slot serves the chapter's stated purpose in AIOM_Structure_v1.md
- [x] Every assigned exit competency is DELIVERED, not merely discussed: a reader could perform it
- [x] The anchor theorem is the right one and is load-bearing in the argument rather than decorative
- [x] Ledger obligations met: terms owned are defined, no earlier chapter's term is redefined, promises owed are paid
- [x] Nothing belonging to a later chapter is front-run
- [x] Independent structural check received and its findings recorded verbatim. SUBSTITUTED FOR THIS CHAPTER ONLY, 2026-08-22: Dan read the chapter against the two documents himself, in an eight-question working session, rather than sending it to a second model
- [x] Dan has ruled every finding

Findings:

---

**STAGE 1 CLEARED 2026-08-24. Claude's pass completed 2026-08-22; Dan ruled every
finding and the Q3 division question, and the independent read was his own.**
Findings in `01_G1_Structural_Gate/AIOM_Ch02_Stage1_findings.md`, five raised, all
ruled. **The record below is kept as written**, including the interim states, so a
later reader can see what was raised and how it moved rather than only where it
landed.

- **S1-1 (HIGH). RULED BY DAN 2026-08-21: the spot-the-error moves to C6.**
  Decision 74. The competency document required C3 to be assessed by a prose
  derivation plus a spot-the-error on three real quotes, and the chapter had no such
  exercise. Rather than commission three sources for it, the exercise joins C6's
  existing sort-and-repair over cited statements, whose set must now cover
  claimed-as-realized, netting-against-access-price and adoption-as-value.
  **C3 keeps the prose derivation, which discussion question 3 already delivers, so
  NO CHAPTER EDIT FOLLOWS and this finding is closed.** The competency map, the case
  bank's CASE 6.3 gap, and the Workplan all carry the change.
- **S1-2 (HIGH). CLOSED 2026-08-22 IN TWO RULINGS, and it took both.** Dan ruled on
  2026-08-21 that P3 becomes an independent mapping, which was applied against a
  constructed regional insurer. **That satisfied half the assessment and not the
  other half**, because C2 specifies a mapping "on a cited real deployment" and a
  stipulated insurer is not one. Dan ruled the remaining half on 2026-08-22: a
  second real deployment is required, and the split was not accepted.
- **WHAT NOW SATISFIES C2.** P3 is "Map a deployment from a published evaluation"
  and runs on CASE 2.2, the Australian Government whole-of-government trial of
  Microsoft 365 Copilot, January to June 2024. The reader marks up Figure 2.1's
  three tracks, diagnoses each flow with the evidence that settles it, states what
  would overturn each diagnosis, and then sorts the three diagnoses into those
  resting on what the published account establishes and those resting on what it
  does not mention. **The specified marked-up flow diagram, the per-flow diagnosis
  and the cited real deployment now sit on one exercise**, which is what the
  assessment asks for and what no earlier arrangement delivered.
- **WHY THIS CASE RATHER THAN ANOTHER, and what was passed over.** It inverts CASE
  2.1 instead of repeating it: Uber never built the value half, and this
  organization commissioned independent evaluators to build it after the fact and
  still could not settle the question, because no measure of the work existed from
  before the trial. The per-seat licence also puts Chapter 1's meter relocation
  inside a real deployment. **Pennsylvania's ChatGPT Enterprise pilot was the other
  candidate and was deliberately withheld**, because its self-reported 95 minutes
  per day is the classifiable value statement CASE 6.3 is short of, and spending it
  here would have worsened finding S1-4 rather than leaving it as it stands.
- **WHAT THIS FINDING HANDS TO STAGE 3, and it is not a count.** CASE 2.2 is Grade
  C: found by WebSearch on 2026-08-22, search summaries read, no evaluation and no
  article read. Secondary coverage disagrees with itself on every count, so the
  problem states none of them precisely. Four claims are load bearing and the
  register names them: the per-seat licence, agency nomination of participants, the
  commissioning and publication of an independent evaluation, and the evaluation's
  own statements about self-assessment and the missing pre-trial measure.
- **S1-3 (MEDIUM).** Three passages sit close to Chapters 8, 10 and 12. All carry
  forward references, so the risk is spending later material early rather than
  front-running the argument.
- **S1-4 (MEDIUM).** MIT NANDA was dual-placed for Chapter 2 or Chapter 6 and is now
  spent here, against a Chapter 6 case supply the bank already records as a gap.
- **S1-5 (LOW).** THM-004 arrives in 2.7, after the argument it anchors. Ruled not a
  defect on the Chapter 1 exemplar, and recorded because the step requires the
  weakest reading to be stated rather than skipped.

---

### The eight-question structural check, run with Dan on 2026-08-22

**WHAT THIS IS AND WHAT IT SUBSTITUTES FOR.** Decision 73 requires a second model
to read the chapter against `AIOM_Structure_v1.md` and
`AIOM_Exit_Competencies_v1.md` independently, because a chapter judged by the
model that drafted it is self-marking. Dan ruled on 2026-08-22 that he would run
that read himself, with Claude supplying the extracts and the evidence, and the
eight questions in `AIOM_Ch02_Stage1_secondmodel_prompt.md` were worked in order.

**WHAT THAT TRADES, STATED PLAINLY SO THE RECORD DOES NOT OVERCLAIM.** This was
not an independent read. Claude drafted the chapter, wrote the five findings being
checked, and supplied every extract Dan judged from, so the drafter framed the
evidence at every question. What it gains instead is the only authority that
outranks independence: Dan is the author and the final editor, and a finding he
rules is settled rather than advisory. **It is stronger on authority and weaker on
independence, and both halves belong on the record.**

**THIS IS A ONE-CHAPTER SUBSTITUTION AND NOT AN AMENDMENT TO DECISION 73.**
`gen_checklists.py` is unchanged and every later chapter still generates the
second-model box. Whether Decision 73 should change is a separate ruling, and it
is worth taking, because the decision was made eight days ago specifically to stop
spending Dan's hours on this step and this session spent one.

**Q1, do the competencies get DELIVERED.** Both now do, and neither did when the
question was asked.
- **C2** was satisfied by the CASE 2.2 ruling recorded under S1-2 above. Before it,
  the marked-up diagram, the per-flow diagnosis and the cited real deployment sat
  on three different exercises and no single one carried all three.
- **C3 is delivered by discussion question 3**, and Dan ruled on 2026-08-22 that a
  discussion question is enough for it. The weakest reading was stated first: after
  Decision 74 the whole of C3's assessment is a prose derivation, and it sits in the
  chapter's gentlest apparatus rather than in a problem. Dan ruled that the
  derivation genuinely is a prose exercise and that inventing a problem to carry it
  would pad the chapter. **NOTE ON NUMBERING: this question was put to Dan as "DQ4"
  and it is DQ3.** The question was quoted verbatim in the framing, so the ruling
  attached to the right text; the number was off by one and is corrected here and in
  the case bank.

**Q2, does the structure match the extract.** Two edits followed, both ruled.
- **The big idea matches on all three clauses**, including the one checked
  adversarially: section 2.4 gives each flow its own degradation behaviour rather
  than establishing decay for the record flow and asserting it for the others.
- **THM-004 is certified, its panel name is character-identical to the manifest, and
  its four antecedents are set as a structured conditional per Decision 56.** What
  the drafter could not see is that it formalizes only the governance consequence of
  the big idea's third clause: the three-flow taxonomy and the degradation claim
  carry no registry object at all. The registry has certified propositions covering
  much of that ground, PROP-043, PROP-045, PROP-018, LEM-016, PROP-151 and AX-018
  among them, and rule 4 forbids restructuring around any of them. **The defect was
  not thin citation. It was that section 2.8 listed three things the chapter does not
  claim and none of them was the provenance of its own central construct.** RULED AND
  APPLIED: 2.8 now opens with a fourth limit saying the three flows are the book's
  organizing construct and that THM-004 formalizes the consequence rather than the
  taxonomy.
- **The craft section claimed to be the recurring diagnostic and no chapter was
  committed to running it.** Four forward references existed, to Chapters 3, 8, 10
  and 12, and none was the mapping. G3 cannot fail a promise that was never made.
  RULED AND APPLIED: the craft section names Chapter 8, and `continuity.py` now
  reads that sentence as a forward reference, so Stage 9 logs it and G3 holds
  Chapter 8 to it. **Verified rather than assumed**, by re-running the scraper.

**Q3, is any of this another chapter's.**
- **What S1-3 missed: section 2.7's three-part apparatus**, record, attribution and
  constraint, which Chapters 8 and 10 build. **RULED NOT A BREACH by Claude and
  reported because the step requires the weakest reading to be stated:** the three
  parts are the three verbs of THM-004's fourth antecedent, and unpacking an
  antecedent of the chapter's own anchor theorem is what a chapter is for.
- **RULED BY DAN 2026-08-24: THE DECISION 74 DIVISION IS CORRECT.** Adoption-as-value
  is taught in section 2.6 and, since Decision 74, assessed in Chapter 6's
  sort-and-repair. The Decision 74 note said the point was that the skill is taught
  once, and the division reads against that note until the two verbs are separated:
  **2.6 TEACHES the substitution and Chapter 6 ASSESSES it, which is one teaching
  and one assessment rather than the same skill taught twice.** Section 2.6 needs
  the substitution to make the asymmetry land and cannot defer it. **No chapter edit
  follows and the front-run box clears**, because nothing in 2.6 belongs to Chapter
  6: what Chapter 6 owns is the exercise, which is already there.
- **THE GENERAL FORM IS WORTH CARRYING FORWARD, because this will recur every time
  a competency is split across chapters.** Decision 74's "taught once" governs
  teaching, not the assessment that tests it, so a chapter teaching a skill a later
  chapter assesses is the division working rather than a breach of it. The
  front-run check reads WHAT A SECTION CLAIMS, not whether a later chapter names the
  same subject.

**Q4, could any of the eight teaching sections be cut.** Seven are load-bearing on
stated grounds. **Section 2.3 is the only section delivering no key term, no
definition callout, no clause of the big idea, neither competency and not the
anchor theorem**, and problem P4 rests on it alone; nothing else in the chapter
depends on it, which was checked against the summary, the key terms, the callouts,
the discussion questions and the other three problems. **DAN RULED OPTION B:** keep
the section and move only the review-cadence prescription to Chapter 10. Applied.
That paragraph was S1-3's second passage, so half of S1-3 is closed by this ruling,
and the cut also removed one uncited frequency claim. **Honest accounting: it saved
seven words. The gain was the boundary, not the length.**

**Q5, what is structurally missing.** Three findings, all ruled in and applied.
- **No real deployment in the chapter manages anything.** Every cited case comes back
  incomplete and the only managed example is constructed. A diagnostic returning one
  answer on every real input reads as a device for finding fault rather than an
  instrument. **The craft section now says so**, as a scope claim about the search
  rather than a claim about the world: no cited deployment was available on which the
  mapping returns a clean flow. Dan ruled against hunting for one, on the reasoning
  that the difficulty is the chapter's own argument.
- **C3 had no figure and C2 had one.** Chapter 1 gives each of its two results a
  figure. **Figure 2.2 now sets a complete cost across five workflows against a
  return measured on two**, and names the remaining three unknown rather than zero,
  which is the word the chapter says is load bearing.
- **The three flows were never said to be coupled.** The craft section demonstrated
  the coupling, a retailer manages its value half because a record already existed,
  and never claimed it. Section 2.4 now states it, so a reader diagnosing two
  unmanaged flows knows which to build first.

**A FIGURE IS JUDGED ON THE PAGE, AND FIGURE 2.2's FIRST GEOMETRY WAS WRONG.** Its
segment ticks ran the full height, so they sat hidden beneath both bars and dangled
through the empty band between them: the render read as a grid and a reader could
not count five segments under cost, which is the whole point of the figure. Rebuilt
with the ticks inside the bars and over the fills, and read again at 190 dpi.
**Gate 12 passed both versions**, because it counts captions and in-text references
and has no opinion about whether a figure is legible. This is the same rule the
accent pass recorded for the drawn marks, applied to a chapter figure.

**Q6 to Q8, the review checking itself.**
- **S1-4 IS OVERSTATED AND CLAUDE WITHDRAWS IT, SUBJECT TO DAN.** It said MIT NANDA
  is spent in Chapter 2 against a Chapter 6 supply the bank records as a gap. The
  bank was then read rather than remembered: CASE 6.2's placement line is "Ch2 or Ch6
  teaching body" and what it documents is the unknown-value-fraction claim at market
  scale, which is exactly Chapter 2's one use of it. CASE 6.3 needs classifiable
  statements, which the bank sources from Klarna and from the MIT-quoted executive
  lines. **A source is not a consumable, and the two chapters need different assets
  from the same report.** What survives is the bank's standing note that Chapter 6's
  supply should be built before Chapter 6 is drafted, and Pennsylvania is now banked
  toward it.
- **S1-3's two remaining passages are ruled not breaches by Claude, subject to Dan.**
  The record flow's three locations in 2.2 exist for the sentence after the list,
  that only the second and third belong to the buyer, and that ownership distinction
  is what the craft section's step 3 turns on. The scope-attached ratio in 2.6 names
  Chapter 12 in the same paragraph, which is the book's convention working rather
  than a breach of it.
- **S1-5 stands as recorded** and cannot cause rework, since it was already ruled not
  a defect.

**DAN RULED S1-3, S1-4 AND S1-5 ON 2026-08-24, AGREEING WITH ALL THREE READINGS AS
WRITTEN ABOVE.** S1-3's two remaining passages are not breaches. S1-4 is WITHDRAWN,
so the record of it stands as a finding that was raised and did not survive contact
with the case bank, not as a defect the chapter carries. S1-5 is confirmed. **No
chapter text changes as a consequence**, because all three rulings sustain the
chapter as it stands, and the re-run matrix is therefore not triggered.

**WHAT SURVIVES S1-4's WITHDRAWAL IS AN OBLIGATION, NOT A DEFECT.** The case bank's
standing note that Chapter 6's supply should be built before Chapter 6 is drafted is
unaffected by this ruling, and Pennsylvania's ChatGPT Enterprise pilot is banked
toward it. Withdrawing the finding retires the claim that Chapter 2 spent something
Chapter 6 needs. It does not retire the gap Chapter 6 still has.

**WHAT THE FIVE FINDINGS MISSED, in one list:** the taxonomy's provenance, the
uncommitted recurrence, C3's missing figure, the missing coupling, the absence of
any managed real deployment, and five uncited claims about what organizations
usually do. Four are fixed, one is stated, one is handed to Stage 3.

**HANDED TO STAGE 3, NOT RECORDED AS A STAGE 1 FINDING.** Five sentences claim what
organizations usually do, with no citation and no derivation: "managers routinely
underestimate it" (2.4), "Most organizations that believe they have cost governance
have the first, sometimes the second, and rarely the third" (2.7), "Organizations
are usually surprised by the second finding rather than the third" (craft), "the
flow this mapping most often finds missing" (craft) and "which is more than most
buyers do" (P3). **The last two were introduced on 2026-08-22 by the edits above.**
Standing rule 2 allows citation, recasting as a formal conditional, or cutting, and
no fourth option. A sixth candidate, "the record flow is skipped most often, and for
structural reasons rather than careless ones", is ruled clean because section 2.5
derives the structural reasons rather than asserting a frequency. Claude offered the
recast and Dan has not called for it.

**ONE REPO ITEM, BOOKED NOT FIXED.** `continuity.py` scrapes forward references from
the whole chapter file, including the `<title>` element and the source register's
`note` field, which gate W9b never publishes. It currently reads "the Chapter 1
convention is that a fixed document..." out of a fact-checking note as a promise
Chapter 2 makes to Chapter 1, and would log it into the ledger at Stage 9. Same
class as the gate 12 line-by-line defect and the first W16b: a check reading the
wrong input.

**WHY THE LEDGER BOX IS TICKED WHILE G3 REPORTS FAIL.** `continuity.py` fails on one
unpaid promise from Chapter 1, that problem sets begin reaching back to earlier
chapters in Chapter 2. **The chapter pays it**: the note under the problems reads
"Interleaving: question 4 and problem P2 require Chapter 1's results." Marking it
paid is `continuity.py --pay 1`, a Stage 9 operation, and running it now would be
editing the ledger to make a gate pass. Checks 1 and 4 of G3 are already clean:
zero term redefinitions and zero registry-gloss drift.

**NOTHING IS OUTSTANDING. STAGE 1 CLOSED 2026-08-24.** All four blockers are ruled,
all by Dan and none by Claude. S1-3, S1-4 and S1-5 were ruled on 2026-08-24, Dan
agreeing with Claude's readings; the Decision 74 division question from Q3 was ruled
correct the same day. **The two open boxes were ticked on that last ruling and not
before**, because both waited on it: the front-run box because the division is a
question about what belongs to Chapter 6, and "Dan has ruled every finding" because
the Q3 item is a finding of this review in everything but its numbering.

**NO CHAPTER TEXT CHANGED AT ANY OF THE FOUR RULINGS, so the re-run matrix is not
triggered and Stage 0 and G1 stand.** Every ruling sustained the chapter as it
stands. This is worth stating plainly because a cleared stage that changed nothing
looks, in a diff, like a stage nobody ran: the six edits Stage 1 DID produce landed
on 2026-08-22 from the earlier rulings, and they are recorded above.

**WHAT STAGE 1 HANDS FORWARD.** Five uncited claims about what organizations usually
do go to Stage 3, listed below. The Chapter 6 supply obligation survives S1-4's
withdrawal and is the case bank's, not this chapter's. Chapter 8 now carries the
craft section's mapping promise, which `continuity.py` reads and G3 will enforce at
Chapter 8's lock.

---

**Passing without qualification:** every slot serves the stated purpose, the craft
section is built as the recurring instrument, no Chapter 1 term is redefined,
"flow" is defined as the ledger requires, the interleaving promise is paid, and
forward references are declared rather than material silently borrowed.

**Next: Stage 2, the developmental edit.** Stage 1 is closed and this chapter's
independent read was Dan's own, so the second-model package was never sent.

**`AIOM_Ch02_Stage1_secondmodel_prompt.md` IS KEPT AND IS NOT SPENT.** It holds the
chapter, the findings and two reference extracts, ordered so a reviewer forms a view
BEFORE reading Claude's, with question 7 asking what this review missed. It remains
runnable at any time, and a finding it raises reopens Stage 1 through `reopen.py`
like any other. **CORRECTED 2026-08-28: the prompt was runnable and its chapter input
was seven commits stale.** See the Stage 2 record below. The extract is regenerated and
the package is runnable in fact as well as in claim. **This is the corrective the substitution record names**: closing
Stage 1 on Dan's own read buys his authority at the cost of independence, and the
package is what can still buy the independence back.


## Stage 2. Developmental edit

Owner: Claude

Status: [x]        Date cleared: 2026-08-28

> Teaching quality, held early so its line edits do not churn fact check, voice, design, and production. Clarity, pacing, cognitive load, example fitness, transitions, and whether the argument carries the target reader without a stall. Claude runs a fresh critical pass; Dan gut-checks with a second model and rules.

Findings:

**CLAUDE'S PASS COMPLETE 2026-08-24. NOT CLEARED: Dan's gut-check with a second
model is outstanding and Dan has ruled nothing.** Nine findings in
`03_Stage2_Developmental_Edit/AIOM_Ch02_Stage2_findings.md`, three of them high.
**Nothing is applied**, because the re-run matrix makes a body prose change re-run
Stages 2, 3, 4, 5 and G2, so applying before a ruling would spend those steps on
text that may not survive it.

- **DE1 (HIGH). Figure 2.1 arrives 575 words after the sentence that introduces
  it.** Measured, and the contrast is the evidence: Figure 2.2 sits 11 words after
  its own introducing sentence. Figure 2.1 is the artifact that makes the chapter's
  central construct holdable in one view, and it lands after the reader has carried
  the three flows unaided through the ownership division, three health tests, three
  locations and three speeds. **The figure that would reduce the load arrives after
  the load has been imposed.** Print gate 12 passes both figures identically, because
  it checks that a reference exists and has no opinion about how far away it sits.
- **DE2 (HIGH). The craft section and problem P1 map the same case to the same three
  diagnoses, in places near-verbatim.** Both read "A per-engineer cost range was
  reported, so consumption was visible at some grain" and both then turn on
  attribution and the plan. P1 is the WORKED problem, the chapter's one end-to-end
  demonstration for a reader who has not tried the diagnostic, and it is spent on the
  case the craft section finished mapping four pages earlier. **The chapter now
  demonstrates the diagnostic three times**, counting the constructed retailer.
- **DE3 (HIGH). "Cost-value asymmetry" is named in 2.4, defined at the end of 2.5,
  and titles 2.6.** The mechanism is built in 2.4, which says the asymmetry is what
  the chapter turns on. The callout sits in 2.5, which is about why the record flow
  is skipped and never uses the term. **The definition sits in the one section least
  about it**, a section after the rule that a coined term arrives after the mechanism
  it names. Any move re-runs `place.py` and gate 4, and Gap G-I means the affected
  pages need reading rather than only gating.
- **DE4 (MEDIUM). Section 2.2 carries six teaching jobs in 846 words**, the longest
  teaching section. Two of the six, the record flow's three locations and the three
  flows' three speeds, are consequences rather than taxonomy. One candidate remedy
  splits the section and therefore re-runs G1.
- **DE5 (MEDIUM). The record-decay claim and its illustration are three paragraphs
  apart**, with the chapter's turn sitting between them. Both halves lose: the claim
  waits for its evidence, and the turn is interrupted.
- **DE6 (MEDIUM). Discussion question 2 asks for an example section 2.4 already works
  in full**, in the same day-to-six-months frame. It tests recall while appearing to
  test transfer.
- **DE7 (MEDIUM). Six three-part structures, and the apparatus's three parts are the
  triad most confusable with the three flows.** Record, attribution and constraint all
  belong to the record flow, and the chapter never says so. **This one rests on reading
  rather than a measurement and is the finding Claude is least confident in.**
- **DE8 (LOW). The opening case reaches its payoff in the tenth of twelve paragraphs**,
  after five paragraphs deriving the seat-forecast mechanism. Recorded as a tension and
  not as a defect, because the slot permits variation in form and Dan ruled the case in.
  A second observation is recorded rather than raised: the case carries seven
  attributions of uncertainty, every one required by the register's UNVERIFIED status,
  and **the question resolves itself if Stage 3 verifies the sources**, so it may be
  cheaper to leave than to rewrite twice.
- **DE9 (LOW). Section 2.3's POSITION interrupts the continuity between 2.2 and 2.4.**
  **This does not reopen Stage 1's ruling to keep the section.** Moving it re-runs G1.

**WHAT THE PASS DID NOT FIND, recorded because a review that reports only faults
gives no information about what is safe.** The argument carries end to end without a
stall. The craft section is the chapter's strongest slot: it names its two failure
modes in advance, returns an unflattering diagnosis on the real case, and says plainly
that its clean example is constructed and why no real one was available.

**THE SELF-MARKING PROBLEM APPLIES HERE AS IT DOES AT STAGE 1, and the corrective is
built into the findings rather than asserted.** Claude drafted this chapter and is
reviewing it. Every finding above except DE7 and half of DE8 is anchored to a
MEASUREMENT or a QUOTED PAIR, so a reader can check it without trusting the reviewer,
and the two that rest on reading say so. **This is not a substitute for the second
model**, which is Dan's half of this step.

**INTERACTION WITH STAGE 3, and it needs whichever step moves first to say so.** Two
of the five uncited frequency claims handed to Stage 3 sit in passages DE5 and DE6
touch. If Stage 2's remedies land first, Stage 3 reads moved text; if Stage 3 moves
first, these findings need re-anchoring.

**THE SECOND-MODEL PACKAGE IS BUILT AND UNSENT, 2026-08-28.** Four files, in
`03_Stage2_Developmental_Edit/` except the chapter:

- `AIOM_Ch02_Stage2_secondmodel_prompt.md`, the prompt. It asks five questions the
  reviewer answers BEFORE opening Claude's findings, then four about the findings
  themselves. **Question 1 is the one the drafter structurally cannot answer**: where
  did you first stall. The drafter has read this chapter perhaps thirty times and can
  no longer be surprised by it. **Question 8 asks what is overstated**, and it is not
  a formality here, because two of the candidate remedies re-run G1 on the whole
  chapter and any body prose change re-runs four later steps.
- `AIOM_Ch02_prose_for_review.md`, the chapter as prose.
- `ch02_reader_model_extract.md`, section 2 of the prose standard and nothing else
  from it, because the rest governs voice and voice is Stage 4's.
- `AIOM_Ch02_Stage2_findings.md`, read last.

**WHAT IS OUT OF BOUNDS IS STATED IN THE PROMPT RATHER THAN LEFT TO THE REVIEWER.**
Fact and sourcing, because Stage 3 has not run and every figure is formally
unverified. Voice and replacement wording, because Stage 4 has not run. And the four
Stage 1 rulings Dan closed on 2026-08-24, named individually, so a reviewer cannot
reopen them by accident. DE9 is flagged in the prompt as concerning section 2.3's
position and not its existence, which is the distinction that ruling turns on.

**THE STAGE 1 PACKAGE HAD GONE STALE AND NOBODY WOULD HAVE NOTICED, FOUND
2026-08-28.** Its prompt was recorded above as remaining runnable at any time, and
its prompt was. Its chapter input was not: `AIOM_Ch02_prose_for_review.md` was last
generated on 2026-08-21 and the chapter moved seven commits after it, gaining Figure
2.2, a rewritten P3 on a cited real deployment, and the 2.8 provenance paragraph.
**A reviewer sent that package would have reviewed a chapter that no longer exists
and reported on a figure the chapter does not have.** This is the repository's own
signature failure, a record claiming to be current while its input has moved, and it
is recorded here so Chapter 3 does not repeat it. The extract is regenerated and both
packages now point at the live text.

**THE SECOND MODEL'S REVIEW IS IN, 2026-08-28, AND IT HOLDS STAGE 2 OPEN.** Recorded
verbatim in `03_Stage2_Developmental_Edit/AIOM_Ch02_Stage2_secondmodel_review.md`, with
the only alteration being em dashes replaced under standing rule 1 and no word changed.
Claude's verification of every checkable claim is appended there in its own marked
section. **Dan rules all of it and Claude rules none of it.**

**THE HEADLINE IS NOT ONE OF CLAUDE'S NINE.** The reviewer's verdict is that the chapter
teaches, the conceptual spine should not be rebuilt, and the argument carries end to
end, but that **the diagnostic itself is not yet internally stable**, and that this
matters more than most of DE1 to DE9 because the three-flow mapping is the chapter's
runnable artifact. Its revision order is NEW-1, NEW-2, DE1, DE2, NEW-3.

**FIVE NEW FINDINGS. All five verified against the chapter by Claude.**

- **NEW-1 (HIGH). VERIFIED. The craft procedure contradicts its own worked example.**
  Craft Step 2 says "If no count exists, that is a finding about the record flow rather
  than the usage flow." Three paragraphs later the Uber mapping downgrades the USAGE
  flow to partly managed, citing 2.2 by name, precisely because request counts cannot
  be established. **THE CONTRADICTION WAS CREATED BY A FIX, and the history is the part
  that binds later chapters.** Step 2's sentence dates from the Stage 0 draft
  (`ec92f25`). The mapping's diagnosis changed at `d89c9df`, the commit applying the
  second-model BIAS REVIEW, whose best finding was that this same mapping had graded the
  flow "managed and healthy" against a test 2.2 sets. **The fix corrected the worked
  example and left the procedure the example follows.** No gate in either suite reads a
  procedure against its own worked example, and none could without reading meaning.
- **NEW-2 (HIGH). VERIFIED as an absence.** The chapter uses managed, partly managed and
  unmanaged in eight places and defines the boundary between them in none. Step 5 names
  the three states and stops. The only threshold sentence in the chapter is one instance
  for one flow, "an organization that can attribute half its consumption has a partly
  managed record flow", and nothing generalizes it. Two readers can follow Steps 1 to 4
  identically and diagnose differently without breaking any rule the chapter teaches.
- **NEW-3 (MEDIUM). VERIFIED.** P2 says "State which of the three antecedents of
  THM-004"; the panel lists four, (i) through (iv). A reader cannot comply with the
  instruction as written. **The panel is not the thing to change**, since rule 4a puts it
  beyond editing and `registry.py` checks it against the pinned manifest. The error is in
  the problem, which is the book's own text.
- **NEW-4 (MEDIUM). VERIFIED, AND THE CAUSE IS WORSE THAN REPORTED WHILE HALF OF IT IS
  CLAUDE'S.** The chapter carries four problems and three `div.problem` wrappers: **P4
  has none of its own and sits inside P3's**, which closes only after P4's last
  paragraph. Chapter 1 carries three problems in three divs. **No gate catches it and no
  read would have**, because `.problem .plab` and `.problem .ptitle` are descendant
  selectors, so P4 keeps its type and loses only the 15pt inter-problem margin. The
  MISSING LABEL the reviewer saw was `prose_extract.py` taking the first `plab` per
  block, so **a real markup fault reached the author disguised as a smaller one**. The
  extractor is fixed and re-verified against both chapters; the chapter markup is
  untouched and is Dan's.
- **NEW-5 (MEDIUM). VERIFIED as a placement fact, and the precedent strengthens it
  beyond what the reviewer had.** The MIT NANDA paragraph is running body prose in 2.6.
  **Chapter 1 admits dated evidence into its teaching body and quarantines every instance
  in a `.dated` box**, the January 2025 OpenAI correction and the July 2025 Anthropic
  limits among them. Chapter 1 has two such boxes. **Chapter 2 has none.** So the
  question is not whether dated evidence may sit in a teaching body, which it plainly
  may, but whether this passage may sit outside the device the book built for it. Stage 1
  ruled on NANDA's CHAPTER ASSIGNMENT under S1-4 and did not rule on its containment, so
  this reopens nothing.

**WHAT THE REVIEWER CONFIRMED, DOWNGRADED AND REJECTED.** DE1 and DE2 confirmed at HIGH
and ranked third and fourth overall. DE4's load confirmed but its remedy resisted until
DE1 is fixed and 2.2 reread. DE5 and DE6 confirmed at lower severity and worth doing
only inside a re-run that is already happening. **DE3 downgraded from HIGH to LOW**, on
the ground that the callout sits immediately before 2.6 opens on "The consequence of the
asymmetry", so the coined-term rule is satisfied and no first-pass difficulty arose. DE7
mostly rejected: the reviewer did not confuse the triads and reads the real problem as
NEW-2. DE8 rejected as a defect and kept as an observation. DE9 confirmed as a real seam
but not as a mandate to move a section and re-run G1. **The reviewer explicitly advises
against acting on DE3, DE7, DE8 and DE9 at all**, given what a body prose change costs.

**DE4 IS CORRECTED IN THE FINDINGS FILE AND THE CORRECTION IS THE REVIEWER'S.** DE4
asserted 2.2 was the longest teaching section at 846 words. Measured with citations and
figures stripped, **2.2 is 838 words and 2.6 is 865**. The superlative is struck; the
six-jobs count stands and carries the finding. **This was an error Claude made about a
chapter Claude drafted, inside a finding written to show the findings could be checked
without trusting the reviewer.** It is the clearest evidence in this step that the
independent read earned its cost, and it is the second time on this chapter that an
outside read found something the drafter could not see in its own work.

**WHAT REMAINS UNVERIFIED AND IS PURE JUDGMENT.** The DE3 severity disagreement rests on
no disputed fact: both descriptions of where the callout sits are accurate, Claude read
the position as a section late, and the reviewer read it as adjacent to the point of use.
The 2.6 to 2.7 transition and the count of sixteen associations at the 2.2 peak are
readings rather than measurements and are recorded as written.

**STAGE 2 STAYS OPEN AND NOTHING IS APPLIED.** Fourteen findings now stand unruled, nine
Claude's and five the reviewer's. The re-run matrix is unchanged: any body prose change
re-runs Stages 2, 3, 4, 5 and G2, so the batching question is Dan's and matters more now
than it did at nine findings.

---

## Stage 2 remedies applied, 2026-08-28

**DAN RULED OPTION A: NEW-1, NEW-2, DE1, DE2, NEW-3 and NEW-4, in one batch.** All six
are applied to the live text. **The print render passes all fifteen gates**, and the
committed state was rebuilt for attribution, so every gate result below is measured
rather than assumed.

- **NEW-1 applied.** Craft Step 2's last sentence now reads "If no count exists, record
  that against both flows: the record flow is missing the count, and the usage flow
  cannot be called managed without one." **The direction of this fix was determined by
  the record, not chosen.** The alternative was to keep Step 2 and restore the Uber
  mapping's earlier "managed and healthy" diagnosis, which would have reversed the bias
  review's BR5 finding and 2.2's own health test. Only one direction reopens nothing.
- **NEW-2 applied**, as a paragraph after Step 5: two tests, both of which a flow must
  pass to be called managed, the first that the organization can state the flow's
  condition from a record it holds itself and the second that the record is fine enough
  that a decision follows from it. Partly managed is one test and not the other, or part
  of the condition and not the rest; unmanaged is not being able to state it at all.
  **The rule was checked against every worked instance in the chapter before it was
  written**, and it returns the diagnosis the chapter already gives in all of them: both
  Uber flows partial, the retailer's three managed, the value half unmanaged, and the
  half-attributed record partial. The half-attribution example moves here from the later
  paragraph, which keeps only what it alone says.
- **DE1 applied, AND NOT AT THE ANCHOR THE FINDING NAMED.** DE1's remedy (a) put the
  figure immediately after its introducing sentence. That renders and passes fifteen
  gates, **and it leaves page 5 a third empty**, because the figure will not fit below
  the introducing paragraph and pushes to page 6 while the paragraphs that would have
  filled page 5 go with it. Five anchors were built and measured. The figure lands at the
  top of page 6 from four of them, so the anchor that also fills page 5 is free. **It is
  now after the four-owner paragraph**: the reference sits two paragraphs from the foot
  of page 5, the figure opens page 6, and the three health tests, the three locations and
  the three speeds are all read with the figure in view, which is what DE1 asked for.
- **DE2 applied by remedy (c), the one that costs no source.** P1 is repointed from
  "Mapping a deployment from public reporting" to "The review that would have changed the
  outcome". It now starts from the craft section's finished diagnosis instead of
  reproducing it, and asks for the record, the grain and the owner each flow would have
  needed for a February review to change anything. **The worked answer reaches something
  the chapter had not stated**: two of the three gaps were closable in February and the
  third was not, because a return measured after the fact requires a measurement taken
  before. The craft section's Uber mapping is untouched, so nothing is lost.
- **NEW-3 applied.** P2 now asks for four antecedents.
- **NEW-4 applied.** P4 has its own `div.problem`. Four problems, four wrappers, and gate
  10 reports "4 found, all with their title".

**THREE SENTENCES WERE TIGHTENED IN THE NEW P1** after `voicecheck` put them at 36, 37
and 40 words. Two are now pairs and one is split at its natural break. Nothing else about
them changed.

### DE3: APPLIED, THEN RULED BY DAN ON 2026-08-28. CONFIRMED AS APPLIED.

**Dan ruled option A on 2026-08-28**: the move stands and DE3 closes as applied. The
reasoning he ruled on is below, and it was put to him as three options, the other two
being to reverse the move and give up something else to satisfy gate 4, or to keep the
move while recording DE3's developmental claim as unproven. **DE3 is therefore a closed
finding and not merely a pagination outcome**: the callout now arrives after the
mechanism it names, which is what the standing rule asks for.

**Applying DE1 broke gate 4, and `place.py` could not fix it.** The committed chapter
passed all fifteen gates; after DE1 the Cost-value asymmetry callout split across a page
break, and the placement pass reported **"'Cost-value asymmetry' has no alternative
anchor in its section, stopping"**. Section 2.5 is 300 words and offers the pass nothing
to work with.

The only remaining remedy was to move the callout out of 2.5, which is DE3. **Both
candidate positions were built and gated rather than reasoned about.** The head of 2.6
still splits. The end of 2.4, directly after the paragraph that builds the mechanism,
passes all fifteen. That is DE3's own remedy (a).

**The reviewer's argument against acting on DE3 was cost, not merit.** Both reads agree
the callout sat a section away from the mechanism it names; they disagreed only about
whether moving it was worth a re-run. The re-run was already happening, and the
alternative to moving it was shipping a chapter that fails a gate. **Page 9 was
rasterized and read**: the callout now floats beside the paragraph that builds the
asymmetry, whole, with no collision with any panel, which is Gap G-I checked rather than
assumed.

### A PAGE THAT IS A THIRD EMPTY PASSES ALL FIFTEEN GATES, AND THIS SHOULD GRADUATE

**No gate in the print suite measures how much of a page is used.** Gate 13 checks that
nothing sits below the text block and gate 14 checks widows, orphans and stranded heads.
A figure that does not fit, pushing to the next page and taking its neighbours with it,
leaves a hole 217pt deep in a 25-page chapter and every gate reads green. **It was found
by rasterizing page 5 and looking at it**, which is the rule already in force for figures
and for callout placement, arriving at a third kind of defect. DR3a records a short page
as an accepted cost in Chapter 1; this one was not accepted and did not have to be.
**Dan's to rule for CLAUDE.md.**

### What was measured after the batch

- **Print: all fifteen gates pass** on the live text, 25 pages. Attribution was done
  against the committed state rather than assumed, which is how the gate 4 failure was
  known to be DE1's rather than pre-existing. Page 11's short page is in the committed
  baseline too and is not from this batch.
- **`voicecheck`: Stage 4 mechanical PASS and house style PASS.** Zero em dashes, zero
  contractions, zero straight marks, no paragraph over 150 words.
- **Pages 5, 6, 9, 17, 20 and 22 were rasterized and read.** Page 6 opens on Figure 2.1
  with the health tests beneath it. Page 9 carries the moved callout clean. Page 17 holds
  all five diagnostic steps and the new decision rule in one view, which is the best
  outcome available for NEW-2. Pages 20 and 22 end short because a summary and a key-term
  list end where they end.
- **`chapter_check.py Ch02`: W14 pass, voicecheck pass, print pass, registry pass,
  checklist self-consistent.** The web build and G3 still report failures and both are
  the expected shape for a chapter at Stage 2: W2 because the chapter is not locked, W10
  because a single-chapter build omits locked Chapter 1, and G3 because the continuity
  ledger carries no Chapter 2 entries until lock.
- **The chapter is 7,513 words**, from 7,257.

### What was NOT applied, and why

**EVERY STAGE 2 FINDING IS NOW RULED. See the per-finding records below.** Option A excluded
them and the reviewer advised against acting on DE7, DE8 and DE9 at all. **NEW-5 is the
one item in the excluded set that has a determinate remedy waiting**, since Chapter 1
already carries the `.dated` device the MIT NANDA paragraph would go into.

### A SECOND INSTANCE OF THE EMPTY-PAGE DEFECT, FOUND AFTER STAGE 2 CLOSED

**Page 11 carried the same defect as page 5 and had done since 2026-08-22.** The page
ended on "Figure 2.2 sets the two quantities against the scope each covers" and then
stopped, 191pt short, because Figure 2.2 would not fit at the foot of the page. **It is
the worse instance**, because the reference is the last line, so a reader is told to look
at a figure and turns away from a hole.

**IT WAS MISSED BECAUSE "NOT MINE" WAS TREATED AS "NOT A PROBLEM".** When the gate 4
failure was attributed against the committed state, page 11's gap was correctly reported
as pre-existing and then left. Establishing that a defect is not yours is the first half
of attribution, and the second half is looking at it.

**Fixed by moving Figure 2.2's anchor one paragraph later**, which is the same remedy the
page-5 hole took. Page 11 now fills, the reference stays on page 11, the figure opens page
12, and all fifteen gates pass. Three later anchors were built and measured; the nearest
was taken.

**`AIOM_build.py` NOW PRINTS PAGE FILL AS AN ADVISORY, Dan's ruling of 2026-08-28.** It
names any page leaving more than 110pt of the text block unused and never fails, because a
short page is often correct. **It was verified in both directions rather than assumed**:
it reports Chapter 1's page 24, which is DR3a's accepted cost, and a negative control that
restored the old Figure 2.2 anchor made it name page 11 and quote the dangling sentence.
The rule and its reasoning are graduated into CLAUDE.md section 6.

**THE REMEDY IS COUNTERINTUITIVE AND IS NOW RECORDED THERE TOO.** A figure that will not
fit is moved LATER, not earlier. Both figures land at the top of the following page from
any of several anchors, so the anchor decides only whether the paragraphs between the
reference and the figure fill the current page or follow the figure onto the next. Placing
a figure immediately after its introducing sentence, which is what a developmental finding
will ask for and what DE1 did ask for, is the one choice that empties the page.

### STAGE 2 CLEARED 2026-08-28, AND THE HOLD CONDITION WAS CHECKED RATHER THAN ASSUMED

**Dan ruled option A of three and Stage 2 is closed.** Claude's pass, the second model's
independent check, and Dan's ruling on every one of the fourteen findings are all
complete.

**THE SECOND MODEL SET A CONDITION FOR CLOSING AND IT WAS NOT MET BY THE BATCH.** Its
verdict was to hold Stage 2 open "until the three-flow mapping itself becomes internally
deterministic". Running the finished diagnostic against the chapter's own worked cases
rather than asserting the condition found that two of the three flows resolve correctly
under the new rule and **the third does not**. Step 4 instructs a reader to trace the
cost-and-value flow "in two halves", every worked instance then diagnoses it by half, and
Step 5 and the NEW-2 rule both assign one label per flow. **A reader following the
procedure reached the third flow and had to guess whether to give it one diagnosis or
two, with the chapter's examples answering differently from its rule.**

**This was a residual of Claude's own NEW-2 remedy**, in the same family as NEW-1, and it
was found only because the condition was tested. One sentence closes it, appended to the
rule paragraph:

> The cost-and-value flow takes a diagnosis on each half, because step 4 traces it that
> way and its two halves are built by different people to different standards.

**WHAT CLOSING THIS STEP CHANGES MECHANICALLY.** Stage 2 owns no check in
`chapter_check.py`, so ticking it binds nothing new by itself. The chapter is now at 4 of
13 and Stage 3 is next, which is Dan's and external.

**Verified at close:** all fifteen print gates pass on the live text at 25 pages, gate 9
among them for the first time on this chapter; `voicecheck` passes mechanical and house
style with no paragraph over 150 words; `chapter_check.py Ch02` reports no broken claim.
The chapter is 7,513 words at the Decision 33 measure.

### DE7, DE8 and DE9: RULED TOGETHER BY DAN 2026-08-28. RECORDED, NOT ACTED ON.

**Dan ruled option A of two.** The three were put as one decision because the second
model's advice was identical for all three and both reads had converged on each. No text
changed.

- **DE7, six three-part structures.** Mostly rejected by the reviewer, who did not confuse
  the triads and read the real problem as the missing decision rule, which is NEW-2 and is
  applied. **The residual claim in Claude's own finding was checked and is not quite
  right.** DE7 said 2.7 never ties the apparatus's three parts back to a flow. The
  paragraph immediately after the triad reads "A dashboard nobody acts on is a record flow
  with no constraint attached", which makes exactly that link. It is oblique and one
  paragraph late, and it is in the text. DE7 has very little left.
- **DE8, the opening case's five paragraphs before its payoff.** Rejected as a defect by
  the reviewer: the intervening forecast and consumption material does genuine causal
  setup and the case does not read as withholding its point. Claude's finding had already
  declined to rule it, since the skeleton permits variation in form inside the
  opening-case slot and Dan ruled the case in. **Its second half is not a defect at all**:
  the seven attributions of uncertainty are each required by the register's UNVERIFIED
  status, and the question resolves itself if Stage 3 verifies the sources, so acting now
  would mean rewriting twice.
- **DE9, section 2.3's position.** Both reads confirm a real seam between 2.2 and 2.3 and
  both stop short of moving the section, the reviewer because the section title does the
  bridging and because a move re-runs G1 to buy a smoother argument rather than to close a
  defect. Nothing in the batch changed the seam. **This does not disturb Stage 1's ruling
  that 2.3 is kept**, which was never in question here.

### NEW-5: RULED BY DAN 2026-08-28. APPLIED, AND IT WAS UNDER-SCOPED BY ONE INSTANCE.

**Dan ruled option A of three.** Both instances are fixed.

**THE REVIEWER FOUND ONE AND THERE WERE TWO.** Scanning the whole teaching body turned up
the MIT NANDA paragraph in 2.6, which NEW-5 named, and **"Uber's position in April 2026 is
the first error in progress"**, also in 2.6, which it did not.

**CHAPTER 1 DRAWS THE LINE AT THE DATE, NOT AT THE NAME, AND THAT MADE BOTH REMEDIES
DETERMINATE.** Its teaching body outside its two `.dated` boxes carries ZERO year
references, and it names ChatGPT, Copilot, Cursor and GitHub in body prose. So the
precedent is not that products go unnamed in a teaching body. It is that dates are
quarantined and names are not. **The reviewer read the rule as being about the study and
it is about the year.**

- The Uber sentence now reads "Uber's position in the opening case is the first error in
  progress." The name stays, the date goes, and the reader is pointed at the slot where
  the date lives.
- The NANDA paragraph moves into a `.dated` box labelled **"Dated: August 2025"**, which
  is the register's own `date` field of `2025-08` rather than a date anyone chose. The
  paragraph after it, carrying the durable point about "no measurable impact", stays as
  body prose. That is Chapter 1's shape exactly: box, then the timeless lesson drawn from
  it.

**MEASURED AFTER THE FIX: the Chapter 2 teaching body carries no year outside a dated
box**, which is now the same statement that is true of Chapter 1.

**IT ALSO WOKE A GATE THAT HAD NEVER RUN ON THIS CHAPTER.** Gate 9 pixel-samples each
dated box for a hairline left rule against its label and had reported "none in this
chapter" on every build since Stage 0. It now reports "1 labelled, 1 rules, max rule width
2px". All fifteen gates pass, still 25 pages, and page 13 was rasterized and read.

**`prose_extract.py` DID NOT KNOW ABOUT DATED BOXES AND NOW DOES.** It flattened the box
to a bare paragraph reading "Dated: August 2025", which would have hidden from any future
reviewer the one thing they most need to see about that material, that it is quarantined
rather than asserted in body prose. Both chapters' extracts were regenerated; Chapter 1's
two boxes now render as boxes as well.

### DE6: RULED BY DAN 2026-08-28. APPLIED.

**Dan ruled option A of three.** Discussion question 2 is replaced. It now reads:

> The chapter claims that an unmanaged record flow decays rather than merely staying
> empty, and gives the case of an engineer whose forty calls lose their context within a
> month. Using that case, state what would have had to be recorded at the moment the work
> happened for the record to have survived, and explain why nobody present had a reason
> to record it.

**THE CHAPTER'S OWN EXAMPLE IS NOW THE PREMISE RATHER THAN THE ANSWER**, which is what
DE6 asked for. The old question could be answered by reproducing section 2.4, so it
tested recall while appearing to test transfer, and both reads confirmed it. The second
clause forces a structural account rather than a blame narrative, which is the guard the
voice standard keeps, and it makes a reader join 2.4's decay to 2.5's reason that the
record flow pays only in the future and belongs to no single function. **The chapter
asserts those two things in two places and never joins them in one.**

**REMEDY (a) WAS PUT ASIDE AND SHOULD NOT BE REVIVED.** DE6 offered asking for an example
from the reader's own organization. Discussion question 5 already uses that exact device,
and two of five questions turning to the reader's own organization is a pattern rather
than a variation.

**NO COMPETENCY MOVED.** Stage 1 ruled that C3 is delivered by discussion question 3, so
nothing in the competency delivery depends on question 2.

**TWO PROXIMITIES ARE RECORDED RATHER THAN BURIED.** The new question sits nearer Chapter
8, which builds the event record schema, than the old one did, though it asks for
reasoning rather than a schema and Stage 1 ruled comparable passages not breaches under
S1-3. And it is nearer the rewritten P1 than DE6 could have anticipated, since P1 was
repointed in the same batch: P1 asks what a deployment needed for a review, this asks
what one morning's work needed at the moment of capture. **Different scale, and they now
rhyme. Stage 3 and the final read should both look at the pair.**

**Verified:** all fifteen print gates pass, still 25 pages, `voicecheck` mechanical and
house style both pass, and page 22 was rasterized and read. All five questions sit on one
page and the new question 2 is the longest of them at 64 words, from 43.

### DE5: RULED BY DAN 2026-08-28. RECORDED, NOT ACTED ON.

**Dan ruled option A of four.** Section 2.4 is unchanged.

**PAGINATION DID NOT DECIDE THIS ONE, AND THAT WAS ESTABLISHED BEFORE THE QUESTION WAS
PUT.** Every candidate ordering was built and gated: DE5 as written, DE5 with the turn
placed last, and a fourth ordering neither read proposed. All four pass fifteen gates
with identical short-page profiles, so nothing mechanical forced the ruling and it was
made on the writing alone.

**WHAT DECIDED IT IS A STRUCTURE NEITHER READ NOTICED.** The three middle paragraphs of
2.4 are a parallel triad, one per flow: usage grows, records decay, cost-and-value
accrues on one side only. That triad is the section's argument and its title, and DE5's
remedy breaks it by dropping the illustration in after the record paragraph, halfway
through a parallelism the reader is following. **The current order states the pattern for
all three flows and then illustrates the one that is least intuitive**, which is a
defensible structure rather than the oversight DE5 read it as.

**WHAT SURVIVES THE RULING.** The illustration is still the strongest concrete particular
in the teaching body and still lands after the section's climax. The finding is recorded
as observed and outweighed, not as wrong. The fourth ordering, swapping the coupling
paragraph and the illustration, keeps the triad intact and moves the illustration one
paragraph closer to its claim; it is gated clean and available if a later step wants it.

### DE4: RULED BY DAN 2026-08-28. RECORDED, NOT ACTED ON.

**Dan ruled option B of three**, after the reassessment the second model asked for. The
alternatives were splitting 2.2 after the four-owner paragraph, which is permitted since
`AIOM_Structure_v1.md` fixes Chapter 2's big idea, competencies, anchor theorem and craft
section and says nothing about section count, or DE4's own remedy (b).

**The finding is confirmed and its cause is addressed.** DE4 said a reader carries six
jobs through 2.2 with nothing to hold them in. Figure 2.1 now opens page 6 with the three
health tests directly beneath it, and 2.2 runs pages 4 to 7, so the locations and the
speeds are read with the figure on the facing page or one turn back. Re-measured after
the batch, 2.2 is unchanged at 838 words across 13 paragraphs and still carries all six
jobs. **What changed is not the section but what the reader has while reading it.**

**REMEDY (b) IS WITHDRAWN AND SHOULD NOT BE REVIVED.** DE4 called it the cheapest
option. It is not a good one. The three-speeds material already sits at the end of 2.2
immediately before 2.3 opens, so moving it into 2.3 changes which heading it sits under
and nothing a reader experiences. And 2.5 argues why the record flow is skipped, not
where it lives, so the three locations would land in a section whose argument they do not
serve.

**LENGTH IS NOT THE DEFECT AND THE CHAPTER'S OWN NUMBERS SAY SO.** Section 2.6 is 865
words across 12 paragraphs, longer than 2.2, and neither read flagged it. That leaves the
six-jobs count as the whole of the finding, and it is also why the superlative struck
from DE4 earlier mattered: the finding read as stronger than it was for as long as 2.2
appeared to be the longest section. A split would additionally give the teaching body
nine sections, where both the reviewer and DE9 already treat eight as a lot.

**THE EXTRACTOR IS NOW A COMMITTED SCRIPT, `prose_extract.py`, and the reasoning is
the one that promoted `factcheck_packet.py` to the root.** The same extraction had
been written from scratch three times on this chapter, for the bias check, for Stage
1 and now for Stage 2. **The throwaway version invented a slot label the chapter does
not carry**, a `[TEACHING BODY]` heading that appears in neither Chapter 1 nor
Chapter 2, because the six-slot skeleton signposts through structure rather than
through labels. It also dropped every key term's NAME, printing six definitions with
nothing to attach them to. The committed version keeps term names, marks each figure
in place with its caption, renders the theorem panel as a structured conditional,
excludes the source register and the citation markers, and was verified by comparing
its word multiset against the chapter's own: no prose dropped and none duplicated.

---

## Stage 3. Source and fact check 1

Owner: Dan

Status: [x]        Date cleared: 2026-08-29

> Every empirical claim traced to primary source. Runs after the developmental edit, so it checks prose that has stopped moving.

Findings:

### STAGE 3 CLOSED 2026-08-29 ON DAN's RULING. TWO ENTRIES OF FIVE ARE VERIFIED AND TWO ARE CARRIED TO STAGE 7.

**This is a first fact check, not a final one, and the two unresolved entries go to
Stage 7 rather than being waved through.** Recorded plainly so nobody later reads a
ticked box as meaning the chapter's sources were all read.

| Entry | State at close |
|---|---|
| `uber-2026-budget` | **VERIFIED** by Dan, rows A1 to A6. Still secondary; the primary is paywalled. |
| `fortune-2026-uber-coo` | **VERIFIED** by Dan, rows B1 to B3, with a title correction and a direct quotation. Secondary to a recorded interview. |
| `uber-2026-adoption` | **SETTLED.** Cites no document by Dan's 2026-08-21 ruling; S3-1 and S3-2 make the footnote say so. |
| `mit-nanda-2025` | **CARRIED TO STAGE 7.** No location. S3-3 stands and its remedy is the report itself. |
| `dta-copilot-2024` | **CARRIED TO STAGE 7.** Grade C, unread by anyone. |

**WHAT THE TWO CARRIED ENTRIES ACTUALLY EXPOSE, because "unverified" is not a uniform
risk.**

- **`mit-nanda-2025` degrades and the chapter was built for that.** Its note records
  that the ninety-five per cent figure drew methodological criticism and that reported
  interview counts vary, and **the chapter rests its argument on the phrase "no
  measurable impact" rather than on the figure's precision**, stating the criticism
  once. A corrected figure narrows a sentence; it does not collapse an argument.
- **`dta-copilot-2024` does not degrade, and it is the larger exposure of the two.**
  Problem P3 is built entirely on it: the trial dates, around sixty agencies, several
  thousand licences, per-seat pricing, and the evaluation's two statements about its
  own method. **Nobody has read the evaluation.** The external check's claim to have
  verified it was rejected as S3-R1, because a model with no source access reported
  that its recollection agreed with three sentences it had just read. If the published
  evaluation contradicts any of those, P3 needs rebuilding rather than rewording.

**DECISION 48 IS NOT SATISFIED ON THOSE TWO AND THIS BOX DOES NOT PRETEND OTHERWISE.**
It requires every source verified live with an access date, and both carry
`accessed: null`. The chapter's own provenance line on page 1 says "pending source
verification", which is the disclosure the external check correctly credited it with
and which Claude wrongly denied at S3-R2.

**WHAT TICKING THIS BOX CHANGES MECHANICALLY.** Stage 3 owns W14, so claim
preservation now BINDS in `chapter_check.py` rather than reporting: the eleven rulings
FQ1 to FQ8 and S3-1, S3-2, S3-4 fail the build if a later step reverts one. That is the
point of closing it before the copy edit, and it is the protection Chapter 1 did not
have when SF8, SF9 and SF10 were reverted with every date and figure intact.

**Verified at close**: W14 pass at 11 rulings, voicecheck mechanical and house style
pass, all fifteen print gates pass, page fill clean, web build pass, G3 pass, registry
pass, checklist self-consistent. The chapter is 25 pages.


### THE PACKET IS BUILT AND THE STEP IS WITH DAN, 2026-08-29

**Three files sit in `04_Stage3_Source_Fact_Check_1/`.** The render, the generated
packet, and a cover note that names what the packet cannot see. Read the cover note
first.

- **`AIOM_Ch02_Stage3_render.pdf`**, 25 pages, all fifteen print gates green and the
  page-fill advisory clean. **The external check is fed this, never the chapter
  HTML**, because both production flags on Chapter 1's first check were phantoms of
  HTML extraction.
- **`AIOM_Ch02_Stage3_packet.md`**, 7 cited passages against 5 register keys, all
  five cited, zero orphans and zero dangling. Every register note reproduced
  verbatim, including the two that carry explicit Stage 3 instructions.
- **`AIOM_Ch02_Stage3_cover.md`**, which carries the five uncited frequency claims.

**THE FIVE UNCITED CLAIMS APPEAR IN NO GENERATED ARTIFACT AND THAT IS WHY THE COVER
NOTE EXISTS.** They carry no citation marker, so `factcheck_packet.py` cannot see
them, and Stage 1 handed them forward in prose that only this checklist held. All
five were confirmed present and unmoved in the live text on 2026-08-29, each
occurring exactly once, because Stage 2 touched the passages holding two of them and
the re-anchoring risk was recorded rather than resolved.

**`factcheck_packet.py` WAS PRINTING CHAPTER 1's HISTORY INTO A CHAPTER 2 PACKET,
FOUND AND FIXED THE SAME DAY.** The tool was promoted to the root on 2026-08-10 so
that fifteen chapters would not each rebuild it, and it had only ever run on Chapter
1, so six facts about that chapter were hardcoded in its preamble. The first
Chapter 2 packet was titled "Chapter 1", told a checker not to re-raise SF1 through
SF10, reported 6 footnotes against an actual 9, and claimed a value surface
"identical to the Stage 3 audited render" for a chapter arriving AT Stage 3. **A
packet that states checks nobody ran is this repository's signature failure,
committed by the one artifact an external checker is meant to trust.** The title,
the footnote count, the register closure result and the ruled-form line are now
computed from the chapter; the value-surface line is removed, because the script
never performed that check and a Chapter 1 measurement taken by hand was being
printed as though it had. Verified by rebuilding Chapter 1's packet, which reports
6 footnotes and its 8 live rulings correctly.

### DAN RULED THE EXECUTIVE NAMED AND QUOTED DIRECTLY, 2026-08-29. THE BOOK'S FIRST DIRECT QUOTATION.

**Both open prose questions raised at the verification are now closed, and Dan took the
same answer to each.** The opening case reads:

> President and chief operating officer Andrew Macdonald said publicly that the company
> could not yet draw a line from its rising use of the tool to the consumer features it
> was producing. "That link is not there yet," he said. The statement suggests a
> documented return was unavailable, incomplete, or unpersuasive to senior leadership.

**THE ATTRIBUTION FOLLOWS CHAPTER 1 EXACTLY**: title, then full name, then "said
publicly that". Chapter 1 reads "Chief executive Sam Altman said publicly that the
company was losing money on its two-hundred-dollar Pro subscriptions", and that string
is REQUIRED text under SF1.

**THE QUOTATION DOES NOT FOLLOW CHAPTER 1, BECAUSE CHAPTER 1 QUOTES NOBODY.** Checked
rather than assumed: the locked Chapter 1 body carries zero direct quotations. **This
is the book's first**, so it sets the house form for the fourteen chapters after it,
and gate 15 passing confirms the marks are typographic rather than straight.

**THE SHORT LINE WAS CHOSEN OVER THE LONGER ONE FOR A MECHANICAL REASON, NOT A
LITERARY ONE.** Macdonald's fuller answer carries three contractions. Body prose bans
them, `VOICED_CLASSES` does not include the opening case, and the contraction check
has no voiced exemption, so quoting the longer passage would have failed Stage 4
mechanical. **"That link is not there yet" is also the sharper sentence**, so nothing
was lost, but the constraint decided it and the record should say so.

**WHAT CHANGED IN THE ARGUMENT.** The chapter previously said he was "publicly asking
whether the spending had been worth it", which B2 verified and which stood. It now
carries what he actually said, which is narrower and stronger: **not that he asked
whether it was worth it, but that the link between usage and consumer value could not
be drawn.** That is the cost-value asymmetry in the executive's own words, in the
opening case, before the chapter names the concept. The interpretive sentence after it
moves from "That question suggests" to "The statement suggests".

**S3-4 was rewritten rather than added to.** Its own opening-case REQUIRED string from
the title fix, made hours earlier, is now FORBIDDEN in turn, with a SUPERSEDED-IN-PART
line recording why. **The 2.6 back-reference is unchanged and stays REQUIRED**, because
B2 verified that Macdonald questions the value of the spend repeatedly, so "was asking,
in public, what the company had received" is supported as it stands.

**Verified after the edit**: voicecheck mechanical and house style pass, all fifteen
print gates pass, page fill clean, W14 pass, register parses as JSON.

### QUOTING A REAL SPEAKER BROKE `voicecheck`, AND FIXING IT FOUND A SECOND DEFECT

**Writing Macdonald's words into the register note failed Stage 4 mechanical on his
contractions and his first person.** `voicecheck.analyse()` scanned every line of the
chapter file, including the Decision 51 register, while `chapter_words()` in the same
module strips it. **The `note` field is the fact checkers' working record, and
CLAUDE.md rules that quoting the source sentence in it is a CONTROL rather than a
convenience**, so a checker that bans contractions there forbids quoting any human
being who used one.

**CHAPTER 1 PASSED THIS FOR MONTHS BY LUCK.** Its notes quote the BOOK's own
sentences, and body prose bans contractions, so quoting it introduced none. **Chapter
2 is the first chapter in this project to quote an external speaker verbatim**, which
makes this the sixth defect the second chapter has exposed.

**The contraction, question and person bans now skip the register. THE EM DASH BAN
DOES NOT**, because standing rule 1 is absolute and because a register page range must
store a hyphen, and `cite_format` turns these fields into footnotes a reader reads.

**THE SECOND DEFECT IS PRE-EXISTING AND WAS FOUND BY A CONTROL THAT WAS PASSING FOR
THE WRONG REASON.** A control injecting "We know a record flow..." into the teaching
body reported that the committed checker caught it. It did not: it was failing on the
register's own "we're" and the injected sentence was invisible to both versions.
**`PERSON` was case-sensitive and listed lowercase forms only**, so "as we know"
failed and "We know" passed, and the start of a sentence is the likeliest place for
second person to appear in an instruction. Capitalised forms are now listed
explicitly rather than using `re.I`, **because case-insensitive `\bus\b` matches "US"
in "the US market" and would fail a chapter for naming a country.** That trap is one
of the eight controls.

**Eight negative controls now cover this, including a clean baseline**, and both
chapters pass unchanged.

### DAN VERIFIED FORBES AND FORTUNE, 2026-08-29. ALL NINE ROWS PASS. TWO ENTRIES OF FIVE ARE NOW VERIFIED.

**A1 to A6 and B1 to B3 all return Y.** Every verdict is written into the register
note in the chapter HTML with its reversal condition, and `accessed` on both entries
moves from 2026-08-21, which recorded only that the articles were reachable, to
2026-08-29, which records that these sentences were checked against them.

**A2 AND A5 WERE THE ROWS WORTH SEPARATING AND BOTH HOLD.** They are the two Forbes
rows that are not figures: that no contract was renegotiated and no vendor raised a
price, and that the cost variation is attributed to workload. Either could have been
the chapter's inference rather than the article's statement, **which is the shape of
Chapter 1's FC9**, an absorbed-cost mechanism inferred from a source that did not
state it and cut at Stage 7.

**THE ONE CORRECTION IS AT B1 AND IT TOUCHED TWO SENTENCES, NOT ONE.** The speaker is
Andrew Macdonald and he is Uber's **president and chief operating officer**; the
chapter said only "chief operating officer". The opening case carried one instance and
section 2.6 the other, they sit nowhere near each other in the file, and **fixing only
one would have been precisely the drift this project has paid for five times.** Both
corrected, ledgered together as S3-4 with a REVIEW field saying so.

**THE VENUE IS THE RAPID RESPONSE PODCAST, so Fortune is secondary to a recorded
interview**, and that is the level the chapter cites. Macdonald's words are quoted
verbatim in the register note, because a note that quotes the sentence is what caught
SF7 and SF11.

**RAISED AND NOT DECIDED: the quotation is stronger evidence than the paraphrase.**
What Macdonald actually said is that it is hard to draw a connection between rising
Claude Code use and consumer-facing innovation, and that "that link is not there yet".
**That is narrower and better than "asking whether the spending had been worth it": it
is the cost-value asymmetry in the executive's own words.** B2 passes on Dan's reading
that he questions the value of the spend repeatedly, so the paraphrase is supported and
stands. Whether the chapter should quote him instead is a prose question for Dan, not a
sourcing defect, and it is recorded in the register note as open.

**A SECOND OPEN QUESTION, ALSO NOT DECIDED: Chapter 2 does not name him and Chapter 1
names its executive.** Chapter 1's opening case says "Chief executive Sam Altman said
publicly", and that phrasing is a REQUIRED string in the claim ledger under SF1. The
fifty-year rule permits a name inside a dated case, so the house precedent is to name.
Chapter 2 names nobody.

**STAGE 3 IS NOT CLOSED BY THIS AND THE BOX STAYS OPEN.** The sheet covered two of the
five register entries. **`uber-2026-adoption` cites no document by Dan's own ruling**
and is settled. **`mit-nanda-2025` still has no location**, which is S3-3 and whose
remedy is the report itself. **`dta-copilot-2024` is still Grade C and unread**, and
the external check's claim to have verified it was rejected as S3-R1 and that rejection
stands.

**Verified after the edits**: all fifteen print gates pass, page fill clean, W14 pass
at 11 rulings, register parses as JSON.

### THE SOURCE VERIFICATION SHEET IS BUILT, 2026-08-29.

**`AIOM_Ch02_Stage3_verification_sheet.md`.** Nine numbered rows across the two
articles, each pairing a sentence quoted from the live text with what to check and a
blank verdict. **Every quotation was verified as a verbatim substring of the chapter
rather than retyped from memory**, which is the direct lesson of the S3-R2 error
recorded below; the two that failed that check were correct fragments carrying a
terminal period where the chapter has a comma and a colon, and were trimmed.

**IT SEPARATES THE FIGURES FROM THE INFERENCES, WHICH IS WHERE THIS BOOK'S DAMAGE
HAPPENS.** A2 and A5 are the two Forbes rows that are not numbers: whether the article
supports "no contract had been renegotiated and no vendor had raised a price", and
whether it attributes the cost variation to workload. **Chapter 1's FC9 was exactly
this shape**, an absorbed-cost mechanism inferred from a source that did not state it,
cut at Stage 7.

**B1 IS THE ROW THAT DOES NOT DEGRADE.** If the COO question cannot be confirmed as
public, with a venue and a date, the paragraph and problem P1 need rework rather than
a looser number, which is what the register note already says.

**Section C lists what needs no verdict**, because each is already marked in the
chapter as not established or is the chapter's own argument. Section D records that
Forbes and Fortune are both SECONDARY, so confirming them establishes that the
reporting says what the chapter says it says and not that the underlying facts hold.
Only The Information moves `uber-2026-budget` off Grade C.

### S3-1 AND S3-2 RULED AND APPLIED, 2026-08-29. DAN TOOK OPTION (C).

**Ruled together, because option (c) resolves both in one edit.** The markers stay,
and the gloss now says plainly that no single source could be attributed and why.

- **Footnote 3** was "Reported adoption, not quantified. See the register." It now
  reads "Consistent values across several outlets with no consistent attribution, so
  no single source is named. The adoption is characterized rather than given as a
  percentage." **The contradiction is gone**: the old note said "not quantified"
  against a sentence saying "about a third".
- **Footnote 4** was "Reported share of committed code." It now reads "Characterized
  rather than quantified, for the same reason."

**S3-3 is NOT applied and cannot be**, because its remedy is the MIT report itself.

**THE FIRST WORDING FAILED GATE 8 AND THAT IS RECORDED RATHER THAN QUIETLY FIXED.**
The glosses were longer than what shipped, and the taller footnote block on page 3
separated **footnote 6** from its call across the page 3 to 4 boundary. Footnote 6 is
the Fortune entry, which is nothing to do with the sentences edited. **This is the
coupling CLAUDE.md records twice on Chapter 1, where a one-sentence reorder pushed
footnotes off their calling pages eleven pages later.** The remedy was to tighten the
glosses, which the prose wanted anyway; it was not to reword the sentence, and it was
found by building rather than by reasoning.

**Both rulings are in `AIOM_Claim_Ledger.md` as S3-1 and S3-2**, so W14 holds them
through Stage 6. The gloss text sits inside the `<cite>` element and `claimcheck`'s
body reader reaches it, which was verified rather than assumed before the entries
were written. S3-2 also carries a REVIEW field, because a later reader WILL raise the
unattributed citation again and the record needs to say that naming an outlet is not
the remedy.

**Verified after the edits**: all fifteen print gates pass, page fill clean, W14 pass
at 10 rulings, voicecheck pass, web build pass, G3 pass.

### EXTERNAL CHECK 1 RECEIVED 2026-08-29. IT CANNOT CLEAR THIS STEP AND SAYS SO ITSELF.

**Recorded verbatim, punctuation only altered, in
`04_Stage3_Source_Fact_Check_1/AIOM_Ch02_Stage3_externalcheck_1.md`, with Claude's
assessment in its own marked section. Dan rules all of it; Claude rules none.**

**THE REVIEWER HAD NO WEB ACCESS**, which puts it in exactly Claude's position and
which is why CLAUDE.md calls Stages 3 and 7 structurally external. It read no primary,
so **it moved no entry off Grade C.** Five findings: three accepted, two rejected.

- **S3-R1, REJECTED. The DTA trial is not verified.** The reviewer marks it "VERIFIED,
  passes" and offers "around sixty agencies", "several thousand licences", "priced per
  seat". **The chapter says all three of those sentences in P3.** It read them and
  reported that its recollection agrees. That is circular, and it is the confirmatory
  shape Chapter 1's withdrawn craft review already cost this project once. The
  register note for `dta-copilot-2024` records the opposite of convergence: agency
  counts of 56, almost 60 and more than 60 all appear. **A confident "around sixty"
  from an unsourced recollection is the signature of one upstream number repeated**,
  which is the exact reasoning on which Dan withdrew the adoption percentages.
- **S3-R2, WITHDRAWN THE SAME DAY. This one was Claude's error and the reviewer was
  right.** The rejection said the chapter carries no pending-verification stamp,
  measured by grepping the render for "pending verification" and "unverified".
  **The provenance line on page 1 says "pending SOURCE verification".** One
  intervening word, zero matches, and a ruling handed to Dan on top of it. The
  reviewer's findings 2 and 5 are correct and stand in full, along with the rest of
  finding 5: the worked example is labelled stipulated, 2.8 asserts nothing about how
  much value a deployment produces, and the executive sentence is qualified. **This is
  the failure this repository records more than any other, a check reading green while
  measuring the wrong thing, and here it was not a gate but a ruling.** S3-R1 is
  unaffected; its reasoning is independent.
- **S3-1, ACCEPTED. Footnote 3 contradicts the sentence it annotates.** The note reads
  "Reported adoption, not quantified" against a sentence reading "about a third of the
  engineering organization was using it". The gloss is what is wrong: it was written to
  mean no PERCENTAGE is given, and it should say that. Needs no source.
- **S3-2, ACCEPTED. Footnotes 3 and 4 name no outlet.** Correct as a press standard,
  and the absence is Dan's own 2026-08-21 ruling, since no single source could be
  attributed and standing rule 2 has no option for citing one you cannot name. **The
  real question is whether a footnote should exist where no document is cited.** Three
  options are set out in the file: drop the markers, name the outlets (external work),
  or keep them and reword the gloss to say plainly that no source could be attributed.
- **S3-3, ACCEPTED, remedy already booked.** "MIT NANDA" reads thin and wants a real
  author line. That is exactly what the entry's `upgrade` field already says it needs.
  Its value is that an independent reader stopped where the register already marks.

**S3-1 and S3-2 pair and should be ruled together.** Both are about the same two
footnotes and option (c) on S3-2 resolves S3-1 in the same edit.

**THE REVIEWER'S BOTTOM LINE STANDS AND NOTHING ABOVE CHANGES IT.** It would not clear
this to press until the Forbes and Fortune pieces are produced. Neither would Claude,
and neither does the register. **A second external check with the same absence of web
access will produce the same class of result**, so the useful second one is a checker
with source access or a human at a terminal with the two articles open.

### DAN RULED ALL EIGHT AND THEY ARE APPLIED, 2026-08-29. STAGE 3 STAYS OPEN.

**Dan ruled "apply your recommendations on all eight claims".** Five carried a
drafted recommendation and three did not, so the recommendation for those three was
formed at application and is recorded in the ledger with the rest. **Five recast,
three cut. None cited, because none needed a source.**

**THE EIGHT ARE IN `AIOM_Claim_Ledger.md` AS FQ1 THROUGH FQ8, AND THAT IS THE POINT
OF WRITING THEM DOWN.** Stage 6 is two steps away. SF8, SF9 and SF10 were reverted
during Chapter 1's copy edit with every date and figure intact, and FC2 repeated the
shape a fourth time. **A recast frequency claim is exactly that shape**, because the
copy edit reaches for the shorter sentence and the shorter sentence is the withdrawn
one. W14 now holds all eight: `claimcheck` reports 8 rulings, 9 required strings, 8
forbidden, 1 review-only, PASSED. **No entry carries a SOURCE-KEY**, which is what
separates these from every Chapter 1 entry: the ruling is against an absent source
rather than in favour of a present one, so REVERSES-IF names what would let each
claim return.

**STAGE 3 IS NOT CLEARED BY THIS AND THE BOX STAYS OPEN.** Dan ruled the claim half.
The source half is untouched and is still external: `mit-nanda-2025` and
`dta-copilot-2024` have no location, every figure in the chapter remains formally
unverified, and no source in it has been read by anyone.

**THE PAGE 11 HOLE REOPENED, WAS CAUGHT BY THE ADVISORY, AND IS FIXED.** Three of the
eight rulings are cuts, the text reflowed, and Figure 2.2 stopped fitting at the foot
of page 11: 166pt unused, the page ending on "every property a reporting metric needs
except relevance". **This is the same page and the same defect the Stage 2 close
fixed six days ago**, reintroduced by an edit in a different slot, which is the
tight-coupling rule in CLAUDE.md section 6 demonstrating itself rather than being
recalled. Four anchors were built and measured rather than reasoned about. Moving the
figure ONE paragraph later, to after "Adoption answers a question about the usage
flow", clears the sweep; the two later anchors both open a 135pt hole on page 12 and
the current anchor is the 166pt one. **The counterintuitive remedy held again, and
the minimum move was enough.**

**THE STAGE 4 RE-READ THAT PARALLEL RUNNING BOOKED HAS BEEN DONE, AND IT CHANGED ONE
RULING.** FQ4's drafted recast read "the one section 2.5 shows is structurally the
easiest to skip", which would have made the craft section's OPENING sentence carry
three references at once: the rest of the book, Chapter 8, and section 2.5. That is
C7 made worse at the worst sentence in the chapter to worsen it. The pointer was cut
and the applied form is "the one that is structurally the easiest to skip". **The
derivation clears the claim whether or not the sentence points at it**, which is
exactly how Stage 1 cleared its sixth candidate: that one sits in the chapter summary
and names no section. Recorded in the ledger at FQ4 as a revision at application.

**WHAT THE EDITS DID TO THE CRAFT METRICS.** Section 2.3 improved most, mean sentence
14.5 to 12.5 and short sentences 40 to 47 per cent, from the FQ6 cut. 2.4 improved
slightly. 2.7 went the other way, 16.5 to 17.0, because the FQ2 recast is longer than
what it replaced. **Chapter level did not move at all**: mean 15.8, median 15,
standard deviation 7.3, 32 per cent short. So F4 stands unchanged and the two closing
slots are still where the chapter departs most from the Chapter 1 band.

**F1 through F7 stand as written.** Only F2's weakest passage moved, and it moved
because FQ8 fixed it: the craft section no longer claims observed recurrence for a
diagnostic the book itself introduces.

**Verified after the edits**: all fifteen print gates pass, page fill clean, W14
pass, voicecheck mechanical and house style pass, registry pass, checklist
self-consistent. The Stage 3 render, the packet and the Stage 4 prose extract were
all rebuilt on the moved text rather than left describing the old one.

### THE FIVE UNCITED CLAIMS ARE DRAFTED FOR RULING, 2026-08-29, AND NONE NEEDS A SOURCE

**`AIOM_Ch02_Stage3_rulings_to_make.md` carries all five with options and a
recommendation. Nothing is applied.** Standing rule 2 allows citation, recasting as
a formal conditional, or cutting, and the sheet's finding is that **three of the
five can be recast onto derivations the chapter already contains and two can be cut
without losing teaching.** Two cuts and three recasts are recommended.

**ITEM 4 IS CLEAN BY AN ARGUMENT STAGE 1 ALREADY ACCEPTED.** Stage 1 ruled a sixth
candidate clean, "the record flow is skipped most often, and for structural reasons
rather than careless ones", on the ground that section 2.5 derives it. Anchoring
item 4's forward reference to the same derivation makes it clean by the same
reasoning rather than by a new one.

**WHAT THIS DOES TO THE CRITICAL PATH.** If the recommendations are taken, the five
claims need no source and no external access, and Stage 3's genuinely external work
is the five register entries alone: two Uber entries with access dates supplied, the
adoption entry ruled to cite no document, and `mit-nanda-2025` and
`dta-copilot-2024`, which have no location. **No recast introduces a new claim**, so
these rulings create no new Stage 7 exposure.

**Mechanical state at handover**: `chapter_check.py Ch02` reports W14 pass,
voicecheck pass, print pass, registry pass, checklist self-consistent. The web build
and G3 still report the expected shape for an unlocked chapter, W2 because Chapter 2
is not locked, W10 because a single-chapter build omits locked Chapter 1, and G3
because the continuity ledger carries no Chapter 2 entries until lock.

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

### CLAUDE's CRAFT READ, 2026-08-29. RUN AHEAD OF STAGE 3 ON DAN's RULING.

**Dan ruled this step run in parallel with his Stage 3 rather than after it**, to
collapse four of his sittings to three. **THE COST IS BOOKED HERE RATHER THAN
DISCOVERED LATER**: the five uncited claims sit in 2.4, 2.7, the craft section twice
and P3, so whatever Dan rules there invalidates the read of those passages and they
are re-read before this step is ticked. Nothing else in the chapter is exposed to
those rulings.

**THE MECHANICAL HALF PASSES.** `voicecheck.py` reports Stage 4 mechanical PASS and
house style PASS: zero em dashes, zero contractions, zero question marks outside
discussion prompts, zero first or second person in unmarked body prose, zero
straight marks, no paragraph over 150 words, antithesis at budget with 3 of 3, and
no defined term differing from its key term.

**F1, C1 concrete particular.** Weakest passage, the craft section's contrast case:

> A retailer deploys an AI assistant to two hundred customer-service agents.

The retailer is unnamed and constructed, and it carries real weight as the only
fully managed example in the chapter, the counterweight to Uber. Uber is named and
dated and the DTA trial in P3 is a named real deployment, so the chapter is not
short of particulars; the weakness is that the ONE example showing what success
looks like is the one that is invented. **This is a finding and not a defect**,
because the fifty-year rule constrains named particulars to cases and the chapter
labels the construction. The remedy if Dan wants one is the case bank, and it is
Chapter 6's supply obligation rather than this chapter's.

**F2, C2 context and stakes.** **Strongest criterion in the chapter**, and section
2.5 is the exemplar: it states three structural reasons the record flow is skipped,
what each settles, and why the remedy is a decision rather than a habit. Weakest
passage, in the craft section:

> Two failure modes recur when organizations run this mapping on themselves, and
> both are worth naming in advance.

**The three-flow mapping is this book's own construct, introduced on the previous
page.** No organization has run it, so no recurrence can have been observed. The
passage states what the failure modes are without stating the conditions under
which they were seen, because there are none to state. This is C2's "conditions
that made it available" failing at the point where the chapter is most exposed, and
it is also a standing rule 2 exposure that Stage 1's sweep did not list. **Raised
now so Dan can rule it with the other frequency claims rather than meet it at
Stage 7.**

**F3, C3 claim first.** Two existential openers, both flagged by the proxy. Weakest:

> There is a second consequence, and it is the one that reaches the value side.

The actual claim arrives a full sentence later, at "A project business case states a
benefit at the moment of approval, when nobody can check it." The same section
opens strongly at "Most AI deployments are funded the way projects are funded", so
the chapter demonstrates the fix two paragraphs above the failure. The second
instance, "There is a reason organizations reach for adoption figures at this point,
and it is not laziness", is the milder of the two because its second clause carries
real content.

**F4, C4 deliberate rhythm.** **The chapter sits above the exemplar band on every
measure**: mean sentence 15.8 words against Chapter 1's 14.3, median 15 against 14,
standard deviation 7.3 against 6.1, 32 per cent under 12 words against 36, and one
sentence at 37 words where Chapter 1 has none over 35. All of that is inside the 12
to 24 band section 15 prescribes, so the chapter is not out of standard; it is
consistently heavier than the book's own exemplar. **Weakest, and it is the two
CLOSING slots.** Key terms runs mean 19.4, standard deviation 4.8 and ZERO short
sentences, against Chapter 1's key terms at 16.0, 5.9 and 12 per cent, and Chapter 2
spends 11 sentences where Chapter 1 spends 17 on the same six entries. The summary
shows the same shape at 17.1 mean and 27 per cent short, against Chapter 1's 12.5
and 50 per cent. **Both are slots the reader reaches last and tired**, which is the
worst place in the chapter to be densest.

**F5, C5 paragraph close.** The criterion bans closing on a cross-reference and five
paragraphs do it. Weakest:

> Figure 2.2 sets the two quantities against the scope each covers.

It hands the reader a pointer instead of the point. **IT IS ALSO THE SENTENCE THAT
LEFT PAGE 11 A THIRD EMPTY FOR SIX DAYS**, recorded at the close of Stage 2 and
graduated into CLAUDE.md section 6. The craft defect and the pagination defect are
the same sentence, which is worth stating because the two were found by different
methods and neither found the other. The other four are Chapter 3, Chapter 10 and
Chapter 8 pointers, all of them legitimate forward references sitting in the wrong
position in their paragraph.

**F6, C6 the guard.** **It holds in the villain direction and does so
deliberately.** "That is rarely dishonest" and "it is not laziness" each block a
character-driven reading at the exact point one is available, which is the guard
working rather than the guard being untested. Weakest in the false-sophistication
direction, in the chapter summary:

> and the load-bearing word is unknown

**The chapter already has the ordinary phrasing and uses it**: section 2.6 says "The
word doing the work in that sentence is unknown, not small." The summary then
reaches for "load-bearing", which is this project's own production vocabulary rather
than ordinary business language, to say the same thing. C6's second direction is an
abstraction where an ordinary word is available, and here the ordinary word is not
merely available, it is thirty lines up in the same chapter.

**F7, C7 business reality first.** Weakest opener:

> The consequence of the asymmetry is the sentence a manager should carry out of
> this chapter.

It opens on a conceptual label and then on the chapter's own apparatus, where a
business statement is available: the section's own title, "All of the cost, an
unknown fraction of the value", is the business statement. Compare 2.3's opener,
"Most AI deployments are funded the way projects are funded." **On the second half
of C7 the chapter is clean**: every coined term arrives after its mechanism. Flow is
defined after the transaction-versus-flow contrast, cost-value asymmetry after 2.4
derives the one-sided accrual, and the three-flow mapping after all three flows and
their health tests are built.

### F8 THROUGH F12 APPLIED ON DAN's RULING, 2026-08-29. NINETEEN EDITS.

**Every finding was re-counted after the edits, not assumed closed.**

| Finding | Before | After |
|---|---|---|
| F8, "worth" announcements | 11 | 3, and **all three are legitimate uses meaning value**, not announcements: "worth the cost of knowing" and "worth reaching" |
| F9, paragraphs ending on a cross-reference | 5 | **0** |
| F10, "per cent" | 3 | 0. "percent" now 4, matching Chapter 1 |
| F11, the verbatim aphorism | 2 | 1 |
| F11, "invisible until" | 3 | 2, and both survivors are the sanctioned body-to-summary restatement |
| F12, both compression failures | 2 | 0 |

**F9 WAS CLOSED BY DELETING THREE POINTERS AND SUBORDINATING TWO, NOT BY DELETING
FIVE.** Every forward reference the chapter makes survives: Chapter 3 keeps two of
three, Chapter 10 one of two, and Chapter 12 its only one, which is why the 2.8
instances were reordered rather than cut. **The craft section's Chapter 8 promise was
never touched**, because `continuity.py` reads it and G3 will enforce it at Chapter 8's
lock.

**THREE RULINGS WERE SUPERSEDED IN PART AND EACH SAYS SO IN THE LEDGER.** F8 removed
the sentence FQ1 installed and the closing clause of FQ8; F11 removed the mechanism
clause of FQ3. **In all three the ruling is unchanged in substance**: the frequency
claim stays forbidden in each case, and FQ1's replacement is now itself FORBIDDEN, so
neither the original nor its announcement-shaped fix can return.

**GATE 8 FAILED TWICE DURING THIS AND THE SECOND TIME IS THE INSTRUCTIVE ONE.** The
edits shortened the opening case by about two lines, which pulled section 2.1's head
onto page 3, which left footnote 6's call on page 3 with its note pushed to page 4.
**Footnote 6 is the Fortune entry and has nothing to do with any sentence edited.**
Shortening footnote glosses was tried first and did nothing, because notes 3 to 5 are
not on page 3; the raster showed the real cause. **Five equally valid phrasings of one
F8 edit were built and measured**, and "usually confused with each other" paginates
where "usually confused" does not. This is the third time on this chapter that a local
edit has moved footnotes pages away, and it is why CLAUDE.md says to build rather than
reason.

**WHAT WAS NOT APPLIED, because Dan ruled F8 to F12 and not the rest.** The reviewer's
C1 finding, that section 2.3 runs entirely on placeholders while sitting adjacent to the
chapter's best instance, and its C2 finding, that 2.3 defers a mechanism wholly to
Chapter 10. **Both are real and both are still open.** F1 through F7 are also unruled.

**C4 IS UNCHANGED AND WAS NEVER IN SCOPE HERE.** Chapter 2 still runs about 1.3 words
above Chapter 1 on the mean with roughly twice the long-sentence load. F4 and the
reviewer's C4 both stand.

**Verified after the edits**: W14 pass at 11 rulings, voicecheck mechanical and house
style pass, all fifteen print gates pass, page fill clean, web build pass, G3 pass.

### THE SECOND MODEL'S CHECK IS IN, 2026-08-29. FIVE NEW FINDINGS, F8 TO F12. DAN RULES.

**Recorded verbatim in `05_Stage4_.../AIOM_Ch02_Stage4_secondmodel_review.md`**, with
Claude's verification in its own marked section. **THE REVIEW'S FORCE RESTS ALMOST
ENTIRELY ON COUNTS, SO EVERY COUNT WAS RE-RUN** against the two extracts the reviewer
was given. Six are exact, one is off by one, and two are directionally right with the
magnitude overstated. **No finding fails verification.**

**F8. THE "WORTH" ANNOUNCEMENT LAYER, 11 AGAINST CHAPTER 1's ZERO. Verified exact, and
it is the best finding in the review.** "Worth naming", "worth stating carefully",
"worth one concrete illustration", "worth reading carefully", "worth naming in advance",
"worth unpacking". The reviewer nominates deleting this layer as the single
highest-yield change in the chapter, on the grounds that it is the chapter narrating its
own procedure instead of performing it. **Claude never counted it, and the pattern is
invisible without the Chapter 1 comparison.**

**F9. C5 IS A CHAPTER-LEVEL FAILURE, NOT A FINDING, AND THIS IS THE REVIEWER'S VERDICT
ON THE WHOLE CHAPTER.** It is the only criterion it fails outright. Claude's F5 found
the same five paragraph-terminal cross-references. **What Claude did not do is the
comparison: Chapter 1 does this ONCE in its whole length, at the end of 1.5, a section
whose job is pointing outward.** Same evidence, better conclusion, and the remedy is the
cheapest in the chapter because every offending paragraph already ends well one sentence
earlier.

**F10. "per cent" AGAINST "percent", AN OBJECTIVE HOUSE-STYLE SPLIT BETWEEN THE TWO
CHAPTERS.** Verified: Chapter 2 writes "per cent" three times, Chapter 1 writes
"percent" once and "per cent" never. **Chapter 1 is right for a Chicago-styled American
book set in `lang="en-US"`, and Chapter 2 is wrong.** Nobody was looking for this and no
gate reads it. **The likeliest source of the drift is this repository's own prose**,
which uses "per cent" throughout, including in CLAUDE.md and in the craft band itself.

**F11. RECURRENCE, WHICH NO CRITERION GRADES, AND THE STRUCTURAL POINT IS THE FINDING.**
"A diagnosis nobody could overturn is an opinion" appears verbatim twice within three
pages, "unknown fraction of the value" three times, "invisible until" three times, all
verified. The epistemic disclaimer fires far more often than Chapter 1's single
dateline. **All seven criteria grade at sentence or paragraph scope, so none can see
accumulation**, which is a gap in the standard rather than in this chapter.

**F12. THE STALL POINT, WHICH IS THE QUESTION A DRAFTER STRUCTURALLY CANNOT ANSWER.**
"Run against Uber as reported, the mapping produces a result worth reading carefully,
because it is less flattering than it first appears." Two referents compete and the
meaning resolves two paragraphs later. Runner-up: P1's "the answer is harder", where the
comparative dangles.

**THE ONE DISAGREEMENT IS ON C4 AND BOTH READS ARE MEASURING SOMETHING REAL.** Claude's
F4 named the two closing slots, key terms at 19.4 mean with zero short sentences,
measured per section against Chapter 1's same slots. The reviewer names 2.6 and the
craft section, measured as a cluster of 30+ word sentences. **Different instruments, not
a contradiction**: a slot can be uniformly long without holding the longest sentences.
Both should be fixed.

**F6 AND F7 WERE INDEPENDENTLY CONFIRMED.** The reviewer finds the same C6 guard holding
in the villain direction, by the same mechanism, and names the same C7 weakest passage,
the craft section opener. **Claude edited that exact sentence at FQ4 on C7 grounds and
the reviewer still flags it at 34 words: the edit helped and did not go far enough.**

**THE REVIEWER'S VERDICT ON THE BOOK'S COHERENCE IS THE THING TO READ TWICE.** It says
the two chapters are recognizably one book in skeleton and baseline voice, that Chapter 2
is the outlier, and that the direction is "from narrative economy toward methodological
self-consciousness". **Its closing observation is measurable and uncomfortable: the
standard was extracted from Chapter 1's prose, and the chapter written under it drifts
further from that prose than the chapter that never saw it.** It holds that the repair is
subtraction rather than rewriting, and that nothing failing here is in the sentences'
bones.

**NOTHING IS APPLIED. Stage 4 stays open and every finding above is Dan's to rule.**

### THE RE-READ IS DONE, 2026-08-29. STAGE 3 CHANGED F1 AND NOTHING ELSE.

**This is the cost parallel running booked, now paid.** Stage 3 moved thirteen things:
the eight frequency claims FQ1 to FQ8, the two footnote glosses S3-1 and S3-2, the
executive's title in two sentences, and the named direct quotation. Each was re-read
against the seven criteria.

**F1 IMPROVES MATERIALLY AND ITS WEAKEST PASSAGE NO LONGER STANDS AS WRITTEN.** F1
said the chapter's one fully managed example, the retailer in the craft section, is
constructed and unnamed. **That is still true and still the weakest C1 instance.** But
the opening case now carries a named executive speaking in his own words, which is the
strongest concrete particular in the chapter and is exactly what C1 asks for. The
proxy moves with it: proper nouns rise from 2.5 to 3.0 per thousand words. **The
finding stands, the balance of the chapter has shifted, and the retailer is now the
only place C1 is thin rather than one of two.**

**F4 STANDS UNCHANGED AND IS NOW THE ONLY FINDING NOTHING HAS ADDRESSED.** Chapter
level did not move at all: mean 15.8, median 15, standard deviation 7.3, 32 per cent
short, against Chapter 1's 14.3, 14, 6.1 and 36. **Key terms is still the outlier at
19.4 mean, 4.8 standard deviation and ZERO short sentences**, against Chapter 1's
16.0, 5.9 and 12 per cent. The summary still runs 17.1 against 12.5.

**F2, F3, F5, F6 and F7 are unchanged.** The two throat-clearing openers are still
there, the five cross-reference closes are still there, "load-bearing" still appears in
the summary where 2.6 uses the ordinary phrasing, and 2.6 still opens on the chapter's
own apparatus.

**THE OPENING CASE IMPROVED ON C4 AS A SIDE EFFECT.** Its mean moves 15.2 to 15.4 and
its standard deviation 6.9 to 7.3, because the new passage runs 26 words, then 8, then
14. The eight-word quotation is doing the work.

**C6 WAS RE-READ SPECIFICALLY, BECAUSE NAMING A REAL PERSON IS WHERE THE GUARD IS MOST
AT RISK.** C6 forbids character-driven causation where a structural account is
available, and a named executive in an opening case is the classic place a book slips
into one. **It does not here.** Nothing is attributed to Macdonald's judgment or
character; his statement is used as evidence about what the company could measure, and
the paragraph after it says the position was structural. The guard holds.

### THE SECOND-MODEL PACKAGE IS BUILT AND UNSENT, 2026-08-29

**Three files in `05_Stage4_Voice_And_Craft_Check/`. THE PROSE EXTRACT WAS REGENERATED
2026-08-29 AFTER STAGE 3 CLOSED**, so a reviewer reads the text as it now stands rather
than the pre-ruling version, and it carries the Macdonald quotation. The prompt and the
criteria extract are unchanged. Built so Dan could run the gut-check in the SAME sitting
as Stage 3, which is the whole point of running this
step in parallel: `AIOM_Ch02_Stage4_secondmodel_prompt.md`,
`AIOM_Ch02_prose_for_craft_review.md`, and `ch02_craft_criteria_extract.md`, which
is sections 26 and 27 of the standard and nothing else from it.

**THE EXEMPLAR IS NOW AN EXTRACT, NOT THE CHAPTER 1 HTML, CORRECTED 2026-08-29 BEFORE
THE PACKAGE WAS SENT.** The prompt originally attached
`AIOM_Ch01_redraft.html`, which would have set clean Chapter 2 prose beside Chapter 1
MARKUP and made every comparison of rhythm, paragraph close and sentence length answer
a question nobody asked. **That is the defect gate W9 was fixed for on 2026-08-22**, a
text lifted under one rule compared against text extracted under another, and it is the
third time that shape has appeared in this project. Worse, Chapter 1's HTML carries its
Decision 51 source register, whose notes quote sentences the book CUT, six of them
introduced by "the sentence now reads": a reviewer reading those would have been
reading withdrawn prose as if it were the exemplar. `ch01_prose_exemplar.md` is the
same `prose_extract.py` output Chapter 2 gets, and it was checked for register leakage
rather than assumed clean.

**THE PROMPT ATTACHES THE LOCKED CHAPTER 1 AND CHAPTER 1's VERSION DID NOT.** The
standard's band is now measured from Chapter 1 rather than from four journalists, so
a reviewer can calibrate against the book's own prose. It also asks a question
Chapter 1's prompt did not: **read the two chapters back to back and say whether
they sound like the same book.** F4 says they measurably do not, and a second model
that names a different section as the heavy one is giving new information.

**Sourcing is declared out of bounds in the prompt**, because Stage 3 is open and
every figure is formally unverified.

### A SEPARATE FINDING THAT BELONGS TO STAGE 3, RAISED HERE BECAUSE STAGE 4 FOUND IT

**STAGE 1's FREQUENCY SWEEP WAS INCOMPLETE, AND THE READ FOUND THREE MORE.** Stage 1
listed five uncited claims about what organizations usually do and cleared a sixth
on the ground that section 2.5 derives it. A sweep run at this step over a wider
pattern returns about eleven candidates, most of them derived in their own sentence
or in their own section and therefore clean by Stage 1's own reasoning. **Three are
not:**

- **"it is usually the only document stating what the deployment was supposed to
  achieve"** (2.3). Nothing in the chapter derives it.
- **"the usual answer is that it crossed some time ago"** (2.8). It asserts that
  most deployments have already passed THM-004's scale antecedent, which is a
  stronger claim than any of Stage 1's five and sits in the limits section.
- **"Two failure modes recur when organizations run this mapping on themselves"**
  (craft), which is F2 above and is the worst of the three, because the recurrence
  is claimed for a diagnostic the book itself introduces.

**These are Stage 3's to rule, not Stage 4's**, and they are recorded here so Dan
rules eight rather than five and does not meet the remaining three at Stage 7.
Standing rule 2 is not a lifecycle step an adjacent step can absorb.

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

### RUN 2026-08-29 ON DAN's INSTRUCTION, AHEAD OF ITS v3 POSITION. THE BOX STAYS OPEN.

**Process v3 puts this step AFTER Stage 7 for one measured reason**: every Chapter 1
design finding was fixed in CSS or in markup and none by rewriting a sentence, so a
design review taken before the copy edit reads a pagination the copy edit is about to
destroy. Stage 6 has not run. **Ticking this box would claim a design review of the
shipped text, which is a scope claim written from intention rather than from what was
done**, so the findings below are banked and the step is re-run after Stage 7.

**WHAT THE EARLY RUN ACTUALLY BOUGHT: two real defects that are NOT pagination
dependent and would have survived to Stage 5's proper position.**

**DR1. FIGURE 2.1 WAS DRAWN WRONG IN TWO PLACES AND ALL FIFTEEN GATES PASSED IT.**
Fixed.

- **The cost-and-value arrowhead was invisible.** The tinted "value recorded only if
  built" rect was painted AFTER the third row's arrow and covers x 248 to 352, which
  is exactly where the arrowhead sits. SVG paints in document order, so the block
  erased it. **The figure's argument rests on the visual parallel between the three
  rows**, since the caption says the solid lines run whether or not anyone attends to
  them; row three had a line that stopped dead while rows one and two ran on. The
  tint is now painted BEFORE the lines, as a background band, and its label dropped
  three units so the cost line runs through the band above the label rather than
  striking it.
- **The record row's arrowhead was dashed.** `stroke-dasharray="3 3"` was set on the
  group holding BOTH the line and its arrowhead, so the arrowhead rendered as a
  broken double chevron rather than as an arrowhead. The arrowhead now sits in its
  own undashed group. The dash carries meaning in this figure, that the record flow
  exists only where built, and the arrowhead is not part of that meaning.

**This is the third time a Chapter 2 figure has been wrong in a way gate 12 cannot
see**, after Figure 2.2's first geometry ran its segment ticks the full height of the
drawing. Gate 12 counts captions, checks numbering and order, and matches in-text
references. **It passed the broken Figure 2.1 and the corrected one identically.**

**DR2. THE PRODUCT NAMES IN P3 WERE UNGUARDED, AND STAGE 6 IS THE REFLOW THAT WOULD
HAVE BROKEN THEM.** The chapter carried `.nb` on Claude, MIT, NANDA and Uber, and not
on "Microsoft 365 Copilot". Nothing is broken at the CURRENT pagination, which is the
point: Decision 58 exists because DR6 and DR7 on Chapter 1 appeared at a reflow, one
of them across a page turn. The body occurrence is now guarded. **The two other
occurrences are in the source register and are deliberately NOT guarded**, because
that block is JSON and markup inside it is a syntax error rather than markup. A first
attempt guarded all three and broke the register, which is recorded here because the
same trap is waiting in every chapter.

**DR3. Figure 2.2 reads correctly at ship size.** Five segments countable in both
bars, two solid and three dashed on the return bar with "unknown" labelled. This is
the corrected geometry and it is confirmed on the raster rather than from the source.

**WHAT WAS READ, stated from what was done rather than from what was intended.** All
25 pages rasterized at 110dpi. Read closely: p6 and p12 for figure legibility, p14
for the theorem panel, p9 and p4 for callout placement, p16, p20, p21 and p22 for
slot openings, p1 for the provenance line.

**GAP G-I HAS NO INSTANCE.** The definition callouts sit on p4 and p9 and the theorem
panel on p14, so no page carries both and no callout can collide with a block panel.
**This must be re-checked after Stage 6**, because it is a fact about the current
pagination and nothing else.

**GAP G-II HAS NO INSTANCE.** Every slot opening carries content below its head
group: the craft section on p16 has two full paragraphs under its label and title,
the summary on p20 runs complete on one page, and p22 carries the last key term, the
"Discussion questions and problems" title, the DISCUSSION QUESTIONS label and all
five questions. Same caveat: re-check after Stage 6.

**PAGE FILL WAS MEASURED, NOT EYEBALLED.** The advisory reports no page over 110pt
unused. Two pages looked close on the raster and were measured directly: p22 leaves
99.6pt and p12 leaves 92.7pt, both under the threshold and both at a slot or section
boundary. **The raster's page margin reads as a hole and is not one**, which is worth
recording because the eye is what raised it.

**HYPHENATION: 85 line-end breaks, ZERO inside a proper noun**, re-run after the
figure and guard changes reflowed the chapter. Two breaks fall inside a capitalised
word, "Re-porting" and "Some-body", and both are sentence-initial ordinary words
correctly divided. `lang="en-US"` is present, so Decision 59 holds.

**THE FIRST VERSION OF THAT SCAN REPORTED 3 BREAKS AND WAS MEASURING NOTHING.** It
tested `endswith("-")` against ASCII while WeasyPrint emits U+2010, and it joined
each hyphenated line to the next line in extraction order, which on p9 is the
floated callout rather than the continuation of the body column. It reported "0
proper-noun breaks" from 3 samples and looked exactly like a pass. The scan now
matches every Unicode hyphen and links lines within the same x-band. **This is the
fourth instance in this repository of a page-level check whose reading rule was
wrong at a boundary**, after gate 12 counting figure references line by line and the
hyphenation scan itself being rewritten from memory with the same defect.


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

### RUN 2026-08-29. EVERY CHECK PASSES. THE BOX STAYS OPEN FOR THE SAME REASON STAGE 5's DOES.

**All fifteen print gates pass** on the current text at 25 pages, and the page-fill
advisory is clean. **The web build now passes too, which it could not do before
today**, and that was a gate defect rather than a chapter defect: see below. **Both
MANUAL boxes were actually performed** and are recorded under Stage 5, the figure
geometry against a raster and the page-level visual review, and the figure check
found DR1.

**Nothing here is ticked, because Stage 6 has not run and every one of these
eighteen boxes is a statement about a pagination the copy edit will move.** Ticking
them would make `chapter_check.py` enforce claims about a text that is about to
change, which inverts what the continuous suite is for.

**GATE W10 MADE G2 UNPASSABLE ON ANY IN-FLIGHT CHAPTER, AND CHAPTER 2 IS WHAT
EXPOSED IT.** W10 is deploy readiness, and its locked-chapter check ran in PREVIEW
builds too, where it asks whether a deliberately single-chapter local build contains
every locked chapter. From the second chapter onward the answer is always no. So the
web build G2 owns could not pass until the chapter locked at Stage 9, **three steps
after G2's own position at 10 of 13**. Chapter 1 never exposed it because its G2 and
its lock were ticked on the same day. The check is now skipped in preview builds,
where the noindex check beside it was already preview-aware, and the publish path was
negative-tested and still fails on a genuinely missing locked chapter.

**The self-test grew a guard on its own inputs at the same time.** It CONSUMES
`build/web` and does not build it, and CLAUDE.md instructs a reader to run it after
any change to `web_build.py`, which does not build it either. Run standalone against
a stale directory the W6 control died on a missing `ch01/index.html` and **the W9a
CLEAN BASELINE reported a MISS**, which reads exactly like a gate defect and is not
one. 115 of 115 controls pass against a correct tree.


---

## Gate G3. Continuity gate

Owner: Claude

Status: [x]        Date cleared: 2026-08-29

> Mechanical, against the running continuity ledger. Catches chapter to chapter drift here rather than at manuscript integration, where the fix would mean reopening a locked chapter. Run `python3 continuity.py <chapter.html> --chapter N`. The ledger is the authority: when a chapter and the ledger disagree the gate fails and Dan rules, and the gate never edits the ledger to make itself pass. At Stage 9, and only then, `--update` appends this chapter's terms, forward references, and registry objects, and `--pay N` marks promises the chapter has now kept.

- [x] Check 1, no term redefined that an earlier chapter already owns
- [x] Check 2, every forward reference this chapter makes is logged
- [x] Check 3, every forward reference assigned to this chapter is paid
- [x] Check 4, registry IDs logged; recurring glosses worded identically
- [x] Check 5, Founding Question references match the canonical table exactly
- [x] Check 6, maturity ladder language consistent with the locked five stages
- [x] Check 7, Northmoor figures diffed against generator output
- [ ] Ledger updated at lock (continuity.py --update), glosses written by hand. DO BEFORE ticking Stage 9: this is a Stage 9 action listed here for visibility, not a G3 check, and it stays open while G3 passes.

Findings:

### G3 CLEARED 2026-08-29 ON DAN's RULING. ALL SEVEN CHECKS PASS.

**Dan ruled the box ticked while G2 sits open, so the record is deliberately out of
v3 order and this note is why.** G3 reads terms, forward references, promises and
glosses rather than a rendered page, so unlike Stage 5 and G2 it does not rest on a
pagination the copy edit will move. **Ticking it makes the check BIND in
`chapter_check.py`**, which is the point: gate W8a requires the ledger's definition of
a term to be character-identical to the chapter's key-term text, so a Stage 6 edit
touching any of the six key terms now fails at the commit rather than at the next time
somebody looks.

**The eighth box stays open on purpose and is not a G3 check.** `continuity.py
--update` appends this chapter's forward references and the THM-004 gloss at Stage 9,
and the box's own text says it stays open while G3 passes.

**Re-run immediately before ticking rather than carried forward from the earlier run
in this session.** G3 PASSED.

### THE RUN, 2026-08-29.

`python3 continuity.py <live> --chapter 2` reports PASSED: no term redefined that an
earlier chapter owns, 14 forward references made, 1 registry gloss with no drift, 0
Founding Questions misquoted, 0 maturity stage names used, and no Northmoor data
cited.

**ITS ONE FAILURE WAS CHAPTER 1's INTERLEAVING PROMISE, AND IT IS PAID IN SUBSTANCE.**
The ledger carried "This is the first chapter; problem sets begin reaching back to
earlier chapters in Chapter 2" as open. **It was verified against the chapter rather
than assumed**: discussion question 4 names Chapter 1's flat-price result and asks the
reader to use it, and problem P2 turns on the consumption-event unit and the seat
forecast, both Chapter 1 results. Marked paid with `continuity.py --pay 2`.

**The remaining notes are Stage 9 actions and are correct as they stand.** The 14
forward references are unlogged and THM-004 has no gloss recorded; both are written
by `continuity.py --update` at lock, which is what the last box in this list says.

**THE BOX STAYS OPEN, AND G3 IS THE CLOSEST OF THE THREE TO TICKABLE.** It is the
least pagination-dependent of them, since it reads terms, references, promises and
glosses rather than a rendered page. **It is not fully independent either**: gate W8a
requires the ledger's definition of a term to be character-identical to the chapter's
key-term text, so a copy edit that touches any of the six key terms breaks it. That
is an argument for ticking it, since a tick makes the check BIND and a Stage 6
regression would fail immediately rather than at the next time somebody looks. It is
left for Dan because ticking G3 while G2 is open puts the record out of order, and
the order is his.


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
