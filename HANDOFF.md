# Session handoff

Last updated: 2026-08-09, session close. Read this plus CLAUDE.md before starting
work, and update this file before ending the session. The protocol is CLAUDE.md
section 11. A SessionStart hook (`.claude/settings.json`) prints this file into
context automatically at the start of every session, alongside the voice and
craft card.

## Repository state

Active working branch: `claude/chapter-1-progress-78opym`, new on 2026-08-09.
It replaces `claude/stage-6-craft-section-r1q9tj`, which is finished; do not add
to it.

**`main` was merged up to this branch at the close of the 2026-08-09 session, on
Dan's ruling.** Every merge so far has been a clean fast-forward, because `main`
carries no commits of its own. A specific SHA is deliberately not recorded here:
it goes stale on the next commit.

**A correction to the previous entry, worth reading before trusting any handoff
claim about sync state.** The 2026-08-08 entry said `main` had been
fast-forwarded at that session's close. It had not. `origin/main` was still at
`2090bcf` when the 2026-08-09 session opened, twenty-eight commits behind, missing
the entire copy-edit session including CSS v7.0. The claim was written and never
checked. Check it, do not copy it forward:

```
git status                                              # working tree
git rev-list --left-right --count origin/main...HEAD    # main behind / ahead
python3 status_check.py                                 # authoritative status
```

## Chapter 1 status: 4 of 13, Stage 2 complete, all fourteen gates pass

25 pages, 7,034 words, `voicecheck.py` mechanically clean, `status_check.py`
reports 4/13 STATUS CONSISTENT.

The number is low because of the 2026-08-08 reopen at Stage 2, not because the
chapter is weak. Every step from Stage 3 forward was reset then, and those passes
had been made against prose the copy edit replaced.

**Stage 3, the source and fact check, is next. It is Dan's and it is structurally
external:** no source host is reachable from a Claude session. Run two checks on
different prompts rather than one thorough check; the 2026-08-06 pair agreed on
one finding out of six and the disagreement was the value.

### What the 2026-08-09 session did

Ran the Stage 2 re-run end to end. Nine findings raised, nine ruled by Dan one at
a time, seven applied to the chapter. Full record with reasoning and verification
is under Stage 2 in `AIOM_Ch01_Checklist_v6.md`.

  DE1  the resource consumption model is now named in the teaching body, in 1.2,
       instead of first appearing in the summary
  DE2  the bridge from the five questions to the three failures, restored. It was
       D1 EDIT 3, ruled 2026-08-01, silently lost in the re-draft and copy edit
  DE3  duplicate causal sentence cut from the opening case
  DE4  theorem antecedent (iv) glossed, so all four are now in plain English
  DE5  the chapter hands off to Chapter 2 once, in the summary, not twice
  DE6  Decision 33 amended to 6,500 to 7,500 with the measure named
  DE7  the Microsoft paragraph names its own date anchor
  DE8  the four-activity clause cut from the consumption-event paragraph
  DE9  theorem panel untouched, gloss split in two, restating paragraph cut

Chapter 7,102 to 7,034 words, 25 pages throughout, all fourteen gates green at
every step.

**Stage 2 was closed with its second-model gut-check still open**, on Dan's
ruling and on the precedent of the archived pass. The tick means the step ran and
every finding was ruled. It does not mean independent verification happened. The
prompt is in the checklist; a stall it finds enters as DE10 and reopens Stage 2.

### Three outputs of that session that are not chapter edits

1. **Gate 12 had a second silent defect and it is fixed.** It counted in-text
   figure references LINE BY LINE, so a reference that wrapped was invisible.
   Applying DE1 moved a line break and the gate failed a chapter whose prose
   names the figure in the sentence beside it. It also dropped any body-size line
   OPENING with a figure label, counting it as neither caption nor reference.
   References are now counted on the joined page text with captions subtracted
   one for one. A NEGATIVE TEST WAS RUN and the fixed gate still fails when the
   reference is genuinely absent.
2. **Standing rule 4a in CLAUDE.md**, from Dan's ruling at DE9: the registry is
   the third rail, and the book is an interpretation of it. A panel rendering a
   registry object is never paraphrased into plainer words. When a statement
   reads as technical, the remedy is the prose beside it, never the statement.
