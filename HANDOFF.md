# Session handoff

Last updated: 2026-08-01. Read this plus CLAUDE.md before starting work, and
update this file before ending the session. The protocol is CLAUDE.md section 11.
A SessionStart hook (`.claude/settings.json`) prints this file into context
automatically at the start of every session.

## Repository state

Active working branch: `claude/handoff-markdown-workflow-p3ce5c`. All manuscript
and tooling work lives here; the branch is 26 commits ahead of `origin/main`,
which still holds only the initial CLAUDE.md commit. `main` is not a mirror of
the work, so do not treat it as synced. Verify state any time with:

```
git status                         # working tree and branch
git rev-list --left-right --count origin/main...HEAD   # how far ahead of main
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
files. New this session: `.claude/settings.json` (the SessionStart hook) and
CLAUDE.md section 11 (the handoff protocol).

## Chapter 1 status (Process v2 numbering)

Through the production gate: 7 of 13 steps passed. Passed: Stage 0 draft, G1,
Stage 1 content review, Stage 3 source and fact check 1, Stage 4 voice, Stage 5
design, G2 (all eleven automated gates green on the 19-page render). Stage 2
developmental edit is in-progress (see thread 1). Remaining to Lock: Stage 6 copy
edit, Stage 7 final fact check 2, G3 continuity, Stage 8 final read, Stage 9
lock. Dan's final visual sign-off on the rendered pages is still open.

## Open threads, in priority order

1. **Chapter 1 developmental pass awaits Dan's ruling.** Claude ran it 2026-08-01;
   findings D1 to D6 are recorded in the Chapter 1 checklist under Stage 2, not
   applied. D1 (Section 1.4 carries too many moves) and D2 (the seat-versus-event
   figure lands late) are the two that most affect teaching quality. Dan
   gut-checks with a second model and rules which to action; each approved edit
   re-runs only its downstream steps per the scoped re-run matrix in CLAUDE.md
   section 8.

2. **Process-hardening items still to build** (Dan approved these):
   - Item 4: close the automated-gate holes (figure validation, widow and orphan
     detection, bottom-margin check) in AIOM_build.py, and finish the hermetic
     build (fonts done; still want pinned deps, graceful poppler, and a fix so a
     chapter builds from its own stage folder without the CSS-adjacency wrinkle).
   - Item 5: decision-log hygiene. Needs the master decision log; the numbers are
     scattered (Addendum 1 to 21, Workplan 24 to 48, Ch1 checklist 36 to 51) and
     the 47/48 numbering is flagged unverified. Assemble a canonical DECISIONS.md
     with a status field per decision (active / repealed-by / superseded-by), then
     have status_check verify references resolve.
   - Item 1 extension: teach status_check to flag when CLAUDE.md section 10 and the
     Workplan disagree with the checklist table, and wire it in as a pre-flight.
   - Item 6 (scoped re-run matrix) and the developmental stage are DONE in
     CLAUDE.md section 8.

3. **Chapter 2 (The Flow)** is the next drafting target and is unblocked.

## Standing reminders

- No em dashes anywhere, including commit messages. A build gate enforces it.
- Fonts are committed; do not run `AIOM_build.py --fonts`. Poppler (gate 9) needs
  installing per session: `apt-get update -qq && apt-get install -y poppler-utils`.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN; do not
  route around policy denials, report them.
- Build Chapter 1 from a clean checkout: copy the stage HTML to repo root, run
  `python3 AIOM_build.py <copy>.html --out <stage>/AIOM_Ch01_Stage4.pdf`, remove
  the copy. Rasterize pages with `pdftoppm -png -r 150`.
- Develop on `claude/handoff-markdown-workflow-p3ce5c`. Do not assume `main` is
  up to date; it trails the working branch.
