# AIOM Claim Ledger

The machine-readable record of every ruled claim narrowing. `claimcheck.py` reads
this file as data and web gate W14 enforces it. Adopted 2026-08-13.

## Why this file exists

**A ruled claim narrowing does not survive a copy edit, and nothing mechanical
sees it go.** SF8, SF9 and SF10 were reverted during the Stage 6 rounds of
2026-08-08 with every date and figure intact, so no check on values could detect
them. FC2 repeated the shape on a second vendor. The case bank carried the
pre-SF3 wording for seventy days and a privacy sweep found it. That is five
instances of one failure, and it is the only class of damage in this project that
no gate could see.

The register notes already quote the ruled sentences, which is what made all five
recoverable. This file makes that recoverability mechanical.

## Why the check does not read the register notes directly

It was tried first and it does not work, for two reasons found by attempting it.

**The notes use the apostrophe as both quote delimiter and possessive.** A note
containing `the team's heaviest users` inside a quoted sentence cannot be parsed
by any rule that treats `'` as a delimiter, and `most users' costs` defeats the
obvious refinement.

**More seriously, a note holds superseded ruled forms alongside the current
one.** The note on `altman-2025-pro` contains two sentences introduced by "the
sentence now reads": the SF1 form from 2026-08-06 and the later form that
replaced it. Both are correct as history. A checker that treated every "now
reads" as REQUIRED would demand a sentence the chapter is right not to contain.
The notes are a record of how the text got here. This file is a statement of
where it must be now, and those are different documents.

## Format

One block per ruling. `claimcheck.py` parses these fields and ignores prose.

- `REQUIRED:` text that MUST appear in the chapter body. A ruling that replaced
  a sentence records the replacement here.
- `FORBIDDEN:` text that MUST NOT appear. The withdrawn form.
- `REVIEW:` a constraint that is real but has no reliable string form. Never
  enforced mechanically, and stated so a human re-reading knows to check it.
- `REVERSES-IF:` the evidence that would legitimately reopen the ruling.

Matching is on normalized text: markup stripped, entities decoded, typographic
quotes folded to straight, whitespace collapsed. Case-sensitive, because these
are quotations.

**Record the chapter's text, not the note's description of it.** Two notes were
found quoting sentences the chapter does not contain, both drift of exactly the
kind this file exists to catch. Every entry below was verified against the
chapter when it was written.

---

## Ch01

### SF1 :: superlative cut :: 2026-08-06 :: Stage 3
- SOURCE-KEY: altman-2025-pro
- FORBIDDEN: The chief executive of the largest provider
- FORBIDDEN: one of the largest
- REQUIRED: Chief executive Sam Altman said publicly that the company was losing money on its two-hundred-dollar Pro subscriptions
- REVERSES-IF: a source naming the metric on which the firm is the largest provider. Neither cited post establishes it and no metric was named.

### SF10 :: consumption mechanism removed :: 2026-08-10 :: Stage 3
- SOURCE-KEY: altman-2025-pro
- FORBIDDEN: because customers were consuming more computing resources than the monthly price covered
- REQUIRED: because subscribers used them more than the price had assumed
- REVERSES-IF: a passage in either source attributing the loss to compute consumption rather than to usage against an assumed price.

### SF3 :: claim narrowed :: 2026-08-06 :: Stage 3
- SOURCE-KEY: github-2025-premium-requests
- FORBIDDEN: began billing premium requests that had previously carried no separate charge
- REQUIRED: began enforcing monthly premium-request allowances for Copilot and letting customers pay for usage beyond them
- REVERSES-IF: a pre-2025-06-18 GitHub pricing or documentation artifact describing the earlier arrangement in its own words.
- DRIFT-FOUND 2026-08-13: the register note quotes this sentence WITHOUT "for Copilot". The chapter is correct and the note's quotation is stale. Recorded here from the chapter. The note should be corrected at the next reopen; it is not edited now because the chapter is locked and the note is right about the ruling, only imprecise about the wording.

### SF7 :: date anchor restored :: 2026-08-10 :: Stage 3
- SOURCE-KEY: microsoft-2026-q2-call
- FORBIDDEN: In January 2026, four months before that change
- REQUIRED: On January 28, 2026, four months before that change
- REQUIRED: had passed 4.7 million paid subscribers
- REQUIRED: growing 75 percent year over year
- REVERSES-IF: nothing. Read as the month at large the interval runs to five months; it is four only from the 2026-01-28 call.
- SUPERSEDED-FORM 2026-08-13: the note's A2 entry of 2026-07-29 records the chapter as reading "over 4.7 million". SF7 restructured the sentence on 2026-08-10 and it now reads "had passed 4.7 million paid subscribers". The A2 wording was encoded here on the first draft of this ledger and the check failed on it immediately, which is the trap this file's own preamble describes: a note holds superseded forms beside current ones. The chapter is the authority.

