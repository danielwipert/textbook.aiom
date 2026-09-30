# Session handoff

Last updated: 2026-09-30. **One page, current state only (Decision 80).** The
protocol is CLAUDE.md section 11. The full history to this date is
`archive/HANDOFF_history_to_2026-09-30.md`: read it for the story of a specific
finding, never for the current state. Keep this file under 150 lines; a durable
rule goes to CLAUDE.md, a lesson to LESSONS.md, and a closed item is deleted.

## Repository state

- Working branch `claude/inspiring-bohr-4gquw9`, pushed, 10+ commits ahead of
  `main` (`1af304d`), nothing behind. **Not yet merged.** It carries the Process
  v4 adoption (Decisions 75 to 81) and its tooling.
- Chapter 1 LOCKED (Process v2). Chapter 2 LOCKED (Process v3). Both live.
  Chapters 3 to 15 not started. `chapter_check.py --all` green on 2026-09-30.
- Run `python3 git_hygiene.py` before merging and before closing.

## Process v4, adopted 2026-09-30

Seven steps, four sittings for Dan: plan approval, review rulings, fact-check
rulings, sign-off, plus his author pass in Word. Evidence and reasoning are in
`AIOM_Process_v4_Proposal_v1.0.md`; rulings in `AIOM_Workplan_v5.md`. The v4
checklist keeps v3 step LABELS so the tools bind unchanged; see its preamble.

## Next actions, in order

1. DONE: tooling (`gen_checklists.py` v4, `freqsweep.py`, folder migration,
   session-start card, `voicecheck.py` label). Commit `c11377d`.
2. DONE: this file cut to one page.
3. **NEXT: CLAUDE.md rewrite** to the rules only, target under 400 lines, with
   the narratives moved to a new `LESSONS.md`. **Dan reviews the draft and a
   table of where every rule went BEFORE it is committed.** Fold in: Decisions
   run to 81 (it says 66); the process section rewritten for v4; the note that no
   source host is reachable is true of Claude's container, not of an external
   checker (old H3). Also refresh the stale Workplan tracker (it shows Chapter 1
   at 9 of 13 and Chapter 2 not started).
4. **Chapter 3 setup:** `python3 gen_checklists.py 3`, then the one-page plan in
   `00_Stage0_Draft/` for Dan's sitting 1.
5. Merge the branch to `main` once items 3 and 4 are committed.

## Waiting on Dan

- The CLAUDE.md draft review (item 3), once presented.
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

Nothing is in flight, so these may be worked now. During a chapter, add here,
one line each, and fix only what blocks.

- **`copyedit_import.py` drops untagged continuation paragraphs.** Fix BEFORE
  Chapter 3's author pass, which now carries Dan's whole rewrite.
- Chapter 1's manual page read is stale since its 2026-08-14 amendment (old H2).
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
