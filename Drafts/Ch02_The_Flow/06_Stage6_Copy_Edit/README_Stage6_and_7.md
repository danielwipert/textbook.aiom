# Chapter 2, Stages 6 and 7. Instructions.

Built 2026-08-29. Stage 4 closed; the chapter is at 7 of 13.

## Stage 6, the copy edit. Yours, in Word.

**Edit this file:** `AIOM_Ch02_Stage6_copyedit.docx`

**Do not edit anything else.** The `.docx` is a proof, never a second source. The live
text stays the HTML (Decision 50), and Claude imports your edits back into it.

**The round-trip control passed before you start**: the UNEDITED export was imported and
reported 195 tagged paragraphs against 195 exported blocks, zero edited, zero refused.
Both tools are trusted on this chapter. That check found both bugs in the pair when it
was written, and neither was visible any other way.

**Two things carried forward that the copy edit can close cheaply:**

- **F4's residual.** Chapter 2 runs a mean of 15.6 words against Chapter 1's 14.3.
  Sentences over 35 words are already at zero. Shortening long-but-sound sentences is in
  scope here and was deliberately not done at Stage 4.
- **Nothing else.** F1 belongs to Chapter 6's supply obligation, not to this step.

**THE ONE THING THAT WILL BREAK THE BUILD.** Twelve rulings are now enforced by W14, and
`voicecheck` binds as of Stage 4. **A copy edit that reverts a ruled claim or reaches for
a shorter form of a withdrawn sentence fails the build**, by design: that is the failure
Chapter 1 suffered five times with every date and figure intact. If a change is refused,
the ledger entry says why and what would reverse it.

## Stage 7, the final fact check. Yours, external.

**It runs AFTER the copy edit, not beside it.** Claude imports your edits, rebuilds, and
then generates the Stage 7 packet and render from the copy-edited text. **A fact check
that predates a copy edit has to be diffed against the audited artifact before it can be
credited**, so pre-building it would cost more than it saves.

**Feed the checker the PDF, never the HTML.** Both production flags on Chapter 1's first
check were phantoms of HTML extraction and cost a build to disprove.

**What Stage 7 must settle, and it is short**, because Stage 3 cleared Forbes and Fortune
across nine rows:

- **`dta-copilot-2024`. The larger exposure.** Grade C, unread by anyone. Problem P3 is
  built entirely on it: the trial dates, around sixty agencies, several thousand
  licences, per-seat pricing, and the evaluation's two statements about its own method.
  **If the published evaluation contradicts any of those, P3 needs rebuilding rather
  than rewording.**
- **`mit-nanda-2025`.** No location. Obtain the report and confirm the wording of the
  headline finding. It degrades gracefully: the chapter rests on the phrase "no
  measurable impact" rather than on the ninety-five per cent figure.
- **S4-1, which no gate can see.** Section 2.3 now says "an annual budget, consumed four
  months into the year." **If you correct the April timing, that sentence changes with
  it**, and nothing will report it.

**Run two checks on different prompts.** Chapter 1's pair agreed on one finding out of
six, and the disagreement was the value. Judge each proposed remedy separately from the
finding it answers.

## What Claude does between them

Imports your `.docx`, dry run first and then `--apply`, reports what it refused rather
than guessing, rebuilds, and produces the Stage 7 render and packet. Then after Stage 7:
Stage 5, G2, and lock at Stage 9 after `continuity.py --update`.