### SF2 :: continuation mechanism removed :: 2026-08-06 :: Stage 3
- SOURCE-KEY: truell-2025-pricing
- SUPERSEDED-FORBIDDEN: after which usage continued to bill against real rates
- REVERSES-IF: a passage from the post describing the default billing behaviour on exhaustion.
- SUPERSEDED 2026-08-14: retired by Dan, the final editor, whose edit supersedes. Reason: Dan's wording carries the continuation mechanism; the Stage 3 removal is overturned. The lines above are kept as history and are no longer enforced by W14.

### SF8 :: the SF2 mechanism restored in different words :: 2026-08-10 :: Stage 3
- SOURCE-KEY: truell-2025-pricing
- SUPERSEDED-FORBIDDEN: billed each additional request at API rates
- REVERSES-IF: same as SF2. This entry exists because the mechanism returned once already, in different words, through a copy edit.
- SUPERSEDED 2026-08-14: retired by Dan, the final editor, whose edit supersedes. Reason: Same mechanism as SF2, restated; retired with it. The lines above are kept as history and are no longer enforced by W14.

### SF9 :: depletion scope :: 2026-08-10 :: Stage 3
- SOURCE-KEY: truell-2025-pricing
- REVIEW: the depletion claim is scoped to the labelled composite team's heaviest users and is NEVER a claim about Pro users generally. The post states that the vast majority of Pro users do not exhaust the allowance. There is no reliable string form for a scope, so this is enforced by reading, not by the gate. The CE11 REQUIRED text below carries the scoping and is the closest mechanical proxy.
- REVERSES-IF: a passage scoping exhaustion to Pro users generally, which this post contradicts.

### CE11 :: ruled sentence, current form :: 2026-08-12 :: Stage 6
- SOURCE-KEY: truell-2025-pricing
- SUPERSEDED-REQUIRED: The credit was consumed in a handful of prompts for the team's heaviest users, the people getting the most value.
- SUPERSEDED-REQUIRED: Additional usage was then priced at the same rates
- REVERSES-IF: nothing. This is the SF8 and SF9 ruled content restructured for prose style guide Part 5 rule 3. Only clause order changed; no value, date or claim moved.
- SUPERSEDED 2026-08-14: retired by Dan, the final editor, whose edit supersedes. Reason: Dan's revision restates the passage; the ruled Stage 6 form is replaced by his wording. The lines above are kept as history and are no longer enforced by W14.

### FC9 :: inferred mechanism cut :: 2026-08-13 :: Stage 7
- SOURCE-KEY: truell-2025-pricing
- FORBIDDEN: Cursor had been paying the difference, but the difference had become too expensive to absorb.
- FORBIDDEN: too expensive to absorb
- REVERSES-IF: a passage in the post carrying absorption, paying the difference, or an equivalent economic mechanism. The words appear nowhere in it.

### FC8 :: footnote narrowed :: 2026-08-13 :: Stage 7
- SOURCE-KEY: anthropic-2025-weekly-caps
- FORBIDDEN: had been tightened on July 17, 2025
- REQUIRED: in addition to five-hour limits that were already in force and that subscribers reported
- REVERSES-IF: a source that dates the tightening itself rather than the report of it.

### FC1 :: date antecedent supplied :: 2026-08-13 :: Stage 7
- SOURCE-KEY: anthropic-2025-weekly-caps
- REQUIRED: Those reports were published on July 17, 2025.
- REVERSES-IF: nothing. If the antecedent is ever changed to the tightening itself, the interval must be recomputed, because the encounter and the report are not the same event.

---

### RV87-1A :: Meta's figure stays a projection :: 2026-10-19 :: Review D87
- SOURCE-KEY: meta-2026-memo
- REQUIRED: the company was "tracking to spend billions on internal use alone in 2026."
- REVERSES-IF: the article is corrected, or Meta reports a realized figure for 2026.

### RV87-1A2 :: Tinder's figures credited to the FT :: 2026-10-19 :: Review D87
- SOURCE-KEY: ft-2026-open-models
- REQUIRED: In September 2026, the Financial Times reported that Tinder
- REQUIRED: from an annual rate of $1 million in January to $10 million by July
- REVERSES-IF: the FT dates the interview, or corrects the figures.

### RV87-1B :: Duolingo's margin decline has two causes :: 2026-10-19 :: Review D87
- SOURCE-KEY: duolingo-2024-q4
- REQUIRED: and to lower advertising margins, partly offset by a greater subscription share of revenue
- REVIEW: the box must never make the whole quarterly decline AI-driven.
- REVERSES-IF: the filing is amended.

