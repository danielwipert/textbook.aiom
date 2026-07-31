# AI Operations Management: Textbook Workplan
Owner: Dan (Chorus AI Systems)
Last updated: 2026-07-28 (v5)
Status legend: [x] done · [~] in progress · [ ] not started

---

## What changed in v5
v5 exists because seventeen rulings from the 2026-07-27 design session lived
only in a conversation. That was a single point of failure. This file absorbs
them.

Base: `AIOM_Workplan_v4.md`, carried forward in full. Nothing in v4 was found
to be wrong. Items were closed, not corrected.

Added or changed in v5:
1. **D0 is closed.** Design finalization is complete. Chapter locks are
   unblocked on the design side. CSS at v6.7, design spec at v6.8 plus three
   addenda.
2. **The chapter lifecycle is replaced.** v4's seven-stage lifecycle is
   superseded by the twelve-step process ruled on 2026-07-27, which separates
   gates from passes. See the reconstruction flag below.
3. **Decisions 29 through 41 recorded**, plus 40a. Decision 24 closed.
   Decisions 34 and 35 recorded as moot.
4. Chapter 1 status updated: renders complete at 18 pages, all ten QA gates
   passing. G1 had failed on source archiving only; Decision 48 later repealed
   the archival checks, so that blocker is retired.
5. Source handling recorded as built: one book-wide register, scripted capture,
   generated citations, Chicago 17 notes and bibliography.
6. Two manuscript fact corrections logged.
7. Restart procedure recorded, because the container does not persist.

Unchanged and still open: **Decision 28**, the Northmoor property gap.

Superseded: `AIOM_Workplan_v4.md`. Delete it. One live workplan at a time.

---

## Where we are (snapshot)
Pre-drafting closeout is complete (M2, CB2, M3 all done). Design finalization
is complete (D0 closed). The design system was tested on the three things it
had never been tested on: Figure 1.2 renders, the craft section typesets using
the model-answer treatment that section 7 of the spec predicted, and a
full-length chapter paginates without defect.

Chapter 1 renders complete for the first time at 18 pages with all ten QA gates
passing. It is not Locked. Its draft stage passed, its source gate failed, and
most of its editorial passes have not started.

The editorial process now exists as a defined thing rather than an intention.

Chapter 2 drafting is unblocked and can run in parallel with Chapter 1's
editorial passes.

Dataset name: Northmoor is final (Decision 23). One open question on its
property coverage: see Decision 28.

---

## Milestone tracker

| ID | Milestone                          | Status | Blocks        |
|----|------------------------------------|--------|---------------|
| M1 | Consolidated Spec review           | [x]    | -             |
| M2 | Registry integration + validation  | [x]    | cleared       |
| CB2| Case-bank research pass 2          | [x]    | cleared       |
| M3 | Northmoor numerical build          | [x]    | cleared (see D28) |
| D0 | Design finalization (lock the system) | [x] | cleared       |
| D1 | Chapter drafts (Ch1 to Ch15)       | [~]    | -             |
| D2 | Front matter and appendices        | [ ]    | -             |
| P1 | Production, QA, delivery           | [ ]    | -             |

---

## Immediate queue (in order)
1. **Rule the G1 contradiction on Chapter 1.** The marker says failed, the
   findings text says closed. See the Ch1 checklist chapter notes.
2. **Source capture retired (Decision 48).** Capture is no longer required; the
   archival checks are gone and G1 drops to ten checks. A source now needs a
   verified primary, an access date, and two independent fact checks.
3. **Chapter 1, stages 1 and 2.** External passes, Dan's.
4. **Chapter 2 drafting.** Runs in parallel with items 2 and 3.
5. **Decision 28 ruling.** Northmoor properties G, H, I. Not urgent: it gates
   Ch9, Ch12, and Ch13 problem sets, not Ch2.

---

## Chapter lifecycle (twelve steps, gates separated from passes)

### Confirmed 2026-07-28
The reconstruction that stood here has been replaced with the actual process,
read off `AIOM_Ch01_Checklist.md`. It was wrong in one respect: the shape is
nine stages (0 through 8) plus three gates, not eight stages plus four gates.
Lock is Stage 8, a pass, not a gate. There is no G4.

Ownership: (C) = Claude, (D) = Dan, external to the Claude system.

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

Sequencing rules from the checklist itself:
- Stages 5, 6, and 7 are all external and may be run in one sitting.
- Stage 1 may not be batched with them. It runs early or it is worthless.
- Gates are mechanical and stop the chapter where it stands. Passes are
  judgment.
