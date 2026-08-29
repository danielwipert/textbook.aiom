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
- REQUIRED: The decay is worth one concrete illustration.
- REVERSES-IF: a study of manager estimation error on record decay. The clause justified including an example rather than carrying argument, so the illustration that follows earns the point unaided.

### FQ2 :: cost governance recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Most organizations that believe they have cost governance have the first, sometimes the second, and rarely the third.
- REQUIRED: The three are separable, and an organization can hold the first without the second and the first two without the third.
- REQUIRED: Where the record exists and the constraint does not, a dashboard nobody acts on is a record flow with no constraint attached.
- REVERSES-IF: a survey of cost-governance maturity establishing the distribution across the three parts. The teaching point is that the three are separable, which survives the recast; only the population claim was withdrawn.

### FQ3 :: surprise frequency recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Organizations are usually surprised by the second finding rather than the third
- REQUIRED: The second finding surprises where the third does not, because the absence of a record is invisible until somebody asks a question that needs one.
- REVERSES-IF: evidence about what surprises organizations running this diagnostic. The mechanism after "because" was already in the sentence and is unchanged; only the population wrapper went.

### FQ4 :: Chapter 8 forward reference recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: the flow this mapping most often finds missing
- REQUIRED: the record flow built there is the one that is structurally the easiest to skip
- REVISED at application, 2026-08-29: the drafted recast read "the one section 2.5 shows is structurally the easiest to skip", and the Stage 4 re-read cut the pointer. **The drafted form made C7 worse at the worst possible sentence**, the craft section's opening, which would then have carried three references at once: the rest of the book, Chapter 8, and section 2.5. **The derivation clears the claim whether or not the sentence points at it**, which is exactly how Stage 1 cleared the sixth candidate: that one sits in the chapter summary and names no section.
- REVERSES-IF: nothing, and this entry is the one to read before reopening any of the others. Stage 1 cleared a sixth candidate, "the record flow is skipped most often, and for structural reasons rather than careless ones", on the ground that section 2.5 derives it. This recast anchors the same claim to the same derivation, so the two now stand or fall together. If 2.5 is ever cut or moved, BOTH lose their support.

### FQ5 :: P3 buyer comparison cut :: 2026-08-29 :: Stage 3
- FORBIDDEN: which is more than most buyers do
- REQUIRED: This organization commissioned an independent evaluation, published it, and let it report the limits of its own method.
- REVERSES-IF: evidence on how often buyers commission and publish independent evaluations. The preceding sentence already distinguishes this case from the opening case, so the clause added a population claim and little else.

### FQ6 :: business case sole-document cut :: 2026-08-29 :: Stage 3
- FORBIDDEN: and it is usually the only document stating what the deployment was supposed to achieve
- REQUIRED: By the time anyone compares the two, the business case describes a deployment that no longer exists.
- REVERSES-IF: evidence that no other document ordinarily states a deployment's objective. **Nothing was lost to the cut**: the next paragraph already makes the point as a formal conditional, at "If nothing revisits that statement, the claimed benefit becomes the organization's permanent belief about what the deployment delivers." The cut removed an unconditional duplicate of a conditional the chapter already had.

### FQ7 :: scale crossing recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: and the usual answer is that it crossed some time ago
- REQUIRED: and nothing announces the crossing at the moment it happens
- REVERSES-IF: evidence on how many deployments have passed THM-004's scale antecedent. **This was the strongest of the eight and sat in the limits section**, which exists to state what the chapter does not claim and closed by claiming that most deployments have already crossed. The recast is anchored to 2.5, which derives that the absence of a record is invisible until it is needed.

### FQ8 :: mapping failure modes recast :: 2026-08-29 :: Stage 3
- FORBIDDEN: Two failure modes recur when organizations run this mapping on themselves
- REQUIRED: Two failure modes follow from the distinctions already drawn, and both are worth naming in advance.
- REVIEW: the two failure modes must continue to follow from distinctions the chapter draws EARLIER than this passage. The first rests on 2.2's division of what belongs to the buyer, the second on 2.6's separation of adoption from value. If either moves after the craft section, this sentence loses its support and reverts to an unsupported claim.
- REVERSES-IF: an observational base for the recurrence. **There cannot be one yet.** The three-flow mapping is this book's own construct, introduced on the page before, so no organization has run it and no recurrence can have been observed. This was the worst of the eight for that reason.
