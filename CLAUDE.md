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
| `AIOM_Specification_Addendum_v1.0.docx` | Decisions 1 through 21 and the Addendum rulings. |
| `AIOM_Structure_v1.md` | Chapter structure and structural devices. |
| `AIOM_Exit_Competencies_v1.md` | The twenty-four competencies. Backward-design root. |
| `AIOM_Maturity_Model_v1.md` | Stage definitions. Ch13 craft. |
| `AIOM_Case_Bank_v1.md` | Cited cases with reuse policy. |
| `AIOM_Northmoor_Dataset_v1.md` | Capstone dataset design. |
| `AIOM_Workplan_v5.md` | Current workplan and per-chapter tracker. Supersedes v4, which is retired. |
| `AIOM_Validation_Matrix_v1.xlsx` | The 28-row Appendix A trace matrix. Working artifact, never book content. Distinct from the full 228-object registry, which lives in Drive. |
| `chapters/` | Chapter HTML sources. |
| `fonts/use/` | Staged fonts. Generated, not committed. |

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

## 8. Chapter lifecycle

Twelve steps, gates separated from passes (confirmed 2026-07-28, per Workplan
v5). This supersedes the earlier seven-stage list. The shape is nine stages
(0 through 8) plus three gates. Lock is Stage 8, a pass, not a gate. There is
no G4. `(C)` is Claude, `(D)` is Dan working outside the Claude system.

| Step | Name | Owner |
|------|------|-------|
| Stage 0 | Draft | C |
| G1 | Structural gate | C |
| Stage 1 | Content review | D |
| Stage 2 | Source and fact check 1 | D |
| Stage 3 | Voice check | C |
| Stage 4 | Design review | C |
| G2 | Production gate | C |
| Stage 5 | Copy edit | D |
| Stage 6 | Final fact check 2 | D |
| G3 | Continuity gate | C |
| Stage 7 | Final read | D |
| Stage 8 | Locked | C |

Sequencing rules:

- **Gates are not passes.** A gate is a mechanical pass-or-fail check run by
  Claude against a stated standard, and it stops the chapter where it stands.
  A pass is editorial judgment. They are tracked separately.
- **Stages 4 and G2 re-run after any prose edit.** A render that passed against
  older prose has not passed.
- Stages 5, 6, and 7 are all external and may run in one sitting. Stage 1 may
  not be batched with them: it runs early or it is worthless.
- A reopen after Stage 8 re-runs every stage from the one that owns the change.
- No chapter is Locked until every step is complete.

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

Chapter 1 ("The Category Error") renders complete at 18 pages with all ten QA
gates passing. It is drafted and confirmed in the locked voice (Stage 0 and
Stage 3 passed). It is not Locked: G1's only open item was source archiving,
which Decision 48 (2026-07-29) repealed, cutting G1 from fourteen checks to ten
and leaving access dates as the one remaining source requirement, so G1 needs a
re-run against the reduced standard. Stage 4 (design review) reverted to not-run
after the Stage 3 prose edits and has since re-run and passed on the current
render; G2 (production gate) is not yet confirmed. Stages 1, 2, 5, 6, 7, 8 and
G3 have not started.

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
