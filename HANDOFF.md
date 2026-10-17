# Session handoff

Last updated: 2026-10-17. **One page, current state only (Decision 80).** The
protocol is CLAUDE.md section 13. The full history to this date is
`archive/HANDOFF_history_to_2026-09-30.md`: read it for the story of a specific
finding, never for the current state. Keep this file under 150 lines; a durable
rule goes to CLAUDE.md, a lesson to LESSONS.md, and a closed item is deleted.

## Repository state

- `main` is level with `claude/inspiring-galileo-9hba1g` as of 2026-10-17
  (fast-forward to 35e519f); web run 131 published it, success. Merged and safe to
  delete (Dan, 403 from the container): `claude/happy-bardeen-hhct43`,
  `claude/inspiring-bohr-4gquw9`, `claude/sharp-dirac-ojfqqz`.
- Chapters 1 (Process v2) and 2 (v3) LOCKED. **Chapter 3 RE-LOCKED 2026-10-17
  (redesign, Decision 85, Process v4) at 17f7960 and PUBLISHED.** Chapters 4 to 15 not
  started.
- Run `python3 git_hygiene.py` before merging and before closing.

## Process v4, adopted 2026-09-30

Seven steps, four sittings for Dan: plan approval, review rulings, fact-check
rulings, sign-off, plus his author pass in Word. Evidence and reasoning are in
`AIOM_Process_v4_Proposal_v1.0.md`; rulings in `AIOM_Workplan_v5.md`. The v4
checklist keeps v3 step LABELS so the tools bind unchanged; see its preamble.

## Next actions, in order

1. **NEXT: the holistic review of Chapters 1 to 3 (Decision 83)**, below, then
   Chapter 4. Fix-between-chapters items first if Dan wants them.

**Decision 84 (2026-10-11): every decision goes to Dan as logic gates**, one at a
time, options A, B and C, one recommended. Rule and format: CLAUDE.md section 5.

## Waiting on Dan

- **Stray branch `claude/dazzling-franklin-1v5arn`** (3 commits, 2026-10-12): a
  parallel Ch3 session that imported the author pass and built fact-check
  packages. Superseded by the locked chapter on `main`; nothing in it is
  needed. Dan decides whether to delete it (403 from the container).
- **After Chapter 3 locks: the holistic review of Chapters 1 to 3** (Decision 83):
  newer evidence and any conclusion that no longer holds, one package, a checker
  with web access, a whole-book pass considered. Chapters 1 and 2 are NOT edited
  before then; the THM-004 "Diligence" gloss question (B8) waits for it. Also for it:
  Chapter 1 now reads "additional usage was billed at the underlying API rates",
  the mechanism its own truell-2025-pricing note ruled out (SF2, SF8); Ch3 uses "priced".
  And Chapter 2's P3 says participants used the tool "a few times a week or less"; check A
  (Ch3 A-46) found that describes most survey respondents, not every participant.
- Not needed yet: Decision 28 (Northmoor properties G, H, I; gates Chapters 9,
  12, 13) and which Northmoor CSVs are student inputs versus worked exhibits
  (Part III build).

## Closed by Process v4

- Old H1, the frequency sweep: Decision 78 and `freqsweep.py`.
- Old H4, the copy-edit row of the re-run matrix: Decision 75 moves the large
  edit before the fact check, and after it only the mechanical checks re-run.

## Carry into Chapter 3

- **Opening case 14.1 (State of FinOps 2026) is unsourced**: the case bank holds
  it only as a research target. WebSearch can find it; nothing here can read it,
  so it enters at Grade C until an external reader confirms it.
- Part I cumulative case: Klarna, February 2024, Grade A in the case bank.
- Three continuity promises are owed to Chapter 3 (`AIOM_Continuity_Ledger.md`
  lines 126, 137, 138).
- Consolidated Spec section 3.1 quotes stale registry counts (now 201
  propositions, 21 lemmas, 11 theorems).

## Fix-between-chapters list (Decision 79)

Chapter 3 is in flight: add here, one line each, and fix only what blocks.

- **`registry.py --check` compares a panel's NAME only, never its statement.**
  That is how Chapter 2's THM-004 panel locked while not rendering the
  registry. Add a statement check (antecedents and consequent against the
  bundle) between chapters; highest value on this list.

- **Single-file review packages (Dan, 2026-10-06).** Every external review (content
  or fact check) ships as ONE markdown file: instructions, output format, all material
  between BEGIN/END markers. Ch3's was hand-assembled; write `review_package.py` so
  every chapter's package is generated the same way.

- **voicecheck read "Part I’s" as a contraction** (fixed 2026-10-17 under the blocking exception, Ch3 V2-A2). Add the case to a voicecheck control.
- **web_gates_selftest snapshot control** expects a reopened chapter not to be materialized; snapshot.py serves its last lock by design. Derive the expected set from lock_commit, not current Stage 9 (Ch3 G2, 2026-10-17).
- **chapter_check preview now leads with the locked chapters before it** (fixed 2026-10-17 under the blocking exception: W9 failed Ch3, which has no theorem panel). **Gate 1 skips whitespace** (same day, a hanging space after an inline span). Add controls for both.
- **`place.py` read a wrapped callout term interleaved** (fixed 2026-10-14
  under the blocking exception; Ch3 P1). Add a negative control for it.
- **The build's page-fill advisory missed pages 7 and 13** of Ch3 (256 and
  266pt unused); it reported only page 15. Measure fill from body text bottom.
- **The "Craft section" slot label has no top margin** (base .slot-label);
  it sits close under the paragraph before it. Design system, every chapter.
- **`claimcheck.normalize` turns every tag into a space** (found 2026-10-13), so
  "<span class=nb>OpenAI</span>." reads "OpenAI ." and a REQUIRED string cannot
  end on an .nb word plus period (FC3-A12 recorded without it). The span.nb rule.
- **`factcheck_packet.py` skips citations inside tables** (found 2026-10-13):
  Ch3 Table 3.1's three cited cells were missing from the packet; added by hand
  in `build_packages.py`.
- **`prose_extract.py` drops tables** (found 2026-10-06): Ch3 Table 3.1 never reached
  the second-model reviewer, who then reported it empty (S-2). Patched into the Ch3
  package by hand; fix the extractor and check the Ch1 exemplar for the same loss.

- Manual page reads are stale for Chapter 1 (since 2026-08-14) and Chapter 2
  (since the 2026-10-01 THM-004 amendment; its panel page WAS read).
- `voicecheck.py` Part 5 rule 1 proxy counts fronted adverbials; do not quote it.
- `place.py` leaves a `.bak` beside the chapter; delete it after every run.
- Gate 4 does not guard the theorem callout; gaps G-I and G-II still open.
- `reopen.py` resets by position, not by the re-run matrix; check what it clears.
- Any new extractor over chapter HTML handles `span.nb` before the generic tag
  rule (the phantom-space defect, found in three tools).

## Operational reminders

- **Remote branch deletion fails from the container (HTTP 403), every time.**
  Do not retry. Delete the local branch, give Dan the one-liner, then
  `git fetch --prune`.
- A local `main` can be stale in a way `origin/main` checks miss. Check
  `git branch -r --contains main` before resetting it.
- WebSearch works; WebFetch and curl do not reach source hosts.
- Dates in records come from the commit clock, not from memory.
- Read CI on the current head, not the topmost completed run.
- A locked chapter changes only through `amend.py`.
