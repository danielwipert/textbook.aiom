# Session handoff

Last updated: 2026-08-06. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session, alongside the voice and craft card.

## Repository state

Active working branch: `claude/chapter-1-progress-fq0brc`, new on 2026-08-06 and
replacing `claude/prose-voice-style-gxjkgj`, which is fully merged into `main` and
is finished. Working tree clean, and the branch is pushed to origin.

**`main` is one commit behind as of 2026-08-06.** It carries everything through
the 2026-08-05 merge: the voice and craft standard, the re-run process, the
continuity ledger, and Chapter 1 through Stage 2. It does not yet carry the
2026-08-06 Stage 3 input render. `main` has no commits of its own, so a
fast-forward still reconciles cleanly.

Keep them synced. When this branch advances, fast-forward `main` again before
ending the session.

Verify state any time with:

```
git status                                              # working tree
git rev-list --left-right --count origin/main...HEAD    # main behind / ahead
python3 status_check.py                                 # authoritative status
```

The 2026-08-06 session, in full: Chapter 1 status confirmed at 4/13, the Stage 2
text rendered as the Stage 3 fact-check input and committed, and CLAUDE.md
section 10 plus this file brought back into line with the checklist. No chapter
text changed, so no step was invalidated and the status is unmoved.

The 2026-08-05 session, oldest first: the voice and craft standard (Decision 52);
the craft-check hardening after the first read failed as verification; the re-run
process plus the reopen of Chapter 1 (Decision 53); the continuity ledger
(Decision 54); the Chapter 1 Stage 0 re-draft; G1; Stage 1 (Decision 55); the
Stage 2 pass; and the Stage 2 rulings applied.

## What now lives in the repo