- A reopen after Stage 8 re-runs every stage from the one that owns the change.

### Rules that hold regardless of labels
- **Gates are not passes.** A gate is a pass or fail check run by Claude against
  a stated standard. A pass is editorial work. They are tracked separately.
- **Stages 4 and G2 re-run after any prose edit.** A render that passed against
  older prose has not passed. Chapter 1's stage 4 and G2 reverted after the
  Stage 3 edits; stage 4 re-ran and passed, then the Figure 1.2 reference fix
  reverted both again. Both re-run after the next render.
- Stage 5 placement is revisited at Chapter 4 (Decision 24). If line edits are
  being churned by structural changes, move it earlier then, not before.
- Fifteen self-contained checklists exist, one per chapter (Decision 32).
- No process document and no book-wide rollup (Decision 32).
- Chapter 1 is not Locked until every step above is complete.

---

## Per-chapter status

Decision 32 rules out a rollup, so this is a status line per chapter rather
than a twelve-column grid. The detail lives in each chapter's own checklist.
If a twelve-column grid in this file would read as the forbidden rollup, say so
and it comes out.

| Ch  | Title                          | Step reached | Notes |
|-----|--------------------------------|--------------|-------|
| 1   | The Category Error             | G1, G2       | Stage 0 and Stage 3 passed. G1's archival block repealed by Decision 48; G1 needs a re-run against the ten-check standard. Stage 4 passed, then reverted with G2 by the Figure 1.2 reference fix; both re-run after the next render. Stages 1, 2, 5, 6, 7, 8 and G3 not started. |
| 2   | The Flow                       | not started  | Unblocked. Next to draft. |
| 3   | A Science and Its Discipline   | not started  | Build the THM-004 trace. |
| 4   | The Playing Field              | not started  | Decision 24 revisited here. |
| 5   | The Anatomy of Cost            | not started  | |
| 6   | The Nature of Value            | not started  | CB2 value statements ready. |
| 7   | Sourcing                       | not started  | |
| 8   | Metering                       | not started  | |
| 9   | Attribution                    | not started  | See Decision 28. |
| 10  | Planning and Budgeting         | not started  | |
| 11  | Allocation and Routing         | not started  | |
| 12  | The Value Boundary             | not started  | See Decision 28. |
| 13  | Diagnosis and Maturity         | not started  | T0 packet ready. See Decision 28. |
| 14  | The Organized Buyer            | not started  | CB2 FinOps data ready. |
| 15  | Standing Up the Discipline     | not started  | Final exam. |

Cumulative cases (Part I, II, III) run the same lifecycle when drafted.

---

## Decisions log

Decisions 1 through 21 live in the Consolidated Spec and its Addendum.
Decisions 22 onward live here.

- **Decision 22.** Founding Questions canonical wording: Section 6 wording,
  leading "And" dropped from Q5. Five questions locked. (A parallel session
  labeled this same ruling "Option B"; the substance is identical. Decision 22
  is the canonical label.)
- **Decision 23.** Northmoor confirmed as the final dataset name.
- **Decision 24. RULED.** Copy edit sits late, at stage 5, after voice and
  design. Revisit at Chapter 4. Rationale: line edits are not churned by
  structural changes.
- **Decision 25.** The axiom layer. The book describes the definition and axiom
  layers accurately in Chapter 3 and reproduces down to the proposition layer
  only. The axiom source files are not loaded into the project. Chapter 3's
  trace set piece terminates at proposition nodes with a pointer to the fuller
  apparatus.
- **Decision 26.** Founding Question numbering. Manifesto numbering is
  retained. Part III resolves the questions out of numerical order (1, 3, 3, 2,
  4, 5 across Ch7 to Ch12), taught as a feature in the Part III introduction.
  Renumbering was rejected.
- **Decision 27.** The nine unassigned lemmas are assigned as prose-level
  grounding, cited by ID where they carry the argument. Tier architecture
  unchanged: theorems remain the only chapter-anchoring callouts, eight,
  one-to-one. Ch9, Ch10, and Ch11 gain formal grounding they previously lacked.
- **Decision 28. OPEN.** Northmoor property coverage. Decision 18 in the
  Specification Addendum extended the property list from A-through-F to
  A-through-I, adding property G (an unreconcilable invoice residual within a
  seeded band), property H (a workflow whose value column is structurally
  absent), and property I (a disputed attribution basis where two bases each
  survive challenge). The M3 build asserts A through F only. Options: (a) extend
  the generator and answer keys to G, H, I; (b) implement G, H, I as authored
  artifacts outside the generator; (c) amend Decision 18. Recommendation:
  option (a) or (b), because G, H, and I are the properties whose answer keys
  grade reasoning rather than answer-matching, and they feed Ch9, Ch12, and
  Ch13. Awaiting ruling. Carried open since v4.
