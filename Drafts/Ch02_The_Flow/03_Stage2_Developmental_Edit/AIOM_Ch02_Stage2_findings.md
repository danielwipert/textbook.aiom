# Chapter 2 Stage 2, developmental edit: Claude's pass

Date: 2026-08-24. Chapter at 3 of 13, Stage 1 closed 2026-08-24.
Live text: `Drafts/Ch02_The_Flow/00_Stage0_Draft/AIOM_Ch02_draft.html`, 7,257 words.

**What this pass is.** Teaching quality: clarity, pacing, cognitive load, example
fitness, transitions, and whether the argument carries the target reader without a
stall. It is not fact checking, which is Stage 3, and not voice, which is Stage 4.
**Claude rules none of these. Dan gut-checks with a second model and rules.**

**What this pass is not allowed to reopen.** Stage 1 ruled that section 2.3 is kept
and that its review cadence moves to Chapter 10. DE9 below concerns that section's
POSITION and does not reopen the decision to keep it.

**NOTHING IS APPLIED.** Nine findings, none acted on. The re-run matrix makes a body
prose change re-run Stages 2, 3, 4, 5 and G2, so applying before ruling would spend
those steps on text that may not survive the ruling.

**A NOTE ON WHO IS GRADING WHOM.** Claude drafted this chapter and is now reviewing
it, which is the self-marking problem Decision 73 names for Stage 1 and which applies
here with equal force. The correctives used are the same two available at Stage 4:
every finding below is anchored to a MEASUREMENT or a QUOTED PAIR rather than to a
judgment about quality, so a reader can check the finding without trusting the
reviewer. Where a finding rests only on reading, it says so.

---

## DE1 (HIGH). Figure 2.1 arrives 575 words after the sentence that introduces it

**Measured, not impression.** Section 2.2 says "Figure 2.1 sets the three side by
side" in its fourth paragraph. The figure itself sits at the END of the section, 575
words and ten paragraphs later. Figure 2.2, by contrast, sits 11 words after its
introducing sentence.

**Why it is a teaching defect rather than a layout preference.** Figure 2.1 is the
one artifact that makes the chapter's central construct holdable in one view, and it
is placed after the reader has been asked to carry the three flows unaided through
their ownership division, three health tests, three physical locations and three
review speeds. **The figure that would reduce the load arrives after the load has
been imposed.** The 11-word figure in 2.6 shows the chapter already knows the right
distance.

**No gate can see this.** Print gate 12 checks that a figure is captioned, numbered,
ordered and referenced in the text. It has no opinion about how far the reference
sits from the figure, and both figures pass it identically.

**Candidate remedies, not ruled.** (a) Move Figure 2.1 to immediately after the
paragraph that introduces it, which puts it after the three flows are named and
before the material that elaborates them. (b) Leave the figure and move the
introducing sentence down to it. **(a) and (b) are not equivalent**: (a) changes what
the reader has in hand while reading ten paragraphs, and (b) only fixes the
cross-reference.

## DE2 (HIGH). The craft section and problem P1 run the same mapping on the same case and reach the same three diagnoses, in places near-verbatim

**The quoted pair.** Craft section: "The record flow is partly managed. A
per-engineer cost range was reported, so consumption was visible at some grain, and
the reporting does not establish that it was attributed to teams or compared against
the plan." Problem P1: "The record flow is also partly managed. A per-engineer
monthly cost range was reported, so consumption was visible at some grain. What the
given facts do not establish is whether that record was attributed to teams or
compared against the plan."

All three diagnoses match: usage partly managed, record partly managed, cost-and-value
complete on cost and unbuilt on value.

**Why it costs the chapter something.** P1 is the WORKED problem, which is the
chapter's one demonstration of the diagnostic performed end to end for a reader who
has not yet tried it. Spending it on the case the craft section has just finished
mapping means the worked example teaches nothing the reader has not read four pages
earlier, and it spends the pedagogically most valuable problem slot on a repeat.
**The craft section already carries a second mapping, the constructed retailer, so
the chapter demonstrates the diagnostic twice and then demonstrates it a third time.**