**Specs and standards.** Consolidated Spec (amended 2026-08-05 at Ch1 Stage 1,
each amendment marked with its date and reason), Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank (now carrying CASE 4.6 and CASE 6.4),
Northmoor Dataset design, Workplan v5, Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` (new 2026-08-05, at v1.1).

**Build and design.** `AIOM_book.css` v6.7 plus the audit-only rule,
`AIOM_DESIGN_SPEC` v6.8, `AIOM_Design_QA_Spec` (updated 2026-08-05 to the
fourteen-gate suite), `AIOM_build.py` (fourteen gates plus a toolchain
preflight), `place.py`, `cite_format.py`, `footnotes.py`, and pinned
`requirements.txt`.

**Process tooling.** `status_check.py` (lifecycle status, authoritative),
`gen_checklists.py`, `voicecheck.py` (mechanical bans plus per-section craft
metrics), `reopen.py` (new), `continuity.py` (new, gate G3),
`AIOM_Continuity_Ledger.md` (new), and `renumber_stage_folders.py` (new,
one-time, already run).

**Content.** Fonts committed under `fonts/`, the Northmoor dataset under
`Northmoor/`, Chapter 1 artifacts under `Drafts/Ch01_The_Category_Error/`, and
`archive/` for superseded files.

## Chapter 1 status: 4 of 13, through Stage 2

Reopened at Stage 0 on 2026-08-05 (Decision 53) and re-drafted the same day
against the craft standard. Passed: Stage 0, G1, Stage 1, Stage 2, all
2026-08-05. `status_check.py` reports 4/13, STATUS CONSISTENT.

**The live text is
`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`**, 5,961
words against a 6,000 ceiling, 39 words of headroom. It supersedes the old Stage
4 render, which is history.

What each step produced:

- **G1** caught a real breach. The re-draft had put the published QJE agent count
  5,172 into prose, where a 2026-07-29 ruling reserves it for Chapter 6 and
  requires "on the order of five thousand" in Chapter 1. Fixed. The fuller ruling
  lives in the chapter's own Decision 51 register, NOT in the shorter
  `AIOM_Source_Ledger.md` note.
- **Stage 1** raised seven structural findings, all ruled (Decision 55). One
  changed an artifact: the case bank held no CASE 4.6 and no CASE 6.4 although
  the spec assigned both to Chapter 1, and both are now written in from
  already-cleared sources. Four amended the spec rather than the chapter. Two
  confirmed the chapter. Not one word of the chapter changed.
- **Stage 2** raised six findings. ND1 to ND4 were ruled and applied; ND5 and ND6
  closed with no action. Applying ND1 exposed a latent defect in gates 12 and 14,
  now fixed (see standing reminders).

Carried items CD1 to CD7 are live in the checklist. CD1, CD6, and CD7 are Stage 5
work and are listed under thread 1 below.

## Open threads, in priority order

1. **Chapter 1 Stage 3, source and fact check 1. DAN'S STEP. Input delivered
   2026-08-06, awaiting Dan's read.**

   The input is
   `Drafts/Ch01_The_Category_Error/04_Stage3_Source_Fact_Check_1/AIOM_Ch1_Stage3_FactCheck_Input.pdf`,
   twenty pages, rendered from the live text after the Stage 2 rulings and
   committed. Twelve of the fourteen gates pass on it; the two that fail are
   gate 4 and gate 14, which are CD1, CD6, and CD7 below, all Stage 5 work and
   deliberately not fixed out of order. Six footnotes generate, all six landing
   on their calling page. The fact check itself runs against the chapter's own
   inline source register in the HTML, which carries the per-source rulings.

   No claim, citation, figure, or slot has changed since the re-draft cleared G1,
   so the fact surface is unchanged. Dan may rule this a confirmation rather than
   a full re-check, as he did on 2026-08-01 for the same class of edit.

   After Stage 3: **Stage 4** voice and craft (Claude; read ADVERSARIALLY and BY
   SECTION, with the second-model check per the prompt in the checklist), then
   **Stage 5** design, then **G2**, then Dan's Stages 6 to 8, then **G3** and lock.

   **Stage 5 inherits three layout items**, all recorded in the checklist:
   - **CD1**, the "Craft section" slot label stranded at the foot of page 12.
   - **CD6**, one definition callout split across a page break, caused by
     applying ND1. Remedy is `place.py`, never CSS: WeasyPrint 69 ignores
     `break-inside` on floated elements.
   - **CD7**, a widow and an orphan on page 16. Pre-existing, and verified as
     such by running the corrected gate 14 against the pre-ND1 render.

   **An obligation booked for Stage 9, easy to lose:** when Chapter 1 locks,
   `continuity.py --update` must NOT record "flow" among the terms Chapter 1
   owns. Chapter 2 owns it. Left unchecked, Chapter 2's proper definition
   registers as a redefinition and G3 fails Chapter 2 for a mis-logged ledger
   entry. This is ND6, closed with no chapter change but with this obligation.

2. **Remaining process hardening** (Dan approved, still to build):
   - `status_check.py` should verify that CLAUDE.md section 10 and the Workplan
     tracker agree with the checklist table. Those three have now been
     hand-mirrored across several sessions; the check would catch drift
     automatically.
   - Canonical `DECISIONS.md` with a status field per decision. Numbers are
     scattered across three files and now run to 55, with 47/48 flagged
     unverified.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout,
     though gate 11 now checks the panel directly.

3. **Chapter 2 (The Flow)** once the Chapter 1 re-draft has settled the craft
   standard in practice. Chapter 2 is the first chapter drafted under the
   standard from the start, so its Stage 0 acknowledgment box is a live
   requirement rather than a retrospective one.

4. **Decision 28**, Northmoor properties G, H, I. Gates the Ch9, Ch12, and Ch13
   problem sets only.

## Standing reminders

**Rules that bite.**

- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4. Craft
  caught at Stage 4 is a rewrite; craft applied at Stage 0 is free. A SessionStart
  hook prints the six-criterion card into context alongside this file.
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  never fork a chapter into a second live text.
- Source register notes inside a chapter's own Decision 51 block can carry
  rulings that `AIOM_Source_Ledger.md`'s summary does not. G1 caught a breach
  this way. Read the in-chapter note before using a figure from a cited study.

**How to read and check.**

- Read Stage 4 ADVERSARIALLY: quote the weakest passage per criterion rather than
  asking whether the criterion is met. The confirmatory version produced a false
  all-clear on Chapter 1. Read the per-section table, never the chapter average
  alone: the average concealed a summary running at twice the chapter's mean
  sentence length, and later concealed a section regression during the re-draft.
- The craft standard was generalized partly from Chapter 1, so it cannot fail
  Chapter 1 on its own. Judge against the named exemplars and the criteria as
  stated. A reusable second-model prompt sits in the Chapter 1 checklist under
  Stage 4, and another under Stage 2.
- `voicecheck.py` craft metrics are proxies and permanently advisory. Do not turn
  them into thresholds: the trailing-qualifier proxy over-reports, flagging three
  strong causal closes in Chapter 1 as weak. C2 and C6 have no proxy at all.

**Tooling facts learned the hard way.**

- **THE DESIGN MIRRORS ITS MARGINS.** The main text column starts at x0 68.4 on
  odd pages and 57.6 on even. Gates 12 and 14 originally hard-coded a single left
  edge and were silently blind on half the book; fixed 2026-08-05 to derive the
  edge per page. Any new geometry check must do the same or it will read green
  while measuring nothing.
- The QA suite is FOURTEEN gates, not eleven. Gates 12, 13, and 14 were added
  2026-08-05, closing three checks the G2 checklist had claimed for months while
  `AIOM_build.py` performed none of them. The G2 checklist now mirrors the printed
  gates one for one, with the two genuinely manual checks labelled MANUAL.
- Three checks in this chapter's re-run were wrong in a way that read as green.
  Every one was a check written in this repo, and every one surfaced by changing
  the input rather than by re-reading the code. Treat a green gate on unchanged
  input as weak evidence.
- A fresh session has neither the Python build deps nor poppler. Run `pip install
  -r requirements.txt` (pinned) and `apt-get update -qq && apt-get install -y
  poppler-utils`. The build REFUSES to start without them and exits 2. A gate that
  did not run is not a gate that passed. The 403s from unrelated third-party PPAs
  during that apt-get are harmless.
- The continuity ledger exists: `AIOM_Continuity_Ledger.md` plus `continuity.py`
  (G3, seven checks). It holds no entries, which is correct: entries append at
  Stage 9 and no chapter has locked. The ledger is the authority; never edit it to
  make a gate pass. Registry glosses are written by hand, and the placeholder
  deliberately fails the gate.
- To reopen a chapter use `reopen.py`, never `gen_checklists.py --force`. The
  latter destroys ticks and writes to `checklists/` rather than the chapter
  folder, which would fork a live checklist. Do not run `gen_checklists.py` in the
  repo root without cleaning up after it; generate to a scratch directory.
- Stage folders are on Process v2 numbering across all eighteen units. Voice is
  `05_Stage4_Voice_And_Craft_Check`, design is `06_Stage5_Design_Review`. Do not
  trust older paths in dated records.
- Build from a repo-root copy: copy the LIVE text
  (`Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`) to
  repo root, run `python3 AIOM_build.py <copy>.html --out <target>.pdf`, then
  remove the copy. Rasterize for visual review with `pdftoppm -png -r 150`.
  Building in place instead of from a root copy does not merely misrender, it
  renders a chapter that is not the book: the CSS link and the fonts resolve
  against the HTML's own directory, so the whole design system drops out and the
  gates report dozens of false defects (no folios, no running heads, DejaVu
  fallback faces, no provenance line). Two side effects to clean up after a build:
  `AIOM_build.py` writes `<name>.print.html` next to its input, and `.gitignore`
  only covers that file when the name begins with an underscore. Name the root
  copy `_ch01_build.html` and both files fall under the ignore rule.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN; do not
  route around policy denials, report them.
- Develop on `claude/chapter-1-progress-fq0brc`, then fast-forward `main` to match
  before ending the session. Do not push to any other branch without Dan's
  explicit say-so. The previous branch, `claude/prose-voice-style-gxjkgj`, is
  merged and finished; do not add to it.