## Ch02

**All eight are the same ruling applied eight times, made by Dan on 2026-08-29 at
Stage 3.** Each was an unsourced claim about what organizations usually do, carrying
no citation and no derivation. Standing rule 2 allows citation, recasting as a
formal conditional, or cutting, and no fourth option. **None was cited, because none
needed a source**: five were recast onto derivations the chapter already contains
and three were cut without losing teaching.

**THESE ENTRIES EXIST BECAUSE STAGE 6 IS TWO STEPS AWAY.** SF8, SF9 and SF10 were
reverted during Chapter 1's copy edit with every date and figure intact, so nothing
checking values could see it, and FC2 repeated the shape a fourth time. A recast
frequency claim is exactly that shape: the copy edit reaches for the shorter
sentence, and the shorter sentence is the withdrawn one.

**NO ENTRY CARRIES A SOURCE-KEY**, which is the difference between these and every
Ch01 entry above. The ruling is against an ABSENT source rather than in favour of a
present one, so REVERSES-IF names the evidence that would let the claim return.

### FQ1 :: decay frequency cut :: 2026-08-29 :: Stage 3
- FORBIDDEN: because managers routinely underestimate it
- FORBIDDEN: The decay is worth one concrete illustration.
- SUPERSEDED-IN-PART 2026-08-29 at Stage 4, F8: the replacement sentence was itself an announcement of the kind F8 removes, so the whole sentence is cut and the paragraph now opens on "Consider an engineer". **THE RULING IS UNCHANGED IN SUBSTANCE**: the frequency claim stays forbidden, and its replacement is now forbidden too, so neither form can return.
- REVERSES-IF: a study of manager estimation error on record decay. The clause justified including an example rather than carrying argument, so the illustration that follows earns the point unaided.

### FQ2 :: cost governance recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Most organizations that believe they have cost governance have the first, sometimes the second, and rarely the third.
- REQUIRED: These elements are separable. An organization can have a record without attribution, or a record and attribution without a constraint.
- REQUIRED: A dashboard that no one acts on is a record flow with no constraint attached.
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling: the copy edit rewrote both sentences and the substance is unchanged, so the REQUIRED text now records the chapter's current wording. The withdrawn population claim did not return in any form.
- REVERSES-IF: a survey of cost-governance maturity establishing the distribution across the three parts. The teaching point is that the three are separable, which survives the recast; only the population claim was withdrawn.

### FQ3 :: surprise frequency recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Organizations are usually surprised by the second finding rather than the third
- REQUIRED: The missing record surprises where the missing value measure does not.
- FORBIDDEN: often surprises managers
- REVERTED AND REPAIRED 2026-08-30 at Stage 6, on Dan's ruling. **The copy edit brought the withdrawn claim back in different words**, as "The missing record often surprises managers more than the missing value measure does." No FORBIDDEN string could see it, which is the SF2-to-SF8 shape this file exists to catch, arriving on schedule at the step the Ch02 preamble named. The frequency wrapper is cut and the sentence keeps the copy edit's nouns; "often surprises managers" is now FORBIDDEN so the same return cannot be silent a second time.
- SUPERSEDED-IN-PART 2026-08-29 at Stage 4, F11: the mechanism clause after "because" is cut, because it was the THIRD appearance of "the absence of a record is invisible until..." in the chapter and 2.5 already carries it in full. **THE RULING IS UNCHANGED IN SUBSTANCE**: the population claim stays forbidden and the sentence still makes no frequency claim. What it no longer does is restate a mechanism the reader met two sections earlier.
- REVERSES-IF: evidence about what surprises organizations running this diagnostic. The mechanism after "because" was already in the sentence and is unchanged; only the population wrapper went.

### FQ4 :: Chapter 8 forward reference recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: the flow this mapping most often finds missing
- REQUIRED: the record flow that organizations are structurally most likely to skip
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. The anchor word is "structurally", and it survives: the claim still rests on 2.5's derivation rather than on observed frequency, which is the same ground on which Stage 1 cleared the sixth candidate. The pairing recorded in REVERSES-IF is unaffected.
- REVISED at application, 2026-08-29: the drafted recast read "the one section 2.5 shows is structurally the easiest to skip", and the Stage 4 re-read cut the pointer. **The drafted form made C7 worse at the worst possible sentence**, the craft section's opening, which would then have carried three references at once: the rest of the book, Chapter 8, and section 2.5. **The derivation clears the claim whether or not the sentence points at it**, which is exactly how Stage 1 cleared the sixth candidate: that one sits in the chapter summary and names no section.
- REVERSES-IF: nothing, and this entry is the one to read before reopening any of the others. Stage 1 cleared a sixth candidate, "the record flow is skipped most often, and for structural reasons rather than careless ones", on the ground that section 2.5 derives it. This recast anchors the same claim to the same derivation, so the two now stand or fall together. If 2.5 is ever cut or moved, BOTH lose their support.

