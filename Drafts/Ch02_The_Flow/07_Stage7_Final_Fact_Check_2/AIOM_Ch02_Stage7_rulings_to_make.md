# Chapter 2, Stage 7. What Dan has to rule.

Written 2026-08-30 from external check A. **Claude rules none of it.** Each item gives
the finding, what Claude verified independently against the chapter and the ledger, and
a recommendation with its reasoning. Nothing below is applied.

**READ R1 FIRST.** It is the only item where the check contradicts Dan's own Stage 3
verification, and it decides the shape of the opening case.

---

## R1. The cost range. THE CHECK CONTRADICTS DAN'S OWN STAGE 3 ROW A4.

**The chapter says:** "Reported monthly spending ranged from several hundred to several
thousand dollars, depending on how often each engineer used Claude Code and the
complexity of the work."

**The check says** Forbes gives an average of "$150 to $250" and power-user spending of
"$500 and $2,000", so neither endpoint is supported: the floor is below several hundred
and the ceiling is $2,000.

**What the register note records:** rows A1 to A6 were VERIFIED BY DAN on 2026-08-29 and
all passed, and A4 is the per-engineer monthly cost range. The note also records the
reason the wording is loose: "The chapter states the cost range as 'several hundred to a
few thousand dollars' rather than as exact bounds, deliberately, so that a corrected
figure does not invalidate the sentence."

**Claude's independent reading, and it is not a tie-break in either direction.** The two
verdicts are answering different questions. Dan verified that the reporting says what the
chapter says it says, at the chapter's deliberately loose grain. The check compared the
loose bounds against the article's actual numbers and found the loose bounds do not
bracket them. **Both can be right at once, and the sentence is still wrong**: $150 to
$250 is not "several hundred", and $2,000 is not "several thousand". **The pre-copy-edit
wording, "a few thousand", had the same floor problem**, so this is not damage the copy
edit did. It is an error the looseness concealed from a checker who had never read the
article, which is now the first time anyone has.

**THE RATIONALE FOR LOOSENESS HAS EXPIRED.** It was written to survive a corrected
figure by a checker who could not read the source. The source has now been read.

**Recommendation: take the exact figures.** The fifty-year rule quarantines perishable
specifics in dated cases and this sentence is in the dated opening case, so exact figures
are permitted here and are stronger. Proposed: "Reported monthly spending averaged $150
to $250 per engineer, while the heaviest users spent between $500 and $2,000." That
also improves the teaching, because the gap between the average and the heavy user IS the
chapter's subject.

**A second half to this item.** The check notes Forbes does not attribute the range to
"the complexity of the work". **That clause predates the copy edit** in the form "how
hard the work was" and was covered by row A5, "the attribution of the variation to
workload", which Dan passed. Workload is not the same as complexity. Either A5 supports
the workload half only, in which case the complexity half should go, or the article
carries both. **Dan is the only person who has seen the article and the sheet together.**

---

## R2. "An independent evaluation" is contradicted, AND IT IS A W14 RULED SENTENCE.

**The chapter says:** "The Digital Transformation Agency commissioned an independent
evaluation and published it in full."

**The check says** Appendix B states the evaluation was "jointly delivered by the DTA and
Nous". DTA designed the plan and a government steering committee endorsed the reports.
That is an externally assisted joint evaluation, not an independent one.

**THIS IS NOT AN ORDINARY CORRECTION.** The sentence is FQ5's REQUIRED text in
`AIOM_Claim_Ledger.md`, restated at Stage 6 on Dan's ruling. Changing it means amending
the ledger, and W14 will fail the build until that is done. **The register note also
anticipated exactly this**: it told Stage 3 to "record whether the evaluation is
attributed to Nous Group on its face, since secondary coverage names that firm as the
evaluator." The check answers that question yes.

**Recommendation: correct it and amend FQ5.** The teaching point of FQ5 was never the
word "independent": the ruling withdrew "which is more than most buyers do" and kept the
point that this buyer produced a public record. That survives. Proposed: "The Digital
Transformation Agency commissioned the evaluation, delivered it jointly with an external
firm, and published the full report." **A jointly delivered evaluation is arguably the
better teaching object**, because it raises the record-quality question the chapter is
about rather than settling it with a word.

---

## R3. "The evaluation identified two limits" is contradicted.

**The chapter says:** "The evaluation identified two limits in its method: participants
assessed the effects themselves, which could understate or overstate them, and no measure
of the work existed from before the trial."

**The check says** Appendix B labels FIVE limitations: representativeness, positive
selection bias, inconsistent rollout, evaluation fatigue, and self-assessment. The
self-assessment limit is explicit and verified. **The absence of a pre-trial work
baseline is NOT one of the report's stated limitations.** The report ran a pre-use survey,
but it baselined sentiment and confidence rather than task time or output.

**Claude's reading: the first half is verified and the second half is the chapter's own
inference presented as the report's statement.** That is the FC9 shape from Chapter 1,
where an inference was attributed to a source, and it is the shape the register note
warned about when it flagged A2 and A5.

**Recommendation: split the sentence so the report's finding and the chapter's inference
are visibly different things.** Proposed: "The evaluation named five limits in its
method, one of which is that participants assessed the effects themselves, which could
understate or overstate them. Its published methodology reports no objective measure of
task time or output from before the trial." **This is better teaching than the current
sentence**, because the chapter's whole subject is the difference between what a record
states and what someone infers from it, and the corrected form performs that distinction
instead of describing it.

---

## R4. "Tools" in the plural is unsupported. Straightforward.

**The chapter says:** "by using the tools it had given them." The check cannot confirm a
second tool drove the overrun; the sources name Claude Code.

