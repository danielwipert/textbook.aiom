# AI Operations Management: Textbook Workplan
Owner: Dan (Chorus AI Systems)
Last updated: 2026-08-02 (v5; currency sweep to Process v2 status)
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
   unblocked on the design side. CSS and design spec were both at v6.9 when v5
   was written; both are at v7.1 as of 2026-08-10. See the snapshot below.
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

Chapter 1 is 9 of 13 as of 2026-08-12, on a 25-page render with ALL FIFTEEN
GATES PASSING against CSS v7.1. Stage 6 closed 2026-08-12 on Dan's ruling after
fourteen copy edits. Only Stage 7 and Stage 8 remain of Dan's; then G3 and Stage 9,
both Claude's.

The paragraph here read "It is now 8 of 13, the chapter is 20 pages" until
2026-08-10. That was true before the 2026-08-08 reopen at Stage 2, which reset
every step from Stage 3 onward, and false for two days after it. THE COUNT IN
THIS FILE IS A MIRROR AND `status_check.py` IS THE SOURCE. This is the second
stale mirror found in this file on the same day, after the lifecycle paragraph
below.

The three steps run on 2026-08-10 each found something no gate could see. Stage 3
cleared on Dan's executive ruling that the 2026-08-06 external checks carry it,
after a diff against the audited render showed the value surface unchanged at
eighteen atoms and found three ruled claim narrowings silently reverted by the
copy edit; all three were restored from the register wording. Stage 4 raised six
findings, one per criterion, four applied, and closed with its second-model
gut-check still open. Stage 5 raised DR6 and DR7, two proper nouns broken by
automatic hyphenation, one of them across a page turn, and both were applied as
Decision 58.

CSS is at v7.1 and the design spec is at v7.1. The spec had read v6.9 while the
CSS shipped v7.0, a debt CLAUDE.md flagged; it was paid on 2026-08-10 with
section 16 for v7.0 and section 17 for v7.1.

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
1. **Chapter 1 Stages 7 and 8. DAN'S, AND THEY MAY RUN IN ONE SITTING.** Final
   fact check 2, then final read. **Stage 6 closed 2026-08-12** after fourteen copy
   edits. G2 re-passed 2026-08-12 at fifteen gates against CSS v7.1.
   Stage 7 is structurally external because no source host is reachable from a
   Claude session, and its checker must be fed a RENDER, never the chapter HTML:
   both production flags on external check 1 were phantoms of HTML extraction.
   External check 2 on a different prompt is still owed. Then G3 and Stage 9, both Claude's, and Stage 9 carries a
   booked pending-actions list: re-set the craft baseline band from the locked
   text, keep "flow" out of Chapter 1's continuity entry, and decide whether
   "category error" is logged as a Chapter 1 term.

2. **Chapter 2 drafting.** Can run in parallel once the Chapter 1 re-draft has
   settled the craft standard in practice.
3. **Decision 28 ruling.** Northmoor properties G, H, I. Not urgent: it gates
   Ch9, Ch12, and Ch13 problem sets, not Ch2.

Closed since v5: the G1 contradiction on Chapter 1 (cleared 2026-07-29 after
Decision 48 repealed the archival checks) and source capture (retired by Decision
48; G1 dropped to ten checks, a source now needs a verified primary, an access
date, and two independent fact checks).

---

## Chapter lifecycle

The authoritative lifecycle is CLAUDE.md section 8 (Process v2, 2026-08-01): ten
stages (0 through 9) plus three gates, with the developmental edit at Stage 2,
the scoped re-run matrix, and the v1-to-v2 stage mapping. This file does not keep
a second copy; that duplication is what drifts. Status is single-sourced in each
chapter's checklist and printed by `status_check.py`.

