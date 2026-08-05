# CLAUDE.md

Project context for *AI Operations Management*. Read this before touching anything
in this repository.

---

## 1. What this is

A founding academic textbook establishing AI Operations Management as a discipline.
Fifteen chapters, four parts. Print-quality PDF produced through a WeasyPrint
pipeline in this repo.

Two named layers, both load-bearing:

- **AI Business Economics** is the science.
- **AI Operations Management** is the practice discipline that acts on it.

Reader: an intelligent, busy, sceptical MBA-level graduate student who has read
business books before and can tell when one is padded. Standard: university press
(Chicago or Oxford caliber). The book is intended to last fifty years.

Author of all decisions: Dan (Daniel S. Wipert, Chorus AI Systems). Claude drafts
and builds. Claude does not rule.

---

## 2. Standing rules, non-negotiable

These have all been explicitly ruled and re-affirmed. Do not relitigate them.

1. **No em dashes. Anywhere.** Body prose, cases, craft sections, summaries, key
   terms, discussion questions, problems, back matter, and every file in this
   repo including commit messages. Rewrite with commas, colons, periods,
   parentheses, or restructure the sentence. This is the single most-violated
   rule under stress. A build gate enforces it.
2. **Every empirical claim is cited to a real source, rewritten as a formal
   conditional, or cut.** No third option. Never invent a citation, a statistic,
   or a source. If the claim cannot be sourced, cut it and say so.
3. **The fixed six-slot skeleton applies to all fifteen chapters, without
   exception.** See section 3.
4. **The registry justifies the book. It does not organize the book.** Never
   restructure a chapter around registry objects.
5. **No decorative apparatus.** Signposting is done through the skeleton, not
   through prose. Do not tell the reader what the chapter is about to say before
   saying it.

### Voice

- **Register:** magisterial. Combative energy transmuted into cold economic
  analysis. Not neutral about the argument, completely neutral about individual
  actors. Do not scold providers, derive their behavior. Do not sneer at buyers
  who bought AI as software, explain why the mental model was legible and where
  it breaks. The manifesto's taunting register is out.
- **Person:** third person throughout body prose. Second person permitted
  sparingly in craft sections and discussion questions.
- **No contractions** in body prose. Permitted in dialogue inside cases and in
  discussion questions where they serve the register.
- **No exclamation points.**
- **No rhetorical questions** in body prose. Permitted in discussion questions,
  which is what they are for.
- **No hedging.** No "perhaps," no "some argue," no "one might say." Hedging is
  a signal that citation, formalization, or omission was skipped.
- **Fifty-year rule:** body prose is timeless. Perishable specifics are
  quarantined in dated cases.

### Craft, the positive half of the voice standard

The rules above are prohibitions. Prose can break none of them and still be dead
on the page. `AIOM_Voice_and_Craft_v1.md` is the positive standard, and it is
binding at drafting time, not only at check time. Read it before drafting a
chapter, not after.

Six criteria, each drawn from a named exemplar. They appear verbatim as
sub-checkboxes under Stage 4 in every chapter checklist, and `status_check.py`
fails a Stage 4 marked passed with one of them left open.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to a named, specific instance. Constrained by the fifty-year rule, so
  it lives mostly in cases, worked examples, and craft artifacts.
- **C2. Context and stakes.** Every mechanism states the conditions that made it
  available and what it settles, not only what it does. The highest-value
  criterion, and the only one with no mechanical proxy.
- **C3. Front-loaded sentences.** Findings lead, qualifications subordinate, no
  throat clearing.
- **C4. Deliberate rhythm.** Sentence length varies. No long stretch at a uniform
  length.
- **C5. Paragraph close.** Paragraphs end on the load-bearing clause, not a
  trailing qualifier.
- **C6. The guard holds.** No hero or villain framing, no populist register, no
  character-driven causation where a structural account is available. This guard
  is what keeps the borrowed techniques from reimporting a register already ruled
  out.