**Candidate remedies, not ruled.** (a) Repoint P1 at a different deployment, which
costs a source and reopens the Grade C sourcing question. (b) Cut the Uber mapping
from the craft section and let P1 carry it, which loses the craft section's most
concrete moment. (c) Keep both and change P1's task, for example asking the reader to
work from the craft section's diagnosis to what a February review would have needed,
which reuses the opening case's own unanswered question. **(c) is the only one that
costs no source and loses no material**, and Claude does not rule it.

## DE3 (HIGH). "Cost-value asymmetry" is named in 2.4, defined at the end of 2.5, and titles 2.6

The mechanism is built in 2.4: "An unmanaged cost-and-value flow accrues on one side
only, and this is the asymmetry the chapter turns on." The definition callout sits at
the end of 2.5, which is about why the record flow is skipped and does not use the
term. Section 2.6 is titled after the consequence and opens by naming it.

**The definition sits in the one section least about it.** CLAUDE.md's rule is that a
coined term arrives after the mechanism it names, and 2.4 is where that mechanism is
built, so the callout is a section late and lands in unrelated material. A reader who
reaches back for the definition while reading 2.6 will look in 2.6 and in 2.4 before
finding it in 2.5.

**Candidate remedies, not ruled.** (a) Move the callout to the end of 2.4, directly
after the paragraph that builds the mechanism. (b) Move it to the head of 2.6, where
it is used. **This interacts with placement**: the callout floats, so `place.py` must
re-run and gate 4 re-checked whichever is chosen, and Gap G-I means the affected pages
need reading rather than only gating.

## DE4 (MEDIUM). Section 2.2 carries six distinct teaching jobs in 846 words

Measured: 846 words across 14 paragraphs, the longest teaching section in the chapter.
The jobs are (1) the three flows named, (2) each described, (3) the four-owner division,
(4) a health test for each of the three, (5) the record flow's three physical locations,
and (6) the three flows' three different speeds and the review cadence that follows.

**Jobs 5 and 6 are not about the taxonomy.** The section's title is "Three flows, not
one", and its argument is complete once the three are named, described and shown to be
separable by ownership. The locations and the speeds are consequences a reader can only
use once the taxonomy has settled.

**Candidate remedies, not ruled.** (a) Split 2.2 after the four-owner paragraph, giving
the health tests, locations and cadences their own section. **This is a structural
change and re-runs G1.** (b) Move the three locations to 2.5, which is already about the
record flow, and the three speeds to 2.3, which is already about mismatched timescales.
(c) Leave it and rely on DE1's figure move to carry the load. Claude notes that (b) is
the cheapest and (a) the cleanest, and rules neither.

## DE5 (MEDIUM). The record-decay claim and its illustration are separated by two paragraphs

