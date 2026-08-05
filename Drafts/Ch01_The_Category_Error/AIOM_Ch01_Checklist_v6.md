# Chapter 1: The Category Error

Editorial checklist.

Markers: `[ ]` not started, `[~]` in progress, `[x]` passed, `[!]` failed.

Stages run in order. A chapter is not Locked until every stage above has
passed. Stages 6, 7, and 8 are all external and may be run in one sitting.
Stage 1 may not be batched with them: it runs early or it is worthless.

Gates are mechanical and stop the chapter where it stands. Passes are judgment.

Standing rules at every stage: no em dashes; every empirical claim cited or
cut; six-slot skeleton without exception; theorems are the only chapter
anchoring callouts; the six craft criteria in AIOM_Voice_and_Craft_v1.md bind
from Stage 0 forward, not from Stage 4.

---

## Process v2 numbering

This chapter was drafted under Process v1 and renumbered to Process v2 on
2026-08-01. The section headers below use v2 numbers. Dated findings and the
chapter's HTML source block keep their original v1 labels; read them through the
CLAUDE.md section 8 mapping (v1 Stage 2 fact check is v2 Stage 3, v1 Stage 3
voice is v2 Stage 4, v1 Stage 4 design is v2 Stage 5, and so on). The
developmental edit, new in v2, is Stage 2.

---


## REOPENED 2026-08-05: Stage 0 and everything after it

Grounds: Full re-draft ruled by Dan 2026-08-05. Chapter 1 was drafted before the voice and craft standard existed (Decision 52), so its prose was never written against C1 through C6, and the Stage 4 craft read found seven findings including a systematic C5 failure and the weakest C4 unit in the book. Chapter 1 is the exemplar fourteen further chapters are drafted against, so it is re-drafted from Stage 0 with the craft standard binding, rather than patched. The re-draft is also the proving run for Process v2 end to end.

Every step from Stage 0 forward is reset to not-run. Their sub-checkboxes are cleared and their findings are archived in place, marked superseded. Steps before the reopen point are untouched and keep their passes.

Reopened by `reopen.py`. Per CLAUDE.md section 8, a reopen re-runs every step from the one that owns the change, and no chapter is Locked until every step is complete again.

| Step | Name | Was | Sub-boxes cleared |
|---|---|---|---|
| Stage 0 | Draft | passed | 0 |
| Gate G1 | Structural gate | passed | 12 |
| Stage 1 | Content review | passed | 0 |
| Stage 2 | Developmental edit | passed | 0 |
| Stage 3 | Source and fact check 1 | passed | 0 |
| Stage 4 | Voice and craft check | passed | 0 |
| Stage 5 | Design review | passed | 0 |
| Gate G2 | Production gate | passed | 10 |
| Stage 6 | Copy edit | not run | 0 |
| Stage 7 | Final fact check 2 | not run | 0 |
| Gate G3 | Continuity gate | not run | 0 |
| Stage 8 | Final read | not run | 0 |
| Stage 9 | Locked | not run | 0 |

---
## Stage 0. Draft

Owner: Claude

Status: [x]        Date cleared: 2026-08-05

> Against the chapter outline and the fixed six-slot skeleton. The craft standard binds here, not only at Stage 4.

- [x] Drafted against the six craft criteria (AIOM_Voice_and_Craft_v1.md), read before drafting rather than after

Findings:

ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

Draft complete, 4,557 words, 167 lines.

RE-DRAFT COMPLETE 2026-08-05. `00_Stage0_Draft/AIOM_Ch01_redraft.html` is the
live text for Chapter 1 and supersedes the Stage 4 render, which is now history.
5,949 words after the G1 fix below, inside the 5,000 to 6,000 band (Decision 33)
with 51 words of headroom left for Stage 2 and Stage 4. Six slots present and in
order. Sources unchanged: the same nine cleared keys, spliced verbatim with the
Decision 51 source block, so no citation is new and none was invented.

DRAFTED AGAINST THE CRAFT STANDARD, which is what makes this a re-draft rather
than a patch. Changes answering the archived Stage 4 findings:

- F1 (C1, the FinOps passage). The three unanchored empirical claims about the
  current state of practice are GONE, replaced by a structural account: each of
  the five questions falls inside some existing practice's scope, every one of
  those scopes was bounded before this resource existed, and a resource crossing
  all five boundaries is owned by none of them. This satisfies the evidence
  policy by conditionalizing rather than by citing. IT ALSO DROPS THE NAME
  "FinOps" FROM CHAPTER 1. RULED at Stage 1 as finding S6, 2026-08-05: fine as
  drafted. Chapter 14 remains where the book engages FinOps by name, with the
  cited CB2 material and the boundary treaty.
- F2 (C1, no arithmetic in the craft artifact). Step 4 now works the numbers.
  Against a stipulated five thousand seats, the deployment bills roughly 54.6
  million consumption events a month, about 10,900 behind every seat. The
  paragraph then states that changing any stipulated figure moves the total while
  the seat count moves for none of them, which is the actual point.
  SUPERSEDED WITHIN THIS STAGE: this draft first used the published count 5,172,
  which broke a standing source ruling. G1 caught it. See the G1 findings; the
  arithmetic gain survives, the precise figure does not.
- F3 (C3). "A word on the borders of the subject" is cut. 1.5 opens on the
  finding. Throat-clearing openers: 1 to 0.
- F4 (C5, systematic). All four cross-reference closes are gone: 0 of 44.
  CORRECTION TO THE ARCHIVED FINDING: one of the four (the Chapter 6 reference)
  sat inside a <cite>, which becomes a footnote at build, so it was never body
  prose. voicecheck.py now strips cite content before measuring, a tooling fix
  this re-draft surfaced.
- F5 (C4, the summary). Rewritten. Mean sentence length 33.6 to 17.9, stdev 17.1
  to 8.5, short sentences 0 percent to 20 percent.
- F6 (C2). "What is absent is not attention. It is assembly." now arrives after
  the explanation of what produced the fragmentation, not instead of it.
- F7 (C2). 1.2 now ARGUES the atomic unit rather than asserting it, ruling out
  the user (two identical seats differ by an order of magnitude) and the task
  (right for value, does not track cost), and stating the decisive criterion:
  the event is the only candidate the meter records, and a unit the meter does
  not record cannot be reconciled against a bill. A fourth discussion question
  makes the reader argue the other side.
- W1, W2 (C6). Both left as drafted. The vendor comparison is recast so the
  structural point closes the passage rather than the characterization.

Metrics after: mean 17.5, stdev 10.6, 33 percent short, 0 throat-clears, 0
cross-reference closes, no section flagged uniform-and-long. Chapter 1 no longer
sets a baseline that contains a known C4 failure and a systematic C5 failure.

REGRESSION CAUGHT AND FIXED IN-PASS. The first version of the F3 fix collapsed
1.5 into one uniform paragraph, mean 23.8 words with zero short sentences, which
the per-section table flagged immediately. The chapter average never moved. This
is the second time the section table caught something the chapter total hid.

CARRIED, NOT FIXED HERE. Gate 14 still reports the CD1 stranded "Craft section"
slot label at the foot of page 12. That is break control, so it belongs to Stage
5, and fixing it at Stage 0 would be doing design work in a drafting stage.
Everything else in the fourteen-gate suite is green on the re-draft.

The craft-criteria box above is ticked on the strength of this re-draft, which
is the first Chapter 1 draft written with the standard in hand rather than
audited against it afterwards.

---

## Gate G1. Structural gate

Owner: Claude

Status: [x]        Date cleared: 2026-08-05

> Mechanical. Runs before Dan sees the chapter, so no reading time is spent on a draft with a defect a script could find.

