# Chapter 3: A Science and Its Discipline

Editorial checklist, Process v4.

Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

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
AIOM_Prose_Standard_v2.0.md bind from Stage 0 forward.

---


## REOPENED 2026-10-14: Stage 0 and everything after it

Grounds: Dan, 2026-10-14: Chapter 3 redesigned and rewritten (Decision 85)

Every step from Stage 0 forward is reset to not-run. Their sub-checkboxes are cleared and their findings are archived in place, marked superseded. Steps before the reopen point are untouched and keep their passes.

Reopened by `reopen.py`. Per CLAUDE.md section 8, a reopen re-runs every step from the one that owns the change, and no chapter is Locked until every step is complete again.

| Step | Name | Was | Sub-boxes cleared |
|---|---|---|---|
| Stage 0 | Plan and draft | passed | 4 |
| Gate G1 | Structural gate | passed | 11 |
| Stage 4 | Review | passed | 14 |
| Stage 6 | Author pass | passed | 3 |
| Stage 3 | Fact check | passed | 5 |
| Stage 5 | Design review | passed | 0 |
| Gate G2 | Production gate | passed | 18 |
| Gate G3 | Continuity gate | passed | 8 |
| Stage 8 | Sign-off | passed | 0 |
| Stage 9 | Locked | passed | 0 |

---
## Stage 0. Plan and draft

Owner: Claude; Dan approves the plan (sitting 1)

Status: [x]        Date cleared: 2026-10-15

> v4 step 1 and 2. A one-page plan comes FIRST (Decision 77) and Dan approves it before a word is drafted, because a structural question is cheapest before the prose exists. Then Claude drafts against the fixed six-slot skeleton, with the craft standard binding from here, and clears the frequency sweep before anyone reads the draft (Decision 78). Sources verified live with an access date; no archival (Decision 48).

- [x] Plan written, one page, in 00_Stage0_Draft: opening case and its source, teaching sections, craft artifact, registry objects rendered, continuity promises paid and made, and a source for every empirical claim the chapter intends to make
- [x] Dan approved the plan (sitting 1)
- [x] Drafted against the SEVEN craft criteria in AIOM_Prose_Standard_v2.0.md, read BEFORE drafting rather than after. The voice is Concrete Management Prose
- [x] Frequency sweep cleared (Decision 78): `freqsweep.py` lists every frequency sentence and each is cited, rewritten as a formal conditional, or cut, or kept as qualification for Dan to rule; the dispositions go in the review package

Findings:

V2-P0. Redesign, Decision 85 (2026-10-14): plan version 2 written (`00_Stage0_Draft/AIOM_Ch03_Plan.md`), real-news candidates in `AIOM_Ch03_Redesign_examples.md`.
V2-S1. Sitting 1, 2026-10-15, one gate each, all A:
V2-S1-1. C4 reworded to the discipline itself and moved to Group 2 (Doing), number kept. Exit competencies updated.
V2-S1-1b. Assessment 4 becomes a function audit on a cited real deployment plus one defended border.
V2-S1-2. Craft example on Lindy.ai; P1 audits Uber, P2 the Australian Copilot trial (both Chapter 2 cases, already fact-checked).
V2-S1-3. Chapter 2's THM-004 promise kept by one or two sentences in 3.1, beside the passage on theorem panels.
V2-S1-4. Five key-term entries, one per function.
V2-S1-5. Planning documents updated to match: structure entry, exit competencies (four places), Consolidated Spec's Chapter 3 outline replaced by a pointer to the plan.
V2-D1. Draft written 2026-10-15, 5,637 words. Kept verbatim from the locked text (checked block by block): the opening case, the borders (now 3.3), the Founding Questions (now 3.4, one phrase changed from "the certified claims" to "the science"), discussion questions 2 to 4 (question 4 points to Section 3.2), the Klarna case. New: 3.1, 3.2 with five dated boxes (Airbnb, Pigment, DoiT, Microsoft, JPMorgan), the function audit worked on Lindy, P1 on Uber, P2 on the Australian trial, P3, the summary, nine key terms. Figure 3.1 is the old two-layer figure.
V2-D2. Sources: eight new entries, all Grade C (search only); four Chapter 2 entries carried with their verified notes; the registry entry dropped (THM-004 is named, not cited). A 36 percent DoiT figure was not used: no primary found.
V2-D3. Frequency sweep, 8 listed. F4 made exact ("at least 8 percent", from 55 plus 53); F7 made conditional ("can arrive"). Kept, 6: F1 cited and ruled; F2, F8 superlatives; F3 a quantity; F5 a logical possibility ruled at sitting 2b; F6 a statement about the procedure.
V2-D4. Print, for Stage 5 and not before (production is never run early): gate 1 flags a trailing space after "Google," in the Airbnb box; the two adjacent citations in the JPMorgan and Lindy boxes were separated, and gate 8 now passes.


ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