- **Decision 29.** Content review is its own pass, at stage 1. It is not folded
  into the fact check.
- **Decision 30.** A final read of the rendered chapter, judged pass or fail on
  the whole rather than line by line.
- **Decision 31.** A running continuity ledger is maintained across chapters and
  checked at G3.
- **Decision 32. AMENDED.** Per-chapter checklist only. No process document and
  no book-wide rollup.
- **Decision 33.** Word bands are set. Chapters 1 and 2 run 5,000 to 6,000
  words.
- **Decision 34. MOOT.** Margins were already correct. No change.
- **Decision 35. MOOT.** The theorem panel is a block, so `break-inside: avoid`
  holds it. No workaround needed.
- **Decision 36.** Draft v2 is authoritative over proof v14. Two divergent texts
  is the failure mode to avoid; delete the loser.
- **Decision 37.** Figure fills use `--tint-fig`. Figures never use apparatus
  tints.
- **Decision 38.** The chapter source register is classed as apparatus, not a
  seventh slot. The six-slot skeleton is intact.
- **Decision 39.** Chicago 17, notes and bibliography, with access dates.
- **Decision 40.** Source standard: upgrade to the most durable primary; a
  social-post-only claim gets a second independent path. The source-upgrade half
  survives; the archival-capture half is repealed by Decision 48.
- **Decision 40a.** Perma.cc is out. Moot under Decision 48, which drops capture
  entirely.
- **Decision 41.** One book-wide source register, generated citations. The
  scripted-capture step is retired by Decision 48.
- **Decision 48 (2026-07-29).** No capture. A source is sufficiently sourced when
  cited to a verified primary, checked live on the access date, and cleared by
  two independent fact checks. Repeals the archival capture of Decisions 39, 40,
  and 40a; the Decision 40 source-upgrade standard survives. Gate G1 drops from
  fourteen checks to ten.

- **Decision 42.** Voiced material. Body prose is third person. First or second
  person is permitted only in material marked as voiced, either by a block class
  (`model`, `dq`, `problem`) or by enclosing quotation marks. Ruled at Ch1
  Stage 3.
- **Decision 43.** Reader address. Second person is permitted in discussion
  questions and problems. "The reader" holds everywhere else.
- **Decision 44.** Definition restatement. A definition given in a definition
  aside is not restated verbatim in body prose. The body names the term instead.
- **Decision 45.** Token gloss. "Token" carries a short appositive gloss at
  first substantive use in Ch1 section 1.2. Revisit when the preface
  reader-assumptions subsection is written.

- **Decision 46.** Microsoft's IR transcript is accepted as the primary source
  for the GitHub Copilot subscriber figure. A filing upgrade is not available:
  the figure appears only in spoken remarks, the earnings press release carries
  no subscriber count, and Microsoft does not break out product-level
  subscriber counts in the 10-Q. Standing principle: a first-party disclosure
  published by the party that holds the data is a primary source, and where no
  filing carries it, capture governs durability rather than a stronger form.

Also settled, not numbered: theorem panels are labeled "Theorem n" while prose
cites registry IDs.

---

## Design system of record (D0 closed)

State: CSS at v6.7. Design spec at v6.8 plus three addenda.

What D0 proved, being the three things the system had never been tested on:
1. Figure 1.2 renders.
2. The craft section typesets using the model-answer treatment, as section 7 of
   the spec predicted.
3. A full-length chapter paginates without defect.

Standing design rules carried out of D0:
- `--tint-fig` for figure fills. Figures never use apparatus tints
  (Decision 37).
- The chapter source register is apparatus, not a slot (Decision 38).
- Theorem panels are labeled "Theorem n"; prose cites registry IDs.
- Margins are as specified; the earlier concern was unfounded (Decision 34).
- The theorem panel is a block and `break-inside: avoid` holds it
  (Decision 35). This does not generalize: WeasyPrint 69 still ignores
  `break-inside: avoid` on floated elements, which is what `place.py` exists
  for.

---

## Source apparatus (built)