- [x] All six slots present, in order, correctly headed
- [x] Opening case carries a provenance line under its title
- [x] Every exit competency assigned to this chapter is addressed
- [x] Every registry ID cited resolves against Locked Registry v1.3
- [x] Tier rules hold: one theorem callout, lemmas by ID, propositions by ID
- [x] Every empirical claim carries a citation; every source carries an access date (Decision 48, no archival)
- [x] Every Slot 5 key term appears defined in the body
- [x] Zero em dashes
- [x] Word count inside the chapter target band
- [x] Gloss-less lemmas carry a book-authored gloss, marked as such

Findings:

G1 PASSED 2026-08-05 on the re-draft, after one real failure was found and
fixed. Run mechanically against
`00_Stage0_Draft/AIOM_Ch01_redraft.html`. All ten checks green on re-run.

    1.  six slots, in order ......... PASS   5 teaching sections, 1.1 to 1.5
    2.  opening-case provenance .... PASS
    3.  competency C1 addressed .... PASS   3/3 markers
    4.  registry IDs resolve ....... PASS   THM-009, statement verbatim vs v1.3
    5.  tier rules ................. PASS   1 theorem callout, 0 lemmas, 0 props
    6.  citations and access dates . PASS   11 keys cited, all in register
    7.  key terms named in body .... PASS   7 of 7
    8.  em and en dashes ........... PASS   0
    9.  word count ................. PASS   5,949 (band 5,000 to 6,000)
    10. gloss-less lemma glosses ... PASS   no lemma cited, none required

FAILURE FOUND AND FIXED: the re-draft violated a standing source ruling.

Check 6 surfaced brynjolfsson-2025-genai, and reading its register note to
settle the question turned up a ruling of 2026-07-29 that the Stage 0 re-draft
had broken. The note reads: the worked example is labelled a stylized
application rather than bound to the study's parameters, "on the reasoning that
a precise agent count above a stipulated inventory would falsely signal that the
whole inventory is reported. Chapter 1 therefore says on the order of five
thousand agents and states no productivity figure at all." The published figure
5,172 is reserved for Chapter 6, where the study is reported rather than adapted.

The re-draft had put 5,172 into the prose in four places, on the strength of the
shorter summary note in AIOM_Source_Ledger.md, which says only "CITE THE
PUBLISHED FIGURES" without carrying the Chapter 1 restriction. The fuller ruling
lives in the chapter's own source register. CD4 states that a reopen resets
steps, not rules, so the ruling stood and the re-draft was wrong.

Fixed: the prose returns to "on the order of five thousand agents," the Step 4
arithmetic now stipulates a round five thousand and says so, and the citation
footnote states explicitly that the event architecture and volumes are
stipulated and not reported by the study. Body prose now contains zero
occurrences of 5,172; the only one left is the Chapter 6 instruction inside the
source register, which is where it belongs. The F2 craft gain survives intact:
25.2 million suggested-reply generations, 25.2 million retrievals, 4.2 million
close operations, roughly 54.6 million consumption events a month, about 10,900
behind every seat. Arithmetic verified: 5,000 x 40 x 6 x 21 = 25,200,000;
5,000 x 40 x 21 = 4,200,000; total 54,600,000; 54,600,000 / 5,000 = 10,920.

Word count moved 5,922 to 5,949 with the fix. Still in band, 51 words of
headroom.

CORRECTION TO THE GATE, NOT THE CHAPTER. Check 6 first reported a failure
because it required an access date on every cited source. Decision 48 rests
durability on the access date for PERISHABLE sources; brynjolfsson-2025-genai
carries `"perishable": false` and a DOI, and its note says plainly "Non-
perishable: cited by DOI, so no access date is required." The check now tests
perishable sources only and names the exempt ones in its output, so the
exemption is visible rather than assumed. The checkbox wording is unchanged and
still accurate.

NOTE FOR STAGE 1, not decided here. The 2026-07-29 ruling reasoned that a
precise count above a stipulated inventory would falsely signal that the whole
inventory is reported. The re-draft mitigates that reasoning: the provenance
line now says volume assumptions are stipulated and labelled where used, Step 4
opens by stipulating them in the prose, and the citation footnote states what
the study does not supply. Dan may wish to revisit whether the precise figure is
now safe in Chapter 1. Until he rules, the ruling stands as written.

## Stage 1. Content review

Owner: Dan

Status: [x]        Date cleared: 2026-08-05

> Is this the right chapter, not is it true. Read against the outline and the competency map. Structural findings only, no line edits.

Findings:

STAGE 1 PASSED 2026-08-05, on the re-draft. Owner: Dan. Read against the
Consolidated Spec Ch1 outline, the competency map, and the assessment list.
Structural findings only, no line edits.

WHAT MATCHED. All six slots present and in order. Teaching body 1.1 to 1.5 as
outlined. THM-009 anchoring callout in 1.3, verbatim against Locked Registry
v1.3. Both dated evidence boxes where the spec puts them: OpenAI January 2025
(Case 4.1), Anthropic July 2025 (Case 4.2). Competency C1 covered end to end.
Assessment 1 is P1, matching the assessment text word for word. Assessment 7 is
seeded, since P1 is framed as a board member writing in.

SEVEN STRUCTURAL FINDINGS RAISED. All seven ruled by Dan the same day.

S1. THE CASE BANK HELD NO ENTRY 4.6 AND NO ENTRY 6.4, both of which the spec
assigns to this chapter: 4.6 is the GitHub Copilot episode, half the opening
case, and 6.4 is the QJE contact-center deployment, the whole craft section. The
bank ran 4.1 to 4.4, 6.1 to 6.3, 5.1, 5.2. The chapter was never defective:
both bodies of material are carried and fully sourced through its own Decision
51 register, all eleven keys resolving under G1. The BANK was out of sync with
the spec, and fourteen further chapters reference bank IDs.
RULED: add both entries from the chapter's already-cleared sources. DONE
2026-08-05. CASE 4.6 and CASE 6.4 are written into AIOM_Case_Bank_v1.md from
sources already cleared through the Ch1 register and its fact check, with no new
research and no new claim. Each carries a provenance line saying so. CASE 6.4
carries the figure discipline (published QJE figures only, never the 2023 NBER
14 percent or 5,179) and the 2026-07-29 stipulation ruling, so the next chapter
to use the study meets both rules in the bank rather than having to find them in
Chapter 1's source register, which is how G1 caught the breach in the first
place.

S2. FIGURE NUMBERING WAS REVERSED against the spec: the spec made 1.1 the two
purchase models and 1.2 the anatomy; the chapter has the anatomy first. The
chapter's order was ruled during the original run so figures appear in document
order.
RULED: the chapter stands and the spec is amended. DONE.

S3. THE OPENING CASE DID NOT CLOSE ON THE SPEC'S QUESTION, "what did these
organizations actually purchase?", because the standing rule forbids rhetorical
questions in body prose. The chapter closes on the category error stated.
RULED: whatever is more effective inside the chapter wins, on educational and
style grounds. The chapter stands and the spec is amended to direct a stated
close rather than a question the standing rules forbid. DONE.

S4. FOUR DISCUSSION QUESTIONS, NOT THREE. The fourth was added at Stage 0 to
answer craft finding F7, asking the reader to argue for the task as the atomic
unit instead of the event.
RULED: accepted. Spec amended to four. DONE.

S5. P2 USED A CONSTRUCTED DEPLOYMENT where the spec said "second cited
deployment."
RULED: relax the spec. The evidence policy governs empirical claims, not
exercise scaffolding, and P3 is constructed for the same reason. Spec amended.
DONE.

S6. FINOPS NO LONGER APPEARS IN 1.4, carried from Stage 0. The three claims
around the name were unsourced empirical statements about the current state of
practice, and the evidence policy allows only cite, conditionalize, or cut. The
passage is now a structural account of why no practice owns the resource.
RULED: fine as drafted. Chapter 14 remains where the book engages FinOps by
name, with the cited CB2 material and the boundary treaty.

S7. THE AGENT-COUNT RULING of 2026-07-29, carried from G1. It reserves the
published 5,172 for Chapter 6 and requires "on the order of five thousand" here.
RULED: fine as written. The ruling stands unchanged. The re-draft's three
stipulation labels do not reopen it.