### FQ5 :: P3 buyer comparison cut :: 2026-08-29 :: Stage 3
- FORBIDDEN: which is more than most buyers do
- REQUIRED: The organization commissioned the evaluation, published the full report, and allowed it to state the limits of its own method.
- FORBIDDEN: commissioned an independent evaluation
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. Wording only. The withdrawn buyer comparison did not return.
- AMENDED 2026-08-30 at Stage 7, on Dan's ruling, because THE SOURCE CONTRADICTED THE RULED SENTENCE. External check A read the evaluation: Appendix B says it was "jointly delivered by the DTA and Nous", so it is an externally assisted joint evaluation and the word "independent" is false. **The ruling's point was never that word.** FQ5 withdrew "which is more than most buyers do", and what it kept was that this buyer produced a public record and let it state its own limits. That survives intact. "commissioned an independent evaluation" is now FORBIDDEN so the corrected form cannot quietly revert. **TWO SENTENCES CARRIED THE CLAIM and both were corrected together**, the P3 setup and this one, which sit far apart in the file: that is the S3-4 shape and the reason this ledger exists.
- REVERSES-IF: evidence on how often buyers commission and publish independent evaluations. The preceding sentence already distinguishes this case from the opening case, so the clause added a population claim and little else.

### FQ6 :: business case sole-document cut :: 2026-08-29 :: Stage 3
- FORBIDDEN: and it is usually the only document stating what the deployment was supposed to achieve
- REQUIRED: By the time anyone compares actual use with the original case, that case describes a deployment that no longer exists.
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. Wording only. "the two" is now named, which is clearer and claims no more.
- REVERSES-IF: evidence that no other document ordinarily states a deployment's objective. **Nothing was lost to the cut**: the next paragraph already makes the point as a formal conditional, at "If nothing revisits that statement, the claimed benefit becomes the organization's permanent belief about what the deployment delivers." The cut removed an unconditional duplicate of a conditional the chapter already had.

### FQ7 :: scale crossing recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: and the usual answer is that it crossed some time ago
- REQUIRED: and no single event announces that crossing when it occurs
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. Wording only, and still anchored to 2.5.
- REVERSES-IF: evidence on how many deployments have passed THM-004's scale antecedent. **This was the strongest of the eight and sat in the limits section**, which exists to state what the chapter does not claim and closed by claiming that most deployments have already crossed. The recast is anchored to 2.5, which derives that the absence of a record is invisible until it is needed.

### FQ8 :: mapping failure modes recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Two failure modes recur when organizations run this mapping on themselves
- REQUIRED: Two errors follow from these distinctions.
- FORBIDDEN: Two common errors
- REVERTED AND REPAIRED 2026-08-30 at Stage 6, on Dan's ruling. The copy edit read "Two common errors follow from these distinctions." **"Common" is a recurrence claim**, and REVERSES-IF below states why there cannot be an observational base for one: the mapping is this book's own construct, introduced on the page before. The derivation clause the ruling required was already present and is kept; only "common" is cut. It is now FORBIDDEN.
- SUPERSEDED-IN-PART 2026-08-29 at Stage 4, F8: "and both are worth naming in advance" is cut as an announcement. **THE RULING IS UNCHANGED IN SUBSTANCE**: what mattered was replacing the claim of observed recurrence with a derivation, and "follow from the distinctions already drawn" is intact.
- REVIEW: the two failure modes must continue to follow from distinctions the chapter draws EARLIER than this passage. The first rests on 2.2's division of what belongs to the buyer, the second on 2.6's separation of adoption from value. If either moves after the craft section, this sentence loses its support and reverts to an unsupported claim.
- REVERSES-IF: an observational base for the recurrence. **There cannot be one yet.** The three-flow mapping is this book's own construct, introduced on the page before, so no organization has run it and no recurrence can have been observed. This was the worst of the eight for that reason.

### S3-1 :: RETIRED 2026-08-30 :: adoption gloss no longer contradicts its sentence :: 2026-08-29 :: Stage 3
- RETIRED-FORBIDDEN: Reported adoption, not quantified. See the register.
- RETIRED-REQUIRED: Consistent values across several outlets with no consistent attribution, so no single source is named. The adoption is characterized rather than given as a percentage.
- RETIRED 2026-08-30 at Stage 7, on Dan's ruling, WITH S3-2, BECAUSE THE CONDITION S3-2 NAMED WAS MET. This ruling governed a gloss on a citation that no longer exists: `uber-2026-adoption` is retired and both footnotes now cite Forbes. The sentence it protected is gone too, because the percentages it declined to give are now given. Kept here as history, with its fields renamed out of enforcement rather than deleted, which is the supersede convention.
- REVERSES-IF: nothing about the source. **This is a ruling about the GLOSS, not about the claim.** The old note read "not quantified" against a sentence reading "about a third of the engineering organization was using it", which cannot both stand. It was written to mean that no PERCENTAGE is given, and it now says that. Found by external check 1 on 2026-08-29 as S3-1 and ruled by Dan the same day, option (c) of three.