Section 2.4 makes the decay claim ("An unmanaged record flow does not merely stay
empty. It decays") and then gives its concrete illustration, the engineer and the
migration and the forty calls, three paragraphs later. Between them sit the
cost-and-value asymmetry paragraph, which is the chapter's turn, and the coupling
paragraph about the three tracks being separated for diagnosis.

**Both halves lose.** The claim waits for its evidence, and the chapter's turn is
interrupted by a return to a subject the reader has moved past. The illustration is the
strongest concrete particular in the teaching body and it lands after the section's
climax rather than before it.

**Candidate remedy, not ruled.** Move the illustration up to sit directly after the
decay claim, leaving the asymmetry paragraph and the coupling paragraph adjacent and
ending the section on the asymmetry, which is what 2.5 and 2.6 both build on.

## DE6 (MEDIUM). Discussion question 2 asks for an example the chapter has already worked in full

DQ2: "Give a concrete example of information about AI usage that is available on the
day the work happens and unavailable six months later, and explain what makes it
perishable." Section 2.4 supplies exactly that, in the same frame: available on the day,
aggregated a month later, an invoice a quarter later.

A reader who has read the chapter can answer by reproducing the passage. The question
tests recall while appearing to test transfer.

**Candidate remedies, not ruled.** (a) Ask for an example from the reader's own
organization, which makes the chapter's example a model rather than an answer. (b) Ask
what would have had to be built ON THE DAY for the example to survive, which is the
step the chapter states as a decision rather than a habit and does not work through.

## DE7 (MEDIUM). Six three-part structures, and a reader has no cue about which triad is in play

Counted: the three flows; the record flow's three locations; the three flows' three
speeds; the three reasons the record flow is skipped; the apparatus's three parts,
record, attribution and constraint; and the three diagnoses, managed, partly managed
and unmanaged. THM-004 then has four antecedents and 2.8 has four limits.

**This rests on reading rather than on a measurement, and it is the finding Claude is
least confident in**, because a taxonomy chapter has a legitimate reason to keep
returning to threes and because each triad is individually well built. What can be
stated is that the apparatus's three parts in 2.7 are the triad most easily confused
with the three flows, since both are three things a deployment either has or lacks,
and 2.7 does not say which of the three flows each part belongs to. It belongs to the
record flow, and the chapter never says so.

**Candidate remedy, not ruled.** One sentence in 2.7 tying record, attribution and
constraint back to the record flow, which is where DE4's remedy (b) would also point.

## DE8 (LOW). The opening case spends five paragraphs on derivation before its payoff

The case runs 826 words. Its payoff, the two things worth separating (the company could
see what it spent, and could not say what it received), arrives in the tenth of twelve
paragraphs. Before it sit the seat-forecast method, the property that made the method
survive, the consumption that did not hold flat, the shape of the surprise, and what a
February review would have required.

**The material is good and some of it is teaching-body work sitting in the case slot.**
The seat-forecast paragraphs in particular derive a mechanism rather than report the
episode. **Claude notes the tension and does not rule it**, because the fixed six-slot
skeleton permits variation in form within the opening-case slot, and because the case
was ruled in by Dan.

**A second observation, recorded and not raised as a defect.** The case carries seven
attributions of uncertainty ("press reporting indicates", "the public account does not
describe", "does not establish", "the reporting does not settle"). Every one is
required by the register's UNVERIFIED status and none is hedging under the prose
standard's section 13 distinction. The developmental question is whether their density
lets the reader feel the episode. **This resolves itself if Stage 3 verifies the
sources**, so it may be cheaper to leave until then than to rewrite twice.

## DE9 (LOW). Section 2.3's position interrupts the flow-condition argument

**This does not reopen Stage 1's ruling to keep the section.** Sections 2.2 and 2.4 are
continuous: 2.2 establishes what each flow's healthy condition looks like, and 2.4
establishes what happens to each when unmanaged. Section 2.3 sits between them on a
different subject, the mismatch between project funding and flow spending.

**Candidate remedy, not ruled.** Move 2.3 to sit after 2.4, where its "funded once, runs
daily" argument follows naturally from "an unmanaged flow does not stay still", or after
2.5. **This re-runs G1**, since it reorders material within the teaching body, and the
gain is a smoother argument rather than a defect closed.

---

## What this pass did not find

**The argument carries.** Read end to end, the chapter reaches its claim without a
stall: the reader is given the unit, the three flows, what happens when they are
unmanaged, the asymmetry, the consequence, and the theorem, in an order where each
step uses the one before it.

**The craft section is the chapter's strongest slot.** It states its two failure modes
in advance, runs the diagnostic on a real case that comes back unflattering, runs it
again on a constructed one that comes back clean, and says plainly that the clean one is
constructed and why no real one was available.

**No finding here is a voice finding.** `voicecheck` passes mechanically and the craft
criteria are Stage 4's, which has not run.

## Handed to other steps, not raised here

Five uncited claims about what organizations usually do are Stage 3's and are already
recorded in the Stage 1 findings. Two of them sit in passages DE5 and DE6 touch, so
**whichever step moves first should say so**, or the other will be reading text that
has moved.