P0. Plan written 2026-10-01 (`00_Stage0_Draft/AIOM_Ch03_Plan.md`); four decisions and one prerequisite (registry bundle) put to Dan for sitting 1.
S1. Sitting 1, 2026-10-01: Dan accepted all four recommendations. (1) No registry counts in body prose; dated counts with the registry version in one dated box. (2) "Neither can most organizations on earth" replaced by the opener's sourced practitioner quote. (3) Part I cumulative case drafted inside Slot 6. (4) THM-002 for P2. Registry-dependent parts (3.2 trace, craft section, P1, P2) wait for the bundle; everything else drafts now.
D1. Draft written 2026-10-01, about 5,100 words (Decision 33 measure). Four marked REGISTRY PULL gaps await the bundle: the 3.2 trace with Figure 3.1, craft steps 3 and 4, P1, P2. Stage 0 stays open until they are filled.
D2. Four unsourced sentences rewritten before the sweep: "most management knowledge", "the commonest misuse", "much executive discussion", and why FinOps practitioners took on AI.
D3. Frequency sweep, 10 listed, all kept, for Dan to confirm: F1 rests on the cited 98 percent; F2, F3, F4, F5, F7 are importance, logic or quantity, not frequency; F6 is a logical possibility; F8 to F10 sit in questions and problems.
D4. Chapter 1's promise covers model internals, prompt engineering and use-case ideation as well as the spec's four neighbors; 3.5 pays both.
D5. G3 caught gloss drift: the ledger's THM-004 gloss added verbatim in 3.2. The three unpaid promises are paid in 3.2 to 3.5 and are marked at lock.
D6. Print render: 14 of 15 gates pass; gate 12 fails only on Figure 3.1, a registry gap. Production notes: page 10 short before Table 3.1; the table caption sets as body text.
D7. For Dan: locked Chapter 1 says "the AI Operations Management registry"; under this chapter's architecture the registry belongs to AI Business Economics. A candidate amendment via amend.py, his call.
D8. Registry attached (danielwipert/dag.aiom at 9d7ee50, the pinned version); all four REGISTRY PULL gaps filled from it; Figure 3.1 drawn and read on the page. Draft 6,050 words.
D9. FINDING: Chapter 2's THM-004 panel does not render the registry statement (antecedents i, iii and the consequent differ; Chapter 1's THM-009 panel is faithful). Chapter 3 renders the registry wording. Chapter 2 fix put to Dan.
D9 ruled 2026-10-01: Dan approved. Chapter 2 amended (commit 0493409): panel now identical to Chapter 3's, three sentences aligned; all mechanical checks pass and the panel page was read on a raster.
D10. Frequency sweep re-run after the gaps: 13 listed, 3 new (F2 "sometimes other lemmas", F5 and F10 "in practice"), all structural or logical, all kept.
D7 ruled 2026-10-01: Dan approved; Chapter 1 amended to "the AI Business Economics registry", commit d9e3922.

---

## Gate G1. Structural gate

Owner: Claude