### S3-2 :: RETIRED 2026-08-30 :: the unattributable citation says so instead of implying a source :: 2026-08-29 :: Stage 3
- RETIRED-FORBIDDEN: Reported share of committed code.
- RETIRED-REQUIRED: Characterized rather than quantified, for the same reason.
- RETIRED 2026-08-30 at Stage 7, on Dan's ruling. **ITS OWN REVERSES-IF WAS MET, WORD FOR WORD.** That field asked for "a single named source for the adoption figures, ideally the primary" and said that with one, "both footnotes get a real citation and both of these rulings retire together." External check A read Forbes and reports 32 per cent adoption in February rising to 84 per cent in March. Forbes is named, dated, read, and was ALREADY IN THE REGISTER as `uber-2026-budget`. **STANDING RULE 2 WAS SATISFIED, NOT BENT**: the percentages came out on 2026-08-21 because no citation could be named without inventing one, and they return because one can. The committed-code sentence is replaced by the first-party figure from the transcript, since check A found that "passed through" has no stable technical definition. **THE CHECK RAISED THIS WITHOUT KNOWING IT WAS RULED**, because the packet was not supplied to it, and it therefore did not reopen a ruling: it delivered the evidence the ruling was waiting for.
- RETIRED-REVIEW: footnotes 3 and 4 deliberately name no outlet, and a later reader WILL raise that again. The container reads "Multiple secondary outlets" because the February and March figures appeared across several outlets with consistent values and no consistent attribution, which is the signature of one upstream source repeated rather than of corroboration. Dan withdrew the percentages on 2026-08-21 rather than invent a citation, and standing rule 2 has no option for citing a source that cannot be named. **The remedy is not to name an outlet. It is that the note now says why none is named.**
- MET-AND-RETIRED 2026-08-30: a single named source for the adoption figures, ideally the primary, which is exactly what the register entry's `upgrade` field asks for. With one, both footnotes get a real citation and both of these rulings retire together. **This is the field that came true.**

### S3-4 :: the executive's title corrected :: 2026-08-29 :: Stage 3
- SOURCE-KEY: fortune-2026-uber-coo
- FORBIDDEN: The chief operating officer was publicly asking whether the spending had been worth it.
- FORBIDDEN: Its chief operating officer was asking, in public, what the company had received.
- FORBIDDEN: The president and chief operating officer was publicly asking whether the spending had been worth it.
- REQUIRED: president and chief operating officer Andrew Macdonald said the company still could not connect its growing use of Claude Code to the consumer features it was producing.
- REQUIRED: “That link is not there yet,” he said.
- REQUIRED: its president and chief operating officer publicly asked what it had received in return
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. Both sentences were rewritten and **both kept the corrected title**, which is the drift the REVIEW below predicted and the one place this ledger was most exposed. The opening case now names the product where it said "the tool", and the 2.6 back-reference is unchanged in substance. Both open lower case because each now sits mid-sentence, and matching is case-sensitive.
- SUPERSEDED-IN-PART 2026-08-29: the title fix landed first and its opening-case form is now FORBIDDEN in turn, because Dan then ruled the executive named and quoted directly. The 2.6 back-reference is unchanged and stays REQUIRED: it is supported by B2, where Dan verified that Macdonald questions the value of the spend repeatedly.
- REVERSES-IF: the title changes, or a source shows Andrew Macdonald did not hold both roles at the time of the interview. Dan verified the title at Stage 3 on 2026-08-29.
- REVIEW: **TWO sentences carry this title and both were corrected together.** The opening case has one and section 2.6 has the other. A later edit that fixes only one reintroduces exactly the drift this ledger exists to catch, and neither sentence is near the other in the file.