- One book-wide source register: `AIOM_sources.json`.
- Citations are generated, not hand-written.
- Capture: retired by Decision 48. No snapshots are filed.
- Style: Chicago 17, notes and bibliography, with access dates (Decision 39).
- Archival standard: repealed by Decision 48. A source is sufficiently sourced
  when cited to a verified primary with an access date and cleared by two
  independent fact checks. The capture requirement of Decisions 40 and 40a is
  withdrawn; the Decision 40 source-upgrade standard survives.

Chapter 1 source state, blocking G1:
- Six of seven sources are blocked.
- Five have no canonical URL.
- Three need upgrading before capture:
  - the Microsoft 4.7 million figure, into an SEC filing;
  - the GitHub documentation, into a permalinked revision;
  - the Altman post, which needs a second independent path.

---

## Manuscript corrections of record

Logged so they are not silently reintroduced by a later edit.

1. **Cursor repricing.** Previously attributed to heavy-user cost. Truell's
   stated reason was rising tokens per request on long-horizon tasks.
   Corrected.
2. **The 4.7 million figure.** Previously attributed to GitHub. It is a
   Microsoft disclosure. Corrected.
3. Dates pinned throughout Chapter 1.

---

## Decision 27 assignments (reference)
| Lemma | Chapter gained | What it grounds |
|-------|----------------|-----------------|
| LEM-011 | Ch9 | Recorded token activity becomes measurable usage |
| LEM-001 | Ch10 | Usage growth increases cost exposure |
| LEM-003, LEM-004 | Ch11 | Rule-based differentiated treatment; capacity constraints require allocation |
| LEM-010 | Ch7 | Model substitution constrained by adequacy and switching cost |
| LEM-018 | Ch5 | Pilot cost structure is not deployment cost structure |
| LEM-013 | Ch4 | Deployment architecture influences economics |
| LEM-014 | Ch5, Ch7 | Resource requirement differences produce cost-exposure differences |
| LEM-005 | Ch2 | Production is operated, not merely accessed |
| LEM-017 | Ch7, Ch12 | Workflow integration creates scoped operational dependency |

---

## Canonical Founding Questions (locked, Decision 22)

| # | Question | Function | Answered in | Maturity stage |
|---|----------|----------|-------------|----------------|
| 1 | Are you paying for capability you do not need, or starving work that needs more? | Sourcing | Ch7 | Governed |
| 2 | What do you expect the AI flow to consume next period, and how will you know when it deviates? | Planning and budgeting | Ch10 | Governed |
| 3 | Who consumed what last month, in service of which work? | Metering and attribution | Ch8, Ch9 | Visible, then Attributed |
| 4 | When capacity is constrained, who decides what runs first, and by what rule? | Allocation | Ch11 | Governed |
| 5 | Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing? | Value boundary | Ch12 | Accountable |

Structural device: posed at the end of Ch3, resolved once each across Ch7 to
Ch12, instrumentalized as the diagnostic in Ch13, re-asked as the ninety-day
plan's targets in Ch15.

---

## Registry facts of record (verified against Registry v1.3)

- 228 objects: 200 propositions, 20 lemmas, 8 theorems.
- All eight book-mapped theorem IDs resolve. One-to-one, no orphans, no gaps.
- Appendix A scope confirmed at 28 objects.
- Dependency graph integrity verified: every internal proposition and lemma
  reference resolves. Zero dangling references.
- Keystones: **LEM-006** (buyer total cost extends beyond access price)
  underpins six theorems; **LEM-021** (ROI evaluation requires measurement
  boundary) and **LEM-002** (measurement enables visibility) underpin five each.
  These three carry the most structural load in the book.
- **LEM-015 does not exist.** IDs run LEM-001 to LEM-021 with 015 absent.
  Nothing references it. Retired, not lost.
- Axioms AX-001 to AX-035 (34 distinct) are cited as dependencies but live in
  separate canonical source files, per the workbook's own reader guide.
  Boundary set by Decision 25.
- **11 of 20 lemmas have no registry plain statement**, only a formal
  statement: LEM-002, 004, 006, 007, 008, 009, 012, 016, 019, 020, 021.
  Appendix A's verbatim reproduction is safe because all 28 have formal
  statements. Prose citation of these 11 requires a plain-language gloss
  written at drafting and marked as book-authored, not registry text.
- The workbook ships a worked recursive trace for THM-005 (`02_TRACE_EXAMPLE`),
  which is a Ch6 asset. The Ch3 trace set piece uses THM-004 and must be built
  separately. Traces for any theorem can be generated mechanically from the
  dependency graph, so Figure 3.1 is buildable from data.