`voicecheck.py` prints advisory craft metrics alongside the mechanical bans. They
are proxies, permanently advisory, and never a pass-or-fail threshold. C2 and C6
have no proxy at all and are enforced only by reading.

---

## 3. The fixed six-slot skeleton

Every chapter, in this order, no optional slots:

1. Opening case
2. Teaching body
3. Craft section
4. Chapter summary
5. Key terms
6. Discussion questions and problems

The opening-case slot permits variation in **form** (a dashboard, a contract
clause, a failed executive memo can all serve). That is drafting freedom inside
the slot, not a structural exception.

Every opening case carries a provenance line beneath the title. Perishable
sources are dated. Constructed material is labelled as constructed.

---

## 4. Repository map

| Path | What it is |
|---|---|
| `AIOM_build.py` | Font staging, WeasyPrint render, ten QA gates. One command. |
| `AIOM_book.css` | The locked design system. |
| `place.py` | Definition-callout placement pass. See section 6. |
| `AIOM_Design_QA_Spec_v1.md` | Gate-by-gate spec. Moves with `AIOM_build.py`. |
| `AIOM_Consolidated_Spec_v1.md` | The full pre-drafting specification. Authoritative. Markdown despite the earlier `.pdf` reference. |
| `AIOM_Voice_and_Craft_v1.md` | The positive voice standard: the four borrowed techniques, the guard, and the six craft criteria. Binds from Stage 0. Read before drafting. |
| `AIOM_Specification_Addendum_v1.0.docx` | Decisions 1 through 21 and the Addendum rulings. |
| `AIOM_Structure_v1.md` | Chapter structure and structural devices. |
| `AIOM_Exit_Competencies_v1.md` | The twenty-four competencies. Backward-design root. |
| `AIOM_Maturity_Model_v1.md` | Stage definitions. Ch13 craft. |
| `AIOM_Case_Bank_v1.md` | Cited cases with reuse policy. |
| `AIOM_Northmoor_Dataset_v1.md` | Capstone dataset design. |
| `AIOM_Workplan_v5.md` | Current workplan and per-chapter tracker. Supersedes v4, which is retired. |
| `AIOM_Validation_Matrix_v1.xlsx` | The 28-row Appendix A trace matrix. Working artifact, never book content. Distinct from the full 228-object registry, which lives in Drive. |
| `chapters/` | Chapter HTML sources. |
| `fonts/` | Committed fonts (IBM Plex Sans, Jost) plus their OFL licenses. `fonts/use/` holds the six faces the CSS loads, so rendering needs no network staging. |

When spec placeholders conflict with operative content, trust the operative
content: the maturity model, Stage definitions, and chapter assignments win over
placeholder glosses.

---

## 5. Build commands

```bash
python3 AIOM_build.py --fonts                    # once per session
python3 AIOM_build.py chapters/AIOM_ch01.html    # render plus all QA gates
python3 AIOM_build.py chapters/AIOM_ch01.html --out build/Ch1.pdf
python3 place.py chapters/AIOM_ch01.html         # callout placement pass
```

Font staging reaches out to `github.com` and `raw.githubusercontent.com` for IBM
Plex Sans and the Jost variable font. The environment needs network access for
that step.

System dependencies WeasyPrint requires: `libpango-1.0-0`, `libpangoft2-1.0-0`,
`libcairo2`, `libgdk-pixbuf-2.0-0`, `libffi-dev`, `shared-mime-info`.
Python: `weasyprint`, `pdfplumber`, `pdf2image`, `pillow`, `openpyxl`, `fonttools`.

---

## 6. QA gates and their remedies

The suite is ten gates. Full detail in `AIOM_Design_QA_Spec_v1.md`. The ones
that fail most often:

- **Gate 1, horizontal overflow.** 428.4pt odd pages, 417.6pt even, 1.5pt
  tolerance. Catches unbreakable strings, oversized SVG text, table cells that
  will not wrap.