RE-RUN CONSEQUENCE: NONE. Under the scoped re-run matrix, no downstream step is
invalidated. Every ruling either confirmed the chapter as drafted (S2 to S7) or
changed an artifact outside the chapter text (S1, the case bank). Not one word
of the chapter changed at Stage 1, so Stage 0 and G1 stand and Stage 2 may
proceed against the same text. This is the outcome the matrix is for: a
content review that ruled seven findings and cost zero re-runs.

## Stage 2. Developmental edit

Owner: Claude

Status: [x]        Date cleared: 2026-08-05

> Teaching quality, held early so its line edits do not churn fact check, voice, design, and production. Clarity, pacing, cognitive load, example fitness, transitions, and whether the argument carries the target reader without a stall. Claude runs a fresh critical pass; Dan gut-checks with a second model and rules.

Findings:

STAGE 2 PASSED 2026-08-05. Dan ruled: apply ND1 through ND4. ND5 and ND6 stand
as recommended, no action. Applied and verified the same day.

ND1 APPLIED. The atomic-unit argument moved to sit after the anatomy and Figure
1.1, so the reader meets the meter as recorder before being asked to judge the
unit on whether the meter records it. Section 1.2 now runs: name the unit,
anatomize the event, Figure 1.1, argue the unit, Figure 1.2, contrast the two
economics. A side benefit not anticipated in the finding: the two figures were
previously jammed together, and each now sits beside the prose it illustrates.
Zero words.

ND2 APPLIED. Twelve words reconcile the two accounts of the absence: "They are
inheritance, and it is the same inheritance that left the resource unowned."
Deliberately placed inside the inheritance paragraph rather than as a new
sentence, so "those absences" keeps referring to the three named in the previous
paragraph and no new terminology competes with them.

ND3 APPLIED. Step 4 splits at "Change any stipulated figure and the total
moves." The arithmetic closes one paragraph; the invariance point, the
two-agents contrast, and the cost driver open the next. Zero words.

ND4 APPLIED. "the definition just given" is now "the definition given in 1.2."

Word count 5,949 to 5,961. In band, 39 words of headroom. Mechanical voice check
clean on all four. G3 passes.

LAYOUT CONSEQUENCES, CARRIED TO STAGE 5, NOT FIXED HERE. Applying ND1 changed
pagination, which is expected and is why the matrix pulls Stage 5 and G2. Doing
the fixes now would be design work inside a drafting stage.

  CD1  (unchanged) "Craft section" slot label stranded at the foot of page 12.
  CD6  (NEW, caused by ND1) One definition callout splits across a page break.
       Remedy is documented and mechanical: run place.py. Do not attempt this in
       CSS; WeasyPrint 69 ignores break-inside on floated elements.
  CD7  (NEW, pre-existing but newly visible) A widow and an orphan on page 16.
       Verified pre-existing by running the corrected gate against the pre-ND1
       render, where both appear. ND1 did not cause them. The gate could not see
       them.

A LATENT DEFECT IN MY OWN GATE, FOUND BY APPLYING ND1 AND NOW FIXED. Moving
Figure 1.1 to an odd page made gate 12 report "text references a figure that has
no caption." The caption was intact. The design MIRRORS ITS MARGINS for binding,
so the main text column starts at x0 68.4 on recto and 57.6 on verso, and gates
12 and 14 hard-coded a single left edge of 60.0. Consequences, both silent:
gate 12 could not recognise a caption on any odd page, and gate 14 excluded every
odd-page line from its corpus, so odd pages were never analysed for widows and
orphans at all and the measure and leading thresholds it applied to even pages
were derived from half the book. Both gates now derive the column edge per page
from the modal x0 of body-size lines. On the corrected gate, gate 12 reads 2
captions and gate 14 finds the page 16 widow and orphan that the eleven-gate and
the broken fourteen-gate suites both passed.

This is the third time in this chapter's re-run that a check has been wrong in a
way that read as green. The pattern is worth naming: every one was a check I
wrote, and every one was found by changing the input rather than by re-reading
the code.

ND5 CLOSED, NO ACTION, as recommended. The chapter still gives no rate against
which to size 54.6 million events a month. The fifty-year rule quarantines
prices and Chapter 5 owns cost anatomy, and the single forward-pointing sentence
that would answer the reader is the decorative signposting standing rule 5
forbids. Recorded as a decision, not an oversight.

ND6 CLOSED, NO ACTION on the chapter, WITH ONE OBLIGATION AT LOCK. "Flow"
carries technical weight in 1.4 and the summary and belongs to Chapter 2. When
this chapter reaches Stage 9, `continuity.py --update` must NOT record "flow"
among the terms Chapter 1 owns. Chapter 2 owns it. Left unchecked, Chapter 2's
definition would register as a redefinition of a Chapter 1 term and G3 would
fail Chapter 2 for a defect that is really a mis-logged ledger entry.

RE-RUN CONSEQUENCE. ND1 to ND3 are body-prose changes; ND4 is a copy edit. Per
the scoped matrix these pull Stage 3 fact, Stage 4 voice and craft, Stage 5
design, and G2. All four are already open following the reopen, so nothing
reverts and no work is lost. No claim, figure, citation, or slot changed, so G1
stands and Stage 3 is a confirmation of an unchanged fact surface rather than a
re-check, which is Dan's call.

SECOND-MODEL GUT-CHECK STILL OPEN. Dan may still run the prompt below against
the amended chapter. Agreement confirms; a stall it names that this pass missed
enters as ND7 onward.

SECOND-MODEL GUT-CHECK PROMPT for Dan, per the Stage 2 protocol. Give the second
model the chapter HTML and this instruction, and do NOT give it the findings
above.

> You are reviewing one chapter of an academic textbook for TEACHING QUALITY, not
> for correctness and not for style. The reader is an intelligent, busy, sceptical
> MBA-level graduate student who has read business books before and can tell when
> one is padded.
>
> Read it once at reading pace. Then answer, with quotations:
>
> 1. Name every place you had to re-read a sentence or paragraph to follow it, and
>    say what caused the stall.
> 2. Name every place where the chapter asks you to accept or judge something
>    before it has given you what you need to judge it.
> 3. Name every place where the same point is made twice, and say whether the
>    repetition earns its place.
> 4. Where does the chapter drag, and where does it move too fast for the load it
>    is carrying?
> 5. Does any worked example fail to earn its space?
> 6. At the end, what can you actually do that you could not do before? Answer
>    concretely; if the answer is thin, say so.
>
> Do not comment on prose style, word choice, or punctuation. Another pass owns
> those. Assume every fact is correct. Your only question is whether this teaches.

Compare the second model's answers against ND1 to ND6. Agreement raises
confidence. A stall it names that this pass missed is the more valuable output
and goes in as ND7 onward. Disagreement is Dan's to rule.

ARCHIVED RECORD OF THE SUPERSEDED PASS FOLLOWS.


ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

Added under Process v2 (2026-08-01). Chapter 1 predates this stage and is being
run retroactively. Claude ran the developmental pass 2026-08-01; findings below
AWAIT Dan's second-model gut-check and ruling. Nothing is applied. Any edit Dan
approves re-runs only its downstream steps per the scoped re-run matrix.

WHAT IS STRONG. The argument arc is clean (two vendors, category error, the two
economic models, the objection answered, what follows, borders). The steel and
goods-flow analogy is apt and on brand. Worked examples earn their place,
especially the CIO memo reply. Backward design is met: 1.1 to 1.3 plus P1 deliver
C1. The notes below lift the chapter from correct to maximally well taught.

FINDINGS, PRIORITIZED (for Dan to rule item by item):

D1 (HIGH). Section 1.4 carries too many distinct moves in about eight
paragraphs: the steel analogy, an informal five questions, the absent-discipline
point, three absences, inheritance not negligence, scale, and stakes. Two
enumerated lists (five questions, three absences) sit two paragraphs apart and
can blur. Recommend signposting the through-line or splitting 1.4.

