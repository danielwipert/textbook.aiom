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

## Chapter 1 status (Process v2 numbering)

Through the production gate: 8 of 13 steps passed. Passed: Stage 0 draft, G1,
Stage 1 content review, Stage 2 developmental edit, Stage 3 source and fact check
1, Stage 4 voice, Stage 5 design, G2 (all eleven automated gates green on the
19-page render). Stage 4 now reports INCONSISTENT in `status_check.py`, by design
and pending one ruling: see thread 1. Stage 2 completed 2026-08-01: all six developmental findings
ruled. D1 (1.4 signpost and tighten) and D5 (theorem aside tightened) were
applied, and their Stage 4, Stage 5, and G2 re-runs are green; D2, D3, D4, and D6
closed with no action. No empirical claim changed, so the Stage 3 fact surface
held (Dan ruled it a pass for that class of edit). Remaining to Lock: Stage 6
copy edit, Stage 7 final fact check 2, G3 continuity, Stage 8 final read, Stage 9
lock. Dan's final visual sign-off on the rendered pages is still open.

## Open threads, in priority order

1. **RULING OPEN: does Chapter 1 adopt the craft standard, or is it
   grandfathered?** This is the one thing blocking a clean `status_check.py`, and
   it is a one-line edit either way. The voice and craft standard was adopted
   2026-08-05 (Decision 52), after Chapter 1's Stage 4 had already passed. Its six
   criteria are now sub-checkboxes under Stage 4 and are recorded OPEN, so the
   gate correctly reports a step marked passed with unaddressed sub-items. The
   craft read has been run against `AIOM_Ch01_Stage4_FINAL.html` and Chapter 1
   meets all six criteria as drafted, with NO prose change required, so adoption
   is free. Adopt: tick the six boxes in the Chapter 1 checklist. Grandfather:
   mark the six with a stated "postdates" exception, as Stage 0 in that file
   already is. Chapter 1's Stage 4 metrics are the baseline band for Chapters 2
   through 15, so adopting is the recommendation.

2. **Chapter 1 to Lock, Dan's remaining passes.** With the developmental edit
   done, the front is Dan's external work: Stage 6 copy edit, Stage 7 final fact
   check 2, and Stage 8 final read, with G3 (continuity gate, Claude-owned)
   between and Stage 9 lock last. Dan's final visual sign-off on the 19-page
   render is also still open. Stages 6 through 8 may run in one sitting.

3. **Process-hardening items still to build** (Dan approved these):
   - Item 4: close the automated-gate holes (figure validation, widow and orphan
     detection, bottom-margin check) in AIOM_build.py, and finish the hermetic
     build. Fonts are done, but a fresh session confirmed that the Python build
     deps and poppler are NOT pre-installed (see standing reminders); pinned deps
     and a graceful bootstrap are still wanted, plus a fix so a chapter builds
     from its own stage folder without the CSS-adjacency wrinkle.
   - Item 5: decision-log hygiene. Needs the master decision log; the numbers are
     scattered (Addendum 1 to 21, Workplan 24 to 48, Ch1 checklist 36 to 51) and
     the 47/48 numbering is flagged unverified. Assemble a canonical DECISIONS.md
     with a status field per decision (active / repealed-by / superseded-by), then
     have status_check verify references resolve.
   - Item 1 extension: teach status_check to flag when CLAUDE.md section 10 and the
     Workplan disagree with the checklist table, and wire it in as a pre-flight.
     (This session mirrored those three by hand after marking Stage 2 done; the
     check would have caught the drift automatically.)
   - Item 6 (scoped re-run matrix) and the developmental stage are DONE in
     CLAUDE.md section 8.

4. **Chapter 2 (The Flow)** is the next drafting target and is unblocked. It is
   the first chapter drafted under the craft standard: read
   `AIOM_Voice_and_Craft_v1.md` BEFORE drafting, not after. Its Stage 0
   acknowledgment box is a live requirement, unlike Chapter 1's.

## Standing reminders

- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4. Craft
  caught at Stage 4 is a rewrite; craft applied at Stage 0 is free. A SessionStart
  hook prints the six-criterion card into context alongside this file.
- `voicecheck.py` now prints advisory craft metrics after the mechanical result.
  They are proxies and permanently advisory. Do not turn them into thresholds:
  C5 in particular over-reports, flagging four strong causal closes in Chapter 1
  as weak. C2 and C6 have no proxy at all and are enforced by reading.
- Do NOT run `gen_checklists.py` in the repo root without cleaning up after it.
  It writes fifteen fresh checklists to `checklists/`, including a stub Ch01 that
  would fork against the live Chapter 1 checklist under
  `Drafts/Ch01_The_Category_Error/`. Generate to a scratch directory to inspect
  its output.
- A fresh session has neither the Python build deps nor poppler installed. Before
  building, run `pip install weasyprint pdfplumber pdf2image pillow openpyxl
  fonttools` and `apt-get update -qq && apt-get install -y poppler-utils`
  (poppler is gate 9). The 403s from unrelated third-party PPAs during that
  apt-get are harmless.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN; do not
  route around policy denials, report them.
- Build the chapter from a repo-root copy: copy the stage HTML
  (`Drafts/Ch01_The_Category_Error/05_Stage4_Design_Review/AIOM_Ch01_Stage4_FINAL.html`)
  to repo root, run `python3 AIOM_build.py <copy>.html --out
  <stage>/AIOM_Ch01_Stage4.pdf`, then remove the copy. Rasterize pages for visual
  review with `pdftoppm -png -r 150`.
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  do not write chapter prose to markdown and never fork a chapter into a second
  live text.
- Develop on `claude/prose-voice-style-gxjkgj`. Fast-forward `main` to match once
  thread 1 is ruled and `status_check.py` is clean, not before.
