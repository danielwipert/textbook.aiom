# AI Operations Management: Consolidated Specification v1.0

Textbook: *AI Operations Management* (founding text of the discipline).
Document type: pre-drafting specification. Purpose: single reference document capturing the complete state of the project after the outlining phase and before the Northmoor numerical build and Chapter 1 drafting.
Compiled July 20, 2026. Author of decisions: Dan (Daniel S. Wipert, Chorus AI Systems). Compiled by working session.

This document is intended to be read in one pass by collaborators and outside reviewers. It is deliberately long and self-contained. A reader who has never seen the project before should be able to reconstruct, from this document alone, what the book is, why it exists, what it argues, what it teaches, how it is organized, what has been ruled and what remains open, and what work is next.

---

# 0. Reader's guide

The document is organized in eight parts.

**Part A: Purpose and register.** What the book is, who it is for, what it argues, and the founding-document ambition.

**Part B: Technical specifications.** Length, tone, voice, format, production, evidence policy, pedagogy.

**Part C: The locked foundation.** The 24 exit competencies, the 15-chapter structure, the theorem map, the coverage map, the maturity model, the Northmoor dataset, and the case bank at v2.0.

**Part D: The chapter-level outlines.** All fifteen chapters, drafted against the fixed six-slot skeleton, with every embedded decision recorded inline as ruled.

**Part E: The complete decision log.** Every one of the fourteen rulings made during outlining, listed in the order ruled, with the option chosen and the reasoning.

**Part F: The figure inventory.** Every figure across all fifteen chapters, with its big idea and its signature-figure designation where applicable.

**Part G: The craft inventory.** The seventeen named artifacts the book contributes, with their competency assignments.

**Part H: Open items, chase lists, and what happens next.** The registry pulls still required, the primary-source chase list before print, the open watch items carried into drafting, and the immediate next milestones.

Two structural notes for the reader.

First, the book is a two-layer architecture, and this document uses both layer names throughout: **AI Business Economics** is the science (the ordered body of conditional propositions about the economics of AI consumption), and **AI Operations Management (AIOM)** is the practice discipline that acts on the science. The textbook is titled for the practice; the science stands behind it in a registry (200 propositions, 20 lemmas, 8 theorems, arranged as a dependency graph) that the book quotes at load-bearing moments and reproduces in an appendix.

Second, one structural amendment was logged during outlining: cumulative cases number three, not four, with Part IV's closing role fulfilled by the Chapter 15 final exam. This amendment is applied throughout Part D and Part E of this document.

---

# PART A: PURPOSE AND REGISTER

## A.1 What this book is

*AI Operations Management* is the founding textbook of a new academic discipline. It names, defines, and teaches the discipline that governs how organizations consume, cost, allocate, and hold accountable the deployed use of artificial intelligence.

The discipline is named. There are two layers, both named:
- **AI Business Economics**, the science: an ordered body of conditional propositions about the economics of AI consumption in commercial settings.
- **AI Operations Management**, the practice: the discipline that acts on the science, organized around five functions (sourcing, metering, attribution, planning and budgeting, allocation and routing, and the value boundary).

The book teaches both layers. The science answers the question "what is true?" about the economics of AI as consumption. The discipline answers the question "what do we do?" given that those things are true.

## A.2 What the book argues

The central argument of the book is stated in one sentence: **deployed AI use is resource consumption, not software access, and the discipline that governs it does not yet exist except in fragments.**

Every chapter serves that argument.