3. **Decision 33 is computable.** It named a band and no measure, and Chapter 1
   produced four defensible counts, two of which put it on opposite sides of the
   band. The measure is now the whole rendered chapter less the source register
   and SVG labels, and `voicecheck.py` prints it as the first craft metric.

### Open observations carried out of Stage 2

- **Page 16 is short by about 1.7 inches** after DE5 pushed the craft-section
  head group to page 17. Read, not gated: the head group is whole and page 16
  ends on a complete paragraph. Carried to Stage 5 as an observation, not booked
  as a defect. Same shape as DR3a.
- **DE7 is flagged for Stage 3.** No figure, date, or source changed, but the
  temporal relation went from vague to explicit, and an explicit claim is
  checkable in a way the vague one was not.
- **A standing practice was proposed and is NOT yet ruled:** when a developmental
  or craft fix is applied, record the SENTENCE it adds, in quotation marks, not
  only the reason. DE2 exists because a ruled fix was silently reverted and
  nothing saw it, and it was recoverable only because D1's archived entry
  happened to quote the sentence. A sentence is greppable; a reason is not.

## What lives in the repo

**Specs and standards.** Consolidated Spec, Addendum, Structure, Exit
Competencies, Maturity Model, Case Bank, Northmoor Dataset design, Workplan v5
(Decision 33 amended 2026-08-09), Validation Matrix, and
`AIOM_Voice_and_Craft_v1.md` at v1.1.

**Build and design.** `AIOM_book.css` v7.0, `AIOM_Design_QA_Spec` (current),
`AIOM_build.py` (fourteen gates plus toolchain preflight, gate 12 fixed
2026-08-09), `place.py`, `cite_format.py`, `footnotes.py`, pinned
`requirements.txt`. **`AIOM_DESIGN_SPEC` is still written to v6.9 and OWES a v7.0
update.**

**Stage 6 round trip.** `copyedit_export.py` and `copyedit_import.py`, plus
`08_Stage6_Copy_Edit/apply_round1.py` as the record of how round 1 was applied
when the importer could not land it. The `.docx` is a proof, never a second live
text (Decision 50).

**Process tooling.** `status_check.py`, `gen_checklists.py`, `voicecheck.py`
(now prints the Decision 33 measure), `reopen.py`, `continuity.py` (G3),
`AIOM_Continuity_Ledger.md`, `typographic_quotes.py`, `renumber_stage_folders.py`.

## Open threads, in priority order

1. **Chapter 1 Stage 3, source and fact check. DAN'S, AND IT IS NEXT.**
   Structurally external. Two checks on different prompts. Judge each proposed
   remedy separately from the finding it answers: a finding can be right and its
   fix still wrong, which happened twice on 2026-08-06.

2. **Then Stage 4, Stage 5, G2, all Claude's.** Two things to carry:

   Into Stage 4, the rhythm finding. The copy edit removed the long tail and also
   removed range: stdev fell from 10.5 to about 6.2 and the prose clusters at 12
   to 18 words. A long run at one length is the other half of what C4 prohibits.
   Watch the longest-uniform-run metric `voicecheck.py` prints. Read
   ADVERSARIALLY, quoting the weakest passage per criterion, and read the
   per-section table, never the chapter average.

   Into Stage 5, the short page 16 above, and a full read. A green gate suite is
   not a read page. Gaps G-I and G-II both require a chapter whose pagination or
   callout placement moves to be READ, and the sharper 2026-08-08 form is that
   the read finds things the gates were never built to see.

3. **Chapter 1 Stages 7 and 8, then G3 and Stage 9.** At lock,
   `continuity.py --update` must NOT record "flow" among Chapter 1's terms.
   Chapter 2 owns it, and a mis-logged entry would fail G3 on Chapter 2.

4. **Remaining process hardening** (Dan approved, still to build):
   - **Teach gate 14 about head GROUPS**, closing gap G-II. Highest value: the
     defect it misses has appeared twice on the same page of the same chapter,
     and the second time the gate reported clean.
   - `status_check.py` should verify CLAUDE.md section 10 and the Workplan
     tracker against the checklist table. All three are hand-mirrored today.
   - Canonical `DECISIONS.md` with a status field. Numbers run to 57 across three
     files, with 47/48 flagged unverified.
   - Gate 4 still keys on `--tint-def` and does not guard the theorem callout.
   - `copyedit_import.py` still drops untagged continuation paragraphs, so a
     split paragraph loses everything after its first line. Unfixed.
   - `place.py` writes a `.bak` beside the chapter, which puts a second chapter
     HTML in the live-text directory and is not gitignored. Delete it after every
     run until the tool is changed.