Chapter 1 was reopened at Stage 0 (2026-08-05, Decision 53), at Stage 5
(2026-08-06, Decision 56), and at Stage 2 (2026-08-08, after three copy-edit
rounds rewrote rather than corrected it), and at G2 twice on 2026-08-11 and
2026-08-12; 9 of the thirteen steps are passed as of 2026-08-12, and only Dan's
Stage 7 and Stage 8 stand between the chapter and G3. `reopen.py` performed every reset, archiving
each step's findings in place rather than destroying them. This paragraph read
"8 of the thirteen" until 2026-08-10, which was true before the Stage 2 reopen
and false for two days after it: the count here is a mirror, and
`status_check.py` is the source. Stage folders across all eighteen units were migrated to
Process v2 numbering on 2026-08-05, so a folder name no longer disagrees with
the live process.

- Copy-edit placement is revisited at Chapter 4 (Decision 24). If line edits are
  being churned by structural changes, move it earlier then, not before.
- Fifteen self-contained checklists exist, one per chapter (Decision 32).
- No process document and no book-wide rollup (Decision 32).
- Chapter 1 is not Locked until every step above is complete.
- **Chapter 1's live text is
  `Drafts/Ch01_The_Category_Error/00_Stage0_Draft/AIOM_Ch01_redraft.html`.** The
  superseded fork `06_Stage5_Design_Review/AIOM_Ch01_Stage4_FINAL.html` was
  deleted 2026-08-06 on Dan's ruling, after Decision 56 was applied to it by
  mistake and had to be reverted and re-applied to the live text. "One live text
  per chapter, supersede and delete, never fork" now holds for Chapter 1. The
  stage-folder render PDFs are kept: they are artifacts, not competing texts.

---

## Per-chapter status

Decision 32 rules out a rollup, so this is a status line per chapter rather
than a twelve-column grid. The detail lives in each chapter's own checklist.
If a twelve-column grid in this file would read as the forbidden rollup, say so
and it comes out.

| Ch  | Title                          | Step reached | Notes |
|-----|--------------------------------|--------------|-------|
| 1   | The Category Error             | Stage 6 done | 9 of 13 as of 2026-08-12, on a 25-page render with all FIFTEEN gates passing against CSS v7.1 and both MANUAL G2 checks performed, all 25 pages read. Only Dan's Stage 7 and Stage 8 remain, then G3 and Stage 9. Stage 6 closed 2026-08-12 on Dan's ruling after fourteen copy edits, CE1 to CE14; CE10 to CE14 were in the text but missing from the checklist and were reconstructed from the commit record before the tick. G2 was reopened and re-passed 2026-08-12 because its 2026-08-11 pass predated CE3 to CE6, and gate 15, typographic marks, ran against this chapter for the first time. Reopened at Stage 0 on 2026-08-05 (Decision 53), at Stage 5 on 2026-08-06 (Decisions 56 and 57), at Stage 2 on 2026-08-08 after three copy-edit rounds rewrote rather than corrected it, and at G2 twice since. Stage 3 cleared 2026-08-10 on Dan's executive ruling that the 2026-08-06 external checks carry it, after a diff against the audited render found three ruled claim narrowings silently reverted (SF8, SF9, SF10), all restored; FC2 repeated the shape a fourth time on a second vendor. Stage 4 closed with its second-model gut-check still open, so the craft verdict rests on one unverified read. Stage 5 raised DR6 and DR7, two proper nouns broken by automatic hyphenation, one across a page turn, neither visible to any gate; applied as Decision 58, CSS to v7.1. The craft baseline band is deliberately NOT set: it is booked to Stage 9 and no chapter is read against a band until then. |
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
- **Decision 33. AMENDED 2026-08-09 at Ch1 DE6.** Word bands are set, and the
  measure is now named. Chapters 1 and 2 run **6,500 to 7,500 words**, counted as
  the WHOLE CHAPTER AS RENDERED, excluding only the Decision 51 source register
  block and SVG label text. Citation notes ARE counted, because they reach the
  reader as numbered footnotes. `voicecheck.py` prints the number under this
  name, so it is read rather than recomputed by hand.

  The original band was 5,000 to 6,000 words with no measure stated, and that
  omission is what made the amendment necessary. Chapter 1 produced four
  defensible numbers at DE6: 7,032 on the measure now ruled, 6,865 with citation
  notes removed, 4,855 for `voicecheck.py`'s craft corpus, and 4,228 for the
  opening case plus 1.1 to 1.5 alone. The chapter was therefore either 1,030
  words over the ceiling or 770 under the floor, depending on a choice the
  decision never made. A band that cannot be computed is not a constraint.

  The band moved rather than the chapter because the three copy-edit rounds of
  2026-08-08 that added roughly 1,100 words were ruled, improved the prose, and
  were not padding. Setting the band to fit the artifact is more honest than
  keeping a target the book has outgrown and booking a permanent exception
  against it. Holding 5,000 to 6,000 was considered and would have meant cutting
  about 1,030 words from the teaching body, which is its own editorial pass and
  not a consequence of a number.
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

