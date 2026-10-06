# Session handoff

Last updated: 2026-10-06. **One page, current state only (Decision 80).** The
protocol is CLAUDE.md section 13. The full history to this date is
`archive/HANDOFF_history_to_2026-09-30.md`: read it for the story of a specific
finding, never for the current state. Keep this file under 150 lines; a durable
rule goes to CLAUDE.md, a lesson to LESSONS.md, and a closed item is deleted.

## Repository state

- Working branch `claude/happy-bardeen-hhct43` (this session; carries the Chapter 3
  sitting 2b work); earlier branch `claude/inspiring-bohr-4gquw9`; `main` fast-forwarded to it on
  2026-10-01 at `5d0fd66` (Process v4 adoption and tooling are on `main`). Later
  commits on the branch carry Chapter 3 work.
- Chapter 1 LOCKED (Process v2). Chapter 2 LOCKED (Process v3). Both live.
  **Chapter 3 (Process v4): Stage 4 passed 2026-10-06; author pass next.** Chapters 4 to 15 not started.
- Run `python3 git_hygiene.py` before merging and before closing.

## Process v4, adopted 2026-09-30

Seven steps, four sittings for Dan: plan approval, review rulings, fact-check
rulings, sign-off, plus his author pass in Word. Evidence and reasoning are in
`AIOM_Process_v4_Proposal_v1.0.md`; rulings in `AIOM_Workplan_v5.md`. The v4
checklist keeps v3 step LABELS so the tools bind unchanged; see its preamble.

## Next actions, in order

1. DONE: registry attached (`/home/user/dag.aiom`, never committed here); the
   four gaps filled; Stage 0 passed; G1 open only on the word band.
2. DONE: Stage 4 closed 2026-10-06. Three external reviews (second model, two
   Sonnet passes) merged into sitting 2b; Dan accepted all; applied in one commit.
   **NEXT: Dan's author pass** on
   `03_Stage6_Author_Pass/AIOM_Ch03_author_pass.docx` (round trip verified at zero
   changes). Then `copyedit_import.py`, the mechanical checks, `freqsweep.py`, and
   the fact-check package (one file, Dan's rule) for a checker with web access.
3. DONE: `copyedit_import.py` now refuses a split paragraph instead of deleting
   its second half (fixed 2026-10-01 under the blocking exception).

## Waiting on Dan

- **Chapter 3:** the author pass: edit the .docx in Word, save it as
  `AIOM_Ch03_author_pass_DAN_EDIT.docx` in the same folder, and say so.
- **Open question, not urgent:** the THM-004 gloss "Diligence from the people running
  the deployment is no longer enough" (fixed by locked Ch2, checked by G3) was
  flagged by a reviewer as going beyond the theorem. Removing it is a Ch2 amendment
  plus a ledger update. Keep or amend?
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
- The THM-004 trace set piece is generable from the registry's edges. THM-004,
  THM-008 and THM-002 are certified.
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

- **`prose_extract.py` drops tables** (found 2026-10-06): Ch3 Table 3.1 never reached
  the second-model reviewer, who then reported it empty (S-2). Patched into the Ch3
  package by hand; fix the extractor and check the Ch1 exemplar for the same loss.

- Manual page reads are stale for Chapter 1 (since 2026-08-14) and Chapter 2
  (since the 2026-10-01 THM-004 amendment; its panel page WAS read).
- `voicecheck.py` Part 5 rule 1 proxy counts fronted adverbials; do not quote it.
- `place.py` leaves a `.bak` beside the chapter; delete it after every run.
- Gate 4 does not guard the theorem callout; gaps G-I and G-II still open.
- `reopen.py` resets by position, not by the re-run matrix; check what it clears.
- Self-test controls that name which chapters exist break when one locks; expect
  it at Chapter 3's lock and prefer derived expectations.
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