- Registry grounding reaches Ch1 through Ch13 after Decision 27. Ch14 and Ch15
  carry none by design: both are Part IV institutional chapters that reprise
  established claims rather than establish new ones. Record in the method note
  so it reads as decided rather than overlooked.

Reference artifact: `AIOM_Validation_Matrix_v1.xlsx` (28 rows; exact statement,
scope conditions, dependent chapters and figures, revision trigger, plus a
Legend sheet). Working artifact only. Never book content. Keep in Drive and in
project knowledge; the Decision 27 assignments exist nowhere else.

---

## Phase 0: Foundation (DONE)
- [x] Stage 1: exit competencies (24) locked
- [x] Stage 2: course architecture locked
- [x] Stage 3: chapter structure locked (15 chapters, 4 parts)
- [x] Theorem map (8 theorems, one-to-one) locked
- [x] Coverage map (all 24 competencies placed)
- [x] Maturity model designed (Unmanaged, Visible, Attributed, Governed, Accountable)
- [x] Northmoor dataset design locked (one company, two moments)
- [x] Chapter-level outlines for all 15 chapters (Consolidated Spec, Part D)
- [x] Case bank pass 1 complete
- [x] Consolidated Spec v1.0 compiled
- [x] Addendum v1.0 ruled (M1 closed)

---

## Phase 1: Pre-drafting closeout (COMPLETE)

### M2: Registry integration + validation matrix [x]
- [x] Load founding paper and Registry v1.3 into the project
- [x] Fill the REGISTRY PULL items (Founding Questions exact wording; Decision 22)
- [x] Build validation matrix: all 28 Appendix A objects traced to ID
- [x] Confirm Appendix A scope (the 28 theorems and lemmas, verbatim)

Registry flags to carry into the Appendix A build (Phase 3):
- LEM-015 is absent from the ID sequence; skip it explicitly.
- The "20 lemmas" count is correct as an object count, but IDs run to LEM-021.
- The registry ships a worked trace for THM-005 (Ch6 asset), not THM-004 (Ch3
  trace set piece per Decision 3); the THM-004 trace must be built separately.

Documentation follow-ups (not blocking):
- [ ] Replace Consolidated Spec section B.5's placeholder gloss with the
      canonical five-question table above. The placeholder had Questions 2 and
      3 swapped relative to the manifesto.
- [ ] Mark the Part H `[REGISTRY PULL]` open items resolved.
- [ ] Upload `AIOM_Validation_Matrix_v1.xlsx` to project knowledge.

### CB2: Case-bank research pass 2 [x]
- [x] Six more classifiable value statements for the Ch6 sort-and-repair set
- [x] Positive value case with real boundaries (Brynjolfsson, Li, Raymond QJE
  2025; METR developer RCT arc as counterweight)
- [x] Opening cases for chapters that were missing one
- [x] FinOps Foundation framework text + State of FinOps 2026
- [x] Token-price volatility corrected (same-model cross-provider ~3x to 4x;
  cross-model spread is the 10x to 50x figure; keep separate in Ch2 and Ch5)
- [x] Model deprecation and forced-migration episodes (Ch7 switching
  economics). Now also formally grounded by LEM-010 per Decision 27.
- [~] Northmoor trade-name check (disclaimer written; collision check is a
  pre-print gate, not a drafting gate)

### M3: Northmoor numerical build [x]
- [x] Confirm final dataset name (Northmoor; Decision 23)
- [x] Seeded Python generator (properties A to F asserted; all pass)
- [x] Emit outputs (raw events, half-cleaned export, budget/actuals, task-class
  and tier tables plus scenarios, capstone netting, T0 diagnostic packet, keys)
- [x] Construction note written
- [ ] **Properties G, H, I per Decision 18. See open Decision 28.**

Gate cleared: Part III (Ch7 to Ch12), Ch13, and Ch15 are unblocked for
drafting. Decision 28 affects Ch9, Ch12, and Ch13 problem sets specifically.

---

## Phase 2: Drafting

### D0: Design finalization [x] CLOSED 2026-07-28
- [x] Review the Ch1 design proof and list what to change
- [x] Rule each open design question (one at a time, per protocol)
- [x] Rebuild the affected assets (CSS, figure templates, running heads)
- [x] Re-render Ch1 as the confirmed design proof
- [x] Lock the design system; record the decision

