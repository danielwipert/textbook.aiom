# Chapter 3 review: reference extract

Everything the reviewer grades against, in one file. Extracted verbatim from the
book's own planning documents on 2026-10-01.

## 1. Part I and Chapter 3, from the structure document

### Part I: The Argument
Purpose: the reader learns why the discipline must exist. Founding Questions posed at part's end, deliberately unanswerable yet.

1. The Category Error
   - Big idea: deployed AI use is resource consumption, not software access.
   - Competency: C1. Anchor theorem: THM-009.
   - Craft section: the consumption-event inventory (reading a deployment as events).
2. The Flow
   - Big idea: AI runs as three flows (usage, records, cost-and-value); unmanaged flows degrade; cost accrues by default, value only by design.
   - Competencies: C2, C3. Anchor theorem: THM-004.
   - Craft section: the three-flow mapping (recurring diagnostic used across the book).
3. A Science and Its Discipline
   - Big idea: AI Business Economics is the science; AI Operations Management is the practice that acts on it.
   - Competency: C4. No single anchor; contains the trace set piece (walk one theorem down through lemmas to propositions).
   - Also: five functions previewed; Founding Questions posed; borders drawn (not AIOps, not FinOps, not MLOps, not regulatory governance).
   - Craft section: the trace procedure (how to read a formal claim).


## 2. Competency C4 and assessment 4, from the exit competencies

Competency C4: Read a formal claim: parse conditions, trace dependencies, state what it does and does not establish.

Assessment 4: Registry literacy on THM-008: restate conditions; state non-claims; trace one lemma to propositions; answer the "word games" objection. Requires the trace set piece earlier in the book.

## 3. The Chapter 3 outline, from the specification

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

## 4. Dan's rulings on the plan, 2026-10-01

1. No registry counts in body prose; dated counts in one dated box.
2. The spec's line "neither can most organizations on earth" is replaced by the opening case's sourced practitioner quotation.
3. The Part I cumulative case sits inside the chapter's last slot.
4. THM-002 is the theorem for problem P2.

## 5. The seven craft criteria, from the prose standard

## 26. The craft criteria, and how Stage 4 grades this standard

Stage 4 has two halves. The mechanical half is `voicecheck.py`. The judgment half
reads the chapter against the criteria below and records a finding per criterion.
They appear as sub-checkboxes in every generated checklist, and `status_check.py`
fails a Stage 4 marked passed with one left open and unexplained.

**There are SEVEN, and C7 is new.** C1 through C6 carry their numbers from the
retired craft file so that Chapter 1's record stays readable, with C3 and C6
restated to match this standard. C7 grades the core principle, which nothing graded
before and which is the failure the rejected draft committed most often.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to a named, specific instance. Bounded by the fifty-year rule, so it
  lives mostly in cases, worked examples and craft artifacts.
- **C2. Context and stakes.** Every mechanism states the conditions that made it
  available and what it settles, not only what it does. No mechanical proxy exists.
- **C3. Claim first.** The main point of a paragraph is visible in its first
  sentence or two. Findings lead, qualifications subordinate, no throat clearing.
  Restated from "front-loaded sentences" to match section 5.
- **C4. Deliberate rhythm.** Sentence length varies, mostly 12 to 24 words, with a
  short sentence after a long explanation. No long stretch at a uniform length.
- **C5. Paragraph close.** Paragraphs end on the load-bearing clause, not a
  trailing qualifier and not a cross-reference.
- **C6. The guard holds, in both directions.** No hero or villain framing, no
  populist register, no character-driven causation where a structural account is
  available. **And no false sophistication:** no abstraction where an ordinary word
  is available, no aphorism standing in for an explanation. Restated, because the
  old guard watched only one direction and the book failed in the other.
- **C7. Business reality first.** No paragraph opens on a framework, category or
  conceptual distinction where a business statement is available. Every coined term
  arrives after the mechanism it names.

**Read adversarially and by section.** For each criterion, quote the WEAKEST passage
in the chapter and rule it, rather than asking whether the criterion is met. Read
the per-section table, never the chapter average alone.

---