**This one the copy edit did introduce.** It is item 4 of the eight in the cover note,
and it is exactly what that list was for.

**Recommendation: revert to the singular.** No ledger consequence, no teaching change.

---

## R5. "No measure of the work existed from before the trial." Narrow it.

Covered by R3's proposed wording, and listed separately because the check ranks it as its
own CANNOT CONFIRM. The defensible claim is about what the published methodology reports,
not about what did or did not exist anywhere in the agencies. **The stronger claim was
never checkable and the narrower one is exactly as useful pedagogically.**

---

## R6. THE BIGGEST ITEM IS NOT A CORRECTION. A RULING'S REVERSAL CONDITION IS NOW MET.

**The check raised footnotes 3 and 4 as unsourced, at findings 7, 22 and 23**, without
knowing they were ruled that way on purpose. **It did not improperly reopen anything.
It supplied the exact thing the ruling was waiting for.**

S3-2's REVERSES-IF reads: "a single named source for the adoption figures, ideally the
primary, which is exactly what the register entry's `upgrade` field asks for. With one,
both footnotes get a real citation and both of these rulings retire together."

**The check read Forbes and reports 32 per cent adoption in February rising to 84 per
cent in March.** Forbes is named, dated, read, and ALREADY IN THE REGISTER as
`uber-2026-budget`. The condition is met on its face.

**What this unlocks, and it is the best outcome available from this check:**

- `uber-2026-adoption`, whose container is the placeholder "Multiple secondary outlets",
  can be retired and its two footnotes repointed at Forbes.
- **The percentages Dan withdrew on 2026-08-21 can come back as figures.** The chapter
  currently says "about a third" and "a large majority" only because no source could be
  named. One can now.
- **S3-1 and S3-2 retire together**, as their own entries say they would.

**Recommendation: take the upgrade, and restore the figures.** The withdrawal was never a
judgment that percentages were the wrong form; it was standing rule 2 refusing an
invented citation. **The rule has been satisfied rather than bent.**

**One caution that is Dan's to weigh.** Forbes is still secondary, and the register's
`upgrade` for it remains The Information's paywalled original. Restoring the figures
raises what the chapter asserts on a secondary source. The counter is that the figures
are now attributable to a named, dated, readable document, which is the standard standing
rule 2 sets, and the chapter says nothing about how they were derived.

---

## R7. Citation metadata. Four fixes, none of them touching prose.

| # | What | Now | Should be |
|---|---|---|---|
| a | MIT report authors | none | Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari |
| b | MIT report date | 2025-08 | **2025-07.** August was the news cycle, not the document |
| c | Forbes byline | "MSV Janakiram" | "Janakiram MSV", the published form |
| d | DTA attribution | DTA alone | DTA and Nous Group, jointly |

**The dated evidence box reads "Dated: August 2025" and changes with item b**, or does
not, depending on what that box dates. If it dates the report, it becomes July 2025. If
it dates the chapter's knowledge of the episode, it stands. **Gate 9 checks the box is
present and ruled, not that its date is right**, so nothing mechanical will catch this
either way.

**Two locations should be added and one should be refused.** The DTA full report has a
real institutional URL at digital.gov.au and should take it. Microsoft's January 2024
pricing announcement should be added as a second key supporting the per-seat claim, which
the DTA evaluation alone does not establish. **The MIT location the check gives is a
third-party mirror on a consulting firm's website, not MIT and not NANDA.** Claude's
recommendation is to refuse it: a vendor mirror can vanish and confers no authority, and
the entry is better carrying its existing "location not obtained" than a citation that
looks solid and is not. That is Dan's call and it is the one place Claude would decline
something the check offered.

---

## R8. Offered, not required. Dan's taste.

- **"Nominated or approved"** rather than "nominated", since participants could also
  self-nominate. Small accuracy gain, no teaching change.
- **The MIT sentence could name the 5 per cent** that did extract value. The check calls
  the current form "acceptable as a headline paraphrase but less exact".
- **"A large share of committed code had passed through it"** could become the
  first-party 25 per cent of commits. The check notes "passed through" has no stable
  technical definition. **This interacts with R6**: if S3-2 retires, quantifying becomes
  available here too.
- **"AI budget" versus "AI coding-tools budget."** Forbes and Macdonald use the broad
  term, Fortune the narrow one. The chapter follows Forbes and is supported.

---

## What this does to P3, and to the lifecycle

**P3 needs its premises rewritten. It does not need rebuilding, and Claude's own README
said it might.** That contingency was written before anyone knew WHICH way the source
would break. Of the four premises the register note calls load bearing, two hold
outright (per-seat pricing, agency nomination), and two are wrong in the same direction:
they overstate the report's independence and overstate what it stated about itself.
**Both repairs make the problem harder and more honest**, and the exercise it sets,
determining what the evaluation made knowable and what it could not establish, is
unchanged. **Dan rules whether that counts as rebuilding.**

**No step needs reopening.** Stage 7 is where these findings belong and it is in
progress. Stage 5, G2 and G3 are open and run after. W14 re-runs mechanically and will
fail until FQ5 is amended, which is the gate working.

**The open question from the copy edit is unchanged and these corrections fold into it**:
whether the judgment halves of Stages 2 and 4 are re-run on prose that has moved.

---

## What has NOT happened yet

**Check B has not been run.** The pair is the method: Chapter 1's two checks agreed on
one finding out of six and the disagreement was the value. **A is a strong check and it
is still one check**, and it read the sources rather than the chapter, which is precisely
the half B is designed to cover.

**A was not given the packet**, which it flags itself. It could not check its findings
against the twelve rulings in force. Claude ran that comparison and it produced R6, the
most valuable item here. **Send B the render only, as designed, and send A's successor
the packet if A is re-run.**