Chapter 1 states the category error. Chapter 2 introduces the three flows (usage, records, cost-and-value) that a deployment generates and the central asymmetry that governs them: cost accrues by default, value accrues only by design, so an unmanaged flow collects all of the cost and an unknown fraction of the value. Chapter 3 introduces the two-layer architecture and the five Founding Questions the discipline exists to answer. Chapters 4 through 6 establish the science: how providers price against variable cost, what total cost actually looks like, and how honest value measurement works. Chapters 7 through 12 teach the five practice functions in the order the dependencies require, culminating at the value boundary (the book's technical summit). Chapters 13 through 15 institutionalize the discipline: a maturity model for diagnosis, an organizational design for the buyer, and a ninety-day sequence for standing the discipline up.

The book is a buyer-side book by explicit design. Provider economics appears once, early, as "the playing field" (Chapter 4). Everything else is written from the seat of the organization operating the deployment.

## A.3 Who the book is for

**Primary reader:** the MBA-level graduate business student. The book must be teachable at Chicago or Oxford press caliber and must serve as the assigned text for a semester-length graduate course on AI operations management.

**Secondary reader:** the practicing executive who must translate the discipline into C-suite decisions. The book must be readable in that seat with material effect. The final chapter's assessment is explicitly a C-suite briefing exercise (three exhibits and 400 words) precisely because this reader must be served by the book's endpoint.

**Not the reader:** the ML engineer, the prompt engineer, the AI strategist, or the regulatory compliance specialist. The book has deliberate exclusions (see A.6) that keep it out of those adjacent territories.

## A.4 The founding-document ambition

The book is written as a founding document. It expects to be superseded within roughly five years as the discipline accumulates practitioners, cases, evidence, and refinements. The point of a founding document is not to be permanent; it is to be the edition against which subsequent editions are measured.

The founding-document ambition shapes several concrete choices:
- Body prose is written to outlive its examples. Perishable specifics (prices, tier names, limits, market shares, company positions) are quarantined inside dated case studies ("In July 2025, ...") and never appear in body prose.
- The registry (theorems, lemmas, propositions) is reproduced in an appendix so that later editions can revise the empirical annotations while the formal claims remain checkable against the same numbered set.
- The last sentence of the book acknowledges the founding-document position openly: the point of a founding document is to become one edition among many.

## A.5 The book's relationship to adjacent disciplines

Four adjacent disciplines are treated at Chapter 3's borders and honored throughout by staying out of their territory.

- **AIOps (IT operations telemetry, systems monitoring).** Watches systems. Not economics. Not this book.
- **MLOps (model lifecycle engineering).** Ships models. Does not govern their consumption. Not this book.
- **FinOps (cloud cost management, and, as of February 2026, "the value of technology").** The nearest neighbor. Owns cost visibility infrastructure at the cloud and SaaS level, is currently mid-expansion into AI spend management, and openly acknowledges that its practitioners cannot yet answer whether the AI is providing value. The book engages FinOps by name and designs a boundary treaty with it in Chapter 14.
- **Regulatory AI governance (risk, compliance, responsible use).** A separate discipline with its own literatures. One border-sentence in Chapter 13 fences it off; the book does not attempt to teach it.

## A.6 Deliberate exclusions (locked)

The book does NOT teach:
- ML internals (how transformers, attention, or any specific model architecture works).
- Prompt engineering.
- AI strategy and use-case ideation.
- AI governance in the regulatory sense (risk, compliance, responsible use), beyond boundary-drawing.
- Any single narrative running case (there is no single fictional company followed throughout the book; the one constructed dataset is threaded through problem sets, not through prose).

These are the exclusions because they either exist as fully served territories already (ML internals, prompt engineering, regulatory governance) or because they belong to a different genre of book (AI strategy books, ideation books). This book is a professional discipline's founding text, not a survey.

---

# PART B: TECHNICAL SPECIFICATIONS

## B.1 Structure

- **Length:** 15 chapters in 4 parts. Estimated finished length: 350-450 pages including front matter, back matter, appendices, and figures. Chapter lengths vary by teaching load; the summit chapter (Ch12) and the institutional chapter (Ch14) are expected to run longest, and the argument chapters (Ch1, Ch2) are expected to run tightest.
- **Chapter skeleton:** fixed at six slots, no exceptions, no optional slots.
  1. Opening case
  2. Teaching body (subdivided as needed for the chapter's argument)
  3. Craft section (procedure, template, and fully worked example of the chapter's named artifacts)
  4. Chapter summary
  5. Key terms
  6. Discussion questions and problems
- **Part-closing cumulative cases:** three total (Parts I, II, III), each reaching backward across earlier chapters (interleaving). Part IV's structural role is fulfilled by the Chapter 15 P1 final exam, marked as the book's culminating exercise. (This is the ruled amendment per Decision 14.)
- **Front matter:** preface, acknowledgments, reader's guide (short), a note on the registry, a note on the Northmoor dataset (labeled as constructed, with the standard fictional-entity disclaimer).
- **Back matter:** appendix reproducing the 28 registry theorems and lemmas (per the standing decision, the 200 propositions are cited by ID but not reproduced in full); a method note on the case selection and evidence policy; a glossary drawn from the chapter Key Terms sections; an index; a bibliography arranged by primary source category.

## B.2 Voice and tone

**Register:** magisterial with combative energy transmuted into cold economic analysis. The book is not neutral about its argument, but its neutrality about individual actors is complete. It does not scold providers; it derives their behavior. It does not sneer at buyers who bought AI as software; it explains why the mental model was legible and where it breaks. The manifesto's original taunting register is out; the argument's force is preserved through the argument itself, not through voice.

**Person:** third-person throughout body prose. Second person permitted sparingly in craft sections ("The reader can now...") and in discussion questions.

**Standing linguistic rules:**
- No em dashes. Anywhere. Rewrite with commas, colons, periods, parentheses, or restructure the sentence.
- No contractions in body prose. Contractions permitted in dialogue inside cases and in discussion questions where they serve the register.
- No exclamation points.
- No rhetorical questions in body prose. Rhetorical questions permitted in discussion questions (that is what they are for).
- No hedging language ("perhaps," "some argue," "one might say"). The evidence policy requires citation, formalization as conditional, or omission. Hedging is a signal that one of the three was skipped.

**On the reader:** the book assumes an intelligent, busy, sceptical MBA-level reader who has read business books before and can tell when one is padded. The book does not condescend, does not repeat itself for reassurance, does not tell the reader what the chapter is about to say before saying it. Signposting is done through the fixed skeleton, not through prose.

**Craft standard (added 2026-08-05):** the standing linguistic rules above are prohibitions, and prohibitions alone can produce prose that breaks no rule and is dead on the page. The positive standard lives in `AIOM_Voice_and_Craft_v1.md` and is binding at drafting time. It extracts four transferable techniques from named exemplars: the concrete particular (Michael Lewis), context and stakes (James Lardner), sentence economy (the Financial Times), and paragraph architecture (The New Yorker). It borrows the techniques and not the registers, and it carries an explicit guard against what those exemplars bring with them: no populism, no hero-and-villain framing, no character-driven causation where a structural account is available. The guard is load-bearing, because character-driven explanation is precisely what the standing rule against scolding providers already forbids.

The standard reduces to six criteria (C1 concrete particular, C2 context and stakes, C3 front-loaded sentences, C4 deliberate rhythm, C5 paragraph close, C6 the guard holds). They appear verbatim as sub-checkboxes under Stage 4 of every chapter checklist, which makes an unaddressed criterion a mechanical failure in `status_check.py` rather than a silent omission. `voicecheck.py` prints advisory metrics that proxy C1, C3, C4, and C5. C2 and C6 have no proxy and are enforced by reading alone.

## B.3 The evidence policy (locked)

Every empirical claim in the book must be one of:
1. **Cited to a real primary source** (peer-reviewed paper, regulatory filing, official document, top-tier press, provider primary documentation).
2. **Rewritten as a formal conditional** (a claim about what follows IF stated conditions hold, not a claim about the world).
3. **Cut.**

Cited sources are graded internally:
- Grade A: primary or top-tier press (Bloomberg, Fortune, TechCrunch, CBC, official provider docs, peer-reviewed journals).
- Grade B: reliable trade press.
- Grade C: SEO or vendor content used only as a pointer to chase to a primary. Grade C sources are NEVER cited in the book.

Every case in the book cites a Grade A primary directly. The primary-source chase list (see Part H) enumerates the ones that must be archived at drafting time.

Limitations are stated once, plainly, where they apply. No self-countering paragraphs.

## B.4 The registry and its role

The book rests on a formal registry: the AI Business Economics Locked Registry v1.3.

The registry contains 200 propositions, 20 lemmas, and 8 theorems, arranged as a dependency graph. Each proposition asserts one testable claim about the economics of AI consumption; each lemma is proved from propositions; each theorem is proved from lemmas.

The book uses the registry in tiers:
- **Theorems** appear as chapter-anchoring callouts at first exposure of the big idea. Eight theorems, eight anchor chapters, one-to-one (per the theorem map, Section C.3.5).
- **Lemmas** are quoted in prose where they carry the argument, cited by ID.
- **Propositions** are cited by ID as evidence for smaller claims; not reproduced in full in body prose.
- **The full registry** appears in the back-of-book appendix, reproducing the 28 theorems and lemmas verbatim and listing the 200 propositions by ID with statements.

The governing relationship, stated explicitly in Chapter 3 and repeated wherever the registry appears in structure: **the registry justifies the book; it does not organize it.** The book's chapter order is derived from pedagogy (Part I, argument; Part II, science; Part III, practice; Part IV, institution) with the maturity model's ladder proven by the registry. This relationship models the science-and-discipline architecture the book teaches: the registry is to the book as the science is to the discipline.

## B.5 The Founding Questions

Five questions constitute the diagnostic instrument of the discipline. They were called "the Monday questions" in the founding manifesto; they were renamed **the Founding Questions** during design work. Each question corresponds to one function of the practice layer and to one stage of the maturity model.

Exact wording is a REGISTRY PULL (see Part H, open items) and will be added to this specification when the founding paper and Registry v1.3 are loaded into the project. Placeholder gloss for review:
1. **The sourcing question** (Ch7): what capacity are we feeding the flow with, on what terms, with what portability?
2. **The visibility question** (Ch8-9, jointly): who consumed what, in service of which work?
3. **The plan question** (Ch10): what do we expect to consume, and what would count as anomalous?
4. **The allocation question** (Ch11): under binding constraint, what runs first, what queues, what is declined, and by what stated rule?
5. **The accountability question** (Ch12): does the flow answer for itself somewhere specific, owned by someone specific?

Structural device: the questions are posed at the end of Chapter 3 (Part I close), resolved once each across Chapters 7 through 12, instrumentalized as the diagnostic in Chapter 13, and re-asked as the ninety-day plan's targets in Chapter 15.

## B.6 The chapter skeleton, standing rules

Every chapter is structured identically. This is enforced without exception. The skeleton is not a template that varies; it is a discipline the book performs on itself.

Slot 1: **Opening case.** A real (or, in Chapters 9 and 13, a constructed-but-labeled) episode that dramatizes the chapter's argument. Read in roughly two to three pages. Every case is dated where perishable. Constructed material is labeled as constructed.

Slot 2: **Teaching body.** The chapter's main argument, subdivided into numbered subsections (typically five to seven). Fully worked examples are inline; figures appear at first exposure of the big idea.

Slot 3: **Craft section.** The chapter's named artifacts, presented as procedure, template, and fully worked example. The book's original contributions are here; each is enumerated in the craft inventory (Part G).

Slot 4: **Chapter summary.** One paragraph. Not a recap of subsections; a statement of what the reader can now do.

Slot 5: **Key terms.** A list of the chapter's named concepts. These terms compose the book's glossary in aggregate.

Slot 6: **Discussion questions and problems.** Self-explanation-register discussion questions (typically three), followed by problems calibrated to the fading policy (see B.7). Part I, II, and III chapters may include the part-closing cumulative case in this slot.

## B.7 The pedagogy commitments (locked)

- **Backward design:** the book was designed by locking exit competencies first, then assessment evidence, then chapter structure. This document is the artifact of that design process.
- **Worked-example fading:** Parts I and II are fully worked throughout. Part III begins with completion problems (Ch7) and progresses to unguided (Ch12). Part IV is integrative unguided throughout.
- **Interleaved and cumulative practice:** problem sets reach back to earlier chapters. Part-closing cumulative cases integrate across the part. The Northmoor dataset threads through Chapters 7 through 15 as recurring practice material.
- **Self-explanation-style discussion questions:** discussion prompts ask the reader to explain a concept, defend a position, or construct the reversal test. They do not ask for opinion.
- **Mayer coherence and signaling:** one strong figure per big idea at first exposure. No decorative apparatus. No stock images. Auxiliary figures permitted only where the content is categorical or architectural and prose cannot render it (RACI matrices, decision trees, reference architectures).

## B.8 Production specifications

- **Book format:** trade academic paperback and hardcover, single volume.
- **Design system:** to be specified in a subsequent production session; not covered in this document. Series positioning: the book publishes standalone; it is positioned as a potential flagship for a later series, but no series banner appears on the first edition.
- **Figures:** produced programmatically where possible; SVG output validated against pdfplumber and pdf2image checks before rendering (per the standing build practice from adjacent projects). Every figure is redrawable from a Python script kept alongside the manuscript source.
- **Typography and layout:** to be specified in production. Standing commitment: no decorative apparatus, generous whitespace around figures, consistent chapter-opening treatment across all fifteen chapters.
- **Registry appendix:** reproduces the 28 theorems and lemmas verbatim; lists all 200 propositions by ID with their exact statement text. The full dependency graph is printed as a foldout or two-page spread.
- **Case citation format:** the book uses author-date citations inline with a bibliography at back; every case includes the dated primary source, the archival capture date for perishable web content, and (where applicable) a note on the criticism or contested reading the straight-spine policy addresses.

## B.9 Book prose never uses em dashes

Repeated here because it is the single most-violated rule under stress. The rule applies without exception: cases, body prose, craft sections, chapter summaries, key terms, discussion questions, problems, and back matter. Rewrite with commas, colons, periods, parentheses, or restructure the sentence. Reviewers of this document should flag any em dash they see in any subsequent draft as a first-priority fix.

---

# PART C: THE LOCKED FOUNDATION

This part captures the design artifacts that were completed and locked before outlining began. They are reproduced here in full because subsequent editions or collaborators may need to work from them directly.

## C.1 Standing decisions (twelve, locked)

1. This book fully replaces the earlier *AI Operations* textbook (abandoned as premature).
2. Two-layer architecture, both named: AI Business Economics is the science; AI Operations Management is the discipline.
3. Primary reader: MBA-level graduate student; must translate to C-suite. University-press standard (Chicago or Oxford caliber). Fifty-year founding-document ambition: body prose written to outlive its examples; perishable market specifics quarantined inside dated case studies.
4. Buyer-side spine. Provider economics appears once, early, as "the playing field" (Chapter 4).
5. Registry objects tiered: theorems as chapter-anchoring callouts; lemmas quoted where load-bearing; propositions cited by ID; the full 28 theorems and lemmas plus proposition IDs and statements as a back-of-book appendix; one early trace set piece (Chapter 3) teaching registry literacy.
6. Evidence policy: straight spine. Every empirical claim cited, formalized as conditional, or cut. Limitations stated once, plainly. No hedging.
7. Many real cited case studies; no single narrative running case. ONE recurring constructed DATASET (the Northmoor Apparel dataset, clearly labeled as constructed) threads the problem sets: its budget appears in budgeting problems, its actuals in variance problems, its records in attribution problems, its T0 state in the diagnostic packet, culminating in the final netting. Cumulative practice without storybook narrative.
8. Fixed chapter skeleton, identical in every chapter, no optional slots.
9. The Founding Questions live at the part level, judiciously.
10. Pedagogy: backward design; worked-example fading; interleaved cumulative practice; self-explanation-style discussion questions; Mayer coherence and signaling; one strong figure per big idea at first exposure.
11. Book prose never uses em dashes.
12. Sequencing constraint: the institutional layer (competencies 20-24) consumes all earlier material and must come last; the Northmoor dataset must be fully exercised before competency 23.

## C.2 The exit competencies (24, locked)

The exit competencies are the whole book. No chapter exists that does not serve at least one competency, and every competency is served by the structure. Each is phrased as "the reader can..." and is observable: an exam problem or case assignment can be set against it.

**Group 1: Thinking (theory layer, AI Business Economics)**

C1. Explain why deployed AI use is resource consumption rather than software access; defend against the flat-rate objection.
C2. Identify the three flows (usage, records, cost-and-value) in any real deployment; diagnose which are unmanaged.
C3. State the central asymmetry (cost by default, value by design) and derive its consequence: all of the cost, an unknown fraction of the value.
C4. Read a formal claim: parse conditions, trace dependencies, state what it does and does not establish.
C5. Model the provider side: why fixed revenue against variable cost is unstable; predict the rational mechanisms (meters, tiers, limits, priority pricing).
C6. Distinguish claimed value, realized value, productivity, ROI; explain why a productivity claim never establishes ROI.
C7. Distinguish technical capability from economic suitability; explain why the frontier model is not automatically correct.

**Group 2: Doing (practice layer, the five functions)**

C8. Decompose a business task into performance requirements; evaluate models economically, not by benchmark rank.
C9. Compute TCO beyond access price: integration, operation, review, error, and governance costs.
C10. Evaluate a switching decision, including functional adequacy gate, transition costs, and payback.
C11. Build a usage-aware budget: driver-based forecast by workflow with pre-committed anomaly thresholds.
C12. Perform variance analysis; classify causes (demand-driven, efficiency-driven, control-driven).
C13. Specify a metering architecture: event record schema, consolidation, tagging enforcement, coverage test.
C14. Choose and defend an attribution basis; compute under alternatives; understand incentive consequences.
C15. Produce the one-page consolidated management report a CFO can act on.
C16. Write a routing policy matching work classes to capacity classes on economic grounds.
C17. Design priority and constraint rules with a stated generative rule (criticality tiers, degradation ladder).
C18. Draw a value boundary and perform the netting: realized value against fully loaded cost, with limitations. **[SUMMIT]**
C19. Assign boundary ownership: owner, cadence, decision thresholds. **[SUMMIT]**

**Group 3: Leading (institutional layer)**

C20. Diagnose an organization with the Founding Questions; locate it on the maturity path.
C21. Design the AIOM function: placement, roles, RACI, the FinOps boundary treaty.
C22. Negotiate with a provider from an organized position: their economics, the buyer's leverage inventory (records), ranked term sheet, walk-away line.
C23. Brief a C-suite in the organization's own numbers: three exhibits, 400 words, specific ask.
C24. Stand up the discipline from zero: the ninety-day sequence with stated logic.

**Summit judgment (locked):** Competencies 18 and 19 are the summit of the book. Everything else exists so the reader can do those two.

## C.3 The 15-chapter structure

### C.3.1 The four parts and their purposes

**Part I: The Argument** (Chapters 1-3). The reader learns why the discipline must exist. Founding Questions posed at part's end, deliberately unanswerable yet.

**Part II: The Science** (Chapters 4-6). What is true, before what to do. Fully worked examples throughout.

**Part III: The Practice** (Chapters 7-12). The five functions. Chapter titles use the manifesto's own verbs. The Northmoor dataset is introduced at the top of this part with its construction note. Worked-example fading: completion problems early in the part, unguided by its end.

**Part IV: The Institution** (Chapters 13-15). The discipline in a real organization. Integrative, unguided assessments throughout. Contains the book's final exam at Ch15.

### C.3.2 The fifteen chapters, listed

1. The Category Error
2. The Flow
3. A Science and Its Discipline
4. The Playing Field
5. The Anatomy of Cost
6. The Nature of Value
7. Sourcing: Feeding the Flow
8. Metering: Seeing the Flow
9. Attribution: Assigning the Flow
10. Planning and Budgeting: Anticipating the Flow
11. Allocation and Routing: Disciplining the Flow
12. The Value Boundary: Making the Flow Answer
13. Diagnosis and Maturity
14. The Organized Buyer
15. Standing Up the Discipline

### C.3.3 The function-order teaching point

Manifesto order (the order the flow encounters the functions): sourcing, planning/budgeting, metering/attribution, allocation, value-boundary.

Book order (the order the dependencies require): sourcing, metering, attribution, planning/budgeting, allocation, value-boundary. Single deviation from manifesto: metering and attribution before planning and budgeting.

Reason: a budget is a comparison of plan against records; records must exist first. The manifesto itself calls metering the function on which the other four depend. The final exam (C24) grades metering-before-budgeting sequencing, so the book's structure must embody the lesson it grades.

The Part III introduction states the reordering openly in one paragraph as a teaching point: functions listed in the order the flow encounters them, learned in the order their dependencies require.

### C.3.4 The competency-to-chapter coverage map

Every competency maps to at least one chapter. All 24 covered; no orphans; no chapter without competencies.

- C1 → Ch1
- C2, C3 → Ch2
- C4 → Ch3
- C5 → Ch4
- C9 → Ch5
- C6 → Ch6
- C7, C8, C10 → Ch7
- C13 → Ch8
- C14, C15 → Ch9
- C11, C12 → Ch10
- C16, C17 → Ch11
- C18, C19 → Ch12
- C20 → Ch13
- C21, C22 → Ch14
- C23, C24 → Ch15

### C.3.5 The theorem map (one-to-one)

Eight theorems, eight anchor chapters, one-to-one. The mapping was not forced; it emerged from the pedagogy. Chapters 3, 9, 10, 11, 13, 14, and 15 run on lemmas, craft, and integration. Reuse is permitted and expected (for example, THM-004 anchors Chapter 2 and is reinvoked in Chapter 10; THM-006 is foreshadowed in Chapter 6 and anchors Chapter 12).

- **THM-009** → Chapter 1 (the category error)
- **THM-004** → Chapter 2 (the central asymmetry; scaled deployment requires cost governance for economic control)
- **THM-007** → Chapter 4 (the playing field; the provider's problem)
- **THM-002** → Chapter 5 (the anatomy of cost; access price is not total cost)
- **THM-005** → Chapter 6 (the nature of value)
- **THM-008** → Chapter 7 (sourcing economics)
- **THM-010** → Chapter 8 (economic control requires visibility)
- **THM-006** → Chapter 12 (the summit: AI ROI requires both a cost boundary and a value boundary)

### C.3.6 Structural devices (locked)

- Fixed chapter skeleton in all 15 chapters, no exceptions.
- Part-closing cumulative cases: three total (Parts I, II, III), each reaching backward across parts (interleaving). Part IV's role fulfilled by the Ch15 P1 final exam, marked as the book's culminating exercise.
- Worked-example fading: Parts I-II fully worked; Part III completion at Ch7 progressing to unguided at Ch12; Part IV integrative unguided.
- The Founding Questions: posed at the end of Ch3; resolved one per function chapter (Ch7, Ch8-9 jointly, Ch10, Ch11, Ch12); instrumentalized in Ch13; re-asked in Ch15.
- Fifty-year rule: body prose timeless; perishable specifics quarantined in dated cases.

## C.4 The maturity model (locked)

Framework home: Chapter 13. Craft item 13 of 17. Approved by Dan, July 19, 2026. All four design rulings accepted.

### C.4.1 Definition

An organization's AI Operations maturity, within a declared scope, is the highest stage for which it can produce all required evidence artifacts on demand, together with all artifacts of the stages below.

Maturity is a claim about records, not intentions. The evidence artifacts are the book's own craft templates; a maturity claim is therefore checkable in an afternoon.

### C.4.2 Design principles (four rulings, locked)

1. **Strict ladder.** Stages are strictly ordered because the ordering is a dependency fact about records: no other Founding Question is answerable with records until Question 3 (metering and attribution) is. Jagged organizational profiles are preserved in the per-question diagnostic beneath the stage label; the label is the honest compression.
2. **Names.** Unmanaged, Visible, Attributed, Governed, Accountable. Each names what the organization HAS. "Accountable" replaces the placeholder "Optimized": optimization is an unending activity, not a state, and the discipline's summit is the value boundary, not efficiency. Accountable is Question 5's own word.
3. **Governed is a strict bundle.** All three control artifacts (budget, sourcing memo, routing policy) or the stage is not claimed. Sub-stages rejected: memorability is the stage model's job; precision is the diagnostic's job. A strict bundle converts partial progress into a to-do list rather than self-congratulation.
4. **One boundary suffices for Accountable.** Per the manifesto's standard: "somewhere specific, someone is accountable." Coverage fractions rejected as arbitrary. Expanding boundary coverage is continuous work WITHIN Stage 5, never finished, and the model does not pretend otherwise.

### C.4.3 The five stages

**Stage 1: Unmanaged.** No Founding Question answerable with records. The flow runs, cost accrues by default, opinions circulate. The manifesto's opening condition.
Evidence artifacts: none exist.

**Stage 2: Visible.** The first half of Question 3: the organization can say who consumed what.
Evidence artifacts: the consolidated usage record with its coverage test, including a shadow-usage estimate (Ch8 templates: event schema, consolidation architecture, coverage test).

**Stage 3: Attributed.** Question 3 fully answerable: who consumed what, in service of which work. Responsibility has an address.
Evidence artifacts: a chosen and defended attribution basis; the attributed cost statement, that is, the one-page AI operations report (Ch9 templates).

**Stage 4: Governed.** Questions 1, 2, and 4 answerable with records. The three control functions are live. ("Governed" is cost governance in THM-004's sense; one border sentence in Ch13 fences off regulatory AI governance.)
Evidence artifacts, ALL required:
- Forecast-versus-actual by workflow with pre-committed deviation thresholds (Ch10 template).
- A sourcing decision memo showing requirements decomposition and cost-at-volume (Ch7 templates).
- A written routing/priority policy plus at least one documented instance of the policy deciding something under a binding constraint (Ch11 templates).

**Stage 5: Accountable.** Question 5 answerable: somewhere specific, the flow answers for itself.
Evidence artifacts: at least one live value boundary with a completed netting (realized value against fully loaded cost, with limitations stated) and a signed boundary charter naming the owner, cadence, and decision thresholds (Ch12 templates).
Work within Stage 5: expanding boundary coverage, tightening nettings, pruning workflows the nettings condemn. This work does not end.

### C.4.4 The scope rule

Maturity is assessed within a declared scope (enterprise, division, workflow portfolio). Different scopes may legitimately sit at different stages, and precise mixed statements are the intended usage: "Claims processing is Accountable; the enterprise is Visible." This is boundary discipline applied to the model itself.

### C.4.5 Registry grounding (the ladder is proven, not asserted)

- Onto the ladder: LEM-002 (measurement enables visibility); LEM-011 (recorded tokenized activity produces measurable usage).
- Up through Attributed: PROP-046/047 (measured usage associates to entities; attribution enables responsibility assignment); LEM-003 (measured, attributed usage enables rule-based differentiated treatment).
- Opening Governed: LEM-020 (visibility enables management mechanisms); THM-004 (scaled deployment requires cost governance for economic control); THM-010 (economic control requires visibility into the managed boundary).
- The summit: LEM-021 (ROI evaluation requires a measurement boundary); THM-006 (AI ROI requires both a cost boundary and a value boundary).

The stages were designed from pedagogy; the registry proves the ordering is necessary. Chapter 13 states this relationship explicitly; it models the science-and-discipline architecture the book teaches.

### C.4.6 Chapter 13 implications

- Opening case: the false-maturity confrontation. Northmoor T0 at Chapter 13 depth (per Decision 12).
- Craft section: the diagnostic procedure (competency 20). Score each Founding Question as answerable, partially answerable, or unanswerable, with cited artifacts; declare scope; assign stage; name the single highest-yield next move, which the strict ladder makes derivable (it is always the lowest missing artifact).
- The diagnostic packet assessment grades evidentiary discipline. Full-transformation prescriptions fail.
- Chapter 15 dependency: the ninety-day sequence is the ladder walked deliberately (metering first, one rough boundary early for political capital); the day-90 self-assessment uses this model.

## C.5 The Northmoor Dataset (locked design at v1.1)

### C.5.1 Overview and naming history

The book's single recurring constructed dataset, threaded through the problem sets of Chapters 7-12 and 15, and supplying the Chapter 13 diagnostic packet.

Naming history: v1.0 approved as "The Northland Dataset" on July 19, 2026. During research pass 2, a trade-name collision check found that "Northland Apparel" is the operating name of a real embroidery and screen-print business in Moose Lake, Minnesota, plus another small US custom-apparel shop; separately, "Northland Professional" is a real Austrian outdoor apparel brand. The company was renamed to NORTHMOOR APPAREL on July 20, 2026 (per Decision recorded in the naming diligence log), after candidate collision checks eliminated Norfell (Härkilä sells a "Norfell" trouser line), Nordmere (live e-commerce brand), Winterfield (Winterfell cultural echo), and Norhaven (Danish book printer, publishing-adjacent conflict). Design otherwise unchanged; reissued as v1.1.

Standing requirement retained: re-run the collision check before print and include the standard fictional-entity disclaimer in the construction note regardless.

### C.5.2 The company

NORTHMOOR APPAREL: a mid-size apparel brand, roughly 4,000 employees (matching the Ch14 org-design problem's specification), selling through direct-to-consumer e-commerce and a wholesale account channel. Mature, conventional supply chain function (sourcing, inventory, freight) already in place.

Why apparel (Dan's selection, ratified): universally understood; nobody needs the industry explained; rich layered seasonality (SS/FW drops, holiday peak, campaign spikes); real complications (returns, sizing, SKU breadth, channel mix); physical goods; and decisively, apparel is the canonical supply chain teaching industry (Zara et al.), so the manifesto's central analogy (the mature goods-flow discipline versus the absent AI-flow discipline) is mirrored inside an industry where MBA readers have already learned what a mature flow discipline looks like.

### C.5.3 Structural ruling: one company, two moments

The Ch13 diagnostic packet and the Part III dataset are the SAME company at two points in time.
- **T0:** Northmoor is Unmanaged (maturity model Stage 1). This state IS the Ch13 diagnostic packet (org chart, budget lines, dashboard screenshots, three stakeholder transcripts).
- The Ch15 final exam (the ninety-day plan) is the plan that stood up Northmoor's metering.
- Part III's dataset is the twelve months of records that resulted.

No narrative, no characters, no story (per Dan's ruling against a running case): one dataset with a timestamp axis. Payoff: the reader's final exam produces the plan that explains where the numbers they have worked all book came from; the Ch15 CFO briefing compresses a year they personally analyzed.

### C.5.4 The workflow portfolio (five workflows, each engineered to its assessment job)

1. **Inquiry and returns triage.** Classifying inbound contacts (order status, sizing, returns initiation). High-volume, cheap per event. The boring workflow quietly carrying the program. Routing class: bulk tier. Forecast texture: steady base with one known post-holiday bump (deliberately more instructive than flat).

2. **Customer service assist [THE CAPSTONE WORKFLOW].** Direct-to-consumer service center, two quarters into production at netting time. Carries the vendor's "30% productivity improvement" claim.
   - Confound 1: a size-guide overhaul (or sizing revision on a top-selling line) that cut sizing-related contacts. Physical, visible, undeniable.
   - Confound 2: agent attrition (two agents departed in the netting period).
   - Engineered outcome (C18): the 30% claim evaporates under boundary discipline; a smaller, real, defensible number survives.

3. **Supplier contract and compliance review.** Sourcing agreements and factory compliance documents. Lumpy around the sourcing calendar. Few users, enormous documents (heavy tokens per request). Attribution triangle corner 1.

4. **Wholesale sales copilot.** Quoting, assortment, account support for the wholesale team. Grows with a planned account-expansion hiring wave (the Ch10 headcount driver). Many users, moderate usage. Attribution triangle corner 2.

5. **Marketing content studio.** Seasonal drops and campaigns make this genuinely erratic and bursty. Small team, token monsters. Attribution triangle corner 3. Home of the silent prompt-change efficiency failure (a template change tripling tokens per task).

Supporting strands:
- Control failure: an e-commerce engineering team's test loop running against a production API key (Ch10's third variance cause; also Ch8 metering texture).
- Shadow usage: designers and marketers on personal accounts for creative work (Ch8 coverage-test texture; realistic for apparel).
- Providers: two external AI providers plus one internal gateway, imperfect workflow tagging (Ch9's half-cleaned multi-provider export).

### C.5.5 Engineered pedagogical properties (assertions the numerical build must satisfy)

Six properties, asserted by automated checks in the generator.

**A. ATTRIBUTION REORDERING (Ch9, C14).** Workflows 3, 4, and 5 share one account; cost rankings must REORDER under per-token, per-request, and per-seat bases (few users on huge requests, many users on moderate, small team on bursty are the levers). Each basis crowns a different "most expensive team."

**B. THE 62% QUARTER (Ch10, C12).** One quarter runs 62% over aggregate budget from three causes in three workflows: wholesale copilot demand surge from the account expansion (healthy, value question open); marketing studio silent prompt change tripling tokens per task (efficiency failure); engineering test loop on production key (control failure). Decomposition: volume versus intensity versus rate effects.

**C. SEASONAL FORECASTABILITY (Ch10, C11).** Drops, holiday peak, and hiring wave produce a forecast an attentive reader can defend driver-by-driver, with pre-committed anomaly thresholds that the 62% quarter then trips.

**D. ROUTING ECONOMICS (Ch11, C16/C17).** Five task classes map to three capacity tiers; an everything-on-frontier baseline versus policy cost gap large enough to motivate, small enough to be honest. Constraint scenarios: a mid-quarter provider rate-limit cut (40%, two weeks) and a budget-ceiling variant.

**E. THE NETTING (Ch12, C18).** Capstone workflow's fully loaded cost (usage plus review labor plus error incidents plus governance) netted against realized-only value (handle-time and deflection changes with both confounds removed). The vendor claim dies; a smaller true number survives; limitations statable in two sentences.

**F. COMPRESSIBILITY (Ch15, C23).** The year must reduce honestly to three exhibits and 400 words.

### C.5.6 Build specification (deferred session)

- Implement as a seeded Python generator script, not a hand-made spreadsheet: parameters at top; every property A-F asserted by automated checks; regenerate and retune at will during drafting.
- Outputs required:
  - Raw event records (Ch8, Ch9 problems)
  - Half-cleaned multi-provider export (Ch9 opener)
  - Budget and actuals tables (Ch10)
  - Task-class and tier tables (Ch11)
  - Capstone workflow panel (Ch12)
  - T0 diagnostic packet artifacts (Ch13 opener): org chart, budget lines, dashboard screenshots, three stakeholder transcripts
  - Answer keys for every problem-set exercise
- Construction note for the book: data is synthetic, how it was generated, fictional-entity disclaimer.
- Session sequencing: run after this consolidated specification is approved and before Chapter 7 drafting begins.

## C.6 The Case Bank v2.0

The full working case bank sits as a separate document (`AIOM_Case_Bank_v2.md`); this section reproduces its structure and enumerates every case with its placement. Full source-grade notes and primary-source chase list are in the companion document.

### C.6.1 Chapter 4 case shelf: provider mechanism episodes

- **Case 4.1: OpenAI Pro subscription losses (January 2025).** Altman's public statement that Pro loses money because users "use it much more than we expected"; "I personally chose the price and thought we would make some money." Placement: Ch4 opening case; also cited in Ch1 as flat-rate objection evidence.
- **Case 4.2: Anthropic weekly rate limits on Claude Code (July-August 2025).** Weekly caps announced after users ran Claude Code 24/7 and resold access; precursor mini-episode July 17, 2025 (tightening without notice). Placement: Ch4 teaching body (mechanism menu); Ch11 opening case (mid-quarter constraint scenario grounding).
- **Case 4.3: Cursor repricing (June-July 2025).** Flat allotment converted to metered usage mid-subscription; CEO apology; explicit statement of upstream cost pass-through. Placement: Ch1 opening case (paired with 4.6); Ch4 teaching body.
- **Case 4.4: OpenAI service tier menu (current state).** Four processing tiers plus Scale; priority pricing invoked per-request via service_tier parameter. Placement: Ch4 (mechanism menu); Ch11 (routing against real tier structures).
- **Case 4.5: Salesforce pay-per-resolution Agentforce (June-July 2026).** Outcome pricing at approximately $2 per autonomous resolution; provider defines "resolved"; session windows; vendor absorbs consumption risk in exchange for defining the billable unit. Placement: Ch4 teaching body (mechanism menu, dated); Ch6 discussion question.
- **Case 4.6: GitHub Copilot two-act metering migration (June 2025 - June 2026).** Act 1: premium request caps on flat plans with per-request overages. Act 2: full migration for 4.7 million subscribers to token-denominated GitHub AI Credits; base plans unchanged; community projections of 10x to 50x cost increases for agentic power users. Placement: Ch1 opening case (paired with 4.3); Ch4 teaching body; Ch10 (mid-life billing-model change as budgeting shock).

### C.6.2 Chapter 6 case shelf: value, productivity, ROI statements

- **Case 6.1: Klarna claim and correction (February 2024 - May 2025).** The joint OpenAI announcement (2.3M conversations, 700-agent equivalence, $40M projection); the May 2025 Bloomberg correction (headcount changes complicated by attrition and hiring freezes; the announcement's overshoot conceded). Placement: Part I cumulative case (announcement only); Ch6 opener with the reveal framing; Part II cumulative case as the reader's netting exercise; Ch12 P2 as unguided problem. Retired from featured slots after three appearances.
- **Case 6.2: MIT NANDA "The GenAI Divide" (August 2025).** 95% of enterprise GenAI pilots delivered no measurable P&L impact; adoption ubiquitous; deployment mainly boosted individual productivity; shadow AI economy. Handle-with-care protocol: state the method, cite the criticism once. Placement: Ch2 opener; also cited in Ch3 discussion questions and Ch13.
- **Case 6.3: The sort-and-repair specimen set** (six specimens plus reserves and Klarna). JPMorgan/Dimon "$2B benefit against $2B spend"; IDC/Microsoft "$3.7x"; Lumen/Microsoft "$50M in revenue over 12 months"; Microsoft internal Althoff "$500M in call center alone"; Salesforce Benioff "220,000 leads worked, $42M pipeline"; Amazon/Jassy Q code transformation "$260M annualized, 4,500 developer-years"; reserves (Honeywell FTE equivalence, Finastra cycle time). Placement: Ch6 teaching body (walked as the classification exercise); Ch6 problems (assessment 6 sort-and-repair).
- **Case 6.4: Brynjolfsson, Li, Raymond, "Generative AI at Work," Quarterly Journal of Economics, May 2025.** 5,172 customer-support agents; 15% average productivity gain (issues resolved per hour); heterogeneity honestly reported (novice/low-skilled ~30% in speed and quality; most experienced with small quality declines); improved customer sentiment; higher agent retention; limitations stated. The book's honest-boundary exemplar. Placement: Ch6 teaching body section 6.5 (introduction); Ch12 opening case at full depth (the summit anchor); Ch12 P2 completes the ROI netting the study did not perform (migrated from Part II per Decision 7).

### C.6.3 Chapter 5 case shelf: cost anatomy episodes

- **Case 5.1: Air Canada v. Moffatt (February 2024).** BC Civil Resolution Tribunal awards C$812.02 after finding the airline's chatbot negligently misrepresented bereavement fare policy; the "separate legal entity" defense called "a remarkable submission" from the bench. Placement: Ch5 teaching body as the error-cost anchor (moved from opener slot per Decision 6).
- **Case 5.2: Shadow AI and the invisible flow (2023-2026 pattern).** IBM 2025 Cost of a Data Breach ($670K higher for shadow-AI-involved breaches); IDC 2025 unauthorized-tool adoption (56% vs 23% governed); Samsung 2023 episode. Placement: Ch8 opening case.
- **Case 5.3: The price paradox (2021-2026), extended.** Three findings.
  - Long-horizon deflation: Epoch AI shows the price to reach a fixed performance level fell between 9x and 900x per year at fixed capability; a16z LLMflation estimates ~10x per year; academic follow-on estimates ~10x per year with rising tokens per task (~18x per year).
  - Same-day dispersion: OpenRouter's public catalog documents 987 models across 69 infrastructure providers; for Llama 3.3 70B, input pricing across serving providers ran roughly 10x from cheapest to most expensive on the same day; default router selects per request by inverse-square of price and reroutes when providers change rates mid-flight.
  - Rising bills: enterprise AI spend rose across the same period; State of FinOps 2026 shows 98% of practitioners now manage AI spend, up from 31% two years earlier.
  - Formal framing: unit price of capability deflates on a long horizon, disperses across providers on any given day, and consumption per task inflates. Net spend direction is a portfolio property, not a market constant. The manifesto's PMT claim is fully replaced by this three-sided finding.
Placement: Ch5 opening case (per Decision 6); Ch10 (variance decomposition grounding).

### C.6.4 Chapter 7 case shelf: switching economics

- **Case 7.1: GPT-4o double deprecation (August 2025 - April 2026).** August 7, 2025: removal without notice at GPT-5 launch; backlash and Change.org petition passing 20,000 signatures; Altman acknowledges "underestimated how much some of the things that people loved about 4o mattered"; access restored within days. January 29, 2026: formal retirement announcement, effective February 13, 2026; staged extensions through April 3, 2026. GPT-5.1 subsequently retired March 11, 2026. Placement: Ch7 opening case; Ch14 negotiation dossier (deprecation notice terms).

### C.6.5 Chapter 14 case shelf: the FinOps boundary treaty material

- **Case 14.1: State of FinOps 2026 (February 2026).** Sixth annual survey, 1,192 practitioners representing $83B+ in annual cloud spend, published February 19, 2026: 98% now manage AI spend (up from 63% in 2025, 31% in 2024); "FinOps for AI" the top forward-looking priority; AI cost management the #1 skillset (58% planning to add); granular AI-spend monitoring the #1 requested tooling capability (commercial tooling has not delivered); 78% of teams report to CTO/CIO, only 8% to CFO; the Foundation formally rewrote its mission from managing the value of cloud to managing "the value of technology" in February 2026; practitioner quote in the report: "Is your AI providing value? No one can answer that question yet"; separately reported: ~73% of organizations report AI costs exceeding original budget planning. Placement: Ch14 opening case (full depth); Ch10 opening case (narrow slice on the 73% budget-overrun finding); Ch3 opening case (mission rewrite as border-drawing evidence); Ch15 opening case (FinOps founding story as structural analog, using different content from the same source body).

### C.6.6 Balance flag status

The Case Bank v1.0 flagged a bank skewed cautionary and required a well-documented positive value-realization case. Case 6.4 (QJE anchor) and specimen F (Amazon Jassy) closed this flag. The book now teaches measurement, not pessimism: the strongest positive evidence in the public record is precisely the evidence with the most honest boundary, which is the book's thesis performed by the literature.

### C.6.7 Case reuse policy

Cases may be reused across chapters where reuse serves the pedagogy. Reuse rules:
- A case reused as an opener in more than one chapter is presented from a different angle in each (e.g., Klarna: announcement only in Part I close, correction reveal in Ch6 opener, netting attempt in Part II close).
- No case is featured more than three times as a primary source in featured slots (openers, worked examples, cumulative cases). Klarna hit the ceiling at three; it now appears only in the Ch12 P2 problem set.
- A dated box treatment (single-paragraph reference inside a teaching body subsection) is not a featured slot and does not count against the ceiling.
- Every reuse must add pedagogical value not achievable by a different case; when the value is achievable elsewhere, use elsewhere.

---

# PART D: THE CHAPTER-LEVEL OUTLINES

Each of the fifteen chapters is outlined against the fixed six-slot skeleton. Every embedded decision has been ruled and is recorded inline. This part reproduces the full outline as approved, so a reader who has not seen the working outline documents can read the entire chapter-by-chapter plan here.

Structural devices reprised for orientation before Part D begins:
- Every chapter has the six slots: Opening case, Teaching body, Craft section, Chapter summary, Key terms, Discussion questions and problems.
- Every chapter serves at least one competency; every competency is served (see C.3.4).
- Anchor theorems attach to eight chapters one-to-one (see C.3.5); the other seven chapters run on lemmas, craft, and integration.
- Founding Questions posed at Ch3 close; resolved once each in Ch7-Ch12; instrumentalized in Ch13; re-asked in Ch15.
- Registry pulls (verbatim theorem, lemma, or Founding Question text) are marked [REGISTRY PULL] and enumerated in Part H.

## D.1 Part I: The Argument

Purpose: the reader learns why the discipline must exist. Founding Questions posed at part's end, deliberately unanswerable yet.

### CHAPTER 1: The Category Error

**Big idea:** deployed AI use is resource consumption, not software access.
**Competency:** C1.
**Anchor theorem:** THM-009 [REGISTRY PULL].
**Prepares assessment:** 1 (CIO memo reply defending consumption economics against the strongest flat-rate objection); seeds assessment 7 (board-member essay).

#### Slot 1: Opening case
Cases 4.3 (Cursor) and 4.6 (GitHub Copilot) together, told from the buyer's seat. Within roughly twelve months, the two most widely used AI coding subscriptions both abolished flat pricing. Cursor (June 2025): the $20/month allotment became metered usage at API rates mid-subscription; allowances vanished in a few prompts; surprise charges arrived; the CEO apologized while explaining that his own upstream costs left no choice. GitHub Copilot (June 2025 to June 2026): first monthly caps on previously flat requests, then, for 4.7 million paid subscribers, the abolition of flat requests entirely in favor of token-denominated credits. One vendor with an apology, one in two acts, the same correction. The case opens with the buyer's experience of the surprise bill and closes on the category error itself, stated rather than asked. [AMENDED 2026-08-05, Ch1 Stage 1: the original wording directed a closing question, which the standing rule against rhetorical questions in body prose forbids. Ruled: whatever is more effective inside the chapter wins, and a statement lands harder here than a question the reader cannot answer yet.] The pairing converts anecdote into pattern and preempts the "one badly run startup" dismissal.

#### Slot 2: Teaching body
1.1 The purchase that is not one. The software access model the buyer brought to the transaction: licenses and seats, near-zero marginal cost of use, cost fixed at signature. Against it, what the organization actually operates: work that consumes a metered resource on every task. The mental model determines what gets managed; the wrong model manages the wrong thing.

1.2 The consumption event. The atomic unit of the discipline defined: a request that consumes computational resource, metered in tokens or their equivalents, at a per-event cost greater than zero. Anatomy of one event: what goes in, what comes back, what the meter records, who holds the record. FIGURE 1.1: anatomy of a consumption event. FIGURE 1.2: two purchase models side by side (seat model, flat line regardless of use; event model, cost as the integral of consumption). [AMENDED 2026-08-05, Ch1 Stage 1: the numbering is the reverse of this document's original, so the figures carry the numbers they appear in. The anatomy is introduced first and the comparison follows it.]

1.3 The flat-rate objection, answered. The strongest objection stated at full strength: "we pay $30 per seat per month; for us this IS software." The reply the reader must be able to make: a flat rate relocates the meter, it does not abolish it. The provider meters what the buyer declines to see; skewed usage makes the arrangement unstable; the correction arrives on the provider's schedule. THM-009 anchoring callout here [REGISTRY PULL]. Evidence in dated case boxes: the January 2025 OpenAI Pro admission (Case 4.1); the July 2025 Anthropic limits (Case 4.2, one paragraph); the opener's Cursor and Copilot episodes re-engaged as the objection's empirical refutation.

1.4 What follows if this is true. Resources that flow get flow disciplines: the reader already knows this from goods. The supply chain analogy stated in its timeless form: a mature discipline exists for physical flows (sourcing, planning, tracking, allocation, accountability); no equivalent yet exists for this one. The stakes: the rest of the book.

1.5 What this book is not. One paragraph: no model internals, no prompt engineering, no use-case ideation. Full border-drawing deferred to Chapter 3.

#### Slot 3: Craft section
The consumption-event inventory. Procedure: given a deployment description, (1) enumerate the event types the deployment generates; (2) identify each type's resource drivers (input tokens, output tokens, calls, retrieval, tool invocations); (3) locate the meter (provider side, and note what the buyer currently receives instead: an invoice); (4) state what the inventory reveals that the seat count conceals. Fully worked example on the QJE contact-center deployment description (Case 6.4), which quietly introduces the study two chapters before its Ch6 anchor role.

#### Slot 4: Chapter summary
The category error named; the consumption event defined; the flat-rate objection answered by meter relocation; the flow-discipline stakes set.

#### Slot 5: Key terms
Consumption event; resource consumption; software access model; access price; metered resource; flat-rate objection; meter relocation.

#### Slot 6: Discussion questions and problems
Discussion (self-explanation register), four questions: why a per-seat contract does not make AI a seat-priced good; what the Cursor and Copilot episodes reveal about where the meter was all along; why the event rather than the user or the task is the atomic unit, argued from the other side; construct the strongest version of the flat-rate objection yourself, then answer it. [AMENDED 2026-08-05, Ch1 Stage 1: a fourth question added, making the reader argue for the task as the unit. It answers craft finding F7, which held that 1.2 asserted the choice of unit rather than arguing it.]
Problems (fully worked): (P1, worked) model CIO memo reply per assessment 1, with annotated reasoning; (P2, worked) consumption-event inventory on a second deployment; (P3, completion) inventory with the event-type column blank. [AMENDED 2026-08-05, Ch1 Stage 1: P2 no longer requires a CITED deployment. The evidence policy governs empirical claims, not exercise scaffolding, and P3 is constructed for the same reason.] Interleaving: none yet (first chapter).

---

### CHAPTER 2: The Flow

**Big idea:** AI runs as three flows (usage, records, cost-and-value); unmanaged flows degrade; cost accrues by default, value only by design.
**Competencies:** C2, C3.
**Anchor theorem:** THM-004 [REGISTRY PULL].
**Prepares assessments:** 2 (three-flow mapping, recurring across the book) and 3 (asymmetry derivation plus spot-the-error).

#### Slot 1: Opening case
Case 6.2, MIT NANDA (August 2025), the market-wide portrait: mass adoption, more than eight in ten organizations piloting, roughly 40% deploying, and 95% of enterprise GenAI pilots showing no measurable P&L impact, alongside a thriving shadow-AI economy. Told per the handle-with-care protocol: the report's own text, method stated plainly, criticism's existence cited once. The case closes on the chapter's question: how can adoption be everywhere and value be invisible? The answer requires seeing deployment as three flows, only one of which runs by itself. (NANDA is reused in Ch13 as the Stage 1 market portrait; Shadow AI, Case 5.2, stays reserved for Ch8.)

#### Slot 2: Teaching body
2.1 From event to flow. Chapter 1's atomic unit aggregated: a deployment is a continuous flow of consumption events, with volume, composition, and seasonality. The flow runs whether or not anyone watches it.

2.2 The three flows defined. Usage (events occurring); records (what is written down about them, by whom, where); cost-and-value (what the events cost and what they return). FIGURE 2.1: the three-flow diagram. **Signature figure.** This diagram is the book's recurring diagnostic image; it is designed once here and reused in every mapping through Chapter 15, so it carries the design weight of a signature figure.

2.3 The default states. Usage flows by default. Cost accrues by default (every event is billed whether or not it is seen). Records do not accrue by default on the buyer's side: the provider holds event-level records; the buyer holds invoices. Value does not accrue as knowledge by default under any arrangement: it must be designed for. THM-004 anchoring callout [REGISTRY PULL]; load-bearing lemma quotes where the registry supplies them (candidates from the maturity model grounding: LEM-002, LEM-011) [REGISTRY PULL].

2.4 The central asymmetry, derived. Cost by default, value by design; therefore an unmanaged flow collects all of the cost and an unknown fraction of the value. The derivation walked stepwise, fully worked, because assessment 3 grades exactly this prose. Why "unknown" is the damning word: not "zero" (the deployment may be succeeding) but "unknown" (the organization cannot distinguish success from waste, so it can neither defend the spend nor cut it with reason). Both errors, expansion and retrenchment, become equally available and equally unjustified.

2.5 How unmanaged flows degrade. Three timeless degradation channels, seeded here as vocabulary and reused through Chapter 10: demand-driven change (the flow grows because work grew), efficiency-driven change (the flow grows because tasks silently got heavier), control-driven change (the flow grows because something runs that nobody decided to run). No numbers yet; the Northmoor 62% quarter will instantiate all three.

2.6 Evidence. The opener re-engaged: NANDA's profile is the asymmetry at market scale. The price paradox (Case 5.3) in a dated box: unit prices fell 9x to 900x per year at fixed capability while intensity per task rose, and on any given day the same model is served by dozens of providers at prices spanning roughly 10x; falling and dispersed prices do not manage a flow, and a buyer who plans on rate alone misforecasts systematically. Shadow-usage pattern cited (Case 5.2, brief; full treatment Ch8).

#### Slot 3: Craft section
The three-flow mapping. Procedure: given a deployment, (1) draw the usage flow (event types from the Ch1 inventory, volumes if known); (2) draw the record flow (what is captured, at what grain, held where, visible to whom); (3) draw the cost-and-value flow (what is billed, what is measured as return); (4) diagnose each flow as managed or unmanaged with one sentence of evidence each. Fully worked on the QJE contact-center deployment (Case 6.4): the rare public example where the record flow was genuinely managed, which lets the worked example show what "managed" looks like rather than only its absence. Problems then map poorly instrumented deployments for contrast.

#### Slot 4: Chapter summary
The three flows; the default states; the asymmetry and its derivation; the three degradation channels; the mapping as recurring diagnostic.

#### Slot 5: Key terms
Usage flow; record flow; cost-and-value flow; central asymmetry; unmanaged flow; shadow usage; demand-driven, efficiency-driven, and control-driven change.

#### Slot 6: Discussion questions and problems
Discussion: explain to a skeptic why "unknown fraction" is worse for decision-making than "zero"; which of the three flows does an invoice belong to, and why the answer is instructive; why does the record flow not accrue by default when the provider records everything?
Problems: (P1, worked) three-flow mapping per the craft section; (P2, worked) asymmetry derivation with model prose; (P3, completion) spot-the-error on three real cited statements drawn from Case 6.3 specimens: claimed-as-realized (Specimen C, the hours-to-revenue conversion), netting-against-access-price (constructed from Specimen A's benefit-versus-spend juxtaposition), adoption-as-value (Specimen E's activity metrics); (P4, completion) three-flow mapping with the record flow left blank. Interleaving: P4's deployment reuses the Ch1 P2 deployment, so the reader's own earlier inventory becomes input.

---

### CHAPTER 3: A Science and Its Discipline

**Big idea:** AI Business Economics is the science; AI Operations Management is the discipline that acts on it.
**Competency:** C4. No single anchor theorem; contains the trace set piece.
**Prepares assessment:** 4 (registry literacy, tested later on THM-008 unseen). Poses the Founding Questions; draws the borders; closes Part I with the cumulative case.

#### Slot 1: Opening case
Case 14.1 excerpted for this chapter's purpose: in February 2026 the FinOps Foundation, a discipline built for cloud cost, formally rewrote its mission from managing the value of cloud to managing the value of technology, with 98% of its practitioners now managing AI spend (up from 31% two years earlier) and its practitioners telling the survey that no one can yet answer whether the AI is providing value. The case dramatizes the vacancy: adjacent disciplines are being pulled toward territory none was built for, and the pull is measurable. The territory needs its own science and its own discipline, named. (The full FinOps treatment, including the boundary treaty, remains Ch14's; this opener uses only the mission rewrite and the arc.)

#### Slot 2: Teaching body
3.1 Why name a science. What "science" claims here: an ordered body of conditional, testable propositions about the business economics of AI consumption, not a metaphor. The registry introduced: 200 propositions, 20 lemmas, 8 theorems, arranged as a dependency graph in which every higher claim rests on stated lower ones. The governing relationship stated plainly: the registry justifies this book; it does not organize it. Pedagogy ordered the chapters; the registry proves the claims.

3.2 The trace set piece. Subject: THM-004, the theorem the reader accepted one chapter ago. Walk it down: theorem to its supporting lemmas to representative propositions [REGISTRY PULL for the exact chain; the maturity model's grounding section indicates THM-004 rests on territory including LEM-020]. The reasoning for this choice: the trace is performed on a claim the reader already believes, so the only new cognitive load is the machinery itself; assessment 4 then tests the machinery cold on THM-008, which the reader will not have seen traced. FIGURE 3.1: the dependency trace as a tree, theorem at top, propositions at the leaves.

3.3 How to read a formal claim. Conditions (when the claim applies); scope (what it quantifies over); non-claims (what it deliberately does not establish); falsification (what evidence would defeat it). The "word games" objection answered: formalization is not decoration; it is the commitment that fixes what would count as being wrong, which is precisely what executive discourse about AI currently lacks.

3.4 The discipline. AI Operations Management defined: the practice that acts on the science. The five functions previewed, each in one paragraph, as what an organization must be able to DO: source the capacity, plan and budget its consumption, meter and attribute the usage, allocate under constraint, and hold value accountable at a boundary. (Function ordering pedagogy is deliberately absent here; the Part III introduction owns that one-paragraph teaching point.) FIGURE 3.2: the two-layer architecture, science below, discipline above, five functions as the load-bearing columns.

3.5 The borders. Four neighbors, each treated with the same two sentences: what it is for, and what it lacks for this territory. AIOps (IT operations telemetry: watches systems, not economics). MLOps (model lifecycle engineering: ships models, does not govern their consumption). FinOps (cloud cost management: the nearest neighbor, mid-expansion per the opener; owns spend plumbing, lacks the value side; the full treaty is Chapter 14's). Regulatory AI governance (one fence sentence, per the standing one-sentence policy). Presented as a table rather than a figure, per Mayer coherence: the content is categorical, not spatial.

3.6 The Founding Questions posed. The five questions stated verbatim [REGISTRY PULL / manifesto pull], each paired with the function that will earn its answer and the chapter where that happens. Then the part's closing move, stated without drama: the reader cannot currently answer any of them with records, and neither can most organizations on earth; Parts II through IV exist to change that. Part I ends.

#### Slot 3: Craft section
The trace procedure. Numbered steps: (1) locate the claim in the registry; (2) restate its conditions in one sentence; (3) list its stated dependencies; (4) walk one level down and restate each dependency; (5) state what the claim establishes and, separately, what it does not; (6) state what evidence would falsify it. Fully worked on the THM-004 chain from 3.2.

#### Slot 4: Chapter summary
The two-layer architecture; the registry and its role; the trace machinery; the five functions previewed; the borders drawn; the Founding Questions on the table, unanswered.

#### Slot 5: Key terms
AI Business Economics; AI Operations Management; registry; theorem, lemma, proposition; dependency; condition; non-claim; falsification; the Founding Questions; the five functions (each named).

#### Slot 6: Discussion questions and problems, plus the Part I cumulative case
Discussion: why does the book insist the registry justifies but does not organize it, and what would go wrong under the reverse; which border is hardest to defend and why; restate one Founding Question in your CFO's language without losing its content.
Problems: (P1, worked) full trace on THM-004 per the craft section; (P2, completion) trace on a second theorem with steps 4 and 5 blank [theorem choice at drafting; candidate THM-002, which Part II is about to teach, making the completion problem double as a preview]; (P3) the "word games" objection assigned as a one-page reply.

**PART I CUMULATIVE CASE.** Subject: Klarna, February 2024 public record only (the announcement, before the correction). The reader performs, in sequence, the consumption-event inventory (Ch1), the three-flow mapping with per-flow diagnosis (Ch2), and then poses all five Founding Questions against the public record, documenting that not one is answerable from it (Ch3). Payoff engineered for Chapter 6: when the correction arc is revealed there, the reader has already discovered its predictability from the flows alone. The cumulative case thereby teaches Part I's whole argument on one page of evidence and sets the Klarna reprise without narrative apparatus. CONSEQUENCE FOR CH6: Chapter 6's opener presents the Klarna arc as the completion of the reader's own Part I analysis (the reveal framing), not as a fresh case.

---

## D.2 Part II: The Science

Purpose: what is true, before what to do. Fully worked examples throughout.

### CHAPTER 4: The Playing Field

**Big idea:** providers carry variable cost against often-fixed revenue; the resolution mechanisms (meters, tiers, limits, priority pricing) are economically derivable, not vendor pathologies.
**Competency:** C5.
**Anchor theorem:** THM-007 [REGISTRY PULL].
**Prepares assessment:** 5 (stylized provider model with predicted mechanisms and one mapped documented episode).

#### Slot 1: Opening case
Case 4.1, OpenAI's Pro subscription losses (January 2025). Sam Altman states publicly that OpenAI is losing money on the $200/month Pro plan because "people use it much more than we expected," and adds "I personally chose the price and thought we would make some money." The strongest possible opener for this chapter: the CEO of the industry's flagship provider conceding, in the first person, that the flat rate his own team set collided with the resource reality underneath. From that admission the chapter derives, rather than asserts, the mechanism menu that would rationally follow.

#### Slot 2: Teaching body
4.1 The provider's problem. Every consumption event the buyer generates costs the provider real resources: compute, memory, energy, network. Under flat-rate pricing, provider revenue is fixed at signature while provider cost is a function of buyer behavior the provider does not control. Set up as the mirror image of Chapter 1: what looked from the buyer's seat like a purchase looks from the provider's seat like an obligation of unknown magnitude.

4.2 The usage distribution problem. FIGURE 4.1: skewed usage under flat pricing (long-tail histogram of monthly consumption per subscriber against a horizontal revenue line). The key observation the assessment tests: under skewed usage, the mean subscriber may be profitable while the top percentiles alone consume the pool. Introduces the "unprofitable subscribers" quantity: given a subscriber-consumption distribution, the fraction whose consumption exceeds break-even. Fully worked example: given a stylized distribution and a per-event cost, compute unprofitable subscribers, expected loss per subscriber, and total loss per 10,000 subscribers.

4.3 The predictable mechanisms. Derived, not catalogued. Given the provider's problem, a rational provider adopts, in an order predictable from cost and reversibility: (a) meters (make consumption visible per subscriber, the precondition of every other move); (b) tiers (create price bands aligned to consumption bands); (c) limits (cap the top percentiles that break the pool); (d) priority pricing (segment latency and reliability as separately purchasable goods); and, most recently in the market, (e) outcome pricing (invert the risk: absorb variable cost in exchange for defining the billable unit). THM-007 anchoring callout here [REGISTRY PULL].

4.4 The mechanism menu, evidenced. Each mechanism carries one dated case box, in the order derived above.
- Meters and tiers: OpenAI's four processing tiers (Case 4.4, dated); the buyer-side implication is a shipped API parameter the reader can inspect.
- Limits: Anthropic's July-August 2025 Claude Code episode (Case 4.2, dated), including the mid-quarter tightening without notice (the precursor that Ch11 will reuse as a constraint scenario).
- Priority pricing: also 4.4, the Priority tier alongside Flex and Batch.
- Outcome pricing: Salesforce's June 2026 pay-per-resolution Agentforce Help Agent (Case 4.5, dated), including the interview clarification that the vendor defines what "resolved" means.
- Full-market conversions of flat to metered: Cursor's June-July 2025 apology (Case 4.3) and GitHub Copilot's two-act migration from premium requests to AI Credits (Case 4.6). These two together demonstrate the derivation running to completion across the two most widely used AI coding subscriptions inside twelve months, and preempt the "one badly run startup" dismissal.

4.5 The buyer implications, in one paragraph. The chapter is provider-side by design (per the buyer-side-spine standing decision, Chapter 4 is where the provider appears exactly once); but the buyer implications must be named so the reader is not left with a spectator's essay. They are the seed of Parts III and IV: if the mechanisms are predictable, they are contract-able; if the meters exist, the meters are duplicable on the buyer's side; if outcomes are the new billable unit, the buyer's ability to define outcomes is the new leverage. Each is deferred to a named later chapter (7, 8, 14).

#### Slot 3: Craft section
The stylized provider model. Procedure: given per-event cost c, subscription price p, and a consumption distribution F(x), (1) compute the break-even consumption x* = p/c; (2) compute the fraction of subscribers with x > x* (the unprofitable set); (3) compute the expected profit per subscriber and the expected total profit per 10,000 subscribers; (4) predict, from the shape of the loss, which mechanisms rational management adopts first; (5) map one dated real episode onto the prediction. Fully worked on a generic stylized distribution (per Decision 5: Part II is kept fully independent of the still-unbuilt Northmoor; the dataset's first appearance stays at the top of Part III with the construction note, and the Northmoor numerical build session retains its degrees of freedom).

#### Slot 4: Chapter summary
The provider's problem stated; the usage distribution problem quantified; the mechanism menu derived (not asserted) in order of adoption; each mechanism grounded in a dated real episode; the buyer implications named as later-chapter seeds.

#### Slot 5: Key terms
Fixed revenue against variable cost; usage distribution; unprofitable subscriber; break-even consumption; meter, tier, limit; priority pricing; outcome pricing; mechanism menu.

#### Slot 6: Discussion questions and problems
Discussion: why is a meter the precondition of the other mechanisms; explain the Cursor and Copilot arcs to a colleague who thinks "AI is like software"; state the strongest argument for outcome pricing from the provider's side and from the buyer's side; the reversal test setup: under what usage distribution would a flat rate be sustainable, and does that distribution describe the market you have seen?
Problems (fully worked): (P1, worked) full assessment 5 walk-through on a given distribution and one mapped episode; (P2, worked) reversal-test computation for a specified sustainable-flat-rate distribution; (P3, completion) mechanism-adoption prediction given a described provider position. Interleaving: P1's mapped-episode step reuses the Ch1 buyer-seat framing on Cursor or Copilot to close the buyer-provider loop.

---

### CHAPTER 5: The Anatomy of Cost

**Big idea:** access price is not total cost; exposure accumulates without decisions.
**Competency:** C9.
**Anchor theorem:** THM-002 [REGISTRY PULL].
**Prepares assessment:** 9 (TCO assembly from scattered internal facts; first-year versus steady-state; multiple over access price).

#### Slot 1: Opening case
Case 5.3, the price paradox, told in three findings.
- Long horizon: Epoch AI's analysis shows the price to reach a fixed performance level fell between 9x and 900x per year at fixed capability from roughly 2021 to 2026.
- Any given day: OpenRouter's public catalog documents that a single model, served by many infrastructure providers at once, carries a price band across providers on the same day (for Llama 3.3 70B, roughly 10x from cheapest to most expensive serving provider in mid-2026), with the router selecting a provider per request and rerouting when providers change rates mid-flight.
- The bills: over the same period, enterprise AI spend rose, agentic workflows multiplied tokens per task, and (per the State of FinOps 2026) 98% of surveyed practitioners now manage AI spend, up from 31% two years earlier.

The case dramatizes the thesis in a single opening: unit price collapsed on a long horizon, disperses roughly 10x across serving providers on any given day, and total exposure rose across the same period. That cannot happen if access price is total cost. The chapter then broadens outward through the ledger to explain what the invoice does not price. Air Canada (Case 5.1) lands full-force in the teaching body as the error-cost anchor rather than as opener.

#### Slot 2: Teaching body
5.1 What the invoice does not price. The invoice charges for access to the model. The organization pays for everything else that the deployment requires, whether it recognizes it or not. This is the thesis in one sentence; the rest of the chapter categorizes the everything else.

5.2 The TCO ledger. FIGURE 5.1: the ledger structure, six cost categories arrayed against the access price for scale. The six categories, each defined with a real cited grounding:
- Access cost. What the invoice shows. The reference line, not the ledger.
- Integration cost. Wiring the model into the workflow: connectors, retrieval infrastructure, evaluation harnesses, prompt and template maintenance. Grows with the number of workflows and providers touched.
- Operation cost. Running the deployment: engineering effort per model migration, template drift maintenance, incident response. Grounded on the Ch7 forced-migration episode (Case 7.1, GPT-4o double deprecation) previewed here as evidence that "operation" is not a one-time integration.
- Review cost. Human labor consumed by the AI's output: quality review, editing, correction, escalation. Grounded on the QJE study's observation that the top of the skill distribution saw small quality declines with AI assistance, making review labor a nonzero item on any serious ledger. This is the item most often omitted, because it appears on payroll rather than on the AI budget.
- Error cost. What errors produced by the deployment cost the organization. Air Canada (Case 5.1) is the anchor: a court-quantified single-instance number, with an argument for the population-scale item (PROP-156-160 territory [REGISTRY PULL]). Included here rather than tucked into risk chapters because errors cost money and the ledger must show them; regulatory and governance detail stays deferred to Ch14's border.
- Governance cost. The overhead of having the discipline the book teaches: metering infrastructure, attribution work, review of the reviews. The book's own machinery, priced honestly.
THM-002 anchoring callout at the ledger figure [REGISTRY PULL].

5.3 First year versus steady state. The ledger's shape changes over time. Integration is front-loaded; operation and review scale with volume; error and governance track deployment breadth. FIGURE 5.2: stacked ledger over three time horizons (month 1, year 1, year 3). The point the assessment tests: the access-price multiple that describes total cost is not one number but a function of horizon.

5.4 The price paradox, closed. Return to the opener with the ledger in hand. Long-horizon deflation lowers one bar in the ledger; same-day price dispersion across serving providers means the access-price line is not even a scalar to lower (a buyer who states "the price of X is $Y" has already misdescribed the object); intensity growth raises usage-linked bars; expansion raises everything else. The direction of total exposure is a portfolio property, not a market constant. The Ch10 variance decomposition (volume, intensity, rate) is previewed here as the discipline that reads such portfolios; the routing decisions that exploit the same-day dispersion are named as Ch11 territory.

5.5 Shadow AI, as a ledger item. Case 5.2 in a dated box: IBM's 2025 finding that breaches involving shadow AI averaged $670,000 higher than other incidents; unauthorized-tool adoption exceeding governed-tool adoption in an IDC survey; the Samsung 2023 canonical episode. The ledger extension: unmetered activity generates cost in categories the ledger cannot see, and the coverage test (Ch8) is the way the ledger closes.

#### Slot 3: Craft section
The TCO ledger, as a reusable checklist. Procedure: given a deployment described only by its access price and a scattered set of internal facts, (1) populate each of the six categories with a defensible line item and its source; (2) mark first-year versus steady-state; (3) compute the ledger multiple over access price at each horizon; (4) name the two most uncertain items and state what evidence would tighten them. Fully worked on a small hypothetical assembled from cited-source line items.

#### Slot 4: Chapter summary
The invoice does not price the deployment; the ledger names what does; the ledger's shape moves over time; falling unit prices do not settle the total-cost direction; the ledger extends to cover shadow usage.

#### Slot 5: Key terms
Access cost; integration cost; operation cost; review cost; error cost; governance cost; total cost of ownership (TCO); access-price multiple; first-year cost; steady-state cost; shadow cost.

#### Slot 6: Discussion questions and problems
Discussion: which category is your organization most likely to leave off, and why; explain how a 10x access-price drop could coincide with a total-cost rise; state a defensible upper bound on the review-cost item for a specified deployment and defend the bound; how does the Air Canada award set a per-error prior for a deployment ten thousand times its volume?
Problems (fully worked): (P1, worked) assessment 9 in full: TCO assembly from scattered internal facts on a described deployment, first-year vs steady-state, ledger multiple; (P2, worked) sensitivity: given a plausible range for the review-cost item, produce the ledger's low, central, and high estimates; (P3, completion) TCO assembly with the error and governance rows blank. Interleaving: P1's deployment reuses the Ch2 three-flow mapping's target, so the reader operates on continuous evidence.

---

### CHAPTER 6: The Nature of Value

**Big idea:** claimed value, realized value, productivity, and ROI are four different things; only boundaries produce honest numbers.
**Competency:** C6.
**Anchor theorem:** THM-005 [REGISTRY PULL]. Foreshadows THM-006 (the Ch12 summit).
**Prepares assessments:** 6 (sort-and-repair) and 7 (essay pair: category error to a board member; then the reversal test).

#### Slot 1: Opening case
Per Part I's committed reveal framing: the Klarna arc, completed. The chapter opens by returning to the Klarna announcement the reader analyzed at Part I's close. The reader's own diagnosis is recalled: not one Founding Question was answerable from the February 2024 announcement, and the value flow was designated unmanaged. Then the correction arc is revealed: May 2025, Bloomberg, CEO Sebastian Siemiatkowski tells the story of what actually happened, the cost-cutting overshoot, the reversal, the human agents being rehired, the headcount narrative complicated by attrition and hiring freezes rather than replacement. The reader learns the correction was predictable from Part I alone: an unmanaged value flow yields an unknown fraction of the announced value, so the announcement had to be corrected downward when observation caught up. The chapter's thesis: distinguishing what Klarna announced, what actually happened, what improved, and whether the improvement paid for itself is not journalism; it is the technique the rest of the chapter teaches.

#### Slot 2: Teaching body
6.1 Four things that look alike. FIGURE 6.1: the value quadrant. Two axes, four cells, defined:
- Claimed value: what the deployment says it produced (a statement).
- Realized value: what the deployment did produce, according to observation with a stated method (a measurement).
- Productivity: rate of output per unit of input (an operational quantity).
- ROI: realized value net of fully loaded cost, inside a declared boundary (a decision quantity).
The chapter's central move: these are not synonyms, they are not ordered along a single quality axis, and confusing any two is the error 6.3 diagnoses.

6.2 Why a productivity claim never establishes ROI. The gap named specifically: productivity is a rate; ROI is a netting. A 30% productivity claim can coexist with negative ROI (review cost, error cost, and governance cost may exceed the value of the freed time; the freed time may not be reallocated to value-producing work; the confounds may have been physical rather than AI-driven; the boundary period may be shorter than the payback period). Each failure mode illustrated with one line from a cited specimen (from the Case 6.3 sort-and-repair set, previewed here as motivation).

6.3 Boundaries produce honest numbers. The boundary as a technical object, defined by four elements: (a) scope (one workflow, or a named set); (b) period (a defined interval with start and end); (c) outcomes (which specific measurements count as value); (d) confounds handled (what would otherwise be attributed to the deployment must be netted out). THM-005 anchoring callout [REGISTRY PULL]. The pointer forward: THM-006 (the summit) will formalize that ROI requires both a cost boundary AND a value boundary, and the Ch12 value-boundary worksheet operationalizes the whole apparatus.

6.4 What the market publishes. The specimen set walked from Case 6.3, in the classification quadrant. Each specimen labeled by category, its boundary elements catalogued (present, missing, ambiguous), the repair sketched. The specimens, treated in this order for pedagogy:
- Specimen A: JPMorgan, "$2B benefit against $2B spend." Realized-value claim with a rare cost side but no boundary; the accidental netting; the missing period and method.
- Specimen B: IDC/Microsoft "$3.7x." ROI claim whose evidence unit is an opinion selected from a menu; methodology transparency as a repair path.
- Specimen C: Lumen/Microsoft "$50M in revenue over 12 months." Time-savings measurement multiplied to a revenue claim; the multiplication step as the boundary failure.
- Specimen D: Microsoft internal, "$500M in the call center alone." Realized-savings claim without method; contextual charge (layoff juxtaposition) separated as reception, not measurement.
- Specimen E: Salesforce, "220,000 leads worked, $42M pipeline." Activity metrics presented as value; "pipeline" defined and located below realized value on the quadrant.
- Specimen F: Amazon/Jassy, Q code transformation, "$260M in annualized efficiency gains, 4,500 developer-years saved." The best-bounded corporate self-report in the record: specific task, counted systems, stated estimation method, still self-reported, cost side still absent. Used to teach that even the best public corporate claim is one repair step short of a true ROI, and that step is the entire discipline.
- Specimen G (reserve, at drafting choice): Honeywell FTE-equivalence or Finastra cycle-time framing.
- Klarna reprised from the opener as the fully worked case: announcement classified, correction narrated, boundary elements catalogued, and the number the announcement should have been if the boundary discipline had been applied at press time.

6.5 The anchor: what honest measurement looks like. Case 6.4, Brynjolfsson, Li, and Raymond in the Quarterly Journal of Economics (May 2025). A staggered introduction of a generative AI assistant across 5,172 customer-support agents; 15% average productivity gain in issues resolved per hour; heterogeneity honestly reported (novice and low-skilled workers improved substantially in both speed and quality; the most experienced saw small speed gains and small quality declines); improved customer sentiment; higher agent retention; suggestive evidence that the tool disseminates top-performer practices; limitations stated plainly. The chapter's exemplar: the confounds are handled by research design (staggered rollout, not press release), the outcomes are defined and defended, the limitations are stated once. And still it is a productivity measurement, not an ROI netting; the tool's cost side is not netted. The gap between this study and full ROI is the exact remaining distance the discipline exists to travel, which the Ch12 summit will name.

#### Slot 3: Craft section
Claim classification and boundary-element repair. Procedure: given a short real value statement, (1) classify it in the quadrant (claim/realized/productivity/ROI); (2) list its boundary elements as PRESENT, MISSING, or AMBIGUOUS across the four elements; (3) sketch the specific repair that would move it one cell toward ROI; (4) if it cannot be repaired without new evidence, state exactly what evidence would suffice. Fully worked on three of the specimens from 6.4 with the fourth left as a completion problem.

#### Slot 4: Chapter summary
Four things that look alike, defined; why productivity never establishes ROI; boundaries as the four-element technical object; the specimen set as a market portrait of the classification errors; the QJE anchor as the exemplar of honest boundary discipline; the summit pointer set (Ch12).

#### Slot 5: Key terms
Claimed value; realized value; productivity; ROI; boundary; scope; period; outcomes; confound; netting; the value quadrant.

#### Slot 6: Discussion questions and problems, plus the Part II cumulative case
Discussion: which specimen from 6.4 is closest to true ROI, and what single boundary element separates it from the destination; construct the strongest case for the "productivity claim IS the value claim" position, then dismantle it; the reversal test setup for assessment 7: under what conditions would the frontier model be economically correct, and how would that conclusion survive the ledger from Chapter 5?
Problems (fully worked): (P1, worked) full assessment 6 sort-and-repair on the specimen set; (P2, worked) essay pair for assessment 7 (board-member category error explanation; then the reversal test with stated conditions); (P3, completion) apply the boundary framework to one new statement supplied at drafting from the Case 6.3 reserve set.

**PART II CUMULATIVE CASE.** The Klarna netting extension. The reader takes the corrected story from Ch6 and attempts to reconstruct the honest number: apply the Ch5 TCO ledger to what is publicly known about the deployment, position the productivity number against the ledger, and produce a defensible range for realized value net of fully loaded cost. The exercise concludes with a stated limits paragraph naming what public information does not support. Payoff: the reader personally executes, on the book's touchstone case, the discipline that would have prevented the announcement's overshoot. Reuse of Klarna is by design: it is the book's canonical claim-and-correction, and reusing it a third time converts the case from illustration to instrument. The QJE ROI extension is not lost; it moves to the Ch12 summit problem set as the summit exercise's prep.


---

## D.3 Part III: The Practice

Purpose: the five functions. Chapter titles use the manifesto's own verbs. The Northmoor dataset is introduced at the top of this part with its construction note. Worked-example fading: completion problems early in the part, unguided by its end.

### Part III introduction (one page before Chapter 7)

Purpose: state the function-order teaching point openly, per the resolved judgment call.
Content: the manifesto orders the functions as sourcing, planning/budgeting, metering/attribution, allocation, value-boundary (the order the flow encounters). The book orders them as sourcing, metering, attribution, planning/budgeting, allocation, value-boundary (the order their dependencies require: records must exist before a budget can be compared to them). The book teaches the second order and grades the first: the final exam (assessment 24) will require the reader to sequence a standing-up plan in the manifesto's operational order, having learned it in the dependency order. This is the book embodying the lesson it grades.
Also introduces the Northmoor dataset with the construction note: synthetic, seeded, fictional-entity disclaimer, engineered to satisfy properties A-F asserted by automated checks. From here forward, problem sets draw on Northmoor cumulatively.

### CHAPTER 7: Sourcing: Feeding the Flow

**Big idea:** sourcing decisions distinguish capability from economic suitability, evaluate models on requirements rather than benchmark rank, and account for switching economics before they arise.
**Competencies:** C7, C8, C10.
**Anchor theorem:** THM-008 [REGISTRY PULL] (the Part II closing theorem that pointed here).
**Prepares assessments:** 8 (legal-ops contract review with the frontier-vs-mid-tier trap) and 10 (switching payback).
**Founding Question resolved:** the sourcing question.

#### Slot 1: Opening case
Case 7.1, the GPT-4o double deprecation (August 2025 through April 2026). The sequence in miniature: OpenAI removes GPT-4o at GPT-5 launch without notice; user backlash; access restored within days; five months later, a formal announcement of retirement with staged extensions; roughly a year later the next generation itself is retired from ChatGPT. The case dramatizes the two claims the chapter must make immediately: model availability is a provider decision on provider timelines, and the buyer's model portfolio can be forcibly migrated more than once inside a year. Sourcing is not a single decision at signature; it is a running practice.

#### Slot 2: Teaching body
7.1 The three questions of sourcing. What capacity do we need, in what economic terms, and with what portability if the answer changes? The chapter's structure follows the three, in order.

7.2 Capability versus economic suitability. FIGURE 7.1: the capability-suitability grid, four cells (capable and suitable, capable but not suitable, suitable but not capable, neither). The distinction taken seriously: benchmark rank is a claim about capability under specific conditions; suitability is a claim about total cost of ownership at required volume against workflow requirements. The frontier model is not automatically correct; the mid-tier model is not automatically wrong. This section prepares the assessment 8 trap: the frontier model wins the benchmark and loses the requirements test at a fraction of the cost.

7.3 Requirements-first evaluation. Introduce the requirements decomposition procedure: (a) enumerate the workflow's performance requirements as testable propositions (accuracy on defined inputs, latency ceilings, context length, tool-calling reliability, refusal behavior, output format constraints); (b) rank the requirements as hard gates versus preferences; (c) score candidate models on the requirements, not on general benchmarks; (d) apply the ledger from Ch5 at expected volume. What emerges is often a mid-tier model chosen for economic reasons after clearing every hard gate, which is precisely the point.

7.4 Switching economics. Anchor theorem THM-008 arrives here [REGISTRY PULL]. Switching between models or providers has three quantities: per-task savings after the switch, transition cost (integration, evaluation, prompt migration, retraining human reviewers, contractual exit costs), and functional adequacy of the alternative. Below a volume threshold, switching never pays regardless of price advantage. Above it, adequacy is the binding constraint: if Model B is inadequate on one workflow, the partial-switch wrinkle (assessment 10) applies. FIGURE 7.2: the switching-payback curve with the adequacy gate as a hard fence.

7.5 The adequacy gate, evidenced. Case 7.1 re-engaged: GPT-4o's dual retirement is a forced-switch event, not an elective one. The buyer's real question is not "would we switch?" but "how quickly can we switch when the choice is not ours?" Section closes with the C22 pointer to Ch14: deprecation notice terms are contract-able, and the ability to contract them is a function of the records the buyer holds.

7.6 The buyer implications from Ch4, closed. Ch4 named three seeds (meters are duplicable, mechanisms are contract-able, outcomes as unit are the new leverage). Ch7 closes the first arc: mechanisms are contract-able, and the tools to do it are what Ch14 builds. The pointer forward is explicit rather than promised.

#### Slot 3: Craft section
Three craft artifacts named and worked in sequence.
- Craft 1 (C8): The requirements decomposition worksheet plus the capability-vs-suitability scoring grid. Procedure and template.
- Craft 2 (C9-adjacent, reused from Ch5): The TCO ledger applied to sourcing at expected volume.
- Craft 3 (C10): The switching-cost model with the adequacy gate. Procedure, template, and the volume threshold formula.
Fully worked example on a described legal-ops deployment (per assessment 8), with the frontier-vs-mid-tier trap illustrated in the worked answer and the switching payback computed with Model B inadequate on one workflow.

#### Slot 4: Chapter summary
Sourcing as a running practice, not a signature event; capability distinguished from economic suitability; requirements-first evaluation over benchmark rank; switching economics with an adequacy gate; forced migration as the base rate the chapter's craft must survive.

#### Slot 5: Key terms
Capability; economic suitability; requirements decomposition; hard gate; benchmark rank; total cost at volume; switching cost; adequacy gate; partial switch; forced migration; deprecation.

#### Slot 6: Discussion questions and problems
Discussion: explain the frontier-vs-mid-tier trap to a colleague who reads benchmark leaderboards; state the conditions under which the frontier model IS economically correct (the C7 reversal test, foreshadowing assessment 7); describe how a running deprecation schedule changes sourcing from a decision into a discipline.
Problems: (P1, fully worked) assessment 8 in full: legal-ops contract review with requirements decomposition, scoring, and cost-at-volume recommendation; (P2, fully worked) assessment 10 in full: switching payback with the adequacy gate and the partial-switch wrinkle; (P3, completion problem, Northmoor) apply requirements decomposition to Northmoor's supplier contract and compliance review workflow (workflow 3), leaving the volume-threshold step blank for the reader; (P4, completion problem, Northmoor) score two candidate models against Northmoor's marketing content studio requirements (workflow 5), completion step is the recommendation memo. Interleaving: P3 and P4 are the reader's first Northmoor encounters and set the stage for Ch8's records.

---

### CHAPTER 8: Metering: Seeing the Flow

**Big idea:** records are the precondition of management; what is unmetered is unmanageable.
**Competency:** C13.
**Anchor theorem:** THM-010 [REGISTRY PULL].
**Prepares assessment:** half of the Ch9 combined assessment (13-14-15 territory, with Ch8 owning the metering architecture step).
**Founding Question resolved (jointly with Ch9):** the visibility question.

#### Slot 1: Opening case
Case 5.2, Shadow AI. Cited findings, in one telling: IBM's 2025 Cost of a Data Breach Report shows breaches involving shadow AI averaged roughly $670,000 more than other incidents, with 97% of breached organizations lacking AI access controls; an IDC 2025 survey finds unauthorized-tool adoption exceeding governed-tool adoption (56% vs 23%); Samsung 2023 as the canonical single-company episode (engineers pasting source code into a public chatbot within a month of rollout). Opening on the record flow's absence with a price attached grounds the chapter's thesis before a single template appears.

#### Slot 2: Teaching body
8.1 The record as artifact. Every consumption event either generates a durable record or it does not. The provider holds provider-side records; the buyer receives an invoice. THM-010 anchoring callout [REGISTRY PULL]: the theorem that says economic control requires visibility into the managed boundary. What the chapter builds is the buyer's side of that visibility.

8.2 The event record schema. FIGURE 8.1: the canonical event record schema. **Signature figure.** Fields: event_id, timestamp, provider, model, workflow_tag, actor (human or system), account/key, input_tokens, output_tokens, tool_invocations, cost_at_ingest, cost_at_reconciliation, session_id, boundary_id (reserved for Ch12). The rationale for each field, with two rules stated once: (a) tagging enforced at ingest, not reconstructed later; (b) cost recorded twice (at ingest and at reconciliation) to make provider-side price changes and same-day price dispersion (Case 5.3) visible on the buyer side.

8.3 Consolidation. The reference architecture: many event sources (two external providers, one internal gateway, per Northmoor's texture), one consolidated ledger, one canonical view. FIGURE 8.2 (auxiliary; architecture requires it): the consolidation flow, sources on the left, ledger in the middle, downstream views (Ch9 attribution report, Ch10 variance analysis, Ch11 routing dashboards, Ch12 boundary panels) on the right. What the architecture guarantees: the organization's own numbers on its own terms, independent of any single provider's report.

8.4 The coverage test. The record flow's own audit. Procedure: enumerate every AI-touching action the organization believes exists (surveys, expense reports, help-desk tickets, license accounts, browser-extension inventories); reconcile against the consolidated ledger; produce a coverage percentage and a shadow-usage estimate. Coverage below a stated threshold triggers a Ch11 constraint scenario before it triggers a Ch9 attribution report. Shadow usage is not a moral failure; it is a metering failure, and the coverage test names it as such.

8.5 The Northmoor illustration. Northmoor's texture, spelled out at Ch8 depth: two external providers, one internal gateway, imperfect workflow tagging, designer/marketer shadow accounts. The half-cleaned multi-provider export (dataset output for Ch9) is previewed here as the artifact Ch9 will operate on. The engineering test loop on a production key (Northmoor's control-failure strand, per property B of the dataset) is introduced here as an artifact the coverage test surfaces before Ch10 explains it as a variance cause.

#### Slot 3: Craft section
Two craft artifacts, worked in sequence.
- Craft 1 (C13 principal): the event record schema. Fields, defaults, enforcement rules, and the two-timestamp cost convention. Fully worked example: derive the schema for a described three-workflow deployment.
- Craft 2 (C13 auxiliary): the consolidation reference architecture and the coverage test. Procedure, template, and thresholds. Worked example: run the coverage test on a described organization with two provider accounts and a known shadow-usage pattern.

#### Slot 4: Chapter summary
Records as the precondition of management; the event record schema and its rules; the consolidation architecture as the buyer's independent view; the coverage test as the record flow's own audit; shadow usage as a metering failure the coverage test names.

#### Slot 5: Key terms
Event record; consumption event (reprised); event schema; workflow tag; ingest cost; reconciliation cost; consolidation ledger; coverage test; shadow usage; coverage percentage; provider export.

#### Slot 6: Discussion questions and problems
Discussion: why is cost recorded at ingest AND reconciliation rather than only once; what does a coverage of 60% actually mean, and what does it forbid the organization from concluding downstream; explain why the record flow's absence is a metering failure rather than a compliance failure.
Problems: (P1, fully worked) design an event schema for the Northmoor deployment; (P2, fully worked) run the coverage test on a described organization and produce the coverage percentage with a shadow-usage estimate; (P3, completion problem, Northmoor) reconcile a fragment of the half-cleaned multi-provider export against Northmoor's stated workflows, completion step is the coverage report; (P4) short essay: state THM-010's condition, then apply it to Northmoor's designer/marketer shadow accounts.

---

### CHAPTER 9: Attribution: Assigning the Flow

**Big idea:** attribution is a governance choice with incentive consequences; the choice reassigns responsibility and can be gamed if made carelessly.
**Competencies:** C14, C15.
**Prepares assessments:** 13-14-15 (with Ch8 having supplied the metering step): choose an attribution basis, defend the choice, compute under alternatives, produce the one-page AI operations report.
**Founding Question resolved (jointly with Ch8):** the visibility question, now with responsibility having an address.

#### Slot 1: Opening case
An original Northmoor illustration. The half-cleaned multi-provider export (dataset output) lands on the reader's desk; workflows 3, 4, and 5 share one account; the reader is asked which team's costs those tokens belong to. The chapter is the answer. Ch9 becomes the first chapter where Northmoor pays off as an opener rather than only in problem sets, and the attribution-reordering property (dataset property A) is encountered as the chapter's problem, not its afterword. The State of FinOps 2026 tooling-gap finding moves to a dated box in the teaching body (section 9.2 or 9.6) as market-scale evidence that the chapter's craft is currently under-supplied by commercial tooling.

#### Slot 2: Teaching body
9.1 What attribution does. Attribution takes a consolidated ledger from Ch8 and assigns cost to entities (workflows, teams, cost centers, projects, customers). Two facts stated immediately: attribution is a choice, not a discovery; and different choices produce different rankings on the same data. Neither is a defect; both are the reason the choice needs a decision framework.

9.2 The attribution bases. Four canonical bases, each defined and worked:
- Per-token: cost proportional to input plus output tokens attributed.
- Per-request: cost proportional to call count.
- Per-seat: cost proportional to headcount assigned.
- Hybrid: a weighted combination, sometimes with a fixed overhead layer.
Each has a defensible use, an incentive it creates, and a way it can be gamed. FIGURE 9.1: the attribution basis comparison, showing the same workload attributed four ways.

9.3 The attribution decision framework. Procedure: (a) identify the entities to attribute across; (b) identify the workflows' cost drivers (few users on huge documents, many users on moderate volume, small team on bursty tokens); (c) test each basis against the fit test (does it rank the entities in the way their behavior would justify?); (d) test each basis against the incentive test (what does the basis reward if minimized?); (e) test each basis against the gaming test (what could an entity do to reduce its attributed cost without reducing its consumption?); (f) choose, defend in one paragraph, and document the choice for the C15 report. FIGURE 9.2: the framework as a decision tree, three tests as three gates.

9.4 The attribution reordering property, demonstrated on Northmoor. Northmoor's workflows 3 (supplier contract review, few users, huge documents), 4 (wholesale copilot, many users, moderate), and 5 (marketing content studio, small team, bursty tokens) share one account. Compute the attribution under per-token, per-request, and per-seat bases; observe the ranking reordering; each basis crowns a different "most expensive team." What this proves at the level of teaching: the reader cannot report an attributed cost without stating the basis, because the basis IS half the number. Note the pedagogy: the Northmoor build guarantees this reordering by construction (property A), so the section can teach the principle on a case where the principle is provable rather than argued.

9.5 The one-page AI operations report. C15's canonical format defined. FIGURE 9.3: the one-page report template. **Signature figure.** Four sections (portfolio at a glance, cost by workflow with basis stated, variance flags, forward look). This is the artifact a CFO reads; the chapter's exam is whether the reader can produce it. The report format is designed to survive being wrong once and useful anyway: every number traces to a record, the basis is stated, and limitations sit inline where they apply rather than in a footnote nobody reads.

9.6 Attribution as governance. One paragraph, load-bearing: attribution is where the technical record flow becomes the political question of who is responsible for how much. The choice is not a technicality; it is where the discipline meets the org chart. Ch14 is where that meeting is designed.

#### Slot 3: Craft section
Two craft artifacts, worked in sequence.
- Craft 1 (C14): The attribution decision framework, template, and the three tests (fit, incentive, gaming). Fully worked on Northmoor.
- Craft 2 (C15): The one-page AI operations report template. Fully worked from the Northmoor attribution.

#### Slot 4: Chapter summary
Attribution as a choice, not a discovery; the four bases and their tradeoffs; the decision framework with three tests; the reordering property, demonstrated on Northmoor; the one-page report as the report a CFO can act on; attribution as the technical-to-political interface.

#### Slot 5: Key terms
Attribution; attribution basis; per-token, per-request, per-seat, hybrid; fit test; incentive test; gaming test; attributed cost; cost center; the one-page AI operations report.

#### Slot 6: Discussion questions and problems
Discussion: why does the same data legitimately rank teams three different ways under three bases; which basis would you defend to a workflow that had gamed a prior basis, and why does the answer depend on the fit test; explain to a CFO why the basis is part of the number.
Problems: (P1, fully worked) full assessment 13-14-15 walk on the Northmoor half-cleaned export: design the schema (Ch8), choose the basis, compute under three bases, produce the one-page report; (P2, completion problem, Northmoor) rerun the attribution after workflow 3 splits into two entities; (P3, completion problem, Northmoor) short memo defending the chosen basis against a workflow contesting it. Interleaving: P1 is the Ch8-Ch9 combined assessment.

---

### CHAPTER 10: Planning and Budgeting: Anticipating the Flow

**Big idea:** a usage-aware budget is a pre-commitment that makes deviation detectable; variance has causes that demand different responses.
**Competencies:** C11, C12. Reinvokes THM-004.
**Prepares assessments:** 11 (usage-aware budget with pre-committed anomaly thresholds) and 12 (variance analysis).
**Founding Question resolved:** the plan question.

#### Slot 1: Opening case
The State of FinOps 2026 finding, narrowly excerpted: roughly 73% of surveyed organizations report AI costs exceeding original budget planning, from the sixth annual survey (1,192 practitioners representing $83B+ in annual cloud spend, published February 19, 2026), alongside the 31%-to-98% two-year AI-spend-management arc. The market has budget failure as a majority experience, and the chapter's craft is what that majority is currently missing. Case Bank 14.1 material used here in a deliberately narrower slice than Ch14 will use: Ch10 uses the budget-overrun finding; Ch14 uses the mission rewrite and boundary treaty. Productive interleaving between chapters that share a source, not conflict. The pointer to Ch14 is one sentence.

#### Slot 2: Teaching body
10.1 What a budget is FOR. A budget is not a spending cap; it is a pre-commitment that turns deviation into information. The claim is anchored in THM-004 reinvoked (scaled deployment requires cost governance for economic control) [REGISTRY PULL]. Under the wrong definition (a cap alone), a budget converts into a game to avoid tripping thresholds; under the right definition (a pre-commitment), a budget converts into a signal about what is actually happening.

10.2 The usage-aware budget: the driver-based forecast. Procedure: (a) name each workflow; (b) identify the workflow's cost drivers (volume, intensity per unit, unit rate); (c) forecast each driver from known plans (headcount, campaign calendar, seasonality); (d) sum to the workflow forecast; (e) sum workflows to the portfolio; (f) commit thresholds in advance for what deviation is anomalous. FIGURE 10.1: the driver-based budget structure, three levels (portfolio, workflow, driver). The pre-committed thresholds are the load-bearing artifact: without them, "the budget was blown" is a story that can be told in the direction of whichever explanation is convenient.

10.3 The variance decomposition. FIGURE 10.2: the variance decomposition, two dimensions.
- The quantity axis: volume (more events), intensity (more tokens per event), rate (higher price per token). These are additive under standard decomposition and reveal WHERE the variance came from.
- The cause axis: demand-driven (the business changed), efficiency-driven (the task quietly got heavier per unit), control-driven (something ran that no one decided to run). These are diagnostic and reveal WHAT the variance means.
The two axes cross: a volume overrun that is demand-driven is healthy growth; a volume overrun that is control-driven is a runaway process; the response is different. The chapter teaches the reader to compute the first and diagnose the second.

10.4 Northmoor's 62% quarter, worked in full. The dataset's property B is instantiated here. Three simultaneous causes in three workflows: wholesale copilot demand surge from the account expansion (healthy growth; volume-driven, demand-caused); marketing studio silent prompt change tripling tokens per task (efficiency failure; intensity-driven, efficiency-caused); engineering test loop on production key (control failure; volume-driven, control-caused). All three roll up to the same 62% aggregate; only the decomposition tells the reader that one is a signal to hire, one is a signal to fix a template, and one is a signal to revoke a key. This is Part III's central worked example, and it is engineered by the Northmoor build to instantiate every teaching point.

10.5 Anomaly thresholds and their false-positive discipline. Thresholds committed in advance produce two failure modes: they alarm when nothing is wrong (false positive) and they miss when something is wrong (false negative). The chapter states the tradeoff plainly (per the straight-spine evidence policy) and offers three pre-committed responses: revise the threshold with a stated reason and a dated log; hold the threshold and investigate; or invoke the Ch11 constraint scenarios if capacity is now the binding limit. Note the interleaving: Ch11's constraints are not a separate topic; they are the natural response to a variance that reveals capacity as the true bottleneck.

#### Slot 3: Craft section
Two craft artifacts, worked in sequence.
- Craft 1 (C11): the usage budget template. Driver-based forecast at the workflow level with pre-committed deviation rules. Fully worked on Northmoor's four in-scope workflows for the budgeted quarter.
- Craft 2 (C12): the variance decomposition, both axes. Fully worked on the 62% quarter, producing a table that names each cause, its axis position, and the response type.

#### Slot 4: Chapter summary
A budget as pre-commitment, not cap; the driver-based forecast with committed thresholds; the two-axis variance decomposition (quantity: volume/intensity/rate; cause: demand/efficiency/control); the 62% quarter as the anchor that makes every distinction non-optional; threshold discipline as a stated tradeoff.

#### Slot 5: Key terms
Usage-aware budget; driver-based forecast; workflow forecast; pre-committed threshold; variance decomposition; volume, intensity, rate; demand-driven, efficiency-driven, control-driven change; anomaly; false positive, false negative.

#### Slot 6: Discussion questions and problems
Discussion: state the difference between a budget as cap and a budget as pre-commitment in one sentence, then defend the second definition to a controller who thinks the first is what a budget is; explain why volume-driven-and-demand-caused calls for a different response than volume-driven-and-control-caused; describe how a false-negative threshold is worse than a false-positive one in the AIOM setting specifically.
Problems: (P1, fully worked) full assessment 11 on Northmoor's forecast quarter; (P2, fully worked) full assessment 12 on the 62% quarter; (P3, completion problem, Northmoor) recompute the variance decomposition if the account-expansion hiring were delayed one quarter; (P4, completion, Northmoor) draft the threshold revision memo after two consecutive false positives on the marketing studio workflow. Interleaving: P1's forecast should be usable in the Ch11 problem set as a starting portfolio.

---

### CHAPTER 11: Allocation and Routing: Disciplining the Flow

**Big idea:** finite capacity under real demand is allocated by stated rule or by accident.
**Competencies:** C16, C17.
**Prepares assessments:** on routing policy and priority/constraint design (specific numbered items to be aligned during drafting).
**Founding Question resolved:** the allocation question.

#### Slot 1: Opening case
Case 4.2, Anthropic's July-August 2025 rate limit episode, told from the buyer's seat. The mid-quarter tightening without notice; the mid-quarter budget already committed in a Ch10 forecast; the routing options the buyer did or did not have prepared; the metered overflow priced at API rates. The case dramatizes the chapter's thesis: when capacity binds, work is either allocated by rule the buyer wrote in advance or by accident dictated by the provider's schedule.

#### Slot 2: Teaching body
11.1 What binds. Three binding constraints named: capacity (the provider limits access), budget (the buyer limits spend), and priority (some work must run first when both bind). Each is a different problem with a different solution family.

11.2 Task classes. FIGURE 11.1: the task-class table (small, categorical, per Mayer coherence). Each task class named with its cost driver profile, its quality requirements, and its latency tolerance. Northmoor's five workflows map onto three canonical classes (bulk tier, standard tier, premium tier) with the mapping shown explicitly, per dataset property D.

11.3 Capacity tiers. Provider-side capacity as tiers (bulk/batch, standard, priority, committed throughput), per Ch4's mechanism menu now reused. The buyer's problem: match task classes to capacity tiers on economic grounds, not on convenience grounds. FIGURE 11.2: the routing matrix, task classes on the rows, capacity tiers on the columns, chosen mappings marked.

11.4 The routing policy. Procedure and format (C16 craft): a written policy naming the default routing for each class, the escalation triggers (when a task moves up a tier), the demotion triggers (when a task moves down), the reroute triggers (when a provider becomes unavailable or expensive; the OpenRouter same-day dispersion (Case 5.3) reappears here as the mechanism a policy can exploit), and the review cadence. Fully worked on Northmoor.

11.5 The priority schema (C17 craft). When the constraint binds harder than routing can absorb, priority rules decide what runs first, what queues, what is declined. The criticality tier structure (which tasks the organization has decided in advance are more critical than others) and the degradation ladder (what a lower-critical task does when denied: retry at a lower tier, queue with a deadline, decline with a message, escalate to human). FIGURE 11.3: the degradation ladder as a decision flow.

11.6 The constraint scenarios, worked on Northmoor. Two scenarios per dataset property D: (a) a mid-quarter provider rate-limit cut of 40% lasting two weeks (the Ch4 precursor rerun on Northmoor); (b) a budget-ceiling variant where aggregate spend is capped mid-quarter. Both require the policy and priority schema to decide the reallocation without ad-hoc reasoning. This section is the C16-plus-C17 combined worked example.

11.7 The everything-on-frontier baseline. One paragraph: computing the naive cost (route every task to the top tier) versus the policy cost on Northmoor produces a gap large enough to motivate the discipline and small enough to be honest. Dataset property D guarantees the size of this gap by construction, so the section teaches on a case where the number is defensible.

#### Slot 3: Craft section
Two craft artifacts, worked in sequence.
- Craft 1 (C16): the routing policy format. Classes, defaults, escalation/demotion triggers, reroute triggers, cadence.
- Craft 2 (C17): the priority schema with criticality tiers and the degradation ladder.
Fully worked on Northmoor for both constraint scenarios.

#### Slot 4: Chapter summary
Three binding constraints (capacity, budget, priority); task classes and capacity tiers; the routing policy as the buyer's written pre-commitment; the priority schema and the degradation ladder for when routing cannot absorb the constraint; policy versus naive baseline as a defensible number.

#### Slot 5: Key terms
Task class; capacity tier; routing policy; escalation trigger; demotion trigger; reroute trigger; priority schema; criticality tier; degradation ladder; queue; decline; everything-on-frontier baseline.

#### Slot 6: Discussion questions and problems
Discussion: state why an unwritten routing policy is a routing policy, and what its author is; explain how the Ch5 same-day price dispersion enters the reroute trigger; describe a case where escalating to human is the correct degradation, not a failure.
Problems: (P1, fully worked, Northmoor) full routing policy plus priority schema on Northmoor; (P2, fully worked, Northmoor) run the 40% rate-limit constraint scenario with the policy in place; (P3, less-guided, Northmoor) run the budget-ceiling constraint scenario, producing the reallocation decisions and the degradation actions taken; (P4) design a criticality tier structure for a described three-workflow deployment (not Northmoor), applying the framework to unseen material. Fading note: P3 and P4 tighten the guidance further in preparation for Ch12's unguided summit.

---

### CHAPTER 12: The Value Boundary: Making the Flow Answer

**Big idea:** THE SUMMIT. Value exists only inside a declared boundary, netted against fully loaded cost, owned by someone.
**Competencies:** C18, C19.
**Anchor theorem:** THM-006 [REGISTRY PULL].
**Prepares assessments:** 18 (the boundary and netting; the summit exercise) and 19 (boundary ownership). Note: the Ch12 problem set also carries the QJE ROI extension migrated from Part II per Decision 7.
**Founding Question resolved:** the accountability question. All five Founding Questions are now answered at least once across Chapters 7-12.

#### Slot 1: Opening case
The QJE anchor at full depth. Return to Case 6.4 (Brynjolfsson, Li, and Raymond, Quarterly Journal of Economics 140(2), May 2025), already introduced at Ch6.5 as the honest-boundary exemplar, and treat it here at the summit's weight. 5,172 customer-support agents; staggered introduction of the assistant as the confound-handling design (not press-release timing); productivity measured as issues resolved per hour; 15% average with the heterogeneity honestly reported (novice and low-skilled workers ~30% in both speed and quality; the most experienced with small speed gains and small quality declines); improved customer sentiment; higher agent retention; limitations stated once. And the one honest step the study did NOT take: the ROI netting. The chapter's whole apparatus is the completion of that step. The reader has been prepared for this framing since Ch6 by design; the summit chapter opens on the discipline's standard as positive rather than cautionary. Klarna is retired from featured slots after three appearances and returns only in the problem set as an unguided completion (P2).

#### Slot 2: Teaching body
12.1 The summit stated. THM-006 in its full statement [REGISTRY PULL]: AI ROI requires both a cost boundary and a value boundary. Everything the book has built is now brought to bear on one number in one declared space, owned by one accountable person. The chapter's tone is deliberately unrhetorical: the peak of the argument is a technical procedure, not a peroration.

12.2 The four elements, revisited with weight. Scope, period, outcomes, confounds handled (from Ch6, now operationalized). Each element defined once more, with the operational question the reader must answer: for scope, which workflow and which period; for period, why this interval and not the one before or the one after; for outcomes, which specific measurements count as value and why others were excluded; for confounds, which alternative explanations for the observed change would have to be true for the netting to be wrong. FIGURE 12.1: the value-boundary worksheet template. **Signature figure. The book's signature artifact.**

12.3 Fully loaded cost, revisited. The Ch5 TCO ledger enters the netting, in full. Every category (access, integration, operation, review, error, governance) has a line in the boundary. The reader who tried to short the ledger has already been graded on that mistake in Ch5; here it becomes a summit-blocking error. FIGURE 12.2: the netting worksheet, cost side (from Ch5) and value side (from Ch6) confronting each other on one page.

12.4 The netting, worked on Northmoor's capstone workflow. Property E of the dataset instantiated. The Customer Service Assist workflow's vendor claim of "30% productivity improvement" enters the boundary; the two confounds (a size-guide overhaul that cut sizing-related contacts; agent attrition of two agents during the netting period) are removed; the fully loaded cost from the Ch5 ledger applied to Northmoor comes in the other side; a smaller, real, defensible number survives, with limitations statable in two sentences. This is the book's central worked example; the dataset engineered the confounds to make the netting non-trivial in exactly the ways the discipline exists to catch.

12.5 The QJE completion, worked openly. Take the QJE 15% productivity finding (from the opener) and attempt the netting the study explicitly did not perform. Build a TCO from publicly stated facts and reasonable ranges. Position the productivity number against the ledger. Produce a bounded ROI estimate with stated confounds. State the limits paragraph naming what the public information does not support. This is the migration of the QJE ROI extension from Part II per Decision 7, and it now serves as the second worked example in the summit chapter proper, alongside the Northmoor netting. The reader ends the chapter having watched the discipline applied to the strongest evidence in the public record and to a constructed case where every number traces.

12.6 Ownership: the boundary charter (C19). A boundary without an owner is a report, not an accountability. The one-page boundary charter names the owner (a specific person or role), the cadence (when the netting is refreshed and re-reviewed), the decision thresholds (what the netting must show to trigger expansion, hold, or prune), and the escalation path (who is briefed when the netting condemns the workflow). FIGURE 12.3: the boundary charter template. This is C19's craft, and it converts C18's number into an institution.

12.7 Why the discipline ends here. One paragraph. The five functions have been taught in the order the flow encounters them (Part III introduction's teaching point, reprised). Every earlier chapter fed this one: Ch7 chose the capacity, Ch8 recorded the events, Ch9 attributed the cost, Ch10 planned and measured the variance, Ch11 allocated the constraint, and Ch12 accounts for the whole. Part IV will now embed the discipline in an organization, but the technical answer to the discipline's question is what this chapter delivers.

#### Slot 3: Craft section
Two craft artifacts, worked in full sequence.
- Craft 1 (C18): the value-boundary worksheet, the book's signature artifact. Template, procedure, and the four-element gate.
- Craft 2 (C19): the boundary charter. Template, procedure, and the ownership tests (does the charter name a person; does the cadence match the workflow's cycle; do the thresholds pre-commit the actions; is escalation defined).
Both worked on Northmoor's Customer Service Assist workflow AND on the QJE completion, so the summit's craft is demonstrated on both a constructed and a real case.

#### Slot 4: Chapter summary
The summit stated (THM-006); the four boundary elements operationalized; fully loaded cost applied without exception; the Northmoor netting as the constructed-case exemplar; the QJE completion as the real-case exemplar; the boundary charter as the ownership artifact; the discipline's technical endpoint declared.

#### Slot 5: Key terms
Value boundary; netting; fully loaded cost (reprised); scope, period, outcomes, confound (reprised); the value-boundary worksheet; the boundary charter; owner; cadence; decision threshold; escalation.

#### Slot 6: Discussion questions and problems, plus the Part III cumulative case
Discussion: state the difference between a boundary and a report in one sentence; explain why the confound removal in the Northmoor netting is not optional; describe what happens to a boundary whose owner cannot name three actions the netting would trigger.
Problems: (P1, unguided, Northmoor) full assessment 18 on a Northmoor workflow OTHER than the capstone (unguided by design; Ch12 sits at the unguided end of the fading policy); (P2, unguided) full assessment 18 on Klarna, February 2024 announcement plus May 2025 correction (the case reappears in problems, not in the opener, per Decision 10); (P3, unguided) full assessment 19: write the boundary charter for the Northmoor capstone workflow; (P4, unguided) an original boundary-and-charter exercise on an unseen described deployment (drafting supplies the deployment). Fading policy fully expressed: no worked models in the problem set; the chapter's own worked examples are the models, and the reader now operates without training wheels.

**PART III CUMULATIVE CASE.** An unseen described deployment, small in scope, requiring every craft artifact from Chapters 7 through 12 in sequence: requirements decomposition and cost-at-volume (Ch7), event schema and coverage test (Ch8), attribution basis choice and one-page report (Ch9), driver-based budget with committed thresholds and variance decomposition (Ch10), routing policy with priority schema (Ch11), value boundary with netting and boundary charter (Ch12). Tests transfer at the Part III close as the fading policy requires, and preserves Part IV's designed pedagogical surprises: Ch13's diagnostic packet IS Northmoor T0 by construction, and Ch15's final exam IS the standing-up sequence that produced the records the reader has been analyzing since Ch8. The unseen deployment description is supplied at drafting; the assessment is fully unguided.


---

## D.4 Part IV: The Institution

Purpose: the discipline in a real organization. Integrative, unguided assessments throughout. Contains the book's final exam at Ch15.

### CHAPTER 13: Diagnosis and Maturity

**Big idea:** the Founding Questions are a measurement instrument; maturity is which of them an organization can answer with records rather than opinions.
**Competency:** C20.
**No single anchor theorem;** runs on the maturity model (v1, locked; reproduced in Section C.4) and its registry grounding [REGISTRY PULL on LEM-002, LEM-011, PROP-046, PROP-047, LEM-003, LEM-020, THM-004, THM-010, LEM-021, THM-006].
**Prepares assessment:** 20 (diagnose an organization with the Founding Questions; locate on the maturity path).

#### Slot 1: Opening case
Northmoor T0, treated at Ch13 depth. Northmoor at the T0 moment (structurally, Stage 1 Unmanaged by construction) is handed to the reader as a diagnostic packet: org chart, budget lines, dashboard screenshots, three stakeholder transcripts (per dataset design). The reader has spent Chapters 8-12 analyzing Northmoor's post-metering records without seeing the state before metering; the opener flips the timeline and reveals where those records came from. The one-company-two-moments payoff engineered from the start of the project lands here. Northmoor T0 IS the assessment 20 packet by construction, so the assessment's grading criteria are made visible in the opener itself: the reader recognizes, in the packet, the earlier state of a company whose records they know intimately. That recognition is the discipline's own diagnostic test being performed on the reader without warning.

#### Slot 2: Teaching body
13.1 The instrument, restated. The five Founding Questions, restated verbatim as the diagnostic instrument [REGISTRY PULL]. The five are not questions to ponder; they are questions to answer with records. What can be shown wins; what can be described but not shown does not. FIGURE 13.1: the diagnostic matrix, five questions as rows, three states as columns (answerable with records, partially answerable, unanswerable), each cell filled with the specific artifact that would move it left.

13.2 The maturity model, stated in full. The five stages from the locked v1: Unmanaged, Visible, Attributed, Governed, Accountable. Each stage defined by which Founding Questions the organization can answer with records, and by the evidence artifact(s) required at that stage. The four design rulings from v1 are reprised as prose without ceremony: the strict ladder (dependency, not permission-slip); the naming ("Accountable" not "Optimized" because the summit is the value boundary, not efficiency); the Governed strict bundle (all three control artifacts or the stage is not claimed); the one-boundary-suffices rule for Accountable. FIGURE 13.2: the ladder. **Signature figure** (reused in Ch15 as the Founding Questions cross-reference). Five stages, each with its Founding Questions, its evidence artifacts, and the artifact-that-moves-it-up.

13.3 Why the ladder is a dependency, not a preference. The registry grounding stated openly (per the design note): the stages were designed from pedagogy; the registry proves the ordering is necessary. Walked in one paragraph: LEM-002 and LEM-011 put the organization onto the ladder; PROP-046/047 and LEM-003 open Attributed; LEM-020, THM-004, and THM-010 open Governed; LEM-021 and THM-006 make Accountable coherent [REGISTRY PULL for exact statements]. The reader who traced THM-004 in Ch3 recognizes the machinery. This is the science-and-discipline architecture the book teaches, applied to the book's own diagnostic instrument.

13.4 Scope, and the honest mixed statement. The scope rule from the maturity model v1: maturity is assessed within a declared scope, and precise mixed statements are the intended usage. Example given: "Claims processing is Accountable; the enterprise is Visible." This is boundary discipline applied to the model itself, and it is what prevents the model from being weaponized for enterprise-scale marketing claims.

13.5 The regulatory-governance fence. One sentence, per the standing decision: this chapter is about the cost-and-value governance of AI consumption; regulatory AI governance is a separate discipline with its own literatures, briefly named for its border, deferred as out of scope.

13.6 The diagnostic procedure, walked on Northmoor T0. The opener's packet becomes the worked example. For each of the five Founding Questions: identify the artifact the packet does or does not supply; score as answerable/partial/unanswerable with the cited artifact; declare Northmoor's scope; assign the stage (which is Stage 1 Unmanaged by construction); name the single highest-yield next move, which the strict ladder makes derivable: it is always the lowest missing artifact. FIGURE 13.3: the completed diagnostic scorecard for Northmoor T0.

13.7 What the diagnostic forbids. The chapter is graded on evidentiary discipline. Full-transformation prescriptions (per the C20 assessment note) fail. The diagnostic's whole thesis is that the ladder's next rung is derivable and specific; a memo recommending everything at once has misread the instrument. This is stated once, plainly, as the guardrail Ch15 will also enforce.

#### Slot 3: Craft section
The diagnostic procedure (C20). Two artifacts, worked in sequence.
- Craft 1: the diagnostic scorecard template. Five Founding Questions, three answerability states, artifact citations required in every cell that is not blank. Fully worked on Northmoor T0.
- Craft 2: the highest-yield next-move rule. Procedure: (a) locate the lowest missing artifact on the ladder; (b) state the artifact required, in one sentence; (c) state which Founding Question that artifact opens, in one sentence; (d) state what the artifact will NOT do, in one sentence (the counter-move to full-transformation prescriptions). Fully worked from the Northmoor T0 diagnosis.

#### Slot 4: Chapter summary
The Founding Questions as diagnostic instrument; the five-stage maturity model with its strict ladder and its registry grounding; scope-declared mixed statements as the intended usage; the diagnostic procedure walked on Northmoor T0; the evidentiary discipline that grades the assessment.

#### Slot 5: Key terms
Diagnostic scorecard; artifact test; the five stages (Unmanaged, Visible, Attributed, Governed, Accountable); the Founding Questions (reprised); scope; declared scope; the ladder (strict, dependency-based); highest-yield next move; false-maturity claim.

#### Slot 6: Discussion questions and problems
Discussion: state one Founding Question the reader's own organization could answer with records today, and one it could not, with the specific missing artifact named; explain to a stakeholder why "we have an AI budget" does not answer Question 3 (the metering-and-attribution question); construct the strongest case for reordering the ladder, then explain, using the registry grounding, why that case fails.
Problems: (P1, unguided, Northmoor T0) full assessment 20 on Northmoor T0: diagnostic scorecard, scope declaration, stage assignment, highest-yield next move, with a stated limits paragraph; (P2, unguided) diagnostic on an unseen described organization supplied at drafting; (P3, unguided) short memo defending a mixed-scope statement against a stakeholder who wants a single enterprise-wide stage label. Fading: all problems unguided, per Part IV's policy.

---

### CHAPTER 14: The Organized Buyer

**Big idea:** institutionalization has an inside (the function) and an outside (the market posture); leverage is records.
**Competencies:** C21, C22. No single anchor theorem.
**Prepares assessments:** 21 (org design under the stated constraint) and 22 (negotiation dossier).

#### Slot 1: Opening case
Case 14.1, the State of FinOps 2026 as the neighboring discipline's arrival. Read at full depth for this chapter, distinct from the narrower budget-overrun slice Ch10 uses.
The case, told in a single arc: the FinOps Foundation's sixth annual State of FinOps survey (published February 19, 2026; 1,192 practitioners representing $83B+ in annual cloud spend) documents 98% of respondents now managing AI spend, up from 63% in 2025 and 31% in 2024; "FinOps for AI" is the top forward-looking priority; AI cost management is the #1 skillset teams plan to add (58%); the #1 most-requested tooling capability is granular monitoring of AI spend, which commercial tooling has not delivered at scale; 78% of FinOps teams report to a CTO or CIO and only 8% to a CFO; the Foundation, in February 2026, formally rewrote its mission from managing the value of cloud to managing "the value of technology"; and one practitioner quote surfaces in the report: "Is your AI providing value? No one can answer that question yet." The chapter's whole apparatus follows from that quote: an adjacent discipline has expanded into the territory this book names, brings cost visibility infrastructure, and openly admits it lacks the value side. The organized buyer's first task is to design the boundary treaty.

#### Slot 2: Teaching body
14.1 Institutionalization has two sides. The chapter's structural claim, stated up front. Inside: the AIOM function itself (placement, roles, RACI, the interfaces with neighboring functions). Outside: the market posture (sourcing dossier, negotiation, term-sheet architecture). Records are what connect the two: inside, records are the function's product; outside, records are the buyer's leverage. FIGURE 14.1: the two-sided institution, inside and outside, connected by the records artifact.

14.2 The placement argument. Where the function reports: CFO, CIO, or COO. Each defensible on stated grounds; the chapter teaches the argument, not the answer. The C21 assessment specifies a 4,000-person firm with roughly 2% opex on AI, an existing FinOps team, and two-role budget for the AIOM function; the chapter's placement discussion is calibrated to this scale. Trade-offs stated plainly: CFO placement centers accountability and dulls technical velocity; CIO placement centers execution and dulls the accountability signal; COO placement centers workflow ownership and requires the strongest neighboring-function interfaces. The State of FinOps datum on 78%/8% reporting split (from the opener) is treated as descriptive, not prescriptive: the market's current placement is where AI cost is currently managed as a technical problem; the book's argument is that the value side reintroduces the CFO's stake.

14.3 The role charter. Two roles, per the C21 constraint. FIGURE 14.2: the role charter template. Each role defined by mandate (what only this role does), accountable outputs (the artifacts the role owns end to end from the book's craft inventory), and decision authority (what this role can decide without escalation, what it cannot). The assessment note that assessment 21 grades the treaty hardest is honored here: the roles are defined against the neighboring functions they must interface with.

14.4 The interface RACI. Four neighboring functions: FinOps, Procurement, IT/Engineering, Business Unit leaders. For each, the interface question is: who is Responsible, Accountable, Consulted, Informed for each of the AIOM function's craft artifacts (Ch7 sourcing decisions, Ch8 metering architecture, Ch9 attribution reports, Ch10 budgets, Ch11 routing policies, Ch12 boundary charters). FIGURE 14.3: the interface RACI as a matrix. The reader completes it in the C21 assessment; the chapter walks a fully worked example on one row.

14.5 The FinOps boundary treaty. The chapter's hardest teaching moment, per the C21 grading note. FinOps (in February 2026, per the opener) formally expanded its mission to "the value of technology"; this book's discipline names the value boundary as its own summit. Both cannot own the whole territory; both are needed. The treaty allocates:
- To FinOps: cost visibility infrastructure at the AI-spend level, cloud and SaaS cost management, the neighboring cost integrations, and the practitioner-community role.
- To AIOM: attribution to workflows (not accounts), budgeting authority against workflow forecasts, routing policy, the value boundary and its ownership, and the netting.
Boundary conditions: metering plumbing may live in FinOps tooling; the schema Ch8 defines is the AIOM function's requirement on that tooling. Attribution results feed both functions; the attribution basis is an AIOM decision (per Ch9). The boundary charter (per Ch12) is an AIOM output, non-transferable. FIGURE 14.4: the treaty as a shared-boundary diagram, with the specific artifacts on each side and the ones that cross. Engaged by name and on the record, per the standing decision to engage the FinOps framework honestly.

14.6 The market posture: the sourcing dossier. The outside institution. The dossier's contents (per C22 craft): provider-exposure analysis (their economics from Ch4, applied to the buyer's actual portfolio), leverage inventory (the records the buyer holds; the routing optionality the buyer has developed; the switching analysis from Ch7), ranked term sheet, walk-away line.

14.7 The term-sheet architecture. Provisions to negotiate, grouped by what each addresses. Price: rate structure, volume commitments, price-change protocols. Capacity: rate limits, priority tier access, degradation notification. Continuity: deprecation notice periods (Case 7.1 as evidence for the requested length), migration support, model-version pinning. Data: export commitments, retention, tagging support. Each provision keyed to a record the buyer holds; the chapter's thesis line: leverage IS the AIOM records.

14.8 The negotiation, walked on a realistic composite proposal. Assessment 22's composite (flat rate, buried soft-cap, unilateral repricing, no export commitment) is walked as a fully worked example: provider-exposure analysis identifying the specific risks each provision creates, leverage inventory named against each, ranked counter-terms, walk-away line stated with the alternatives it implies (per the Ch7 switching analysis).

#### Slot 3: Craft section
Two craft artifacts (C21 and C22), worked in sequence.
- Craft 1 (C21): the function charter with interface RACI, including the FinOps boundary treaty. Templates for the placement argument, role charters, and the RACI matrix.
- Craft 2 (C22): the sourcing dossier and term-sheet checklist. Templates for provider-exposure analysis, leverage inventory, ranked term sheet, and walk-away line.
Both worked on the assessment 21 firm (4,000-person, 2% opex) and the assessment 22 composite proposal.

#### Slot 4: Chapter summary
The two-sided institution (inside function, outside posture, records as connector); the placement argument as taught trade-offs, not a mandated answer; the two-role charter under the C21 constraint; the interface RACI with named neighbors; the FinOps boundary treaty (engaged by name, honored honestly); the sourcing dossier and term-sheet architecture; the negotiation walked on the composite proposal.

#### Slot 5: Key terms
Institutionalization; function charter; RACI; interface function; FinOps; boundary treaty; sourcing dossier; leverage inventory; term sheet; walk-away line; deprecation notice; export commitment; unilateral repricing; soft-cap.

#### Slot 6: Discussion questions and problems
Discussion: state the strongest case for each of the three placements (CFO, CIO, COO) for the C21 firm, then commit to one and defend against the strongest objection; explain to a FinOps counterpart, using the treaty language, why the value boundary is not FinOps territory even though the metering plumbing might live in FinOps tooling; the reversal test on term-sheet architecture: describe the provider position under which each provision becomes unnecessary, and explain what that reveals about the buyer's actual exposure.
Problems: (P1, unguided) full assessment 21 on the specified firm: placement argument, role charters, RACI, boundary treaty; (P2, unguided) full assessment 22 against the composite proposal; (P3, unguided) short memo explaining to the reader's own organization what would have to be true for the C21 org design to succeed at scale. Fading: unguided, per Part IV.

---

### CHAPTER 15: Standing Up the Discipline

**Big idea:** the discipline is adopted in a sequence, and the sequence is derivable; the case must survive translation into the CFO's numbers.
**Competencies:** C23, C24. No single anchor theorem.
**Contains the book's final exam.**
**Prepares assessments:** 23 (three-exhibit briefing) and 24 (final exam: first Head of AI Operations, ninety-day plan).

#### Slot 1: Opening case
The FinOps discipline's founding story as a structural analog. Its founders' account of the 2019 practitioner community formation, and the trajectory from "practitioners in cloud finance" to a Linux Foundation program with 1,192 surveyed practitioners in 2026, is a documented parallel to what this book's discipline is announcing. The opener is transparent about analogy: the FinOps discipline is not the AIOM discipline (the two are neighbors, per Ch3's borders and Ch14's boundary treaty), but its founding is real evidence that a comparable discipline can be stood up in the timeframe the reader is about to plan for. Closes an arc across the book: FinOps first appeared as a border to draw (Ch3), returned as a neighboring discipline to design a treaty with (Ch14), and now returns as a documented founding case that grounds the chapter's central claim in the record. The reserve option (an original constructed inaugural-function brief) is held if the FinOps material proves thinner than expected at drafting; a Northmoor T+90 opener was rejected on assessment-integrity grounds.

#### Slot 2: Teaching body
15.1 The discipline is adopted in a sequence. The chapter's thesis, stated up front. The sequence is not a preference; it is derivable from the maturity model's ladder (Ch13) and the function-order teaching point from the Part III introduction. The sequence is what the reader's final exam will produce.

15.2 The sequence, derived. Ninety days in three tranches, per the C24 assessment structure. Each tranche derived, not asserted:
- Days 1-30: metering first (the ladder's Stage 2 evidence, the precondition of everything else); one rough boundary declared early, for political capital and to force the discipline's summit into visibility from day one. The rough boundary is small in scope and honest about its limits; it is not the Ch12 summit artifact but a scoped forerunner.
- Days 31-60: attribution stood up (Stage 3 evidence); the one-page report begun; the first sourcing decision documented with the requirements decomposition.
- Days 61-90: budgeting against actuals (Stage 4 opening); one routing policy in force; the day-90 self-assessment, whose criteria were declared on day one, is run.
FIGURE 15.1: the ninety-day sequence as a Gantt-style chart against the maturity ladder, showing which stage each tranche's artifacts open.

15.3 What the sequence forbids. The C24 grading rubric made explicit: standing up all five functions at once fails; routing before attribution fails (per the function-order logic); a value boundary declared without metering fails; no explicit not-doing list fails. The C24 assessment is designed to make these failure modes appealing and expensive. The chapter names them once as the anti-patterns the sequence exists to prevent.

15.4 The Founding Questions, re-asked. Per the structural device: Ch3 posed them; Ch7-12 resolved them once each; Ch13 instrumentalized them as the diagnostic; Ch15 re-asks them, now as the ninety-day plan's targets. Which Founding Question does day 30's artifact open? Day 60's? Day 90's? FIGURE 15.2: the Founding Questions across the ninety days, each answered by a specific artifact on a specific date, no earlier.

15.5 Compression: the CFO briefing. Assessment 23's territory. The three-exhibit briefing format (C23 craft):
- Exhibit 1: the flow picture (Ch2's three-flow diagram, applied to the reader's organization).
- Exhibit 2: the netting (Ch12's boundary and its number, with its limits).
- Exhibit 3: the ask (the ninety-day sequence's next thirty days, with the decision required).
Plus 400 words. Every number traces to a record; no vendor statistics; a specific ask. FIGURE 15.3: the three-exhibit template. **Signature figure.** The CFO-chair rubric: cost, benefit, verification, accountability.

15.6 The Northmoor closing. Northmoor is the reader's final exam by design. The T0 packet from Ch13, the twelve months of records from Chapters 8-12, the year of decisions the reader has personally analyzed. The final exam is the ninety-day plan that stood up Northmoor's metering. The CFO briefing compresses the year. This is the one-company-two-moments payoff, delivered as the book's closing argument: the reader personally produces the plan that explains where the numbers they have worked all book came from. No narrative apparatus is required; the structure is the payoff.

15.7 Why the book ends here. One paragraph, deliberately quiet. The discipline has been named, its science stated, its practice taught, its institution designed, and its adoption sequenced. What remains is not more material but its use, in the reader's own organization, on the reader's own next quarter. The book is a founding document; per the standing decision, it expects to be superseded within roughly five years as the discipline accumulates real practitioners, real cases, and real evidence. The last sentence of the book acknowledges this: the point of a founding document is to become one edition among many.

#### Slot 3: Craft section
Two craft artifacts (C23 and C24), worked in sequence.
- Craft 1 (C24): the ninety-day standing-up sequence. Template, procedure, the three-tranche structure, the explicit not-doing list, the day-90 self-assessment declared on day one. Fully worked on Northmoor: the reader watches the plan being derived that will then be graded when they produce it themselves.
- Craft 2 (C23): the three-exhibit briefing format. Template, procedure, the CFO-chair rubric. Fully worked on Northmoor's year (compression to three exhibits and 400 words).
Both crafts are demonstrated on Northmoor by design, so the final exam is graded against the same craft the reader has just watched executed.

#### Slot 4: Chapter summary
The discipline is adopted in a derivable sequence; the ninety-day plan in three tranches with the derivation stated; the not-doing list; the day-90 self-assessment declared on day one; the Founding Questions re-asked as the plan's targets; the three-exhibit CFO briefing as the compression the case must survive; the Northmoor closing as the book's one-company-two-moments payoff; the founding-document acknowledgment.

#### Slot 5: Key terms
Ninety-day sequence; tranche; rough boundary; not-doing list; day-90 self-assessment; three-exhibit briefing; CFO-chair rubric; the flow picture; the netting; the ask; the founding document.

#### Slot 6: Discussion questions and problems (contains the book's final exam)
Discussion: state the strongest case for compressing the ninety-day sequence to sixty days, then explain, using the maturity ladder, why the compression fails; describe what "one rough boundary declared early" is FOR, in political and technical terms; construct a defensible not-doing list of five items for a described first-Head-of-AI-Operations arrival, and explain why each item is on the list.
Problems: (P1, THE BOOK'S FINAL EXAM, assessment 24 in full) first Head of AI Operations arrives at Northmoor; T0 packet inherited from Ch13; ninety-day plan in three tranches with sequencing logic stated; day-90 self-assessment defined on day one; explicit not-doing list; standing up all five functions at once fails; (P2, assessment 23 in full) three-exhibit CFO briefing on Northmoor's year, plus 400 words, every number tracing to a record; (P3, unguided) an original inaugural-function arrival at an unseen described organization, per assessment 24 applied to a case where the reader has not analyzed the records personally. Fading: fully unguided.

**PART IV closing note.** No separate Part IV cumulative case. The Ch15 P1 final exam (assessment 24) IS the cumulative case, structurally and pedagogically. Marking it explicitly as the book's culminating exercise, rather than as one problem among several, is the honest treatment of what it already is.


---

# PART E: THE COMPLETE DECISION LOG

Every embedded decision made during outlining, listed in the order ruled, with the option chosen and the reasoning. Fourteen decisions were embedded and ruled across the four parts (four in Part I, three in Part II, four in Part III, three in Part IV).

Reference format for each decision: number, chapter, subject, options considered, ruling, reasoning.

## Part I decisions

### Decision 1: Chapter 1 opening case
**Subject:** which real case dramatizes the category error at the book's opening moment.
**Options considered:**
- A. Cursor repricing, told from the buyer's seat.
- B. The State of FinOps 31%-to-98% arc.
- C. Hold the slot pending drafting research.
**Ruling:** Option A, paired with GitHub Copilot (Case 4.6, added to the case bank at ruling time).
**Reasoning:** The buyer's-seat framing dramatizes the flat-rate objection refuting itself in real time. Pairing Cursor with GitHub Copilot's two-act migration converts an anecdote into a documented pattern across the two most widely used AI coding subscriptions inside twelve months, preempting the "one badly run startup" dismissal.

### Decision 2: Chapter 2 opening case
**Subject:** which case dramatizes the three-flow argument and the central asymmetry.
**Options considered:**
- A. MIT NANDA "The GenAI Divide" market portrait.
- B. Shadow AI (Case 5.2).
**Ruling:** Option A, told per the handle-with-care protocol.
**Reasoning:** NANDA states the whole chapter's problem in one finding (adoption everywhere, value invisible), and Chapter 3's discussion questions already plan to have students critique the study's own boundary discipline. Reserving Shadow AI preserves Chapter 8's opener.

### Decision 3: Trace set piece subject in Chapter 3
**Subject:** which theorem the trace set piece dissects.
**Options considered:**
- A. THM-004, the theorem the reader accepted one chapter ago.
- B. THM-006, the summit theorem, as foreshadowing.
- C. THM-008, the assessed theorem.
**Ruling:** Option A.
**Reasoning:** Tracing a believed claim keeps the machinery the only new cognitive load. Assessment 4 tests THM-008 cold, as designed; pre-tracing THM-008 would convert a transfer test into a recall test.

### Decision 4: Part I cumulative case
**Subject:** the evidence the reader works on at Part I's close.
**Options considered:**
- A. Klarna, February 2024 public record only.
- B. The Microsoft $500M call-center claim.
- C. A constructed composite.
**Ruling:** Option A, with the Chapter 6 reveal framing committed as a downstream consequence.
**Reasoning:** Only option with enough public texture for the exercise. The engineered payoff (Chapter 6 reveals the correction the reader has already diagnosed as predictable) proves the book's argument on the reader's own homework. Chapter 6's opener is bound to present the arc as the completion of the reader's Part I analysis.

## Part II decisions

### Decision 5: Chapter 4 craft example distribution
**Subject:** the distribution used in the stylized provider model's worked example.
**Options considered:**
- A. A Northmoor-style distribution seeding later recognition.
- B. A generic stylized distribution keeping Part II independent of Northmoor.
**Ruling:** Option B.
**Reasoning:** Part II's independence from Northmoor is a structural feature (the science teaches on any real distribution). Committing Part II parameters before the Northmoor numerical build reduces the build's degrees of freedom for no teaching gain.

### Decision 6: Chapter 5 opening case
**Subject:** which case sets the register for the anatomy-of-cost chapter.
**Options considered:**
- A. The price paradox (Case 5.3), extended in scope.
- B. Air Canada v. Moffatt (Case 5.1).
**Ruling:** Option A, extended with the OpenRouter same-day dispersion finding as the second of three findings.
**Reasoning:** Thesis-scale opener separates access price from total cost more cleanly than a specific cost category. The OpenRouter angle strengthens the finding: unit price is a moving distribution across serving providers, not a scalar. Air Canada lands full-force in the teaching body as the error-cost anchor. The manifesto's PMT claim is fully replaced by a three-sided finding (long-horizon deflation, intraday dispersion, intensity inflation).

### Decision 7: Part II cumulative case
**Subject:** the integrative exercise closing Part II.
**Options considered:**
- A. The Klarna netting extension.
- B. The QJE contact-center ROI extension.
**Ruling:** Option A. The QJE extension migrates to Ch12 as summit-exercise prep.
**Reasoning:** Klarna has been the book's living argument since Part I; giving the reader the tools to close the netting fulfills the pedagogical arc. Ends Part II on a defensible number rather than another correction, preempting a "Klarna is only a warning tale" reading. The QJE extension is preserved for the Ch12 summit problem set, retaining the pedagogical asset without diluting Part II's close.

## Part III decisions

### Decision 8: Chapter 9 opening case
**Subject:** what dramatizes attribution before the reader knows how to do it.
**Options considered:**
- A. An original Northmoor illustration (the shared-account attribution problem).
- B. The State of FinOps tooling-gap finding as market-scale opener.
**Ruling:** Option A.
**Reasoning:** Northmoor's attribution-reordering property (dataset property A) is best encountered as the reader's own problem, not as an afterword. The FinOps finding relocates to the teaching body as market-scale evidence that the chapter's craft is currently under-supplied by commercial tooling. Ch9 is the first chapter where Northmoor pays off as an opener rather than only in problem sets.

### Decision 9: Chapter 10 opening case
**Subject:** what dramatizes budgeting's absence at market scale.
**Options considered:**
- A. The State of FinOps 2026 73% budget-overrun finding.
- B. Defer the slot pending drafting research.
**Ruling:** Option A, narrow slice.
**Reasoning:** Market-scale opener is the honest one; a single-company overrun narrative is not cleanly available in the bank and reconstruction would strain the evidence policy. Ch14 uses the mission rewrite and boundary treaty from the same source; the two chapters share the source and treat it differently.

### Decision 10: Chapter 12 opening case (the summit)
**Subject:** what opens the book's technical summit.
**Options considered:**
- A. The QJE anchor (Case 6.4) at full depth.
- B. Klarna returning for a fourth pass.
**Ruling:** Option A.
**Reasoning:** Klarna has been carried three times already; a fourth pass converts a touchstone into a crutch. Opening the summit chapter on the strongest exemplar of honest measurement in the public record declares the discipline's standard as positive rather than cautionary. Klarna returns only in the unguided problem set.

### Decision 11: Part III cumulative case
**Subject:** the integrative exercise closing Part III.
**Options considered:**
- A. The full Northmoor twelve-month narrative, integrated end to end.
- B. An unseen described deployment testing transfer across all six functions.
**Ruling:** Option B.
**Reasoning:** Option A would have converted three Part IV assessments into previews (Ch13's diagnostic packet IS Northmoor T0; Ch15's final exam IS Northmoor's standing-up sequence). Option B tests transfer at the Part III close as the fading policy requires and preserves Part IV's designed pedagogical surprises.

## Part IV decisions

### Decision 12: Chapter 13 opening case
**Subject:** what dramatizes the false-maturity confrontation.
**Options considered:**
- A. Northmoor T0 at Ch13 depth.
- B. A real single-company false-maturity episode.
**Ruling:** Option A.
**Reasoning:** Northmoor T0 IS the assessment 20 packet by construction. Opening on it delivers the one-company-two-moments payoff engineered from the start of the project. Public disclosures rarely include the diagnostic packet's contents, so Option B would strain the evidence policy for lower pedagogical yield.

### Decision 13: Chapter 15 opening case
**Subject:** the inaugural-function or discipline-founding case at the book's closing chapter.
**Options considered:**
- A. The FinOps discipline's founding story as a structural analog.
- B. An original constructed inaugural-function brief.
- C. Northmoor T+90 as opener.
**Ruling:** Option A. Option B held in reserve if the FinOps material proves thinner than expected at drafting.
**Reasoning:** The FinOps founding is real evidence that a comparable discipline can be stood up, grounding the chapter's central claim in the record rather than constructed material. Closes the book's engagement with FinOps that began in Ch3 (border) and continued in Ch14 (boundary treaty). Option C rejected on assessment-integrity grounds: the Ch15 final exam IS the Northmoor T+90 plan.

### Decision 14: Part IV cumulative case
**Subject:** whether to add a Part IV cumulative case in addition to the Ch15 final exam.
**Options considered:**
- A. No separate Part IV cumulative case; the Ch15 P1 final exam marked as the book's culminating exercise.
- B. A separate Part IV cumulative case in addition to the final exam.
**Ruling:** Option A.
**Reasoning:** The Ch15 P1 assessment IS the cumulative case, structurally and pedagogically. Marking it explicitly as the book's culminating exercise is the honest treatment of what it already is. Structural amendment logged: Structure v1's "part-closing cumulative cases (4 total)" is amended to "3 total (Parts I, II, III); Part IV's role fulfilled by the Ch15 P1 final exam."

## Decision-log summary table

| # | Chapter | Subject | Ruling |
|---|---------|---------|--------|
| 1 | Ch1 opener | Category-error case | Cursor + GitHub Copilot, paired |
| 2 | Ch2 opener | Three-flow case | MIT NANDA (handle-with-care protocol) |
| 3 | Ch3 trace | Trace set piece subject | THM-004 (believed claim) |
| 4 | Part I cumulative | Cumulative case subject | Klarna Feb 2024 public record only |
| 5 | Ch4 craft example | Distribution used | Generic stylized (Northmoor-independent) |
| 6 | Ch5 opener | Anatomy-of-cost case | Price paradox, extended with OpenRouter |
| 7 | Part II cumulative | Cumulative case subject | Klarna netting extension |
| 8 | Ch9 opener | Attribution case | Original Northmoor illustration |
| 9 | Ch10 opener | Budgeting case | State of FinOps 73% budget-overrun finding |
| 10 | Ch12 opener | Summit case | QJE anchor at full depth |
| 11 | Part III cumulative | Cumulative case subject | Unseen described deployment (transfer test) |
| 12 | Ch13 opener | Maturity-diagnosis case | Northmoor T0 at Ch13 depth |
| 13 | Ch15 opener | Standing-up case | FinOps founding as structural analog |
| 14 | Part IV cumulative | Cumulative case handling | None; Ch15 P1 marked as book's culminating exercise |


---

# PART F: THE FIGURE INVENTORY

Every figure across all fifteen chapters, with its big idea and its signature-figure designation where applicable. Thirty-four figures total. Every figure is redrawable from a script and validated before rendering per the standing build practice.

## F.1 Signature figures (recurring or load-bearing across the book)

Four figures are designated signature figures. Signature status means the figure appears at a hinge moment in the argument, carries pedagogical weight beyond its chapter, or is reused in later chapters as a diagnostic instrument.

- **Fig 2.1: The three-flow diagram.** The book's recurring diagnostic image; designed once in Ch2, reused in every mapping through Ch15; used in the Ch15 CFO briefing as Exhibit 1 (the flow picture).
- **Fig 8.1: The event record schema.** The template artifact that recurs in Ch9 (attribution), Ch10 (budgeting), Ch12 (boundary), and Ch14 (metering plumbing under the FinOps treaty).
- **Fig 9.3: The one-page AI operations report.** The CFO-actionable output that recurs in Ch10 (variance reporting), Ch13 (diagnostic scorecard's cousin), and Ch15 (compression to three exhibits).
- **Fig 12.1: The value-boundary worksheet.** The book's signature craft artifact; the summit of the discipline; recurs in Ch13 (Stage 5 evidence) and Ch15 (Exhibit 2 in the CFO briefing).

A fifth figure, **Fig 13.2 (the five-stage ladder)**, carries signature status within Part IV as the diagnostic instrument and reappears in Ch15 as the Founding Questions cross-reference.

## F.2 Full inventory by chapter

**Chapter 1: The Category Error** (2 figures)
- Fig 1.1: Two purchase models side by side (seat model vs consumption integral). Big idea: the category error.
- Fig 1.2: Anatomy of a consumption event. Big idea: the atomic unit.

**Chapter 2: The Flow** (2 figures)
- Fig 2.1: The three-flow diagram. **Signature figure.** Big idea: the flows.
- Fig 2.2: The central asymmetry (cost accruing by default vs value flat until designed). Big idea: the asymmetry.

**Chapter 3: A Science and Its Discipline** (2 figures)
- Fig 3.1: The dependency trace tree (THM-004 down to representative propositions). Big idea: registry literacy.
- Fig 3.2: The two-layer architecture with five function columns. Big idea: science and discipline.

**Chapter 4: The Playing Field** (1 figure)
- Fig 4.1: Skewed usage under flat pricing (long-tail histogram against horizontal revenue line). Big idea: the usage distribution problem.

**Chapter 5: The Anatomy of Cost** (2 figures)
- Fig 5.1: The TCO ledger, six categories against access price. Big idea: the ledger as reference frame.
- Fig 5.2: Stacked ledger over three horizons (month 1, year 1, year 3). Big idea: shape changes over time.

**Chapter 6: The Nature of Value** (1 figure)
- Fig 6.1: The value quadrant (claimed, realized, productivity, ROI). Big idea: four things that look alike.

**Chapter 7: Sourcing: Feeding the Flow** (2 figures)
- Fig 7.1: Capability-suitability grid (four cells). Big idea: capability vs economic suitability.
- Fig 7.2: Switching-payback curve with adequacy gate. Big idea: switching economics.

**Chapter 8: Metering: Seeing the Flow** (2 figures)
- Fig 8.1: The event record schema. **Signature figure.** Big idea: records as artifact.
- Fig 8.2: Consolidation reference architecture. Auxiliary (architecture requires it).

**Chapter 9: Attribution: Assigning the Flow** (3 figures)
- Fig 9.1: Attribution basis comparison (same workload attributed four ways). Big idea: the choice is half the number.
- Fig 9.2: Attribution decision framework (three-gate decision tree). Auxiliary (framework requires it).
- Fig 9.3: One-page AI operations report template. **Signature figure.** Big idea: the CFO-actionable artifact.

**Chapter 10: Planning and Budgeting: Anticipating the Flow** (2 figures)
- Fig 10.1: Driver-based budget structure (three levels: portfolio, workflow, driver). Big idea: pre-commitment as information.
- Fig 10.2: Variance decomposition, two axes (quantity: volume/intensity/rate; cause: demand/efficiency/control). Big idea: variance has causes.

**Chapter 11: Allocation and Routing: Disciplining the Flow** (3 figures)
- Fig 11.1: Task-class table (rendered as figure per Mayer categorical convention). Auxiliary.
- Fig 11.2: Routing matrix (task classes × capacity tiers). Big idea: match classes to tiers on economic grounds.
- Fig 11.3: Degradation ladder decision flow. Big idea: what happens when the constraint binds.

**Chapter 12: The Value Boundary: Making the Flow Answer** (3 figures)
- Fig 12.1: The value-boundary worksheet. **Signature figure. The book's signature artifact.** Big idea: the boundary as technical object.
- Fig 12.2: Netting worksheet (cost side meets value side). Big idea: fully loaded cost applied.
- Fig 12.3: The boundary charter template. Big idea: ownership.

**Chapter 13: Diagnosis and Maturity** (3 figures)
- Fig 13.1: The diagnostic matrix (five Founding Questions × three states). Big idea: the instrument.
- Fig 13.2: The five-stage ladder. **Signature figure within Part IV.** Big idea: the maturity model.
- Fig 13.3: The completed Northmoor T0 scorecard. Auxiliary (worked example).

**Chapter 14: The Organized Buyer** (4 figures)
- Fig 14.1: The two-sided institution (inside function, outside posture, records connecting). Big idea: institutionalization has two sides.
- Fig 14.2: The role charter template. Auxiliary.
- Fig 14.3: The interface RACI matrix. Auxiliary.
- Fig 14.4: The FinOps boundary treaty diagram (shared boundary with artifacts allocated on each side). Big idea: shared boundary treaty.

**Chapter 15: Standing Up the Discipline** (3 figures)
- Fig 15.1: The ninety-day sequence as Gantt against the maturity ladder. Big idea: the sequence.
- Fig 15.2: The Founding Questions across the ninety days (each answered by a specific artifact on a specific date). Big idea: the questions answered by dated artifacts.
- Fig 15.3: The three-exhibit CFO briefing template. **Signature figure.** Big idea: the compression.

**Total: 34 figures.** Signature figures: 2.1, 8.1, 9.3, 12.1, and 13.2 (Part IV signature). All other figures serve one big idea at first exposure or are auxiliary where the content is architectural or categorical and prose cannot render it.

## F.3 Border comparisons rendered as tables, not figures

Per Mayer coherence, categorical content that is neither spatial nor architectural is rendered as tables. Two prominent instances:
- **Ch3 border comparison** (AIOps, MLOps, FinOps, regulatory AI governance). Two sentences each: what it is for, what it lacks for this territory. Table, not figure.
- **Ch14 provisions checklist** (price, capacity, continuity, data provisions in term-sheet architecture). Table with columns for provision, purpose, buyer's record supporting it, provider's likely position. Table, not figure.

---

# PART G: THE CRAFT INVENTORY

The seventeen named craft artifacts the book contributes. Each is defined by (a) its competency assignment, (b) its home chapter, (c) its purpose, and (d) its reuse across chapters where applicable.

## G.1 The seventeen craft artifacts

1. **The consumption-event inventory** (C1; Ch1 home). Enumerate a deployment's event types with their resource drivers; locate the meter. First artifact the reader produces.

2. **The three-flow mapping** (C2, C3; Ch2 home; recurring). Diagnose a deployment as three flows (usage, records, cost-and-value); mark each as managed or unmanaged. The book's recurring diagnostic; reused in every subsequent Northmoor exercise and in the Ch15 CFO briefing.

3. **The registry trace procedure** (C4; Ch3 home). Read a formal claim by tracing it through its dependencies; state what it does and does not establish; state what would falsify it.

4. **The stylized provider model** (C5; Ch4 home). Compute break-even consumption, unprofitable subscriber fraction, and expected loss per 10,000 subscribers under skewed usage; predict rational mechanisms in order of adoption.

5. **The TCO ledger** (C9; Ch5 home; recurring). Populate six cost categories against access price for a deployment; mark first-year vs steady-state; compute the ledger multiple over access price. Reused in Ch7 (sourcing at volume) and Ch12 (fully loaded cost for the netting).

6. **Claim classification and boundary-element repair** (C6; Ch6 home). Classify a value statement in the four-cell quadrant (claim/realized/productivity/ROI); catalog boundary elements as present, missing, or ambiguous; sketch the repair.

7. **The requirements decomposition worksheet plus the capability-suitability grid** (C8; Ch7 home). Enumerate a workflow's performance requirements as testable propositions; score candidate models on the requirements, not on general benchmarks.

8. **The switching-cost model with the adequacy gate** (C10; Ch7 home). Compute per-task savings, transition cost, and functional adequacy; produce the switching payback with the adequacy gate as a hard fence.

9. **The event record schema** (C13; Ch8 home; recurring). Fields, defaults, enforcement rules, two-timestamp cost convention. The metering foundation everything else builds on.

10. **The consolidation reference architecture and coverage test** (C13; Ch8 home). Multi-source consolidation with a coverage percentage and shadow-usage estimate.

11. **The attribution decision framework** (C14; Ch9 home). Four bases (per-token, per-request, per-seat, hybrid); three tests (fit, incentive, gaming); chosen basis defended in one paragraph.

12. **The one-page AI operations report** (C15; Ch9 home; recurring). Portfolio at a glance, cost by workflow with basis stated, variance flags, forward look. The CFO-actionable artifact; recurs in Ch10 and Ch15.

13. **The usage budget template** (C11; Ch10 home). Driver-based forecast by workflow with pre-committed anomaly thresholds.

14. **The variance decomposition** (C12; Ch10 home). Two-axis decomposition (quantity: volume/intensity/rate; cause: demand/efficiency/control) with response type named per cell.

15. **The routing policy** (C16; Ch11 home). Task classes matched to capacity tiers; escalation, demotion, and reroute triggers; review cadence.

16. **The priority schema with degradation ladder** (C17; Ch11 home). Criticality tiers and the degradation ladder (retry, queue, decline, escalate to human).

17. **The value-boundary worksheet and boundary charter** (C18, C19; Ch12 home). The book's signature craft: value boundary with four elements (scope, period, outcomes, confounds handled) and the boundary charter (owner, cadence, decision thresholds, escalation path). The summit artifact.

Additional Part IV craft artifacts (institutional layer):

- **The diagnostic scorecard and highest-yield next-move rule** (C20; Ch13 home). Five Founding Questions × three answerability states; artifact citations required in every cell; the lowest missing artifact identifies the next move.
- **The function charter, interface RACI, and FinOps boundary treaty** (C21; Ch14 home). Placement argument, two-role charters, four-function RACI, and the shared-boundary treaty.
- **The sourcing dossier and term-sheet checklist** (C22; Ch14 home). Provider-exposure analysis, leverage inventory, ranked term sheet, walk-away line, provisions grouped by price/capacity/continuity/data.
- **The three-exhibit briefing format** (C23; Ch15 home). Flow picture, netting, ask, plus 400 words; the compression the case must survive.
- **The ninety-day standing-up sequence** (C24; Ch15 home). Three tranches with sequencing logic stated; explicit not-doing list; day-90 self-assessment declared on day one.

## G.2 Craft reuse across chapters

Some artifacts recur across chapters. The reuse map:
- Three-flow mapping (Ch2): reused in Ch8 (metering texture), Ch12 (netting frame), Ch13 (diagnostic), Ch15 (Exhibit 1).
- TCO ledger (Ch5): reused in Ch7 (cost-at-volume), Ch12 (fully loaded cost), Ch14 (leverage inventory groundwork).
- Event record schema (Ch8): reused in Ch9 (attribution basis), Ch10 (budget reconciliation), Ch12 (boundary_id field), Ch14 (metering plumbing under the treaty).
- One-page report (Ch9): reused in Ch10 (variance reporting output), Ch13 (relative of the diagnostic scorecard), Ch15 (Exhibit 3 basis).
- Value-boundary worksheet (Ch12): reused in Ch13 (Stage 5 evidence), Ch15 (Exhibit 2).
- Diagnostic scorecard (Ch13): reused in Ch15 (day-90 self-assessment format).

The book's originality is concentrated in these seventeen artifacts. Each is a first-edition contribution to the discipline; each is the operational output of the corresponding competency.

---

# PART H: OPEN ITEMS, CHASE LISTS, AND WHAT HAPPENS NEXT

## H.1 Registry pulls required before drafting

The registry (Locked Registry v1.3) and the founding paper are not yet loaded into the project's readable knowledge base. Loading them is a prerequisite to Chapter 1 drafting.

Verbatim text required from the registry, chapter by chapter:
- **Ch1:** THM-009 exact statement.
- **Ch2:** THM-004 exact statement; LEM-002 and LEM-011 if load-bearing in section 2.3.
- **Ch3:** The five Founding Questions in verbatim wording; THM-004's supporting lemma chain and representative propositions (for the trace set piece); THM-002 statement (for the P2 completion problem candidate).
- **Ch4:** THM-007 exact statement.
- **Ch5:** THM-002 exact statement; propositions in the PROP-156-160 range for the error-cost grounding.
- **Ch6:** THM-005 exact statement; THM-006 statement (for the foreshadow pointer).
- **Ch7:** THM-008 exact statement.
- **Ch8:** THM-010 exact statement.
- **Ch10:** THM-004 restatement.
- **Ch12:** THM-006 in its full statement (the summit anchor).
- **Ch13:** LEM-002, LEM-011, PROP-046, PROP-047, LEM-003, LEM-020, LEM-021 statements (the registry grounding walked at 13.3); the five Founding Questions in verbatim wording (again, at 13.1).
- **Ch15:** The five Founding Questions in verbatim wording (again, at 15.4).

**Standing action item:** load Registry v1.3 and the founding paper into project knowledge before Chapter 1 drafting begins.

## H.2 Primary-source chase list before print

Every case in the book cites a Grade A primary source directly. The following primaries must be located, verified against their original release, and archived at drafting time (perishable web content):

- Sam Altman post on X (Jan 5-6 2025) re: OpenAI Pro losses.
- Anthropic Claude Code rate-limit announcement (July 28, 2025; the July 17 tightening).
- Michael Truell blog post (Cursor apology, June-July 2025).
- Klarna / OpenAI joint press release (February 2024).
- Bloomberg interview with Sebastian Siemiatkowski (May 2025).
- CNBC coverage of Klarna headcount trajectory.
- MIT NANDA "The GenAI Divide: State of AI in Business 2025" report PDF.
- BC Civil Resolution Tribunal decision text: Moffatt v. Air Canada 2024 BCCRT 149.
- IBM Cost of a Data Breach 2025 report.
- IDC 2025 shadow-AI survey.
- Samsung 2023 chatbot incident contemporaneous reporting.
- OpenAI service tier documentation and pricing pages (archive on capture date).
- Salesforce Agentforce Help Agent June 25, 2026 announcement + Salesforce Ben interview with SVP Prasad Raje.
- Salesforce Q1 FY27 earnings call transcript.
- Jamie Dimon Bloomberg TV interview (October 2025).
- IDC/Microsoft "The Business Opportunity of AI" report PDF + VentureBeat interview with IDC's Ritu Jyoti.
- Microsoft AI agents blog post (October 2024) including Honeywell and Finastra customer stories.
- Lumen customer stories on Microsoft (archive; vendor-hosted pages move).
- Judson Althoff Microsoft $500M call-center remarks (Bloomberg, July 2025); TechCrunch coverage.
- Andy Jassy LinkedIn post on Amazon Q code transformation (August 2024); AWS DevOps blog on methodology.
- Brynjolfsson, Li, Raymond, "Generative AI at Work," Quarterly Journal of Economics 140(2), May 2025 pp. 889-942; NBER WP 31161 as historical reference only.
- Epoch AI data insight "LLM inference prices have fallen rapidly but unequally across tasks."
- a16z LLMflation post (Guido Appenzeller, 2024).
- arXiv 2511.23455 "The Price of Progress" (2026, working paper caveat).
- OpenRouter model catalog and provider routing documentation (archive at capture given daily change cadence).
- Gartner March 2026 agentic-workload token estimate (locate and verify before citing).
- State of FinOps 2026 full report (data.finops.org); Linux Foundation press release February 19, 2026.
- OpenAI GPT-4o retirement blog post and help-center page (August 2025, January 2026 announcements).
- CNBC coverage of January 29, 2026 OpenAI retirement announcement.
- Anthropic and Azure OpenAI model deprecation schedule pages (archive at drafting).
- GitHub Copilot premium-request changelog (June 18, 2025) and AI Credits billing documentation (June 1, 2026).
- FinOps discipline founding sources for Ch15 opener (2019 practitioner community formation, Linux Foundation program history).

Archive requirement: every perishable web source captured at drafting time via web.archive.org or equivalent, with capture date noted in the case citation.

## H.3 Watch items carried into drafting

Three watch items were identified during outlining and remain open as low-priority items to reconsider during drafting rather than blocking it:

1. **Ch1 opening case upgrade.** The Cursor + Copilot pairing is strong, but if a single-company "we thought we bought software" episode with even purer buyer-side texture surfaces during drafting, consider substitution.
2. **Ch9 opening case upgrade watch.** The Northmoor illustration is the ruled opener, and it's strong. But if a documented single-company attribution episode surfaces with public texture during drafting (e.g., an internal memo becoming public), consider adding as a dated box in the teaching body.
3. **Ch15 opening case fallback.** The FinOps founding story is the ruled opener. Option B (an original constructed inaugural-function brief, labeled as constructed) remains in reserve if the FinOps material proves thinner than expected at drafting.

## H.4 Structural amendment logged

Per Decision 14: Structure v1's text "part-closing cumulative cases (4 total)" is amended to read:

> "Part-closing cumulative cases (3 total; Parts I, II, III), each reaching backward across parts (interleaving); Part IV's structural role is fulfilled by the Ch15 P1 final exam, marked as the book's culminating exercise."

This amendment is applied throughout this consolidated specification.

## H.5 Immediate next milestones (in order)

**M1: Consolidated specification review.** This document circulated to Dan and external reviewers/models for structural and substantive feedback. Turnaround expected: informal review before proceeding.

**M2: Registry integration.** Load the Locked Registry v1.3 and the founding paper into project knowledge, so all [REGISTRY PULL] items resolve to verbatim text. Blocking prerequisite for drafting; not for the Northmoor build.

**M3: Northmoor numerical build session.** Dedicated session to produce:
- The seeded Python generator script (parameters at top, automated property checks for A-F).
- Raw event records for Ch8, Ch9 problems.
- Half-cleaned multi-provider export for Ch9 opener.
- Budget and actuals tables for Ch10.
- Task-class and tier tables for Ch11.
- Capstone workflow panel for Ch12.
- T0 diagnostic packet for Ch13 opener (org chart, budget lines, dashboard screenshots, three stakeholder transcripts).
- Answer keys for every Northmoor problem-set exercise.
Sequenced to run after M1 (consolidated spec approved) and after M2 (registry available), and before M4 begins.

**M4: Chapter 1 drafting.** Full-quality draft of Chapter 1 against this specification, using the WeasyPrint build system established for the *Anatomy of a Hit* and *Governed AI Systems* projects. Design system to be specified in a small production session concurrent with M4.

**M5-M18: Chapter 2 through Chapter 15 drafting.** In order, each chapter drafted against the corresponding Part D outline; QA (pdfplumber overflow, header/footer checks, pdf2image rasterization sampling) after each; primary sources archived at drafting time per H.2.

**M19: Front matter and back matter drafting.** Preface, acknowledgments, reader's guide, registry appendix (reproducing 28 theorems and lemmas verbatim; 200 proposition IDs with statements), method note, glossary, index, bibliography.

**M20: Manuscript integration and final QA.** Full-book render; final overflow, header, and citation-format QA; index page-references verified; bibliography reconciled against every case's chase-list entry.

**M21: Submission.** Manuscript to publisher (Chicago, Oxford, or as directed by Dan).

## H.6 Series positioning (deferred)

The book publishes standalone with no series banner on the first edition (per standing decision). Series positioning as a potential flagship for a later series (*Governed AI Systems* family, or a new *AI Business Economics* series) is deferred to a post-publication decision informed by first-edition reception. This consolidated specification captures the state of the book itself; series decisions are not committed here.

---

# CLOSING NOTE

This consolidated specification is the complete pre-drafting state of *AI Operations Management* as of July 20, 2026. It captures the founding-document ambition, the argument structure, the twenty-four exit competencies, the fifteen chapters against the fixed six-slot skeleton, the maturity model, the Northmoor dataset design at v1.1, the case bank at v2.0 with all six chapter shelves populated, the thirty-four figures with signature designations, the seventeen craft artifacts, the fourteen embedded decisions ruled during outlining, the registry pull list, the primary-source chase list, and the immediate next milestones.

A reader who has never seen the project before can reconstruct, from this document alone, what the book is, why it exists, what it argues, what it teaches, how it is organized, what has been ruled and what remains open, and what work is next.

The next document produced against this specification will be the Northmoor numerical build. The document after that will be the first-quality draft of Chapter 1.

**Status:** consolidated specification v1.0, ready for external review.
**Compiled:** July 20, 2026.
**Author of decisions:** Dan (Daniel S. Wipert, Chorus AI Systems).
**Compiled by:** working session against the four part outlines, the locked foundation documents, and the case bank v2.0.

END OF DOCUMENT.
