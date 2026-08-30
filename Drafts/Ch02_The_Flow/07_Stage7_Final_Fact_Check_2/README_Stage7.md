# Chapter 2, Stage 7. The final fact check. Instructions.

Built 2026-08-30, from the copy-edited text. Stage 6 is cleared; the chapter is at
8 of 13.

**THIS SUPERSEDES THE STAGE 7 HALF OF `06_Stage6_Copy_Edit/README_Stage6_and_7.md`.**
That file was written before the copy edit and quotes a sentence the copy edit changed.
Sending a checker after a sentence the chapter does not contain is the exact drift this
project has recorded twice inside its own register notes, so the wording below is quoted
from the current live text rather than carried forward.

## The package, and the order to read it in

**`AIOM_Ch02_Stage7_cover.md` first.** It carries the one thing this step has that
Stage 3 did not: the copy edit landed AFTER Stage 3 closed, so the cover diffs all
seven cited passages across it and lists the eight changes that touch what a source
must support. **No gate can see any of the eight**, because each leaves a grammatical
sentence with a live citation attached. Item 1 is a numeric range that moved.

**Then send two checks, in separate sessions, and show neither the other's output.**

| Send | To whom | With |
|---|---|---|
| `AIOM_Ch02_Stage7_prompt_A.md` | Model 1 | the render AND the packet |
| `AIOM_Ch02_Stage7_prompt_B.md` | Model 2 | the render ONLY |

**B is given no packet on purpose and that is the design.** A reads outward to the
sources; B reads the chapter as a sceptical reader receives it, with nothing but the
page. A claim that survives only because a reader trusts a footnote they cannot see is
what B exists to find, and it cannot find it holding the register.

## What to check with

**Feed the checker `AIOM_Ch02_Stage7_render.pdf`, never the chapter HTML.** Both
production flags on Chapter 1's first check were phantoms of HTML extraction and cost a
build to disprove. The claim inventory is `AIOM_Ch02_Stage7_packet.md`, generated from
the live text: every cited passage, the keys it cites, and each register entry
reproduced in full.

**The render carries one known print-gate failure and the packet says so on its RENDER
line.** Footnote 5 does not sit on its calling page, which is reflow from a copy edit
that changed 104 of 195 blocks. It is Stage 5's business, after this step, because
Process v3 puts the design review after the fact check so pagination is not fixed twice.
**It does not affect what a fact checker reads**, and it is named here so nobody reports
it as a finding.

## What Stage 7 must settle

Stage 3 cleared Forbes and Fortune across nine rows. What is left is short, and the copy
edit did not change what any of it rests on.

- **`dta-copilot-2024`. The larger exposure.** Grade C, unread by anyone. Problem P3 is
  built entirely on it. The facts to check, in the chapter's current wording: the trial
  ran "Between January and June 2024", "Around sixty agencies participated", "the
  government issued several thousand licences", "The product was priced per seat rather
  than by unit of use", and the evaluation "identified two limits in its method:
  participants assessed the effects themselves, which could understate or overstate
  them, and no measure of the work existed from before the trial." **If the published
  evaluation contradicts any of those, P3 needs rebuilding rather than rewording.**
- **`mit-nanda-2025`.** No location. Obtain the report and confirm the wording of the
  headline finding. **The chapter still rests on the phrase "no measurable impact"**
  rather than on the ninety-five per cent figure, and the copy edit left that phrase in
  place and still set in italic, so it degrades gracefully.
- **S4-1, which no gate can see, IN ITS NEW WORDING.** Section 2.3 now reads: "The
  opening case shows the mismatch clearly: the organization approved an annual budget
  that the deployment consumed in four months." It refers to the opening case rather
  than asserting the timing independently, which is why it carries no citation marker.
  **If you correct the April timing, this sentence changes with it**, and nothing will
  report it, because both forms are grammatical and neither is a forbidden string.

## How to run it

**Run two checks on different prompts.** Chapter 1's pair agreed on one finding out of
six, and the disagreement was the value. **Judge each proposed remedy separately from the
finding it answers**: in that same pair both findings survived and neither proposed fix
did.

**Twelve rulings are in force and a checker should not re-raise them.** They are listed
in `AIOM_Claim_Ledger.md` and reproduced in the packet. A checker who reaches one should
say whether the condition named in REVERSES-IF is now met, not restate the finding.

**Two of those rulings were reverted by the copy edit and repaired on Dan's ruling**,
FQ3 and FQ8, and both reverted forms are now FORBIDDEN in turn. If a Stage 7 remedy
proposes either frequency claim back, it is proposing something already withdrawn twice.

## What Claude does after this

Stage 5, then G2, then `continuity.py --update` and lock at Stage 9. **Stage 5 inherits
the gate 8 footnote failure** and is where the pagination is settled, once this step has
stopped moving the text.