### S4-1 :: section 2.3 now depends on the opening case's figure :: 2026-08-29 :: Stage 4
- SOURCE-KEY: uber-2026-budget
- REQUIRED: The opening case shows the mismatch clearly: the organization approved an annual budget that the deployment consumed in four months.
- RESTATED 2026-08-30 at Stage 6, on Dan's ruling. Wording only. The sentence still refers to the case rather than asserting the fact independently, so it still carries no citation marker, and the REVIEW below still binds: if Stage 7 corrects the April timing, this sentence changes with it.
- REVIEW: **THIS SENTENCE RESTATES A FIGURE THAT LIVES IN THE OPENING CASE**, added at Stage 4 to close the second model's C1 finding that section 2.3 ran entirely on placeholders while sitting one page from the chapter's best instance. It refers to the case rather than asserting the fact independently, which is why it carries no citation marker. **If the opening case's timing ever changes, this sentence changes with it**, and nothing mechanical will say so, because both forms are grammatical and neither is a forbidden string.
- REVERSES-IF: the April timing is corrected at Stage 7. Dan verified it at Stage 3 as row A1.

### RV87-G3 :: opening sentence timing :: 2026-10-19 :: Review D87
- SOURCE-KEY: theinformation-2026-uber-cto
- FORBIDDEN: just four months into the year
- REQUIRED: By April 2026, only a few months into the year
- REVIEW: the case title and section 2.4's "consumed the annual budget in April" still say IN April; the sources say BY April. Not ruled; listed for Dan.
- REVERSES-IF: a source dates the exhaustion exactly.

### RV87-R1 :: control-and-return sentence narrowed :: 2026-10-19 :: Review D87
- SOURCE-KEY: uber-2026-q1-call
- FORBIDDEN: or a measure that connected the use to a return
- REQUIRED: changed the course of the spending before the budget was gone, or quantifies the net return on that spending
- REVERSES-IF: Uber publishes a quantified net return for the period, or a source shows a control that changed spending before the budget was gone.

### RV87-2A :: leaderboard figures credited to the publication :: 2026-10-19 :: Review D87
- SOURCE-KEY: meta-2026-memo
- REQUIRED: The Information reported that a copy of an internal leaderboard it reviewed in April showed
- REVERSES-IF: Meta confirms the figures on the record.

### RV87-2B :: Amazon workers tried, and Treadwell is reported speech :: 2026-10-19 :: Review D87
- SOURCE-KEY: ft-2026-amazon-leaderboard
- REQUIRED: after workers tried to boost their scores
- REQUIRED: told staff not to use AI just for the sake of using AI
- REVIEW: the direct quotation was replaced by reported speech because voicecheck bans contractions inside quotations (Dan, 2026-10-19).
- REVERSES-IF: the article is corrected.

### RV87-2C :: only the cap is Uber's own statement :: 2026-10-19 :: Review D87
- SOURCE-KEY: bloomberg-2026-uber-caps
- FORBIDDEN: Uber told Bloomberg News
- REQUIRED: An Uber spokesperson confirmed that all employees were limited to $1,500 a month
- REQUIRED: Bloomberg also reported that every employee had a dashboard
- REVERSES-IF: Uber confirms the dashboard and exception process on the record.

## Ch03

**Ruled by Dan at sitting 3, 2026-10-13, in three groups, each accepted whole**
(`Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_Sitting3_rulings.md`).
Group 1 rests on external check A, which read the sources with live web access.
Groups 2 and 3 rest on external check B, which read only the render, and Group 2
was checked by Claude against the pinned registry, dag.aiom 9d7ee50. Entries
below cover the narrowings a copy edit could silently undo; the rest are
wording that no shorter sentence would restore.

### FC3-A1 :: mission wording quoted exactly :: 2026-10-13 :: Stage 3
- SOURCE-KEY: finops-2026-mission
- FORBIDDEN: who manage cloud value
- FORBIDDEN: who manage technology value
- REQUIRED: "advancing the people who manage the value of cloud."
- REVERSES-IF: the Foundation's announcement gives a different wording.

### FC3-A3 :: history not in the report :: 2026-10-13 :: Stage 3
- SOURCE-KEY: finops-2026-state
- FORBIDDEN: work the discipline had not originally been created to do
- SUPERSEDED-REQUIRED: Its central finding concerned the expansion of FinOps into AI spending.
- REVERSES-IF: a source states that FinOps was not created for AI spending, cited here.
- REQUIRED: Its central finding was how far FinOps had expanded into AI spending:
- RE-RULED 2026-10-17 at sitting 3 of the redesign: Dan's author-pass wording, verified by external check A (A-34); it states no history of the discipline. The FORBIDDEN form stays enforced.

### FC3-A6 :: provisioning by code unsourced :: 2026-10-13 :: Stage 3
- SOURCE-KEY: finops-definition-2024
- FORBIDDEN: a few lines of code
- SUPERSEDED-REQUIRED: cloud consumption varied with use, and the bills arrived after capacity had been used.
- REVERSES-IF: a source describing provisioning by code is cited.
- REQUIRED: cloud bills varied with use and arrived after capacity had been consumed.
- RE-RULED 2026-10-17 at sitting 3 of the redesign: Dan's author-pass wording, verified by external check A (A-35); no provisioning-by-code mechanism. The FORBIDDEN form stays enforced.