D2 (HIGH). The seat-versus-event cost curves (now Figure 1.2) are the chapter's
big-idea visual (cost flat versus cost as area under use), but they land at the
end of 1.2 after the anatomy, while the big idea is stated in 1.1. Pedagogy
commitment is one strong figure per big idea at first exposure. Consider
anchoring the seat-versus-event contrast nearer 1.1. Interacts with the figure
order set 2026-08-01, so a judgment call, not a redo.

D3 (MEDIUM). The opening front-loads vendor mechanics (request counts, Sonnet
counting as two, the twenty-dollar pool, exact dates) before the reader has the
consumption-event frame. Consider lightening the opener to the shape of the
correction and letting Ch4 carry the granular numbers. Tension: the opener is a
dated case, where specifics are allowed, so a judgment call.

D4 (MEDIUM). The informal five questions in 1.4 are the same five posed formally
as the Founding Questions in Ch3. This may be deliberate withholding, which the
standing rules protect, or an accidental near-duplicate. Dan rules which; if
intentional, leave it, if not, a light this-book-will-return signal helps.

D5 (MEDIUM). The what-a-theorem-means aside in 1.3 interrupts the meter-relocation
momentum (necessary, first theorem in the book). Consider tightening it or
repositioning so the argument does not brake for a definitional aside.

D6 (LOW). Seven key terms is a heavy vocabulary load for a first chapter; confirm
each is load-bearing (likely locked by spec).

NEXT: Dan gut-checks with a second model, rules which findings to action. D1 and
D2 most affect how well the chapter teaches. On a ruling, Claude drafts the
specific edits for approval, then re-runs the downstream steps each edit touches.

D1 RULED AND RESOLVED 2026-08-01. Dan ruled: signpost and tighten, no split. The
section is correct and in band on length; the defect is enumeration blur and move
density, not length. Three edits applied to AIOM_Ch01_Stage4_FINAL.html, the
authoritative source:

- EDIT 1 (signpost), 1.4 paragraph 2. The five questions are now named as the
  same five practices recast, so the reader reads a concrete-then-abstract pairing
  rather than two independent lists. "The same five practices, stated in timeless
  form, are not techniques belonging to manufacturing. They are the questions ..."
- EDIT 2 (tighten), 1.4 paragraph 3. The third full re-enumeration of the five
  ("no practice yet sources ... plans ... records ... allocates ... holds") is
  compressed to "no practice yet assembles them under one vocabulary and one
  owner." The assembly and one-owner payoff is preserved; about 25 words drop.
- EDIT 3 (signpost), 1.4 paragraph 5. The three absences now open with "The
  failure to answer those questions is not abstract," bridging the five-to-three
  count shift as symptom of cause rather than a fresh list.

The five is now enumerated once in full (as practices), recast once as questions
with the link made explicit, and referred back to thereafter. The steel texture
in paragraph 1 is untouched.

D4 TOUCH NOTED. EDIT 1 moves the numeral "five" one paragraph earlier than it
previously appeared (paragraph 3 already said "the five questions"). This lightly
sharpens the tie to Ch3's five Founding Questions, which is D4's territory. If D4
is later ruled accidental, revisit this word.

DOWNSTREAM RE-RUNS (scoped re-run matrix, body prose edit):
- Stage 4 voice: RE-RAN 2026-08-01, PASS. voicecheck.py clean (0 em dashes, 0
  contractions, 0 stray question marks, 0 first or second person in body prose).
- Stage 5 design: RE-RAN 2026-08-01 on the post-D1 render, PASS. Callouts intact,
  figures on page 6 (section 1.2) untouched; first-pass visual review of pages 9
  to 11 shows no widows, orphans, or stranded heads, and the 1.4 head is well
  seated.
- G2 production: RE-RAN 2026-08-01, PASS. Full eleven-check suite green on the
  19-page re-render (page count unchanged).
- Stage 3 fact check (Dan): RULED PASS 2026-08-01 by Dan. Body prose changed but
  no empirical claim, citation, number, or figure changed, so the fact-checkable
  surface is untouched and the 2026-07-29 pass holds.