- **Gate 2, em and en dashes.** Fails on any `U+2014` or `U+2013`. Note this is
  stricter than the standing rule, which bans em dashes only. Open question Q2.
- **Gate 4, definition callout splits.** Fails a callout sitting flush at the top
  margin, the signature of one that broke across a page. **Remedy: run
  `place.py`.** Do not try to fix this in CSS. WeasyPrint 69 ignores
  `break-inside: avoid` on floated elements.
- **Gate 5, font faces.** Expected set only. Catches a missing `@font-face`, an
  unstaged font falling back to a system face, and stray faces inside SVG.
- **Gate 7, provenance line.** Page 1 must carry the 7pt amber semibold line
  beneath the opening case title.

Known gaps, do not assume the suite catches these: the theorem callout is
unguarded (it uses `--tint-thm`, gate 4 keys on `--tint-def`); there is no figure
validation at all; there is no bottom-margin or widow-orphan check. Inspect
figures and theorem callouts by eye.

---

## 7. Environment quirks, learned the hard way

- The registry `.xlsx` must be loaded with `openpyxl` and `data_only=True` to
  read computed values rather than formulas. Load rows via
  `ws.iter_rows(values_only=True)`, index columns off the header row, then use
  `Counter` and set operations for cross-checks.
- The founding paper and spec files carry `.docx` extensions but are plain
  markdown. `grep`, `sed`, and `wc` work on them. `python-docx` fails.
- CSS `content:` strings: a Unicode hex escape consumes the following space as an
  escape terminator. Use literal UTF-8 characters instead.
- SVG figures with `rx` render as curve paths in WeasyPrint and do not appear in
  `pdfplumber`'s `.rects`. Verify that geometry by pixel-sampling a raster.
- WeasyPrint is invoked with `base_url` set to the HTML file's own directory.

---

## 8. Chapter lifecycle (Process v2)

Thirteen steps, gates separated from passes. Process v2 (2026-08-01) inserts a
developmental edit as Stage 2 and renumbers the stages that follow. The shape is
ten stages (0 through 9) plus three gates. Lock is Stage 9, a pass, not a gate.
There is no G4. `(C)` is Claude, `(D)` is Dan working outside the Claude system.

| Step | Name | Owner |
|------|------|-------|
| Stage 0 | Draft | C |
| G1 | Structural gate | C |
| Stage 1 | Content review | D |
| Stage 2 | Developmental edit | C; Dan gut-checks with a second model |
| Stage 3 | Source and fact check 1 | D |
| Stage 4 | Voice and craft check | C |
| Stage 5 | Design review | C |
| G2 | Production gate | C |
| Stage 6 | Copy edit | D |
| Stage 7 | Final fact check 2 | D |
| G3 | Continuity gate | C |
| Stage 8 | Final read | D |
| Stage 9 | Locked | C |

**Stage 2, developmental edit.** The teaching-quality pass, held early so its
line edits land before fact check, voice, design, and production, and do not
churn them. It interrogates clarity, pacing, cognitive load, example fitness,
transitions, and whether the argument carries the target reader without a stall.
Claude runs it as a fresh critical pass; Dan gut-checks with a different model
and rules, the same independence he applies to fact checking.

**Stage 4, voice and craft check.** Two halves. The mechanical half is
`voicecheck.py`, which fails on the prohibitions. The judgment half reads the
chapter against the six craft criteria in `AIOM_Voice_and_Craft_v1.md` and
records a finding per criterion, not a single verdict. The criteria appear as
sub-checkboxes in the generated checklist, so `status_check.py` fails a Stage 4
marked passed with one left open and unexplained. The craft standard binds from
Stage 0, at drafting time; Stage 4 is where it is verified, not where it is first
consulted.