- **Decision 52. RULED 2026-08-05.** The voice standard gains a positive half.
  `AIOM_Voice_and_Craft_v1.md` extracts four transferable techniques from named
  exemplars (the concrete particular from Michael Lewis, context and stakes from
  James Lardner, sentence economy from the Financial Times, paragraph
  architecture from The New Yorker), carries an explicit guard against the
  registers those exemplars arrive with, and reduces to six criteria C1 through
  C6. Enforcement is four-layered, all four ruled together: the criteria are
  sub-checkboxes under Stage 4 so `status_check.py` fails a Stage 4 marked passed
  with one left open; the standard binds from Stage 0 at drafting time, with a
  Stage 0 acknowledgment box; `voicecheck.py` prints advisory craft metrics
  proxying C1, C3, C4, and C5, permanently advisory and never a threshold; and
  worked before-and-after exemplars are carried in the standard file, drawn from
  Chapter 1. Stage 4 is renamed the voice and craft check. Rationale: the
  standing rules were entirely prohibitive, and prose can break none of them and
  still be dead on the page. C2 and C6 have no mechanical proxy and are enforced
  by reading alone, which is stated rather than papered over.

- **Decision 53. RULED 2026-08-05.** Chapter 1 is reopened at Stage 0 and fully
  re-drafted, rather than patched, because it was drafted before the craft
  standard existed and is the exemplar fourteen further chapters are drafted
  against. The re-draft is also the proving run for Process v2 end to end.
  Supporting process, built the same day: `reopen.py`, so a reopen resets steps
  and archives findings instead of destroying them; the Process v1 to v2
  stage-folder migration across all eighteen units; gates 12, 13, and 14 in
  AIOM_build.py, closing the three checks the G2 checklist had claimed for
  months while performing none of them; a toolchain preflight and pinned
  requirements.txt, since a gate that did not run is not a gate that passed; and
  a G2 checklist mirroring the fourteen printed gates one for one, with the two
  genuinely manual checks labelled manual. Gate 14 found a real defect on its
  first run that the eleven-gate suite had passed.

- **Decision 54. BUILT 2026-08-05.** The continuity ledger exists:
  `AIOM_Continuity_Ledger.md` as the record and `continuity.py` as gate G3, with
  all seven checks the checklist names. The ledger carries terms owned per
  chapter, forward references and whether paid, registry glosses, Northmoor
  figures, and the canonical Founding Questions and maturity stages parsed from
  the ledger itself rather than hard-coded. Policy: entries are appended at
  Stage 9 on lock, never at draft time; the ledger is the authority and is never
  edited to make a gate pass; registry glosses are written by hand, and the
  placeholder fails the gate deliberately. Verified end to end against the
  superseded Chapter 1 render. Lock is no longer blocked for any chapter.

- **Decision 55. RULED 2026-08-05, Chapter 1 Stage 1.** Seven structural
  findings ruled, four of which amend the Consolidated Spec's Ch1 outline rather
  than the chapter. (S1) The case bank held no CASE 4.6 and no CASE 6.4 although
  the spec assigned both to Ch1; both are now written into AIOM_Case_Bank_v1.md
  from sources already cleared through the Ch1 register, with provenance lines
  saying so and no new research. CASE 6.4 carries the QJE figure discipline and
  the 2026-07-29 stipulation ruling, so a later chapter meets both rules from the
  bank. (S2) Figure numbering stands as the chapter has it, anatomy at 1.1, and
  the spec is amended. (S3) The opening case closes on the category error stated
  rather than the spec's question, since the standing rule forbids rhetorical
  questions in body prose; general principle ruled, whatever is more effective
  inside the chapter wins on educational and style grounds. (S4) A fourth
  discussion question is accepted, added to answer craft finding F7. (S5) P2 no
  longer needs a CITED deployment: the evidence policy governs empirical claims,
  not exercise scaffolding. (S6) FinOps stays out of Ch1; Ch14 owns the named
  engagement. (S7) The 2026-07-29 agent-count ruling stands unchanged. No word of
  the chapter changed, so no downstream step was invalidated.