Status: [x]        Date cleared: 2026-10-15

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
- [x] voicecheck.py mechanical bans clean before anyone reads the draft

Findings:

V2-G1. 2026-10-15: ten of eleven boxes pass. Open: the word count, 5,637 against the 6,000 to 7,500 band (Decision 82), put to Dan. Tier rules hold with no theorem callout, by design (Decision 85).
V2-G1-1. Word band. Dan: A, 2026-10-15, accept 5,637 below the floor; Decision 82 forbids padding, and words added later come from a teaching gap the review finds. G1 passed.

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

G1-1. All boxes pass except the word band: Decision 33 sets 6,500 to 7,500 for Chapters 1 and 2 only. Chapter 3 is 6,050. Band put to Dan at sitting 2; G1 stays open until ruled.
G1-1 ruled 2026-10-01 as Decision 82: band 6,000 to 7,500 for Chapters 3 to 15. Chapter 3 at 6,401 passes. G1 passed.
G1-2. Key term "Falsifying case" absent from the body; body aligned to the term.

---

## Stage 4. Review

Owner: Claude; second model reads independently; Dan rules (sitting 2)

Status: [ ]        Date cleared: 

> v4 step 3, Decision 77. ONE pass replacing v3 Stages 1, 2 and 4: structure against AIOM_Structure_v1.md and AIOM_Exit_Competencies_v1.md, teaching quality, and voice and craft against AIOM_Prose_Standard_v2.0.md. Labelled Stage 4 because it owns voicecheck. Read ADVERSARIALLY: for each competency and each criterion quote the WEAKEST evidence and rule it, reading the per-section table rather than the chapter average. ONE second-model package carries the three questions as separate sections, read without Claude's findings, and is BUILT BEFORE the sitting (Decision 81). Claude applies what is not a judgment call and hands Dan ONE decision list; Dan rules every finding, Claude rules none, and the ruled list is applied in ONE commit.

- [ ] Structure: every slot serves the chapter's stated purpose in AIOM_Structure_v1.md
- [ ] Structure: every assigned exit competency is DELIVERED, not merely discussed: a reader could perform it
- [ ] Structure: the anchor theorem is the right one and is load-bearing in the argument rather than decorative
- [ ] Structure: ledger obligations met, no earlier chapter's term redefined, promises owed are paid, nothing belonging to a later chapter front-run
- [ ] Teaching: clarity, pacing, cognitive load, example fitness and transitions carry the target reader without a stall
- [ ] C1 concrete particular: every abstraction carrying argumentative weight is anchored to a named, specific instance
- [ ] C2 context and stakes: every mechanism states the conditions that made it available and what it settles, not only what it does
- [ ] C3 claim first: the main point of a paragraph is visible in its first sentence or two, qualifications subordinate, no throat clearing
- [ ] C4 deliberate rhythm: sentence length varies, mostly 12 to 24 words, a short sentence after a long explanation, no long stretch at a uniform length
- [ ] C5 paragraph close: paragraphs end on the load-bearing clause, not a trailing qualifier and not a cross-reference
- [ ] C6 the guard holds in BOTH directions: no hero or villain framing, no populist register, no character-driven causation where a structural account is available, and no false sophistication, no abstraction where an ordinary word serves, no aphorism standing in for an explanation
- [ ] C7 business reality first: no paragraph opens on a framework, category or conceptual distinction where a business statement is available, and every coined term arrives after the mechanism it names
- [ ] Second-model package (one, three sections) returned and its findings recorded, one line each
- [ ] Dan has ruled every finding (sitting 2), applied in one commit

Findings:

V2-R0. Second-model package built 2026-10-17 by 02_Stage4_Review/build_review_v2.py: AIOM_Ch03_Review_v2_package.md, one file, three sections (structure, teaching, voice and craft), the chapter with Table 3.1 patched in, the reference extract (structure, C4, plan v2, craft criteria) and the Chapter 1 exemplar. No Claude findings in it (Dan: A). Waiting on Dan to run it.

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