**Process v1 to v2 mapping**, for reading records written before 2026-08-01:
Stages 0 and 1 and gates G1, G2, G3 are unchanged. v1 Stage 2 (source and fact
check 1) is now Stage 3; v1 Stage 3 (voice) is now Stage 4; v1 Stage 4 (design)
is now Stage 5; v1 Stage 5 (copy edit) is now Stage 6; v1 Stage 6 (final fact
check 2) is now Stage 7; v1 Stage 7 (final read) is now Stage 8; v1 Stage 8
(locked) is now Stage 9. Dated records keep their original v1 numbers.

Sequencing rules:

- **Gates are not passes.** A gate is a mechanical pass-or-fail check run by
  Claude against a stated standard, and it stops the chapter where it stands.
  A pass is editorial judgment. They are tracked separately.
- **Edits re-run only what they can break, per the scoped re-run matrix below.**
  A render that passed against older prose has not passed, but a figure move need
  not re-run the voice check.
- Stages 6, 7, and 8 are all external and may run in one sitting. Stage 1 may
  not be batched with them: it runs early or it is worthless.
- A reopen after Stage 9 re-runs every step from the one that owns the change.
- No chapter is Locked until every step is complete.

**Scoped re-run matrix.** After a step passes, an edit re-runs only the steps it
can invalidate:

| Edit class | Re-runs | Leaves intact |
|---|---|---|
| Body prose (claim or teaching change) | Stage 2 dev, Stage 3 fact, Stage 4 voice, Stage 5 design, G2 | G1, unless a slot moves |
| Citation or source only | Stage 3 or Stage 7 fact check, G2 | dev, voice, design |
| Figure order, geometry, or number (caption text unchanged) | Stage 5 design, G2 | dev, fact, voice |
| Copy edit (typo, punctuation, no meaning change) | G2 | dev, fact, voice, design |
| CSS or design system | Stage 5 design and G2, every chapter | dev, fact, voice |
| Voice or craft standard change | Stage 4, every chapter not yet Locked | fact, design, G2, unless the re-run changes prose |
| Structural (slot added, removed, reordered) | G1, then every downstream step | nothing |

Status is single-sourced: the per-chapter checklist checkbox is authoritative,
and `status_check.py` prints and validates it. CLAUDE.md section 10 and the
Workplan tracker must mirror what it prints.

---

## 9. How to work here

- **Present decisions one at a time**, with options, a recommendation, and the
  reasoning. Dan rules quickly when the framing is complete. Do not proceed past
  an unruled decision.
- **Structure before content.** Structure is treated as almost more important
  than the content itself.
- **Verify programmatically before delivering.** Do not report a build as clean
  without running the gates.
- **Single attempts over retries.** Token waste is flagged explicitly.
- **Protect pedagogical surprises.** Later chapters withhold things deliberately.
  Do not front-run them.
- **Real cited evidence over constructed material,** every time it is available.

---

## 10. Current state