- **Decision 56. RULED 2026-08-06.** Theorem statement form. A registry
  conditional carrying more than two antecedents is set as a structured
  conditional in the panel, never as running prose: scope boundary first, before
  the word "if"; antecedents enumerated in lower-case roman, one per line,
  semicolon-closed, "and" before the last; consequent on its own line opening
  with "then" and carrying the registry's negation. Antecedents are set in
  parallel grammar and full English, so elided articles are restored and a
  dangling disjunct is attached to the noun it modifies. The logic is untouchable:
  no antecedent may be added, dropped, merged, split, weakened, or strengthened,
  and the consequent may not be restated in the chapter's vocabulary. The registry
  statement is the authority, the panel is a faithful rendering, and the ID in the
  panel label is what a reader follows to the verbatim form. Rationale: THM-009 as
  drafted was a single sixty-word sentence with four conjoined antecedents and its
  scope clause trailing the negation, so the reader had to finish the statement and
  then retroactively re-scope it. The form is ruled now, at one theorem, rather than
  after the remaining seven are set. Spec: AIOM_DESIGN_SPEC.md section 5. CSS to
  v6.8: `.theorem .cond`, `ol.ante`, `li .mk`, `.conseq`. The dependency chain stays
  out of the panel, because Chapter 3 owns the trace set piece.

- **Decision 56a. RULED 2026-08-06.** `.slot-label` gains `break-after: avoid`.
  `h3.section` and `.problems-sec .slot-label` already carried the rule and the
  base slot label did not, which is why the craft-section label could strand at a
  page foot. It stranded once at Ch1 gate 14's first run, was cleared by cutting
  two sentences of prose at Stage 4, and returned the moment the theorem panel
  changed height. A defect whose only remedy is shaving prose until the page breaks
  elsewhere is a CSS defect, not a prose defect. Ch1 now reports zero stranded heads
  with the prose untouched.

- **Decision 56. RULED 2026-08-06.** Theorem statement form. A registry
  conditional carrying more than two antecedents is set as a structured
  conditional, never as running prose: scope boundary first before the word
  "if", antecedents enumerated in lower-case roman one per line, consequent on
  its own line opening with "then". Registry shorthand is rendered into full
  parallel English, restoring elided articles and attaching dangling disjuncts,
  and the logic may not change in any way. Rationale: THM-009 as a single
  sixty-word sentence put the scope boundary fifty-eight words after the reader
  needed it, so the whole statement had to be re-scoped retroactively. Full rule
  in AIOM_DESIGN_SPEC.md section 5. Decision 56a, the same day, added
  `break-after: avoid` to `.slot-label`; see Decision 57, which corrects it.

- **Decision 57. RULED 2026-08-06, Chapter 1 Stage 5.** Three design-system
  changes, CSS to v6.9, all found by reading rasterized pages and none by a gate.
  (a) `break-after: avoid` chains through `h2.case-title` and `p.provenance`, so a
  slot label, title, and provenance line move as one head group. Decision 56a had
  put the rule on `.slot-label` alone, which bound the label to the title, left
  the provenance line last, and made gate 14 report zero stranded heads while
  three head lines sat orphaned at the foot of page 12. A partial fix that
  silences the check is worse than none. Gap G-II opened. (b) DR2: `.model p + p`
  gains 6pt, because the model block relied on `p + .mlab` for all its structure
  and a block running one label over several paragraphs set them flush. 6pt not
  9pt, so a label stays the stronger break. (c) DR3: `table.inv` moves from
  `break-inside: auto` to `avoid`, because the P3 completion table spilled its
  header and one row onto an otherwise blank final page. `break-before: avoid` was
  also tried and REJECTED: WeasyPrint binds it to the preceding line box rather
  than the preceding block, so it split the problem statement across the spread.
  Accepted cost: a table may open a page while its instruction closes the one
  before. Chapter 1 goes from 19 pages to 20.

