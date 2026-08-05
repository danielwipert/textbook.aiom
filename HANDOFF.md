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

## Chapter 1 status: 3 of 13, re-drafted and through Stage 1

Reopened at Stage 0 on 2026-08-05 (Decision 53), re-drafted the same day against
the craft standard. Passed since: Stage 0, G1, Stage 1, all 2026-08-05.
`status_check.py` reports 3/13, STATUS CONSISTENT. The live text is
`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`, 5,949
words, and it supersedes the old Stage 4 render.

G1 caught a real breach: the re-draft had put the published QJE agent count
5,172 into prose, where a 2026-07-29 ruling reserves it for Chapter 6 and
requires "on the order of five thousand" in Chapter 1. Fixed. The fuller ruling
lives in the chapter's own Decision 51 register, NOT in the shorter
`AIOM_Source_Ledger.md` note.

Stage 1 raised seven structural findings, all ruled by Dan (Decision 55). Only
one changed an artifact: the case bank held no CASE 4.6 (GitHub Copilot) and no
CASE 6.4 (QJE contact center) although the spec assigned both to Chapter 1, and
both are now written into `AIOM_Case_Bank_v1.md` from already-cleared sources.
Four rulings amended the Consolidated Spec's Ch1 outline instead of the chapter
(figure numbering, the case close, a fourth discussion question, P2 need not
cite). Two confirmed the chapter as drafted (FinOps stays out of Ch1; the
agent-count ruling stands). NOT ONE WORD OF THE CHAPTER CHANGED at Stage 1, so
no downstream step was invalidated.

Carried items CD1 to CD5 remain live in the checklist. CD1, the gate-14 stranded
"Craft section" slot label at the foot of page 12, is Stage 5 work.

## Open threads, in priority order

1. **Chapter 1 Stage 3, source and fact check 1. DAN'S STEP.** 4/13 passed:
   Stage 0, G1, Stage 1, Stage 2, all 2026-08-05. Stage 2 findings ND1 to ND4
   were ruled and applied; ND5 and ND6 closed with no action. Chapter is 5,961
   words, 39 of headroom.

   Stage 3 note: no claim, citation, figure, or slot changed at Stage 1 or Stage
   2, so the fact surface is unchanged since the re-draft. Dan may rule this a
   confirmation rather than a full re-check, as he did on 2026-08-01 for the same
   class of edit.

   AFTER STAGE 3: Stage 4 voice and craft (Claude, read ADVERSARIALLY and BY
   SECTION, second-model check per the prompt in the checklist), then Stage 5
   design, which owns three carried layout items, then G2.

   STAGE 5 INHERITS CD1, CD6, CD7, all recorded in the checklist:
   CD1, the "Craft section" slot label stranded at the foot of page 12.
   CD6, one definition callout split across a page break, caused by ND1. Remedy
   is `place.py`, never CSS: WeasyPrint 69 ignores break-inside on floats.
   CD7, a widow and an orphan on page 16, pre-existing and verified as such
   against the pre-ND1 render.

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
- Source register notes inside a chapter's own Decision 51 block can carry
  rulings that AIOM_Source_Ledger.md's summary does not. G1 found one this way.
  Read the in-chapter note before using a figure from a cited study.
- The continuity ledger EXISTS as of 2026-08-05: `AIOM_Continuity_Ledger.md`
  plus `continuity.py` (gate G3, seven checks). It holds no entries yet, which
  is correct: entries are appended at Stage 9 by `continuity.py --update` and no
  chapter has locked. The ledger is the authority; never edit it to make a gate
  pass. Registry glosses are written by hand, and the placeholder deliberately
  fails the gate.
- THE DESIGN MIRRORS ITS MARGINS: the main text column starts at x0 68.4 on
  odd pages and 57.6 on even. Gates 12 and 14 originally hard-coded a single
  left edge and were silently blind on half the book; fixed 2026-08-05 to derive
  the edge per page. Any new geometry check must do the same or it will read
  green while measuring nothing.
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