Chapter 1 ("The Category Error") renders complete at 19 pages with all eleven QA
gates passing. It is not Locked, but the Claude-owned production path is green and
Dan's early passes are done. Passed so far (Process v2 numbering): Stage 0
(draft); G1 (structural gate, cleared 2026-07-29 after Decision 48 repealed the
archival checks); Stage 1 (content review, 2026-07-29); Stage 3 (source and fact
check 1, 2026-07-29, whose record is carried in the chapter's own source block);
Stage 4 (voice check, 2026-07-28); and Stage 5 (design review) with G2
(production gate), both 2026-08-01 on the render carrying the Figure 1.2
reference fix, with AIOM_build.py's full eleven-check suite green. Stage 2
(developmental edit, new in Process v2, run retroactively on Chapter 1) passed
2026-08-01: all six developmental findings were ruled, with D1 (Section 1.4
signpost and tighten) and D5 (theorem aside tightened) applied and their Stage 4,
Stage 5, and G2 re-runs green on the 19-page render, and D2, D3, D4, and D6 closed
with no action. Reaching the G2 pass required adding an audit-only hide rule to the CSS, since
the committed v6.7 CSS predated the Decision 51 source-block apparatus; that
committed CSS plus the rule is the working version of record. The
figure-geometry, widow, and page-visual checks, outside the automated suite,
passed a first-pass visual review and await Dan's final sign-off. Remaining to
Lock: Stage 6 (copy edit), Stage 7 (final fact check 2), G3 (continuity gate),
Stage 8 (final read), and Stage 9 (lock).

**Chapter 1 Stage 4 is currently INCONSISTENT in `status_check.py`, by design and
pending one ruling.** The voice and craft standard was adopted 2026-08-05, after
Stage 4 cleared. Its six criteria are now sub-checkboxes under Stage 4 in the
Chapter 1 checklist, and they are recorded open, so the gate reports a step
marked passed with open sub-items. That report is accurate: the 2026-07-28 pass
tested the prohibitions only. The craft read has been run against
`AIOM_Ch01_Stage4_FINAL.html` and the chapter meets all six criteria as drafted,
with no prose change required, so adoption costs nothing here. What is open is
whether Chapter 1 adopts the standard (tick the six) or is grandfathered (mark
the six with a stated "postdates" exception, as Stage 0 already is). Either
resolution is a one-line edit and clears the gate. Chapter 1's Stage 4 metrics
are the baseline band that Chapters 2 through 15 are read against.

Design finalization is complete (D0 closed, 2026-07-28). The design system is
locked: CSS at v6.7, design spec at v6.8 plus three addenda. The registry is
validated: 228 objects load (200 propositions, 20 lemmas, 8 theorems), eight
book-mapped theorem IDs resolve, zero dangling references in the dependency
graph.

Chapter 2 ("The Flow") is the immediate next drafting target and is unblocked.
Chapters 3 through 15 follow in sequence. Front and back matter come after the
manuscript.

One decision still open: **Decision 28**, the Northmoor property gap. The M3
build asserts properties A through F; Decision 18 in the Addendum extended the
list to A through I. G, H, and I remain unbuilt. This gates the Ch9, Ch12, and
Ch13 problem sets, not Ch2.

Registry flags to carry into the appendix build (Phase 3, Appendix A):

- LEM-015 is retired. Skip it explicitly. IDs run LEM-001 through LEM-021 with
  LEM-015 absent.
- The "20 lemmas" count is correct as an object count. The ID range runs to 21.
- The registry ships a pre-built trace for THM-005, which is a Ch6 asset, not
  THM-004. Chapter 3's trace set piece uses THM-004 and must be built
  separately. Traces are generable mechanically from the dependency graph, so
  Figure 3.1 is buildable from data.

Appendix A reproduces the 28 theorems and lemmas only. The 200 propositions are
cited by ID and not reproduced in full.

---

## 11. Session handoff protocol

`HANDOFF.md` is the running session-to-session log. It carries the working state
that does not belong in this file: the active branch, what is committed and
pushed, the live open threads, and the standing reminders learned in recent
sessions. CLAUDE.md holds the durable rules; HANDOFF.md holds the perishable
state.

1. **At the start of every session, read `HANDOFF.md` before doing any work,**
   alongside this file. A SessionStart hook in `.claude/settings.json` prints it
   into context automatically, so it is in front of you already; read it rather
   than skipping past it.
2. **Before ending a session, update `HANDOFF.md` so it is accurate.** Refresh
   the last-updated date, the repository state (branch, what is pushed, whether
   `main` is behind), the chapter status, the open threads in priority order, and
   any standing reminder that changed. Then commit it. A handoff that lies about
   the branch or the sync state is worse than none, so verify the facts against
   `git status` and `status_check.py` rather than copying the previous entry.
3. **Keep the division of labor clean.** A durable rule or a closed decision
   graduates into CLAUDE.md or the decision log. Do not let HANDOFF.md accumulate
   settled rulings, and do not let CLAUDE.md drift into session bookkeeping.