5. **Chapter 2 (The Flow).** Drafts against the amended band, 6,500 to 7,500, and
   is the first chapter written under the craft standard from Stage 0, so its
   acknowledgment box is a live requirement rather than a retrospective one.

6. **Decision 28**, Northmoor properties G, H, I. Gates Ch9, Ch12, Ch13 problem
   sets only.

## Standing reminders

**Rules that bite.**

- **Building a chapter under `Drafts/` needs `AIOM_book.css` and `fonts/`
  symlinked beside it,** or better, copy the live text to the repo root as
  `_ch01_build.html`, build there, and delete both it and the `.print.html`
  sibling. `AIOM_build.py` sets `base_url` to the HTML's own directory, so
  building in place drops the whole design system and reports dozens of false
  defects. `place.py` is different: run it from the repo root ON the live text
  path, with the symlinks in place, because it rewrites the file it is given.
- **A green gate suite is not a read page.** With all fourteen gates passing,
  reading found flush paragraphs in the summary and a dated box (2026-08-08) and
  confirmed three moved-page cases (2026-08-09). No gate measures paragraph
  separation inside a block.
- **When a check and the prose disagree, fix whichever is actually wrong, and say
  which.** Gate 12 on 2026-08-09 is the cleanest case: rewording the sentence so
  the reference did not wrap would have passed the gate and left every later
  chapter exposed.
- **Read the archived rulings before writing findings.** Two of the nine Stage 2
  findings exist only because that was done: DE2 recovered a ruled fix that had
  been lost, and DE3 was framed as a different finding on rewritten text rather
  than as reopening D3.
- **Read the decision text before proposing an edit that touches it.** DE9 was
  first raised claiming Decision 56 does not constrain the panel's vocabulary. It
  does. Had that gone unchecked, the ruling would have breached it.
- No em dashes anywhere, including commit messages. A build gate enforces it.
- The craft standard binds at Stage 0, at drafting time, not at Stage 4.
- The chapter HTML is the single source of truth (Decision 50). Never fork.
- Source register notes inside a chapter's own Decision 51 block can carry
  rulings the summary ledger does not. Read them before using a figure.
- **Write every fact-check ruling back into the register note, with the condition
  that would reverse it.** A ruling recorded only in the checklist is a ruling
  the next checker will raise again.
- **Not every proposed remedy is an improvement.** Evaluate the remedy separately
  from the finding.

**Tooling facts learned the hard way.**

- **THE DESIGN MIRRORS ITS MARGINS.** Main text starts at x0 68.4 on odd pages,
  57.6 on even. Any new geometry check must derive the edge per page or it will
  read green while measuring nothing.
- The QA suite is FOURTEEN gates. Three checks written in this repo have been
  wrong in a way that read as green, and gate 12 has now been wrong twice. Every
  one was found by changing the input, never by re-reading the code. Treat a
  green gate on unchanged input as weak evidence.
- A fresh session has neither the Python deps nor poppler. `pip install -r
  requirements.txt`, then `apt-get update -qq && apt-get install -y
  poppler-utils`. The build exits 2 without them. The 403s from unrelated
  third-party PPAs during that apt-get are harmless.
- **NO SOURCE HOST IS REACHABLE FROM THIS ENVIRONMENT.** Verified 2026-08-06
  against six hosts; all fail CONNECT with a gateway 403 recorded as a policy
  denial. Do not offer to check a primary. Do not treat a register note as a
  substitute for one either; say which it is.
- The proxy blocks `raw.githubusercontent.com` and the Google Fonts CDN. Report
  policy denials, do not route around them.
- To reopen a chapter use `reopen.py`, never `gen_checklists.py --force`. After a
  reopen, check the box TEXT against the generator, not only the ticks.
- Stage folders are on Process v2 numbering across all eighteen units.
- Fonts are committed; do not run `AIOM_build.py --fonts`.
- Rasterize for visual review with `pdftoppm -png -r 150`.
