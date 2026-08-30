# Chapter 2, Stage 7. Cover note

Built 2026-08-30, from the copy-edited text. Read this before the packet. It names
what the packet cannot see, and nothing here is a verification.

## What is in this folder

| File | What it is |
|---|---|
| `AIOM_Ch02_Stage7_render.pdf` | The artifact the external check reads. Built from the copy-edited text. |
| `AIOM_Ch02_Stage7_packet.md` | Every passage carrying a citation marker, paired with its register entry and the note verbatim. Generated. |
| `AIOM_Ch02_Stage7_prompt_A.md` | Check 1. Outward, to the primary documents. |
| `AIOM_Ch02_Stage7_prompt_B.md` | Check 2. Inward, on the render alone, deliberately given no sources. |
| `AIOM_Ch02_Stage7_cover.md` | This file. |
| `README_Stage7.md` | Instructions for Dan, not for a checker. |

**The check is fed the PDF, never the chapter HTML.** Both production flags on
Chapter 1's first check were phantoms of HTML extraction: the theorem panel's
antecedents read as missing and a student-blank column read as misplaced.
Disproving them cost a build.

**Run BOTH prompts, in separate sessions, and do not show either the other's
output.** Chapter 1's pair agreed on one finding out of six, and the disagreement
was the value. A and B are pointed in opposite directions on purpose: A goes out to
the sources, B stays inside the text and is told nothing about them.

**Judge each proposed remedy separately from the finding it answers.** In Chapter
1's pair both findings survived and neither proposed fix did: one proposed hedging
language the voice rules prohibit, the other a second-source path below the floor
already in force.

## THE ONE THING THAT MAKES THIS STEP DIFFERENT FROM STAGE 3

**Stage 3 audited a text the copy edit then rewrote.** 104 of 195 blocks changed on
2026-08-30, after Stage 3 closed on 2026-08-29. A fact check that predates a copy
edit cannot be credited until it is diffed against the audited artifact, so that
diff was run rather than assumed, restricted to the seven passages carrying a
citation marker.

**All seven still cite the same keys and none gained or lost a citation.** Six of
the seven changed wording. **Eight of those changes touch what a source must
support**, and they are listed below because no gate can see any of them: every one
leaves a grammatical sentence with a live citation attached.

### The eight, in priority order

| # | Key | Was | Now | Why it matters |
|---|---|---|---|---|
| 1 | `uber-2026-budget` | "several hundred to **a few thousand** dollars per engineer" | "several hundred to **several thousand** dollars" | **A NUMERIC RANGE CHANGED.** This citation exists to support the per-engineer monthly cost range and nothing else. If the source says "a few thousand", the chapter now overstates its top end. **Check this first.** |
| 2 | `fortune-2026-uber-coo` | "could not yet draw a line from its **rising use of the tool**" | "could not connect its **growing use of Claude Code**" | The executive's attributed statement now names the product. If Macdonald's remark was about AI spending generally rather than about Claude Code, this narrows an attributed statement past what the source supports. |
| 3 | `uber-2026-budget` | "**press reporting indicates that** Uber had spent the annual budget" | "Uber had **already exhausted** its annual AI budget" | The in-text attribution hedge is gone and the claim is now asserted directly. The footnote still carries the citation, so this is not unsourced, but the sentence no longer tells a reader it rests on reporting. |
| 4 | `uber-2026-budget` | "with **the tool** the company had given them" | "by using **the tools** it had given them" | Singular to plural. The case concerns one named tool. |
| 5 | `dta-copilot-2024` | "The evaluation **states two things about its own method**" | "The evaluation **identified two limits** in its method" | "Limits" is a characterization the evaluation may not use of itself. P3 rests entirely on this source and it is the one nobody has read. |
| 6 | `fortune-2026-uber-coo` | "said **publicly** that" | "said that" | Not false, but "publicly" is what made the remark citable to a news account. |
| 7 | `dta-copilot-2024` | "**The licence is** priced per seat" | "**The product was** priced per seat" | The licence and the product are not the same object, and the distinction is the chapter's own subject. |
| 8 | `uber-2026-adoption` | "**Reporting indicates** that by spring" | "**Press reports indicated** that by spring" | Ruling S3-2 has these footnotes deliberately naming no outlet. "Press reports" asserts a little more about provenance than "reporting" does. |

**Changes NOT in that table are style and carry no sourcing consequence**, and were
checked rather than skipped: "Ninety-five percent" to "95 percent", "roughly five
thousand engineers" to "roughly 5,000 engineers", the MIT NANDA sentence compressed
from four sentences to two with "a far higher share" becoming "even though a far
larger share", and various tightenings that change no fact.

## What each register entry still owes

Five keys, all five cited, no orphans and nothing dangling. **No source in this
chapter has been read by anyone**, in the sense a fact checker means: WebSearch
returns summaries and the egress proxy blocks `WebFetch` and `curl`, so Claude can
discover a candidate and cannot verify one.

- **`dta-copilot-2024`. The largest exposure, and the reason to start here.** Grade
  C, no location, unread. **Problem P3 is built entirely on it**: the trial dates,
  around sixty agencies, several thousand licences, per-seat pricing, and the
  evaluation's two statements about its own method. Its note records that the
  secondary coverage disagrees with itself on every count. **If the published
  evaluation contradicts any of it, P3 needs rebuilding rather than rewording.**
- **`mit-nanda-2025`.** No location. Obtain the report and confirm the wording of the
  headline finding. **It degrades gracefully**: the chapter rests on the phrase "no
  measurable impact" rather than on the ninety-five per cent figure.
- **`uber-2026-budget`** (Forbes) and **`fortune-2026-uber-coo`** (Fortune) carry
  access dates of 2026-08-21, supplied by Dan, and both are perishable and paywalled.
  Items 1, 2, 3, 4 and 6 above all land on these two.
- **`uber-2026-adoption`** carries no access date because it cites no document. The
  adoption figures appeared across outlets with consistent values and no consistent
  attribution, which is the signature of one upstream source repeated rather than of
  corroboration. **That is the ruling rather than a gap.**

## What a checker must not re-raise

**Twelve rulings are in force**, recorded in `AIOM_Claim_Ledger.md` and reproduced in
the packet. A checker who reaches one should say whether the condition named in its
REVERSES-IF is now met, not restate the finding.

**Two were reverted by the copy edit and repaired on Dan's ruling on 2026-08-30**,
FQ3 and FQ8, and both reverted forms are now forbidden in turn. **If a remedy
proposes either frequency claim back, it is proposing something withdrawn twice.**

**S3-2 is the one most likely to be raised again and it is settled.** Footnotes 3 and
4 name no outlet on purpose. Standing rule 2 has no option for citing a source that
cannot be named, so the percentages were withdrawn rather than a citation invented,
and the note now says why none is named. **The remedy is not to name an outlet.**

**A sixth frequency candidate is ruled clean and should not be raised**: "Organizations
skip the record flow most often for structural reasons", because section 2.5 derives it.

## One defect in the render, named so nobody reports it

**Footnote 5 does not sit on its calling page.** Print gate 8 reports it and the
packet's RENDER line carries the failure verbatim. It is reflow from a copy edit that
changed 104 of 195 blocks, it is Stage 5's business after this step, and it is
deliberately not fixed yet because Process v3 puts the design review after the fact
check so pagination is not settled twice. **The other fourteen print gates pass.** It
affects nothing a fact checker reads.