D2 RULED AND CLOSED 2026-08-01, no action. Dan ruled to keep the seat-versus-event
figure (Figure 1.2) at the end of 1.2. Reasoning: first exposure to the big idea
is already delivered verbally in 1.1 ("the marginal cost of an additional use is
not approximately zero. It is the central fact."); the figure reinforces it one
section later, where its own vocabulary ("event model," "consumption event") is
defined; build-then-visualize is a legitimate teaching order; moving it would
forward-reference an undefined term in the caption, gut the 1.2 closing crescendo,
and reopen the figure order deliberately set 2026-07-31. No prose or figure change,
so no downstream re-runs.

D3 RULED AND CLOSED 2026-08-01, no action. Dan ruled to leave the opener as
drafted. The opening case is a dated case, where granular specifics (request
counts, Sonnet counting as two, the twenty-dollar pool, exact dates) are allowed,
and Ch4 carries the granular numbers by design. No change, no downstream re-runs.

D4 RULED AND CLOSED 2026-08-01, no action. Dan ruled the near-duplicate
intentional: the informal five questions in 1.4 foreshadow the formal Founding
Questions in Ch3. Left as drafted, and deliberately with no "this book will
return to these" signal, since a forward flag would telegraph the Ch3 payoff and
dilute the foreshadow (protect pedagogical surprises, CLAUDE.md section 9). The
D1 EDIT 1 "five" numeral now reinforces the intended foreshadow and stays. No
change, no downstream re-runs.

D5 RULED AND RESOLVED 2026-08-01. Dan ruled: tighten in place. The theorem aside
in 1.3 (paragraph after the THM-009 callout) did two things, and only the first
braked momentum: a methodological aside defining "theorem," then the application
of the theorem to the flat-rate objection. The application also translates the
dense formal THM-009 statement into plain antecedents, teaching work, so it is
left intact. One edit applied to AIOM_Ch01_Stage4_FINAL.html:

- The methodological aside is compressed from four sentences to two. The qualifiers
  ("not an empirical generalization ... binds only where its antecedents hold") are
  folded into the definition sentence, and the standalone Chapter 3 pointer
  ("Chapter 3 sets out the registry and traces one theorem to its foundations") is
  dropped as the most aside-like part; Ch3's trace set piece stands on its own.
  About 22 words drop and the reader returns to the argument at "The theorem does
  not say ..." without the two detours.

DOWNSTREAM RE-RUNS (scoped re-run matrix, body prose edit):
- Stage 4 voice: RE-RAN 2026-08-01, PASS. voicecheck.py clean.
- Stage 5 design: RE-RAN 2026-08-01 on the post-D5 render, PASS. THM-009 panel
  intact, page 8 visual review shows no widows, orphans, or stranded heads.
- G2 production: RE-RAN 2026-08-01, PASS. Eleven checks green on the 19-page
  re-render (page count unchanged).
- Stage 3 fact check (Dan): no empirical claim, citation, number, or figure
  changed, so the fact surface is untouched and the pass holds (Dan's standing
  ruling of 2026-08-01 for this kind of edit).

D6 RULED AND CLOSED 2026-08-01, no action. Dan ruled to keep all seven key terms.
Confirmed load-bearing against the body: consumption event (12 body uses, the
atomic unit), software access model (3, the wrong model) and resource consumption
model (1, its named counterpart, set against it in the chapter summary as the C1
payoff), access price (4), metered resource (4), flat-rate objection (2), and
meter relocation (2). All seven are exactly the terms the spec names (Stage 1),
so they are spec-locked. Nothing cut. No change, no downstream re-runs.

STAGE 2 COMPLETE 2026-08-01. All six developmental findings ruled: D1 resolved
(1.4 signpost and tighten), D2 closed (figure placement kept), D3 closed (opener
kept), D4 closed (five questions are intentional Ch3 foreshadowing), D5 resolved
(theorem aside tightened), D6 closed (seven key terms confirmed load-bearing).
The two applied edits (D1, D5) re-ran Stage 4 voice, Stage 5 design, and G2, all
green on the 19-page render; the Stage 3 fact surface was untouched throughout.

---

## Stage 3. Source and fact check 1

Owner: Dan

Status: [ ]        Date cleared: 

> Every empirical claim traced to primary source. Runs before voice and design so corrections do not churn later polish.

Findings:

ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

STAGE 2 PASSED 2026-07-29, run by Dan against AIOM_ch01.html. The fact-check
record lives in the chapter's own source block (Decision 51): every source
verified live on its access date, bylines and dates confirmed by direct fetch,
and the raises resolved are logged there as items A2 to A7 and B1, B2 (for
example the Microsoft 4.7 million and 75 percent figures pinned to the Nadella
sentence, the Anthropic July 17 tightening given its own primary, the Cursor
date held at July 4, and the GitHub exceptions and all-plans scope verified).

The current Stage 4 render differs from that fact-checked draft only by the
Figure 1.1 and 1.2 reorder and reference fix, which is layout and touches no
prose, citation, or fact. Verified by diff 2026-08-01: the two files are
byte-identical outside those figure lines, so Stage 2 holds against the current
version.

---

## Stage 4. Voice and craft check

Owner: Claude

Status: [ ]        Date cleared: 

> Two halves. The mechanical half is voicecheck.py. The judgment half is the six craft criteria below, read against AIOM_Voice_and_Craft_v1.md. voicecheck.py prints advisory craft metrics proxying C1, C3, C4, and C5; the metrics inform the read and never decide it. C2 and C6 have no proxy and are enforced by reading alone.

- [ ] C1 concrete particular: every abstraction carrying argumentative weight is anchored to a named, specific instance
- [ ] C2 context and stakes: every mechanism states the conditions that made it available and what it settles, not only what it does
- [ ] C3 front-loaded sentences: findings lead, qualifications subordinate, no throat-clearing openers
- [ ] C4 deliberate rhythm: sentence length varies, no long stretch at a uniform length
- [ ] C5 paragraph close: paragraphs end on the load-bearing clause, not a trailing qualifier
- [ ] C6 the guard holds: no hero or villain framing, no populist register, no character-driven causation where a structural account is available

Findings:

ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

CRAFT HALF ADDED 2026-08-05. The six criteria above postdate the 2026-07-28
pass, which tested the prohibitions only. The craft read below has been RUN but
the boxes are deliberately left OPEN, because whether Chapter 1 adopts the new
standard or is grandfathered is Dan's ruling and it is not yet made.
status_check.py will report Stage 4 as FAILED until that ruling lands. The
failure is accurate, not a defect: this step is marked passed against a standard
that has since changed.

Resolution is one action either way. Adopt: tick the six boxes on the strength
of the read below, no prose change required. Grandfather: mark the six with a
stated "postdates" exception, as Stage 0 above is marked.

CRAFT READ, 2026-08-05, against AIOM_Ch01_Stage4_FINAL.html.

METHOD NOTE, AND A CORRECTION. A first read the same day returned "meets all six
criteria, no finding." That read was not adequate verification and its verdict is
withdrawn. Two defects in it. It was CIRCULAR: the craft standard was extracted
partly from this chapter's prose, so grading this chapter against it was a test
that could not fail. And it was CONFIRMATORY: it asked whether each criterion was
met rather than hunting the worst instance of each. The read below is adversarial
and section-by-section, and it found five criteria carrying real findings. The
chapter-level metrics did not change. The conclusion drawn from them did.

Metrics (advisory): 43 paragraphs, 225 sentences, 3,992 words of teaching prose.
Sentence words mean 17.7, median 15, stdev 10.5, range 3 to 61. Short sentences
under twelve words 32 percent, long over thirty-five 6 percent. Longest uniform
run 4 sentences. Throat-clearing openers 1. Copulas 4.0 per 100 words.
Nominalizations 50.6 per 1,000. Numerals 9.5 per 1,000, proper nouns 12.3 per
1,000. Trailing-qualifier closes 4 of 43, cross-reference closes 4 of 43. THIS IS
THE BASELINE BAND. Chapters 2 through 15 are read against these numbers.

TOOLING HARDENED BY THIS AUDIT. Two blind spots the audit found in voicecheck.py
are now closed: it reports per section, because the chapter average concealed the
summary entirely, and it detects cross-reference closes, which the
trailing-qualifier proxy cannot see because a cross-reference is not a
subordinate clause. Both changes are committed. A proxy that misses a whole class
of defect is worth more once the miss is known than a proxy nobody has tested.

FINDINGS. Seven, plus two watch items. None is a chapter-level failure of a
criterion. All are Dan's to rule.

F1 (C1, section 1.4). The FinOps, observability, and chargeback passage makes
three claims about the current state of practice with no named instance, no
number, and no citation key: "Cloud financial management, practiced as FinOps,
has turned its attention to AI spend. Observability tooling reports token
consumption by model, by team, and by workload. Chargeback conventions borrowed
from cloud allocate some of that cost to the units that incur it." This is the
weakest C1 stretch in the chapter, and it also brushes the evidence policy, since
all three are empirical claims about the world. Note the Workplan records CB2
FinOps data as ready for Chapter 14.

F2 (C1, craft section). The consumption-event inventory contains no arithmetic
anywhere. The chapter asserts the gap between "five thousand seats" and
quantities "that run to the millions" but never shows one number doing the work.
For the book's first craft artifact, whose stated purpose is revealing what the
seat count conceals, a single worked multiplication would demonstrate what four
paragraphs currently assert. This is the largest craft opportunity in the
chapter, and it is a Stage 2 developmental question as much as a Stage 4 one.

F3 (C3, section 1.5). "A word on the borders of the subject." is a
throat-clearing opener: a sentence announcing that a statement is coming. The
metric missed it because the regex does not cover the construction. It also
brushes standing rule 5, no decorative apparatus, since it signposts in prose
what the section heading already says.

F4 (C5, systematic). Four paragraphs close on a cross-reference rather than on
argument: 1.2 ends on "Figure 1.1 sets out that anatomy, from the assembled input
through the computation to the meter beneath"; 1.5 ends on "are the business of
Chapter 3"; the craft-section case ends on "It returns in Chapter 6 as the book's
anchor case on realized value"; the summary ends on "which is the work of Chapter
2." Each hands the reader a pointer where the load-bearing clause belongs. This
is the clearest systematic C5 pattern in the chapter and the original proxy was
blind to all four.

F5 (C4, chapter summary). The weakest C4 unit in the chapter, by the chapter's
own baseline. One 168-word paragraph, five sentences, mean 33.6 words against a
chapter mean of 17.7, stdev 17.1, and ZERO sentences under twelve words. Nothing
lands because nothing is short. Invisible in the chapter average, which is why
the per-section table now exists.

F6 (C2, section 1.4). "What is absent is not attention. It is assembly." asserts
the gap without explaining what conditions produced the fragmentation. It sits
two paragraphs from the inheritance passage, which is the chapter's strongest C2
work, so the standard it falls short of is its own local one.

F7 (C2, section 1.2). Why the consumption event is the atomic unit, rather than
the request, the task, or the conversation, is asserted and not argued. C2 asks
for the conditions that make a choice available and what it settles. Possibly
deliberate, since Chapter 2 takes up flows; recorded so the deferral is a
decision rather than an omission.

W1 (C6 watch, opening case). "One vendor corrected its pricing under public
pressure, retroactively, with an apology and refunds. The other corrected its
pricing on a published schedule, announced in advance and supported by tooling."
The comparison characterizes conduct before "The correction was the same" pulls
it back to structure. Defensible and the closest approach to the guard in the
chapter.

W2 (C6 watch, section 1.3). "added that he had set the price himself" is
character-flavored. It earns its place, because it establishes that the provider
mispriced its own product knowingly, which is a structural point. Recorded so the
line is deliberate.

WHAT HELD. C6 is clean: no provider is characterized as exploitative, no buyer as
careless, and causation is structural throughout. C1 and C2 are strong wherever
the chapter is doing its central work, and the inheritance passage and the steel
analogy are the standard's own reference examples. C4 is strong everywhere except
the summary. The findings above are concentrated in apparatus, transitions, and
the one section nobody reads slowly.

CRAFT READ VERDICT: no criterion fails at chapter level. Five of six carry
specific findings. F4 and F5 are the two worth fixing before Lock, because both
are mechanical to fix, both are now caught by tooling, and both would otherwise
set the wrong baseline for fourteen chapters drafted against this one. F1 and F2
are judgment calls with real cost. F3, F6, F7, W1, W2 are recordable as no
action if Dan rules that way.

INDEPENDENT VERIFICATION STILL OWED. Every word above was written by the same
model that drafted the chapter and wrote the standard it is graded against. Per
the Stage 2 precedent, Dan gut-checks this class of judgment with a second model
before it is accepted. The verification prompt is in the chapter notes.

---

MECHANICAL HALF, PASSED 2026-07-28, against AIOM_ch01.html. Run with
voicecheck.py. Re-run 2026-08-05 against AIOM_Ch01_Stage4_FINAL.html: all four
still clean.

MECHANICAL, all clean on re-run after edits:
- Em dashes: 0.
- Contractions: 0.
- Question marks: 0 in the entire file, so no rhetorical questions arise.
- First or second person in unmarked body prose: 0.
- Hedging: one instance, "often read as" in discussion question 2. It reports
  how the episodes are commonly read rather than softening a claim of the
  book's. Not hedging. No change.

CARRIED ITEM FROM G1, RESOLVED. The contraction reported at line 149 of the
markdown draft inside quoted speech does not exist in the HTML. The CIO reply
runs "I am not asking," "we did not plan," "does not exist" throughout.
Verified against the HTML only. If the markdown draft is still live it may
still carry it, which is a further argument for the deletion Decision 36
already directs.

FOUR JUDGMENT ITEMS RAISED AND RULED. Decisions 42 to 45.

Decision 42. Voiced material. Body prose is third person. First or second
person is permitted only in material marked as voiced, either by a block class
(model, dq, problem) or by enclosing quotation marks. Applied: the flat-rate
objection in 1.3 now takes quotation marks. Quotation marks were preferred over
recasting to third person because the paragraph's stated purpose is to put the
objection at full strength, which third person would drain. Standing rule for
all fifteen chapters.

Decision 43. Reader address. Second person is permitted in discussion questions
and problems. "The reader" holds everywhere else. NO EDIT REQUIRED. On
re-examination the chapter was already consistent: all three discussion
questions and all three problems use imperative address, and questions 1 and 3
additionally use a second-person possessive where they refer to the reader's
own organization. Question 2 needs no such possessive. The inconsistency
reported at the time of the ruling was not real.

Decision 44. Definition restatement. A definition given in a definition aside
is not restated verbatim in body prose; the body names the term instead.
Applied: the consumption-event definition appeared verbatim three times (aside,
body, Key Terms) where access price and software access model each appeared
once with a naming sentence in prose. The body restatement is cut to "That unit
is the consumption event." Now two occurrences, both apparatus, matching the
other two definitions.

Decision 45. Token gloss. "Token" carried substantial load from the opening
case onward and was never explained. A short appositive gloss is added at the
anatomy paragraph in 1.2, where the concept starts doing work, rather than at
the opening case where it is incidental: "the units into which a model divides
the text it reads and writes." Conditional on the preface not assuming the term.
The preface does not yet exist. See chapter notes.

WORD COUNT after edits: 5,362 by HTML text extraction. In band per Decision 33.
Note this counts differently from the 5,669 recorded for markdown draft v2. Both
are in band; the delta is extraction method, not text loss.

CONSEQUENCE. These are prose edits, so Stage 4 and Gate G2 revert to not run.

---

## Stage 5. Design review

Owner: Claude

Status: [ ]        Date cleared: 

> Blocked until D0 closes. Layout, figures, typography, running heads, callout placement, key-term register, against the locked design system.

Findings:

ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

Passed provisionally 2026-07-28. REVERTED to not run on the same date, because
Stage 3 made prose edits in sections 1.2 and 1.3. A design review that passed
against superseded prose has not passed. Re-run after the render.

Re-run 2026-07-31 on the Stage 4 render (AIOM_Ch01_Stage4), per Dan: design
review passed.

REVERTED again 2026-07-31, same day, by the Figure 1.2 reference fix. The two
section 1.2 figures were reordered (anatomy becomes Figure 1.1, seat and event
becomes Figure 1.2) so both are referenced in figure order. That is a figure and
prose edit, so Stage 4 and G2 revert and must re-run against the next render.

Re-run 2026-08-01 on the re-render carrying the figure fix: design review
passes. The two section 1.2 figures now appear and are referenced in order
(anatomy is Figure 1.1, seat and event is Figure 1.2), callouts are intact, and
the mechanical gates confirm the layout under G2 below.

---

## Gate G2. Production gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, run on the rendered PDF.

- [ ] Renders under WeasyPrint without error or warning
- [ ] Zero overflow: all character bounds inside the text block
- [ ] Running heads correct and correctly sided on every page
- [ ] All figures present, numbered, captioned, referenced in text
- [ ] Figure geometry validated by pixel sampling (gap G-B; first-pass visual review 2026-08-01, p6 figures correct and in order; Dan final sign-off)
- [ ] Callout placement correct: no splits, ordering correct after place.py
- [ ] Footnotes on correct pages, numbering sequential and unbroken
- [ ] Key-term register renders with correct rule and tint alternation
- [ ] No widows, no orphans, no section head stranded at a page foot (gap G-D; first-pass visual review 2026-08-01, none seen; Dan final sign-off)
- [ ] Rasterized visual sample reviewed at page level (19 pages rasterized and reviewed 2026-08-01, first pass by Claude)

Findings:

ARCHIVED 2026-08-05, superseded by the reopen at Stage 0. The record below describes a version of the chapter that no longer exists. It is kept because it states what was examined and how it was ruled, which the re-run should not have to rediscover. It is NOT evidence that this step has passed.

Passed provisionally 2026-07-28. REVERTED to not run on the same date, for the
same reason as Stage 4.

DEFECT FOUND AT STAGE 3, to be fixed before G2 re-runs. Figure 1.2 is never
referenced in body prose. The caption is present and correctly numbered, and
the figure renders, but no sentence points the reader at it. Figure 1.1 is
referenced correctly in the closing paragraph of 1.2. The checkbox "All figures
present, numbered, captioned, referenced in text" was marked passed on the
provisional run and should not have been. Fix: add a reference to Figure 1.2,
most naturally in the anatomy paragraph of 1.2 that the figure illustrates.

RESOLVED IN SOURCE 2026-07-31, pending re-render. Rather than only add a
reference, the two section 1.2 figures were reordered so they appear and are
referenced in figure order. The anatomy figure is now Figure 1.1, referenced in
the anatomy paragraph it illustrates; the seat-and-event figure is now Figure
1.2, referenced in the closing paragraph of 1.2. Both figures are now referenced
in body prose, in order. G2 confirms this against the next render.

PASSED 2026-08-01 on the re-render (19 pages). AIOM_build.py ran the full
automated suite and all eleven checks passed: right-margin overflow 0; em and en
dashes 0; heads and folios present and correctly sided; definition callout
splits 0 (place.py not needed); font faces the six expected only; key terms 7
fields and 7 header bands; opening-case provenance present; footnotes 6 called
and all on the calling page; dated evidence boxes 2 labelled and 2 hairline rules
at 2px; problem labels 3 all with their title; theorem panel intact.

One CSS fix was required to reach this pass: the committed v6.7 CSS lacked a rule
to hide the audit source block (Decision 51 apparatus, marked class="audit-only"
by the build), so the raw JSON block rendered as monospace and overflowed. A
rule "#aiom-sources, .audit-only { display: none; }" was added to AIOM_book.css.
The committed CSS predates Decision 51. Ruled 2026-08-01: the committed CSS
(v6.7 plus this audit-only rule) is the working version of record; no external
CSS reconciliation is pending.

The three items outside the automated suite were given a first-pass visual review
2026-08-01 against the 19 rasterized pages: figure geometry is correct (the two
section 1.2 figures render cleanly and in order on page 6), and no widows,
orphans, or stranded heads were seen. Final visual sign-off remains Dan's. The
chapter is 19 pages, up from the prior 18; the added figure reference and the
page footnotes shifted pagination.

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

## Gate G3. Continuity gate

Owner: Claude

Status: [ ]        Date cleared: 

> Mechanical, against the running continuity ledger. Catches chapter to chapter drift here rather than at manuscript integration, where the fix would mean reopening a locked chapter.

- [ ] No term redefined that an earlier chapter already owns
- [ ] Every forward reference assigned to this chapter is paid
- [ ] Every forward reference this chapter makes is logged
- [ ] Northmoor figures diffed against generator output
- [ ] Registry IDs logged; recurring glosses worded identically
- [ ] Maturity ladder language consistent with the locked five-stage model
- [ ] Founding Question references match the canonical table exactly
- [ ] Ledger updated on lock

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

~~OPEN, UNRULED. G1's marker and G1's findings contradict each other.~~
RESOLVED 2026-07-29 by Decision 48. The contradiction was real and the reading
recorded here was correct: G1 was failed on the archiving checks only. Decision
48 repeals those checks, so the contradiction dissolves rather than being
adjudicated. The struck "G1 CLOSED 2026-07-28" line stays struck, because it
was written against a ten-check gate that is not the ten-check gate now in
force. The current closure is dated 2026-07-29 and stands on its own.

~~OPEN. Source count discrepancy.~~ RESOLVED 2026-07-29. The register holds
nine sources after the two second paths added 2026-07-28 under Decision 40's
two-path standard. The "five sources" figure predates the wiring pass and the
"seven" figure predates the second paths. Nine is current. NOTE: Decision 40 is
repealed by Decision 48 as to capture, but its two-path standard is not
disturbed. Confirm that reading at Stage 2.

CARRIED TO STAGE 2. The QJE paper reports 5,172 agents and a 15 percent
productivity gain in the published version, against 5,179 and 14 percent in the
NBER working paper. The book cites the published figures consistently. Matters
most at Ch6, where the study is the anchor case.

~~CARRIED TO STAGE 1 (Dan). Spec 1.3 calls for the OpenAI Pro and Anthropic
episodes as dated case boxes.~~ RESOLVED 2026-07-29 by Decision 49. The premise
was also partly wrong as recorded: the episodes are not inline prose. They are
already dated blocks with a date label and cite wiring.

CARRIED TO THE PREFACE. Decision 45 added a token gloss in 1.2 on the condition
that the preface does not already assume the term. The preface does not yet
exist. When the reader-assumptions subsection is written, check for redundancy
against this gloss.

CARRIED TO STAGE 5. Page range in the Brynjolfsson, Li, and Raymond entry is
set with a hyphen (889-942). Chicago 17 takes an en dash. Copy-edit item, not a
voice item.

FOR CH2. Chapter 1 closes by promising that Chapter 2 takes the atomic unit
defined here and asks what becomes visible when many events are seen together.
Chapter 2 also owes LEM-005 per Decision 27, production is operated rather than
merely accessed. The summary's stated handoff is "seeing the deployment as flows
rather than events."

DECISION 47 (2026-07-29). Sourcing is chapter-local. Each chapter carries its
own source list, resolved and closed when the chapter locks rather than deferred
to a pre-print pass. The book-wide primary-source chase list in Consolidated
Spec Part H is struck. Rationale: chapters are drafted weeks apart, and a
deferred book-wide list cannot survive that cadence. The register remains the
single store; chapter-local means the work closes per chapter, not that each
chapter keeps a separate register.

DECISION 48 (2026-07-29). No capture. A source is sufficiently sourced when it
is cited to a primary, verified live on the accessed date, and cleared by two
independent fact checks against that source. Wayback capture and the local dark
archive are repealed.

  REPEALS: Decision 39, Decision 40 as to capture and local archiving, and
  Decision 40a in full. Decision 40's two-path standard survives; confirm.
  AMENDS: Gate G1 from fourteen checks to ten.
  AMENDS: the internal A/B/C source grading is retired. One operative rule
  survives, that an aggregator or vendor page is never cited, only the primary
  it points to.
  CODE CONSEQUENCE: `sources.py check` currently blocks on three fields,
  Wayback link, local copy, and access date. It must block on access date only.
  Until that change lands, `check` will report false blocks. On the fix list.

  KNOWN COST, ACCEPTED. Accessed dates now carry the whole durability burden.
  A reader in 2040 holding a citation to a Cursor blog post or a GitHub docs
  page already marked legacy will find a dead link. Normal for academic books
  and no reviewer will fault it. Record it plainly in the method note: web
  sources were verified live at drafting and were not archived.

DECISION NUMBERING WARNING. 47 and 48 were assigned against a log whose highest
seen entry is 46. If any session landed a decision above 46, renumber before
this file is treated as authoritative.

CARRIED TO STAGE 2, STATUS UNKNOWN. Nadella said "over 4.7 million"; the
chapter reportedly says "reported at 4.7 million", which understates. A fix was
applied 2026-07-29 but only to a markdown fork, not to AIOM_ch01.html. Treat as
UNFIXED until verified against the HTML.

FORK WARNING, 2026-07-29. A markdown draft v2, a standalone Ch1 source list,
and a markdown source ledger were generated this date from stale project
knowledge. All three are divergent second copies of AIOM_ch01.html and
AIOM_sources.json. Discard them.

RESOLVED 2026-07-29. The three uncertain items were checked against the live
HTML. All three are real and all three survive in the chapter. See the Stage 2
carried items below.

DECISION 49 (2026-07-29). The dated block stands; the spec is amended. Chapter 1
keeps the OpenAI Pro and Anthropic episodes as `div.dated` blocks with a date
label and cite wiring. They are not promoted to case boxes.

  REASONING. The case box's defining feature is its evidence-taxonomy tag, and
  the taxonomy is introduced in Ch6. An untagged box in Ch1 imitates the device
  without being it; a tagged box forward-references vocabulary the reader meets
  five chapters later. The two blocks are also not cases: they run forty-five
  and forty-seven words against the spec's two-to-three-page definition, and
  Ch1 already has its case in the Cursor and Copilot pairing, which Decision 1
  built to be the chapter's evidentiary center of gravity. A third case-like
  object would dilute it. Importing the device early would additionally oblige
  Ch2 through Ch5 to use it, or leave Ch1 an orphan.

  SPEC AMENDMENT REQUIRED. Consolidated Spec Part D.1, Chapter 1, section 1.3
  reads "Evidence in dated case boxes." Amend to "Evidence in dated blocks."
  The collision between that wording and Ch6's tagged case box is what sent
  this item to Stage 1 in the first place; leaving it will re-fire at every
  future read of Part D.1 against a draft. Amend once, in Drive, and resync.

  SCOPE. Ch1 only as to placement. The naming fix is book-wide vocabulary.

CARRIED TO STAGE 2, THREE ITEMS, all verified present in AIOM_ch01.html on
2026-07-29:

1. "Two quiet steps." The chapter describes GitHub's second act as quiet. It
   was announced on 2026-04-27 by GitHub's Chief Product Officer on the company
   blog, six weeks before it took effect, with a preview-bill tool shipped in
   advance. The apology-versus-no-apology contrast the sentence wants survives
   without the word. Note that "quietly" is used accurately elsewhere, in the
   cite note on the Anthropic block, where the July 17 tightening genuinely
   carried no announcement.

2. "Reported at 4.7 million." Nadella said "over 4.7 million." The chapter
   understates. Previously carried, still unfixed, now confirmed against the
   HTML rather than a fork.

3. Anthropic sequence in the second dated block. The block reads that Anthropic
   "introduced usage limits ... and then announced weekly caps." The five-hour
   rolling limits predate July; 17 July was a tightening of limits already in
   force, not an introduction. The cite note on the same block states the
   sequence correctly, so the block contradicts its own footnote.

AVAILABLE, NOT A DEFECT. The GitHub announcement states in the provider's own
voice that under the retiring model a brief chat question and a multi-hour
autonomous session could cost the user the same, and that the arrangement was
no longer sustainable. The chapter does not use it. This is a provider stating
the chapter's thesis in the first person, which is stronger evidence than the
book's own restatement of it. Content decision, not a correction. Raise at
Stage 2 or leave to Stage 5.

DECISION 50 (2026-07-29). Version control. AIOM_ch01.html is the single source
of truth for Chapter 1, and the same rule holds for every chapter.

  1. HTML IS AUTHORITATIVE. Markdown drafts are scaffolding. Once a chapter
     reaches HTML with cite wiring, every prior markdown is dead and is
     deleted, not archived. Decision 36 already said this and was not
     enforced; it is now a gate condition.
  2. NO VERSION NUMBER IS REUSED ACROSS FORMATS. The HTML carries the version
     and the PDF inherits it: AIOM_ch01_v19.html renders AIOM_Ch1_v19.pdf. If
     those two numbers disagree, stop and reconcile before any stage runs.
  3. CLAUDE DOES NOT WRITE CHAPTER PROSE TO MARKDOWN. Proposed prose goes in
     chat or as a patch against the HTML, never as a file that could be
     mistaken for a draft.
  4. FINGERPRINT BY HASH, NOT WORD COUNT. This chapter reads as 5,116, 5,362,
     or 5,437 words depending on extraction method. Three numbers, one
     chapter. Record the SHA-256 prefix when citing a version.

  ESTABLISHED 2026-07-29 BY HASH. Three distinct artifacts existed, not two
  competing versions of the prose:
    b6815af1de07  draft_v1.md            4,557w  dead ancestor
    4460505bc580  "draft_v2".md          4,736w  CLAUDE FORK, delete on sight
    335af891e698  AIOM_ch01.html         5,116w  LIVE
  The three markdown uploads were byte-identical to each other and to the fork
  generated 2026-07-29 from draft_v1. The two HTML uploads were byte-identical.
  Body prose in the PDF matches the HTML; the apparent sentence-level diff is
  hyphenation and running heads.

  ROOT CAUSE: filename collision. A legitimate AIOM_Ch1_draft_v2.md (5,216w,
  the 1.4 expansion) existed and was superseded into the HTML. Claude then
  generated a different file from draft_v1 and gave it the same version number.
  One version number, two lineages. That file is what reached the fact
  checkers, which voided a large share of their findings.

PDF v18 IS STALE. Superseded 2026-07-29. Its bibliography carries seven entries
and no TechCrunch; the HTML register carries nine sources with two-path
citations on altman-2025-pro and anthropic-2025-limits. v18 therefore predates
the source pass of 2026-07-28. Consequences:
  - Any design or production review conducted against v18 is void. Stage 4 and
    G2 were already reverted to not run, so no gate is affected.
  - A re-render is required before Stage 4 and G2 can run. Next render is v19.
  - The v18 footnotes also lack the second paths, so footnote numbering and
    content will change at re-render.

---

## Stage 4 craft read: independent verification prompt

Added 2026-08-05. The Stage 4 craft read was written by the same model that
drafted this chapter and wrote the standard it grades against. Dan runs this
prompt on a different model, per the Stage 2 precedent, and rules on the result.
Give the second model the chapter HTML and AIOM_Voice_and_Craft_v1.md, and
nothing else. Do NOT give it the findings above: the point is an independent
read, and showing it the answer key destroys that.

> You are reviewing one chapter of an academic textbook against a written craft
> standard. Both are attached. The standard lists six criteria, C1 through C6.
>
> Two warnings about this task. First, the standard was written partly by
> generalizing from this chapter's own prose, so it is calibrated to flatter the
> chapter. Correct for that: judge against the named exemplars the standard cites
> (Michael Lewis, James Lardner, the Financial Times, The New Yorker), not
> against how closely the chapter resembles itself. Second, the previous review
> of this chapter returned "meets all six criteria, no findings," and that
> verdict was withdrawn as confirmatory.
>
> For each criterion, do not report whether the chapter meets it. Instead:
>
> 1. Quote the WEAKEST passage in the chapter against that criterion, by
>    section, and say precisely what is wrong with it.
> 2. Quote the STRONGEST passage, so your calibration is visible.
> 3. State whether the weakest passage is a defect worth fixing, a deliberate
>    choice serving something else, or noise.
>
> Then answer three questions directly. Which single change would most improve
> the chapter's prose? Which criterion, if any, does the chapter fail outright at
> chapter level? And is there any defect the six criteria do not cover, which a
> serious reader would notice?
>
> Assume the chapter is good. Your job is not to praise it. Your job is to find
> what a hostile reviewer at a university press would find.

Compare the second model's findings against F1 through F7 and W1 and W2 in Stage
4 above. Agreement on a finding raises confidence. A finding the second model
raises that Stage 4 missed is the more valuable output, and it goes in as F8
onward. Disagreement is Dan's to rule.

---

## Carried into the re-draft (reopen of 2026-08-05)

Reset to not-run does not mean these were not learned. The re-draft inherits:

**CD1. Production defect, found by gate 14 on its first run.** The "Craft
section" slot label sits alone at the foot of page 12, with the section it
labels opening on page 13. This render PASSED the eleven-gate suite on
2026-08-01. It FAILS the fourteen-gate suite. Fix at Stage 5 design, not at
Stage 0: it is a break-control problem in the CSS or a place.py concern, not a
prose problem. Recorded here so it is not rediscovered.

**CD2. The seven craft findings and two watch items** from the Stage 4 craft
read, archived above. F4 (four paragraphs closing on a cross-reference) and F5
(the summary at twice the chapter mean sentence length, zero short sentences)
are prose defects the re-draft should not reproduce. F1 (the unanchored FinOps,
observability, and chargeback passage) and F2 (a craft artifact containing no
arithmetic) are the two substantive opportunities.

**CD3. Nine verified sources** in `AIOM_Source_Ledger.md`, cleared at the
original Stage 3. The re-draft should reuse them rather than re-verify, subject
to Dan's Stage 3 re-run. The sequence note on S-002 still applies: the
unannounced July 17 2025 tightening is a separate and earlier event from the
July 28 announcement, which carried thirty days notice.

**CD4. Rulings that survive the reopen.** Decisions 42 to 45 (voiced material,
reader address, definition restatement, the token gloss), the Stage 2
developmental rulings D1 through D6, Decision 33 (5,000 to 6,000 words for Ch1
and Ch2), Decision 50 (the chapter HTML is the single live text), and Decision
51 (the audit source block). A reopen resets steps, not rules.

**CD6. One definition callout splits across a page break**, caused by applying
ND1 at Stage 2. Remedy: run `place.py`. Not a CSS problem; WeasyPrint 69 ignores
`break-inside` on floated elements. Stage 5.

**CD7. A widow and an orphan on page 16.** Pre-existing, and verified as such by
running the corrected gate 14 against the pre-ND1 render. It was invisible until
the mirrored-margin bug in gates 12 and 14 was fixed. Stage 5.

**CD5. What the re-draft must do differently.** The craft standard binds from
Stage 0 this time. Read `AIOM_Voice_and_Craft_v1.md` before drafting, tick the
Stage 0 acknowledgment box on the strength of having done so, and expect Stage 4
to be read adversarially and by section against C1 through C6.
