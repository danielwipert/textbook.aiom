# Session handoff

Last updated: 2026-08-05. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session.

## Repository state

Active working branch: `claude/prose-voice-style-gxjkgj`. The previous branch,
`claude/handoff-markdown-workflow-p3ce5c`, is fully merged into `main` and is
done. This session's voice and craft work is committed and pushed to the new
branch. `main` has NOT been fast-forwarded to it: the branch carries one open
ruling (see thread 1), so it is held for Dan rather than merged. Verify state any
time with:

```
git status                         # working tree and branch
git rev-list --left-right --count origin/main...HEAD   # 0 0 means synced
python3 status_check.py            # authoritative lifecycle status per chapter
```

## What now lives in the repo

The whole documented file set is present: the specs (Consolidated, Addendum,
Structure, Exit Competencies, Maturity Model, Case Bank, Northmoor Dataset design,
Workplan v5, Validation Matrix), the design layer (AIOM_book.css v6.7 plus the
audit-only rule, AIOM_DESIGN_SPEC v6.8, AIOM_Design_QA_Spec v1.3, AIOM_build.py
v6.2, place.py, cite_format.py, footnotes.py, voicecheck.py), the voice and craft
standard (`AIOM_Voice_and_Craft_v1.md`, new 2026-08-05), the fonts
(committed under `fonts/`, so rendering needs no network staging), the Northmoor
capstone dataset (`Northmoor/`), the Chapter 1 artifacts under
`Drafts/Ch01_The_Category_Error/`, and `archive/` for superseded and variant
files. The session-handoff workflow is in place: `.claude/settings.json` (the
SessionStart hook) and CLAUDE.md section 11 (the handoff protocol). The Workplan
had a currency sweep 2026-08-02: its live sections now carry Process v2 numbering
and current Chapter 1 state; its dated changelog and decisions log keep their
original v1 numbers.

## Chapter 1 status: REOPENED at Stage 0

Reopened 2026-08-05 on Dan's ruling (Decision 53). `status_check.py` reports
0/13 steps passed, STATUS CONSISTENT. Every step's prior findings are archived
in place in the checklist, marked superseded, not destroyed.

Why: Chapter 1 was drafted before the voice and craft standard existed, so its
prose was never written against C1 through C6, and the Stage 4 craft read found
seven findings. Chapter 1 is the exemplar fourteen further chapters are drafted
against, so it is re-drafted rather than patched. The re-draft is the proving run
for Process v2 end to end.

Carried into the re-draft, recorded as CD1 to CD5 at the end of the checklist:
the production defect gate 14 found (a stranded slot label at the foot of page
12, which the eleven-gate suite passed), the seven craft findings, the nine
verified sources, the rulings that survive a reopen, and what must be done
differently.

## Open threads, in priority order

1. **Chapter 1 Stage 0 re-draft.** The immediate work. Read
   `AIOM_Voice_and_Craft_v1.md` BEFORE drafting; the Stage 0 acknowledgment box
   is a live requirement now. Carry CD1 to CD5. Then run the thirteen steps in
   order.

2. **Remaining process hardening** (Dan approved, still to build):
   - `status_check.py` should verify that CLAUDE.md section 10 and the Workplan
     tracker agree with the checklist table. Those three were hand-mirrored three
     times in two sessions; the check would have caught any drift automatically.
   - Canonical `DECISIONS.md` with a status field per decision. Numbers are
     scattered across three files and now run to 53, with 47/48 flagged
     unverified.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout,
     though gate 11 now checks the panel directly.

3. **Chapter 2 (The Flow)** after the Chapter 1 re-draft has settled the craft
   standard in practice.

4. **Decision 28**, Northmoor properties G, H, I. Gates Ch9, Ch12, Ch13 problem
   sets only.

## Standing reminders

- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4. Craft
  caught at Stage 4 is a rewrite; craft applied at Stage 0 is free. A SessionStart
  hook prints the six-criterion card into context alongside this file.
- `voicecheck.py` now prints advisory craft metrics after the mechanical result,
  PER SECTION as well as per chapter. They are proxies and permanently advisory.
  Do not turn them into thresholds: the trailing-qualifier proxy over-reports,
  flagging four strong causal closes in Chapter 1 as weak. C2 and C6 have no
  proxy at all and are enforced by reading.
- Read Stage 4 ADVERSARIALLY: quote the weakest passage per criterion rather
  than asking whether the criterion is met. The confirmatory version of that
  read produced a false all-clear on Chapter 1. Read the per-section table, not
  the chapter average: the chapter average concealed the summary completely.
- The craft standard was generalized partly from Chapter 1, so it cannot fail
  Chapter 1 on its own. Judge chapters against the named exemplars and the
  criteria as stated, never against how closely prose resembles Chapter 1.
  A reusable second-model verification prompt sits in the Chapter 1 checklist
  under the Stage 4 craft read; Dan runs it, per the Stage 2 precedent.
- Do NOT run `gen_checklists.py` in the repo root without cleaning up after it.
  It writes fifteen fresh checklists to `checklists/`, including a stub Ch01 that
  would fork against the live Chapter 1 checklist under
  `Drafts/Ch01_The_Category_Error/`. Generate to a scratch directory to inspect
  its output.
- A fresh session has neither the Python build deps nor poppler installed. Run
  `pip install -r requirements.txt` (pinned) and `apt-get update -qq && apt-get
  install -y poppler-utils`. The build now REFUSES to start without them and
  exits 2, rather than tracebacking partway through the gates. A gate that did
  not run is not a gate that passed. The 403s from unrelated third-party PPAs
  during that apt-get are harmless.
- The continuity ledger EXISTS as of 2026-08-05: `AIOM_Continuity_Ledger.md`
  plus `continuity.py` (gate G3, seven checks). It holds no entries yet, which
  is correct: entries are appended at Stage 9 by `continuity.py --update` and no
  chapter has locked. The ledger is the authority; never edit it to make a gate
  pass. Registry glosses are written by hand, and the placeholder deliberately
  fails the gate.
- The QA suite is FOURTEEN gates, not eleven. Gates 12 (figures), 13 (bottom
  margin), and 14 (widows, orphans, stranded heads) were added 2026-08-05,
  closing three checks the G2 checklist had claimed for months while
  AIOM_build.py performed none of them. Gate 14 found a real defect on its first
  run. The G2 checklist now mirrors the printed gates one for one.
- Stage folders are on Process v2 numbering across all eighteen units as of
  2026-08-05. Voice is `05_Stage4_Voice_And_Craft_Check`, design is
  `06_Stage5_Design_Review`. Do not trust older paths in dated records.
- To reopen a chapter, use `reopen.py`, never `gen_checklists.py --force`. The
  latter destroys ticks and writes to `checklists/` rather than the chapter
  folder, which would fork a live checklist.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN; do not
  route around policy denials, report them.
- Build the chapter from a repo-root copy: copy the stage HTML
  (`Drafts/Ch01_The_Category_Error/06_Stage5_Design_Review/AIOM_Ch01_Stage4_FINAL.html`)
  to repo root, run `python3 AIOM_build.py <copy>.html --out
  <stage>/AIOM_Ch01_Stage4.pdf`, then remove the copy. Rasterize pages for visual
  review with `pdftoppm -png -r 150`.
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  do not write chapter prose to markdown and never fork a chapter into a second
  live text.
- Develop on `claude/prose-voice-style-gxjkgj`. Fast-forward `main` to match once
  thread 1 is ruled and `status_check.py` is clean, not before.
