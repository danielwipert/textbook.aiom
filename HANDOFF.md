# Session handoff

Last updated: 2026-08-02. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session.

## Repository state

Active working branch: `claude/handoff-markdown-workflow-p3ce5c`. As of this
update `origin/main` is fast-forwarded to the same commit as this branch, so the
two are synced and `main` reflects the full body of work. Keep them that way:
when this branch advances, fast-forward `main` to match before ending the
session. Verify state any time with:

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
v6.2, place.py, cite_format.py, footnotes.py, voicecheck.py), the fonts
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
19-page render). Stage 2 completed 2026-08-01: all six developmental findings
ruled. D1 (1.4 signpost and tighten) and D5 (theorem aside tightened) were
applied, and their Stage 4, Stage 5, and G2 re-runs are green; D2, D3, D4, and D6
closed with no action. No empirical claim changed, so the Stage 3 fact surface
held (Dan ruled it a pass for that class of edit). Remaining to Lock: Stage 6
copy edit, Stage 7 final fact check 2, G3 continuity, Stage 8 final read, Stage 9
lock. Dan's final visual sign-off on the rendered pages is still open.

## Open threads, in priority order

1. **Chapter 1 to Lock, Dan's remaining passes.** With the developmental edit
   done, the front is Dan's external work: Stage 6 copy edit, Stage 7 final fact
   check 2, and Stage 8 final read, with G3 (continuity gate, Claude-owned)
   between and Stage 9 lock last. Dan's final visual sign-off on the 19-page
   render is also still open. Stages 6 through 8 may run in one sitting.

2. **Process-hardening items still to build** (Dan approved these):
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

3. **Chapter 2 (The Flow)** is the next drafting target and is unblocked.

## Standing reminders

- No em dashes anywhere, including commit messages. A build gate enforces it.
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
- Develop on `claude/handoff-markdown-workflow-p3ce5c`, then fast-forward `main`
  to match before ending the session so `main` stays current.