R0. Independent review 2026-10-01, 44 findings (02_Stage4_Review/AIOM_Ch03_Review_claude_findings.md). Applied: R-1, R-3 to R-8, R-11, R-13, R-17, R-18, R-21 to R-24, R-26, R-28 to R-33, R-35 to R-37, R-39 to R-43, R-15 wording; R-12, R-38 resolved by those; R-19, R-20, R-44 noise. Eleven decisions to Dan (AIOM_Ch03_Sitting2_decisions.md). Second-model review not yet run.
S2. Sitting 2 (Claude's list), 2026-10-01: Dan accepted all eleven recommendations. Applied: band ruled (Decision 82); registry private, so 3.1 states Appendix A reaches lemma level; R-9 sentence cut; R-10 clause added; R-14 Klarna wording; P1 on LEM-020 and Q4 kept, recorded in the plan; R-25, R-27, R-34 kept; all 16 frequency hits kept. The second-model review is still outstanding, so Stage 4 stays open.
T1. Tool fix under the blocking exception (Decision 79), 2026-10-01: copyedit_import.py read a Word paragraph split as deleting the second half and would have written it. Reproduced on this chapter's export, fixed to refuse the block as a SPLIT, verified: split refused, --apply writes nothing, clean round trip still zero.
R0a. Self-caught while applying: P1 paraphrases of PROP-039 and PROP-041 were written from names and overstated; corrected against the statements.
R0b. Print after fixes: gate 4 now fails (one callout split) and page 13 runs 388pt short before Table 3.1. Both are pagination, left to the production step after the author pass.
S2b-0. External reviews 2026-10-06: one-file package (AIOM_Ch03_Review_package.md); second model 26 findings, Sonnet subagent 24 plus a second pass of 22. Table 3.1 findings (E-2, E-3, S-4) were extraction artifacts: prose_extract.py drops tables (fix-between list). Merged list AIOM_Ch03_Sitting2b_decisions.md.
S2b. Sitting 2b, 2026-10-06: Dan accepted all recommendations (A1 to A5, B1 to B18). Applied in one commit, except B8: the "Diligence" sentence is the THM-004 gloss fixed by locked Chapter 2 and checked by G3, so it stays; removing it is a Chapter 2 amendment, put to Dan separately. B3 cut the 3.3 tail, and the Chapter 2 promise it paid (ledger, "formalizes the economic consequence of the third flow's asymmetry") moved to 3.2 beside the proof. B14 names the record flow and leaves the other mappings to question 4, reworded, so the question is not answered in 3.4. B15's worked contextual line sits in P2 (LEM-020), because the only other contextual edge in the registry is to THM-001, which is not certified. B13 trims not needed: 7,038 words. Freqsweep 18 hits, the 5 new ones logic or structure, kept.
SR0. Scoped re-review (re-run matrix: body prose edited after the review), 2026-10-13: package `02_Stage4_Review/AIOM_Ch03_Review_scoped_package.md`, built by `build_scoped_review.py`, carries all 35 passages sitting 3 changed (Groups 1 to 3, not Group 3 alone), before and after, for one second model. Stage 4 stays ticked; findings go to Dan.
SR1. Scoped re-review returned 2026-10-13, 13 findings (`02_Stage4_Review/AIOM_Ch03_Review_scoped_secondmodel.md`). Dan ruled A (accept all 9 fixes, keep 4). One line per finding:
SR-1. Cut restated LEM-021 sentence (3.4). Accept.
SR-2. 3.6 opening no longer repeats the next paragraph. Accept; ledger FC3-B26 restated.
SR-4. 3.3 non-claims: provenance of the three-flows exclusion joined to it. Accept; ledger FC3-R1 restated.
SR-5. Craft: "where the lemma's support stops". Accept.
SR-6. 3.3 flat fee: a deployment under the contract is the falsifying case. Accept.
SR-10. P2 step 3 split in two. Accept.
SR-11. 3.4: Chapter 1's conditions lead the sentence. Accept.
SR-12. Opening case: repeated "one practitioner" removed. Accept.
SR-13. 3.4 two layers: opens on the business mechanism. Accept.
SR-3, SR-7, SR-8, SR-9. Deliberate per reviewer. Keep.
A4-note. Assessment 4 (THM-008, competency C4) must supply THM-008's propositions: the registry is private and Appendix A stops at lemma level (sitting 2, item 2).

---

## Stage 6. Author pass

Owner: Dan

Status: [ ]        Date cleared: 

> v4 step 4, Decision 75. Dan's own pass and rewrite, in Word, through `copyedit_export.py` and `copyedit_import.py`. It sits BEFORE the fact check so that every step after it checks the text Dan wants: on Chapter 2 this pass changed 104 of 195 blocks after three checks had run. Includes the whole-chapter read the old Stage 8 was.

- [ ] Unedited export round-trips at zero reported changes before the pair is trusted on this chapter
- [ ] Dan's pass imported; every block the importer refused resolved by hand
- [ ] After import, `voicecheck.py`, `claimcheck.py` and `freqsweep.py` re-run, and every new hit fixed or put to Dan

Findings:

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

A1. Import 2026-10-12: 278/278 blocks, no splits, 106 edited; 674 spans placed, 9 refused (inline markup or entity) applied by hand verbatim; re-extract matches the docx in 0/278 differing blocks (control: 106). Commit 3c0afca.
A2. voicecheck: new 'the reader' in 3.2. Dan: A, 'a reader'. Commit 8e7b4ff.
A3. freqsweep: new 'often remain informal' in 3.1. Dan: A, 'can remain informal'. Commit e8fc636.
A4. freqsweep: new 'a common objection' in 3.3. Dan: A, 'an objection'. This commit. Remaining 15 hits are rewordings of those kept at S2b.

---

## Stage 3. Fact check

Owner: Dan, external (sitting 3)

Status: [ ]        Date cleared: 

> v4 step 5, Decision 76. ONE external fact check replacing v3 Stages 3 and 7, on a fresh RENDER of the post-author-pass text, never the HTML. Two checks run in parallel on different prompts: A reads the sources, B reads only the render. THE CHECKER MUST HAVE WEB ACCESS: Chapter 2's first checker could not read, and its work was redone. Labelled Stage 3 because it owns W14. Rulings go into the register notes, with the condition that would reverse them, and into AIOM_Claim_Ledger.md.

- [ ] Packet built with `factcheck_packet.py` against a fresh render, BEFORE the sitting
- [ ] Check A (reads the sources, web access confirmed) returned
- [ ] Check B (reads only the render) returned
- [ ] Dan has ruled both sets in one sitting (sitting 3); register notes and AIOM_Claim_Ledger.md updated; applied in one commit
- [ ] Any empirical claim added after this check carries a source before lock (standing rule 2)

Findings:

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

F0. Packages built 2026-10-13 from a fresh render (gate 8 fails on footnote 7, pagination, booked to Stage 5): one file each, A (render text + packet) and B (render text only), by `04_Stage3_Fact_Check/build_packages.py`. Table 3.1's three citations added by hand (packet tool skips tables). Registry passages checked by Claude against dag.aiom 9d7ee50: all match except R-1, "every claim's non-claims" (LEM-015, THM-003 empty, both uncertified), for Dan.
F1. Checks returned 2026-10-13: A (web access yes) 13 findings, 6 verified, 6 partly supported, 1 cannot confirm (Gartner blocked, Cisco corroborates), none contradicted; B 36 findings. Sitting 3 list with recommendations: `04_Stage3_Fact_Check/AIOM_Ch03_Sitting3_rulings.md`.
S3. Sitting 3, 2026-10-13: Dan ruled Groups 1, 2 and 3 A (every recommendation). Applied commit 1eca9c9; para split (gate, A) in the next commit. One line per finding:
S3-A1/B30. Mission wording quoted exactly ("the value of cloud/technology"). Accept. Ledger FC3-A1.
S3-A2/A5. Survey figures and quotation verified in the report. Record. Register note.
S3-A3. Central finding recast to the expansion of FinOps into AI. Accept. FC3-A3.
S3-A4. Mission source replaced by the Foundation's own announcement. Accept. Register.
S3-B2. Provenance banner now says checked against the report. Accept (banner, not body). FC3-B2.
S3-B10. "nearly all of the survey's respondents"; gloss "respondents". Accept narrowed. FC3-B10.
S3-A6/B12. "few lines of code" cut; new source finops-definition-2024; 3.5 matched. Accept narrowed. FC3-A6.
S3-A7/A8/B11. Definition verified; table cell carries value purpose; opening "FinOps ... not built to govern". Accept.
S3-A13/B9. Table "grew from managing cloud cost and usage"; one remark not generalized. Accept narrowed.
S3-A9/B36. Gartner cannot confirm (Cisco corroborates); cell follows reproduced wording; gloss "Gartner's definition". Accept. Grade C.
S3-A10. Kreuzberger verified. Record.
S3-A11/B28. Klarna figures verified; resolution time attributed. Accept.
S3-A12. "powered by OpenAI". Accept. FC3-A12.
S3-B29. Case tasks: "the announcement"; "would be metered". Accept narrowed.
S3-R1/B15. Non-claims of every certified claim; record not exhaustive. Accept. FC3-R1.
S3-B4. Dated box: 9 of 11 theorems, 20 of 21 lemmas certified. Accept. FC3-B4.
S3-B14. Status computed; no one enters the status by hand. Accept narrowed.
S3-B17. "any certified theorem" (twice). Accept.
S3-B18. "a circular chain of recorded support" (zero cycles in the registry). Accept narrowed.
S3-B25. Disagreement over a proposition names the deciding fact. Accept.
S3-B13. Value boundary: book's practice separated from LEM-021, key term matched. Accept. FC3-B13.
S3-B21. P2 steps 3 and 6 state THM-002's risk. Accept. FC3-B21.
S3-B23. P1 step 2 states LEM-020's scope. Accept.
S3-B22. P1 "Its scope adds a requirement". Accept, P1 only.
S3-B7. Craft section: cut "the theorem says nothing about it" and the pilot sentence. Accept narrowed.
S3-B19. Flat-fee case recast. Accept. Para over 150 words, split (gate, A).
S3-B24. Procedure step 1: a name is a label. Accept (gloss, name untouched).
S3-B6, B8, B5, B16. Keep: proof record, scope and locked Ch2 wording support the text.
S3-B1. Caption and 3.6 no longer say the science establishes what is true. Accept. FC3-B1.
S3-B3. "each formal result the book presents" (3.1, summary). Accept narrowed.
S3-B27. "careful execution does not repair" (3.1, 3.4). Accept. FC3-B27.
S3-B31, B32, B33, B34. Practice not presented as fact; Chapter 1 conditions; example labelled; start of the discipline. Accept.
S3-B35. "A costly misreading". Accept. FC3-B35.
S3-B26. Five questions "from an organization's own records" (3.6). Accept. FC3-B26.
S3-B20. Keep: the book's argument.
S3-NEXT. Group 3 edited teaching prose after the review: scoped matrix re-runs the review for those passages before Stage 5.

---

## Stage 5. Design review

Owner: Claude

Status: [ ]        Date cleared: 

> v4 step 6, with G2 and G3 in the same session. Once, after the text is final, NEVER EARLY: Chapter 2 ran it early and ran it twice. Rasterize EVERY page and read it at the size it ships at: figures, callout placement, page fill, slot openings, running heads, key-term register, against the locked design system.

Findings:

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

P1. Gate 4: place.py could not name the split callout (wrapped term read interleaved). Fixed under the blocking exception: term read line by line. Callout moved one paragraph earlier, no text change. Commit 307d5a9.
P2. Gate 8: footnote 6 off page 2. Four glosses built and measured; footnote 5's gloss shortened to "The Foundation's definition." clears it. Commit 307d5a9.
P3. Page fill measured directly (the build advisory reports only page 15): pages 7, 13, 15 short before Figure 3.1, Figure 3.2 and Table 3.1. Figure 3.1 later splits the AI Business Economics callout, no fix in section; Figure 3.2 later strands the table caption. Kept: 7 at 207pt, 13 at 266pt, 15 at 353pt (DR3a, short page before a whole table).
P4. Cumulative case provenance set at 10pt (.problem > p beat p.provenance). Dan: A, CSS v7.2 .problem > p.provenance. Ch1, Ch2 pixel-identical.
P5. Table 3.1 caption had no rule (body text) and could strand. Dan: A, CSS v7.2 p.caption (figcaption style, break-before: avoid); Figure 3.2 kept at its reference. Ch1, Ch2 pixel-identical.
P6. Every page read at 75 dpi; figures at 150 dpi. Figure 3.1's smallest text 5.2pt (Ch2 minimum 6.0), legible on the raster. Kept.
P7. Observation, not fixed: the "Craft section" slot label sits close under the paragraph before it (base .slot-label has no top margin). Design system; fix-between-chapters list.

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

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

G2-1. AIOM_build.py on the final text: QA PASSED, fifteen of fifteen, 27 pages, 22 footnotes all on the calling page. Web preview W1 to W17 passed, none skipped (W6, W15, W16 ran in a browser). Site build and both self-tests passed (print 23/23 controls). MANUAL items done: figure geometry read on the raster, every page read, figure legibility checked (P6).

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

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

G3-1. Three promises owed to Ch3 verified kept in substance (Ch1: 3.5 says where each subject ends; Ch2: 3.2 and 3.3 on the third flow; Ch2: 3.4 names the discipline, now "addresses" the error after B-32) and marked paid with continuity.py --pay 3.
G3-2. THM-004 gloss drift: the author pass rewrote the gloss locked Chapter 2 fixed. Dan: A, ledger wording restored in 3.2; the B8 question stays with the holistic review (Decision 83). G3 PASSED. The eighth box stays open for Stage 9.
G3-3. Lock: continuity.py --update appended 16 terms, 21 forward references, 13 registry objects; the 13 glosses written by hand from the chapter's own restatements (craft section step 4, P1 step 4, P2 step 2, key terms). G3 re-run: 0 drifted, PASSED.
G3-4. Lock: the update logged Ch3's 14 back-references to Ch1 (5) and Ch2 (9) as open, which failed G3 on both locked chapters. All 14 are references back to locked text; spot-checked the two flagged by check B (Ch2's budget case, Ch1's Cursor licenses). Marked paid with --pay 1 and --pay 2, as Ch2 did at its lock. No other open rows pointed at Ch1 or Ch2.

---

## Stage 8. Sign-off

Owner: Dan (sitting 4)

Status: [ ]        Date cleared: 

> v4 step 7. Claude sends the render plus a short diff of everything that changed since the author pass. Dan approves the whole, or names ONE structural reason and the chapter returns to the step that owns it. The full read already happened in the author pass.

Findings:

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

SO0. Package built 2026-10-14 in `08_Stage8_Sign_Off/` by `build_signoff.py`: the final render (27 pp, fifteen print gates pass) and a diff since the author pass (b56819c), 45 changes by step (Sitting 3: 34, scoped re-review: 9, production: 2), plus one move with no words changed.
SO1. Sitting 4, 2026-10-14: Dan approved the whole (gate, A).

---

## Stage 9. Locked

Owner: Claude

Status: [ ]        Date cleared: 

> Frozen. Continuity ledger committed. After lock the only path is `amend.py` (CLAUDE.md section 8).

Findings:

ARCHIVED 2026-10-14, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

L1. Locked 2026-10-14. Ledger committed; final checks in the lock commit message.

---

## Chapter notes

Open items, deferrals, and anything a later chapter needs to know.