### FC3-B10 :: survey population :: 2026-10-13 :: Stage 3
- SOURCE-KEY: finops-2026-state
- FORBIDDEN: nearly all of them were managing it
- SUPERSEDED-REQUIRED: nearly all of the survey's respondents were managing it.
- REVERSES-IF: a source covering all FinOps practitioners, not one survey's respondents.
- REQUIRED: nearly all respondents to the Foundation's survey were managing it.
- RE-RULED 2026-10-17 at sitting 3 of the redesign: Dan's author-pass wording, verified by external check A (A-37); still scoped to the survey's respondents. The FORBIDDEN form stays enforced.

### FC3-B2 :: provenance banner after the check :: 2026-10-13 :: Stage 3
- FORBIDDEN: have not yet been checked against the report itself
- REQUIRED: Figures and the quotation checked against the Foundation's report and announcement, October 2026.
- REVERSES-IF: a figure or the quotation is found to differ from the report.

### FC3-A12 :: the release's own words :: 2026-10-13 :: Stage 3
- SOURCE-KEY: klarna-2024-assistant
- FORBIDDEN: built on OpenAI's models
- REQUIRED: an AI assistant powered by OpenAI
- REVERSES-IF: none expected; the release is fixed.

### FC3-R1 :: non-claims recorded for certified claims only :: 2026-10-13 :: Stage 3
- SOURCE-KEY: aibe-registry-2026
- SUPERSEDED-FORBIDDEN: The registry records every claim's non-claims.
- SUPERSEDED-REQUIRED: The registry records non-claims for every certified claim, but its lists are not exhaustive.
- RESTATED 2026-10-13 at the scoped re-review (SR-4), on Dan's ruling: wording only; the narrowing to certified claims stands.
- REVERSES-IF: a pinned registry version in which every claim, certified or not, carries exclusions.
- SUPERSEDED 2026-10-17: Retired by Dan at sitting 3 of the redesign (Decision 85): the sentence was cut when the registry walk-through left the chapter. The lines above are kept as history and are no longer enforced by W14.

### FC3-B4 :: certified count by type :: 2026-10-13 :: Stage 3
- SOURCE-KEY: aibe-registry-2026
- SUPERSEDED-REQUIRED: including 9 of the 11 theorems and 20 of the 21 lemmas.
- SUPERSEDED-REVIEW: the counts belong to the pinned version; if the manifest is refreshed, the dated box changes with it.
- REVERSES-IF: the manifest is refreshed.
- SUPERSEDED 2026-10-17: Retired by Dan at sitting 3 of the redesign (Decision 85): the sentence was cut when the registry walk-through left the chapter. The lines above are kept as history and are no longer enforced by W14.

### FC3-B13 :: value boundary is the book's practice, not LEM-021 :: 2026-10-13 :: Stage 3
- SOURCE-KEY: aibe-registry-2026
- SUPERSEDED-FORBIDDEN: The organization must set that boundary for each deployment
- SUPERSEDED-REQUIRED: This book adds two requirements of practice that the lemma does not state
- REVERSES-IF: a certified registry claim requiring a per-deployment boundary set in advance.
- SUPERSEDED 2026-10-17: Retired by Dan at sitting 3 of the redesign (Decision 85): the sentence was cut when the registry walk-through left the chapter. The lines above are kept as history and are no longer enforced by W14.

### FC3-B21 :: THM-002 claims a risk :: 2026-10-13 :: Stage 3
- SOURCE-KEY: aibe-registry-2026
- SUPERSEDED-FORBIDDEN: yet the cost is not understated
- SUPERSEDED-REQUIRED: yet doing so creates no risk of understating the cost within the evaluation boundary.
- REVERSES-IF: THM-002's statement changes upstream.
- SUPERSEDED 2026-10-17: Retired by Dan at sitting 3 of the redesign (Decision 85): the sentence was cut when the registry walk-through left the chapter. The lines above are kept as history and are no longer enforced by W14.

### FC3-B1 :: certification is not truth :: 2026-10-13 :: Stage 3
- FORBIDDEN: states what is true about consuming AI
- FORBIDDEN: Part II establishes what is true
- REQUIRED: AI Business Economics states conditional claims about consuming AI and records what each one rests on.
- REVERSES-IF: none; 3.1 says the validator checks structure, not truth.

### FC3-B27 :: wrong claims, careful execution :: 2026-10-13 :: Stage 3
- FORBIDDEN: however carefully managers carry it out
- FORBIDDEN: fails however well it is run
- REVERSES-IF: none; the absolute form had no support.