- **Decision 60. RULED 2026-08-13.** The web edition carries the full text, free.
  The paid product is the print and ebook editions plus the apparatus the site
  does not carry: Appendix A reproducing the 28 theorems and lemmas, the Northmoor
  dataset and capstone materials, problem solutions, and instructor materials.
  Chapters publish as they lock, and the site publishes no free-forever promise,
  so a press conversation stays open. Rationale: the book's differentiator is that
  every empirical claim is cited, formalized, or cut, and only the full text with
  its per-chapter source register demonstrates that. A discipline is established
  by adoption and citation rather than by unit sales.

- **Decision 61. RULED 2026-08-13.** The enriched-markdown pipeline is retired
  permanently. `aiom_md.py` stays deleted and is not restored. Markdown is never a
  committed chapter source on either the book path or the web path, because after
  Stage 0 a chapter passes through twelve steps that all operate on the HTML, so a
  committed markdown source goes stale at Stage 1 and stays stale for the
  chapter's life. `archive/AIOM_ch01_markdown_noncanonical.md` is KEPT, for its
  diff value against pre-fact-check prose, and its warning is strengthened: it
  carries the SF2 continuation mechanism, the FC9 absorbed-cost inference, and the
  forbidden word "introduced", in prose that reads well and whose dates and
  figures are all correct. It must never be read for prose.

- **Decision 62. RULED 2026-08-13.** The web edition is built by `web_build.py`
  with Jinja2 templates and a web stylesheet, in Python, with no Node toolchain.
  Any figure that earns interactivity gets a self-contained island on its own
  page. Rationale: citation formatting (`footnotes.py`, `cite_format.py`), the
  text-equivalence gate (`pdfplumber`), and lock status (`status_check.py`) are
  all already Python, so a JavaScript build would not remove Python from the build
  but would put the language boundary in the middle of the citation path. The
  toolchain does not constrain the design: scroll-driven animation, view
  transitions, container queries and the rest are browser platform features
  available to any static page.

- **Decision 63. RULED 2026-08-13.** The web edition lives in this repository,
  beside the print build. Rendered output is NOT committed, exactly as `build/`
  is not, so the full text of a chapter exists once in version control rather than
  twice. Deployment is a CI workflow that installs `requirements.txt`, builds,
  runs the web gates, and publishes, so the gates run on every push rather than
  on memory.

- **Decision 64. RULED 2026-08-13.** The site shows locked chapters only, enforced
  mechanically rather than by intention. Gate W2 asks `status_check.py` and
  refuses any chapter not at Stage 9. A `--preview` flag builds an in-flight
  chapter to a local, `noindex`, unlinked path, and CI never publishes it.
  CARRY FORWARD: the web render must never be the artifact for an external fact
  check. Both production flags on Chapter 1's first check were phantoms of HTML
  extraction, which dropped the `<li>` contents of the theorem panel and collapsed
  empty table cells leftward. A web page is HTML and reproduces both. Stages 3 and
  7 keep getting the PDF.

- **Decision 65. RULED 2026-08-13.** The web edition is hosted on GitHub Pages,
  published from `main` by `.github/workflows/web.yml`. Chosen over Cloudflare
  Pages and Netlify because it needs no third-party account and no API token in
  repository secrets, and because the source already lives here, so there is one
  fewer system to keep in sync. A custom domain is a DNS record plus the CNAME
  the build already emits from `--base-url`. **The domain was ruled on 2026-08-19
  as Decision 70.**

