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
like any other. **This is the corrective the substitution record names**: closing
Stage 1 on Dan's own read buys his authority at the cost of independence, and the
package is what can still buy the independence back.


## Stage 2. Developmental edit

Owner: Claude

Status: [ ]        Date cleared: 

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