### FC3-B26 :: the five questions :: 2026-10-13 :: Stage 3
- FORBIDDEN: cannot answer without the discipline
- REQUIRED: An organization that manages its AI consumption can answer five questions from its own records:
- RESTATED 2026-10-13 at the scoped re-review (SR-2), on Dan's ruling: the 3.6 opening that repeated this was cut; the claim now rests on the next paragraph's sentence, and the withdrawn form stays FORBIDDEN.
- REVERSES-IF: evidence that organizations cannot answer the questions without the discipline, cited.

### FC3-B35 :: no cost ranking :: 2026-10-13 :: Stage 3
- FORBIDDEN: The most costly misreading
- REVERSES-IF: evidence comparing the costs of misreadings, cited.

**Redesign, ruled by Dan at sitting 3, 2026-10-17, six group gates, all A**
(`Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_v2_Sitting3_decisions.md`).
External check A read the sources with live web access; check B read only the
render. FC3-A3, A6 and B10 are re-ruled above; R1, B4, B13 and B21 retired.

### FC3V2-A21 :: "stale" was the CFO's own estimate :: 2026-10-17 :: Stage 3
- SOURCE-KEY: jpmorgan-cfo-ai-spend
- FORBIDDEN: called the earlier figure
- REQUIRED: million, while calling that estimate "a little stale at this point."
- REVERSES-IF: a transcript shows "stale" referred to Dimon's $2 billion figure.

### FC3V2-A26 :: Lindy moved most traffic, not all :: 2026-10-17 :: Stage 3
- SOURCE-KEY: lindy-2026-migration
- FORBIDDEN: had moved all its traffic
- FORBIDDEN: Sending all traffic to one model
- REQUIRED: own technical account says most of its managed-agent traffic moved, while selected uses stayed on
- REVERSES-IF: the post is revised to say all traffic moved.

### FC3V2-A28 :: unconfirmed Lindy statements cut :: 2026-10-17 :: Stage 3
- SOURCE-KEY: npr-2026-lindy
- FORBIDDEN: 100x more work than we thought
- FORBIDDEN: consider returning to
- FORBIDDEN: a company of about 25 people
- REVERSES-IF: a readable source carries the statement, cited here.

### FC3V2-A45 :: the evaluation was joint, not independent :: 2026-10-17 :: Stage 3
- SOURCE-KEY: dta-copilot-2024
- FORBIDDEN: commissioning an independent evaluation
- REQUIRED: commissioning an evaluation delivered jointly with an outside firm
- REVERSES-IF: none expected; the methodology names the DTA and Nous Group.

### FC3V2-A38 :: Cursor plan scope, priced not billed :: 2026-10-17 :: Stage 3
- SOURCE-KEY: truell-2025-pricing
- FORBIDDEN: Both conditions therefore held for a team on that plan.
- FORBIDDEN: each request drew down
- REQUIRED: and further use was priced at the same rates.
- REVERSES-IF: as SF2, a passage from the post describing billing on exhaustion.

### FC3V2-A13 :: no overlap inferred from two percentages :: 2026-10-17 :: Stage 3
- SOURCE-KEY: doit-2026-ai-spend
- FORBIDDEN: at least 8 percent named both
- REVERSES-IF: the questionnaire shows a multi-select question on a common base.

### FC3V2-A16 :: no task-selection rule reported for Microsoft :: 2026-10-17 :: Stage 3
- SOURCE-KEY: microsoft-2026-mai
- FORBIDDEN: Routine tasks moved to the in-house models
- REQUIRED: The reporting did not say how the tasks that moved were chosen.
- REVERSES-IF: a report documents the task-selection rule.

### FC3V2-A3 :: Airbnb's integration remark :: 2026-10-17 :: Stage 3
- SOURCE-KEY: airbnb-2025-qwen
- FORBIDDEN: tools for connecting its models to
- REVERSES-IF: the interview shows he meant connecting OpenAI's models to Airbnb's systems.

### RV87-3A :: AT&T figures kept to their scope :: 2026-10-19 :: Review D87
- SOURCE-KEY: theinformation-2026-att
- REQUIRED: fell by as much as 56 percent
- REQUIRED: open models powered 40 percent of employees' AI queries
- REVIEW: never merge this 40 percent of QUERIES with the FT's 40 percent of AI WORKLOADS, and never imply the move to open models began in August or September.
- REVERSES-IF: the article is corrected.

### RV87-3B :: ServiceNow timing dropped :: 2026-10-19 :: Review D87
- SOURCE-KEY: theinformation-2026-servicenow
- FORBIDDEN: tools early in the year
- REQUIRED: In May 2026, ServiceNow said it had already used up its full-year budget
- REVERSES-IF: ServiceNow dates the exhaustion itself.