- **Decision 66. RULED 2026-08-13.** No analytics. The site makes no third-party
  request of any kind, which the search page already states to the reader in as
  many words. For a book whose selling point is that every claim is auditable,
  sending readers to a tracker would undercut the pitch, and the host's own
  request counts answer most of what is actually worth knowing. ENFORCED BY GATE
  W11 rather than by intention: every subresource the site fetches must be
  same-origin. Outbound anchor links are deliberately exempt, because a link a
  reader chooses to follow is not a request the page makes on their behalf, and
  the sources page exists to link out to every cited source.

- **Decision 67. RULED 2026-08-15.** The site publishes the typeset PDF, one per
  locked chapter, alongside the page. Chosen over a whole-book download, which
  needs a book-level render that does not exist: continuous folios across
  chapters, front matter, cross-chapter figure numbering, and the appendix. Today
  such a file would be one chapter labelled as the book, and several print gates
  assume a single chapter opening at page 1. The book PDF is booked for the
  completed manuscript instead, and the link text says "chapter" so nothing has
  to be walked back when it arrives. The download sits under the "This website"
  edition card rather than on a card of its own, because it is a second format of
  the same free text: the "Print and ebook" card still reads "In preparation" and
  still promises the appendix, the dataset, the solutions and the instructor
  materials that a chapter download does not carry. ENFORCED BY GATE W17: the
  file the site serves is rendered from the SAME injected document the web page
  is transformed from, so the two cannot be different readings of the chapter,
  and it goes through all fifteen print gates before it can publish.

- **Decision 68. RULED 2026-08-19.** Process v3: Stage 5 and Gate G2 move to sit
  after Stage 7, so the two reads of a rendered page happen once, on text nothing
  further will move. Ruled after the Chapter 1 process review measured what the
  step order actually costs: G2 ran at position 8 of 13 with three text-changing
  steps scheduled after it, so the scoped re-run matrix correctly sent the chapter
  back through the most expensive step on every late edit, and five of Chapter 1's
  eight reopens were that one defect. Stage 5 moves with the gate because every
  Stage 5 finding on Chapter 1 was fixed in CSS or in markup and none by rewriting
  a sentence, which makes the design read exactly as pagination-sensitive as the
  gate is. NO STAGE IS RENAMED OR RENUMBERED, so unlike the Process v1 to v2
  migration this needs no mapping table for reading dated records: only the
  position of two steps moves. Chapter 1 does not migrate and keeps v2 ordering
  and v2 stage folders, because it is locked and its checklist records v2 order.
  Option C of `AIOM_Process_v3_Proposal_v1.0.md`, which carries the evidence, the
  rejected alternatives and the reversal condition.

- **Decision 69. RULED 2026-08-19.** The mechanical suite runs continuously, on
  any chapter, in flight or locked, through `chapter_check.py` and the `chapter`
  workflow. THE CHAPTER'S OWN CHECKLIST DECIDES WHAT BINDS: a check fails the run
  only once the chapter has ticked the step that owns it, so a half-drafted
  chapter reports without failing and red always means a tick is currently lying.
  This adds no standard. Every check in it was already ruled, already written and
  already run by hand at a checkpoint; what changes is that a passed step's claim
  is now held at the commit that breaks it rather than at the next time somebody
  looks. Ruled on the evidence that Chapter 1's 2026-08-08 reopen records in its
  own grounds, that `status_check.py` "reporting 8 of 13 had been false since
  round 1 landed". The suite is IMPORTED by `amend.py` rather than duplicated in
  it. The two MANUAL G2 boxes and gaps G-I and G-II cannot run continuously and
  are reported stale when the text has moved, never ticked and never failed, which
  takes a G2 re-run from eighteen boxes to two and not to zero. Adopted as
  specified in `AIOM_Continuous_Suite_Proposal_v1.0.md`.