### Drafting (chapter by chapter)
Protocol: one editorial decision at a time, ruled before proceeding. Every
chapter uses the fixed six-slot skeleton, no exceptions, and runs the full
lifecycle above. Per-chapter registry grounding is in the validation matrix.
Word band: 5,000 to 6,000 for Ch1 and Ch2 (Decision 33).
- [~] Ch1  The Category Error        (renders at 18 pages; G1 failed)
- [ ] Ch2  The Flow                  (next; unblocked)
- [ ] Ch3  A Science and Its Discipline   (M2 ready; build THM-004 trace)
- [ ] Part I cumulative case
- [ ] Ch4  The Playing Field          (revisit Decision 24 here)
- [ ] Ch5  The Anatomy of Cost
- [ ] Ch6  The Nature of Value        (CB2 value statements ready)
- [ ] Part II cumulative case
- [ ] Ch7  Sourcing                   (M3 ready)
- [ ] Ch8  Metering                   (M3 ready)
- [ ] Ch9  Attribution                (M3 ready; see Decision 28)
- [ ] Ch10 Planning and Budgeting     (M3 ready)
- [ ] Ch11 Allocation and Routing     (M3 ready)
- [ ] Ch12 The Value Boundary         (M3 ready; see Decision 28)
- [ ] Part III cumulative case
- [ ] Ch13 Diagnosis and Maturity     (M3 diagnostic packet ready; see D28)
- [ ] Ch14 The Organized Buyer        (CB2 FinOps data ready)
- [ ] Ch15 Standing Up the Discipline (final exam; M3 ready)

Standing drafting tasks:
- [ ] Write plain-language glosses for the 11 lemmas lacking them, at the
      chapter where each is first cited. Mark every gloss as book-authored,
      never as registry text.
- [ ] Maintain the continuity ledger across chapters (Decision 31).

---

## Phase 3: Front and back matter
- [ ] Appendix A: 28 theorems and lemmas, verbatim (skip LEM-015, IDs run to
  LEM-021, build the THM-004 trace separately)
- [ ] Glossary (aggregated key terms from all chapters)
- [ ] Method note (include: LEM-015 retirement; the 20-lemma count against a
  21-wide ID range; the axiom-layer boundary per Decision 25; Ch14 and Ch15
  carrying no registry grounding by design)
- [ ] Index
- [ ] Bibliography, generated from the source register (Decisions 39 and 41)
- [ ] Front matter (title, preface, founding-document framing, 14-week course map)

Front and back matter clear the same lifecycle where a fact check applies
(Appendix A, method note, glossary).

---

## Phase 4: Production, QA, delivery
- [x] Render pipeline built (WeasyPrint, AIOM_book.css, AIOM_build.py, place.py
  for callout placement, ten-gate QA suite)
- [x] Design system locked (D0)
- [ ] Validate all figures before render
- [ ] Programmatic QA (pdfplumber overflow and header checks; zero em dashes)
- [ ] Rasterized visual QA (pdf2image pixel sampling)
- [ ] Northmoor trade-name collision check (pre-print gate)
- [ ] Final PDF delivery to /mnt/user-data/outputs/

---

## Working files and restart procedure

The container does not persist. Files must be downloaded from the outputs panel
before a session closes, and re-uploaded to restart.

Files to upload at the start of a session:
- `AIOM_book.css`
- `AIOM_build.py`
- `place.py`
- `sources.py`
- `voicecheck.py`
- `AIOM_sources.json`
- `AIOM_ch01.html`
- `AIOM_DESIGN_SPEC.md`

Then:
```
pip install weasyprint==69.0 fonttools
python3 AIOM_build.py --fonts
```

File handling rules:
- Edit `AIOM_ch01.html`. Never edit `AIOM_ch01.built.html`, which is generated.
- `AIOM_Ch1_draft_v2.md` is to be deleted. Two divergent texts is the exact
  failure the v14 episode produced.

---

## Standing rules (do not violate)
- No em dashes anywhere. Rewrite with commas, colons, periods, parentheses.
- Every empirical claim cited or cut.
- Fixed six-slot skeleton in all 15 chapters, no exceptions. The source
  register is apparatus, not a slot.
- Registry justifies the book; it does not organize it.
- Theorems are the only chapter-anchoring callouts. Eight, one-to-one.
  Lemmas are prose-cited by ID. Propositions are cited by ID only.
- No chapter is Locked until it clears the full lifecycle.
- One live workplan at a time. Supersede and delete; never fork.
- One live text per chapter. Supersede and delete; never fork.
- Verify currency before reporting. A file in front of you is not necessarily
  the current file. Check the version before drawing a conclusion from it.

END OF WORKPLAN v5.