- **Decision 70. RULED 2026-08-19.** The domain is `aioperationsmanagement.ai`.
  This closes the last item the web edition was waiting on Dan for, open since
  Decision 65 chose the host on 2026-08-13. **The site now serves at the ROOT
  rather than under a project prefix**, so `web.yml` passes
  `--base-url https://aioperationsmanagement.ai` and no `--base-path` at all. The
  prefix was DERIVED from the repository name precisely so a rename could not
  leave it stale, and on a custom domain it becomes the defect instead: the 404
  page is served for any missing address at any depth, so it cannot use a
  relative path, and a `/textbook.aiom/` prefix would now reach for a path the
  host does not have. The plan booked this reversal in advance rather than
  discovering it, and **gate W15 is the check that would catch it**, because it
  serves the tree at whatever prefix the build was given and fails when a
  subresource 404s. `--base-url` also writes the CNAME that keeps Pages pointed
  at the domain and makes the sitemap, robots.txt and llms.txt absolute.
  **Verified locally at the domain: CNAME correct, all three address files
  absolute, the 404 page root-absolute with no prefix, seventeen gates green and
  108 of 108 self-test controls.** NOT verified from here and it cannot be: the
  container's egress proxy answers 403 to CONNECT for this domain exactly as it
  does for github.io, so **whether DNS resolves and Pages is serving is Dan's
  observation to make, never Claude's.**

- **Decision 71. RULED 2026-08-19.** The prose standard is ONE file,
  `AIOM_Prose_Standard_v2.0.md`, and the voice is **Concrete Management Prose**.
  Ruled after Dan rejected Chapter 1's drafted prose as unreadable, supplied his own
  style guide, and had the chapter edited outside the Claude system. **The named
  register "magisterial" is RETIRED**, because it sat above every other instruction
  and a drafter resolving a conflict between it and "keep the actor visible" chose
  the weighty sentence every time. What survives of it is the part about the
  argument rather than the prose: not neutral about the argument, completely neutral
  about individual actors. `AIOM_Prose_Style_Guide_v1.md` and
  `AIOM_Voice_and_Craft_v1.md` are retired to pointers, which also ends a
  duplication that had the prose rules living in four documents at once.
  **THE COST THAT JUSTIFIED THIS IS IN THE RECORD:** the Stage 6 copy edit "rewrote
  the chapter rather than corrected it", changing 59 of 155 blocks in round 1,
  growing body prose 25 per cent and taking the chapter from 20 pages to 26, which
  forced the 2026-08-08 reopen of five steps. The deeper cause was not the step
  order that Decision 68 fixed. It was that the draft arriving at the copy edit was
  in the wrong voice. Three things the old files lacked are why their sentence-level
  rules did not bind: a generative pattern telling a drafter what to write next, a
  ban on abstract openings, and ordinary business language as the default. Stage 4
  now grades SEVEN criteria rather than six: C7 is added for business-reality-first,
  C3 becomes "claim first", and C6's guard watches false sophistication as well as
  the populist register, because the book failed in the direction the old guard did
  not watch. **The exemplar of the voice is the locked Chapter 1**, and the baseline
  band is measured from it rather than from four journalism exemplars, which are
  retired.

- **Decision 72. RULED 2026-08-21.** The book reconnects to the AI Business
  Economics registry, now `dag.aiom` at commit `9d7ee50`, and rules A through E of
  `AIOM_Registry_Reconnection_Proposal_v1.0.md` are adopted.
  **(A) The book renders and cites CERTIFIED objects only**, and "certified",
  derived by the registry's own `validate.py` from the proof graph, replaces
  "locked", which was asserted by hand. **(B) Appendix A reproduces the certified
  theorems and lemmas**, 9 plus 20, listing uncertified objects by ID with their
  blockers rather than reproducing them. **(C) The inherited-vocabulary source is
  GENERATED from the registry's 140 definitions** into
  `AIOM_Inherited_Vocabulary.md`, superseding the hand-maintained ledger preserved
  in `archive/`, which could drift and this cannot. **(D) The manifest and the
  panel gate are built**: `registry.py` derives `AIOM_Registry_Manifest.json` from
  a supplied bundle and `chapter_check.py` runs the check under Gate G1. **The
  bundle is never committed**, because a manifest carries hashes and no statements
  and therefore cannot become a second copy of the authority, while the bundle
  could. **(E) Chapter 1's directional sentence and THM-001's provisional status
  are referred to the fact-check lane**, not amended on Claude's reading.
  **THE CHANGE WAS ADDITIVE AND NOTHING PUBLISHED WAS WRONG**: Chapter 1 cites one
  ID, THM-009, whose panel matches the registry name character for character; all
  28 IDs the project references resolve, 27 certified; all eight anchor theorems
  exist and are certified. **This also closes what rule 4a could not**: the panel
  promise is checked rather than trusted, for the first time since the rule was
  written, and three negative controls prove the check fails on a wrong name, an
  uncertified object and a missing one.

Also settled, not numbered: theorem panels are labeled "Theorem n" while prose
cites registry IDs.

---

## Design system of record (D0 closed)

State: CSS at v6.9. Design spec at v6.9 plus four addenda.

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

Chapter 1 source state (resolved 2026-07-29, G1 cleared):
- The register carries nine sources, each cited to a verified primary and checked
  live on its access date.
- The three upgrades are done: the Microsoft 4.7 million figure is sourced to the
  FY26 Q2 earnings call (Decision 46, no filing carries it), the GitHub claim to
  the dated changelog entry, and the Altman post carries a second independent path.
- Capture is retired (Decision 48), so no snapshots are filed.

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
Word band: 6,500 to 7,500 for Ch1 and Ch2 (Decision 33, amended 2026-08-09),
counted as the whole rendered chapter less the source register and SVG labels.
`voicecheck.py` prints the number.
- [~] Ch1  The Category Error        (25 pages, all fifteen gates pass; 9 of 13 as of 2026-08-12, Stage 6 closed, awaiting Dan's Stage 7 and Stage 8)
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
  for callout placement, fourteen-check QA suite, toolchain preflight)
- [x] Design system locked (D0)
- [ ] Validate all figures before render
- [ ] Programmatic QA (pdfplumber overflow and header checks; zero em dashes)
- [ ] Rasterized visual QA (pdf2image pixel sampling)
- [ ] Northmoor trade-name collision check (pre-print gate)
- [ ] Final PDF delivery to /mnt/user-data/outputs/

---

## Working files and restart procedure

The repository is version-controlled and is the source of truth. Work is
committed and pushed to the working branch each session, with `main` kept in
sync; nothing is downloaded or re-uploaded by hand. A fresh session clones the
repo, so the file set is already present.

Build environment and commands live in CLAUDE.md section 5; the perishable
per-session state (active branch, what is pushed, and the standing environment
reminders) lives in HANDOFF.md. This file keeps no second copy of either, since
duplication is what drifts. In particular: the fonts are committed under
`fonts/`, so `AIOM_build.py --fonts` is not run; poppler-utils installs per
session for gate 9; and a chapter builds from a repo-root copy of its stage HTML
because of the CSS-adjacency wrinkle.

File handling rules:
- The chapter HTML is the single source of truth (Decision 50). Edit it directly;
  the built HTML and PDF are generated. Do not write chapter prose to markdown,
  and never fork a chapter into a second live text. Two divergent texts is the
  exact failure the v14 episode produced.

---

## Standing rules (do not violate)
- No em dashes anywhere. Rewrite with commas, colons, periods, parentheses.
- Every empirical claim cited or cut.
- The six craft criteria in AIOM_Voice_and_Craft_v1.md bind from Stage 0, at
  drafting time, and are verified at Stage 4. Read the file before drafting.
- Fixed six-slot skeleton in all 15 chapters, no exceptions. The source
  register is apparatus, not a slot.
- Registry justifies the book; it does not organize it.
- Theorems are the only chapter-anchoring callouts. Eight, one-to-one.
  Lemmas are prose-cited by ID. Propositions are cited by ID only.
- Theorem statement form (Decision 56): more than two antecedents means scope
  first, antecedents enumerated, consequent on its own line. Render the registry
  into readable English; never change its logic.
- No chapter is Locked until it clears the full lifecycle.
- One live workplan at a time. Supersede and delete; never fork.
- One live text per chapter. Supersede and delete; never fork.
- Verify currency before reporting. A file in front of you is not necessarily
  the current file. Check the version before drawing a conclusion from it.

END OF WORKPLAN v5.
