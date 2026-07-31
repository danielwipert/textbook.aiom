# AI Operations Management: Derived Structure v1.0 (Stage 3)

Status: DRAFT for Dan's review. Stages 1 and 2 (see AIOM_Exit_Competencies_v1.md) are locked; this structure is derived from them.
Method: constraint satisfaction over the locked competencies, assessments, sequencing constraints, and pedagogy commitments. The registry justifies the book; pedagogy organized it.

## The structure: 15 chapters, 4 parts

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

### Part II: The Science
Purpose: what is true, before what to do. Fully worked examples throughout.

4. The Playing Field
   - Big idea: providers carry variable cost against often-fixed revenue; the resolution mechanisms (meters, tiers, limits, priority) are economically derivable.
   - Competency: C5. Anchor theorem: THM-007.
   - Craft section: the stylized provider model (flat-rate profitability under skewed usage).
5. The Anatomy of Cost
   - Big idea: access price is not total cost; exposure accumulates without decisions.
   - Competency: C9. Anchor theorem: THM-002.
   - Craft section: the TCO ledger (standard cost-category checklist; reused book-wide).
6. The Nature of Value
   - Big idea: claimed value, realized value, productivity, and ROI are four different things; only boundaries produce honest numbers.
   - Competency: C6. Anchor theorem: THM-005.
   - Craft section: claim classification and boundary-element repair.

### Part III: The Practice
Purpose: the five functions. Chapter titles use the manifesto's own verbs. The capstone dataset is introduced at the top of this part with its construction note. Worked-example fading: completion problems early in the part, unguided by its end.

7. Sourcing: Feeding the Flow
   - Big ideas: capability vs economic suitability; requirements-first evaluation; switching economics.
   - Competencies: C7, C8, C10. Anchor theorem: THM-008.
   - Craft: requirements decomposition worksheet; capability-vs-suitability grid; switching-cost model with adequacy gate.
8. Metering: Seeing the Flow
   - Big idea: records are the precondition of management; what is unmetered is unmanageable.
   - Competency: C13. Anchor theorem: THM-010.
   - Craft: event record schema; consolidation reference architecture; coverage test incl. shadow usage.
9. Attribution: Assigning the Flow
   - Big idea: attribution is a governance choice with incentive consequences.
   - Competencies: C14, C15.
   - Craft: attribution decision framework; the one-page AI operations report.
10. Planning and Budgeting: Anticipating the Flow
    - Big idea: a usage-aware budget is a pre-commitment that makes deviation detectable; variance has causes that demand different responses.
    - Competencies: C11, C12. (Reinvokes THM-004.)
    - Craft: the usage budget; variance decomposition (volume/intensity/rate; demand/efficiency/control).
11. Allocation and Routing: Disciplining the Flow
    - Big idea: finite capacity under real demand is allocated by stated rule or by accident.
    - Competencies: C16, C17.
    - Craft: routing policy format; priority schema with degradation ladder.
12. The Value Boundary: Making the Flow Answer
    - Big idea: THE SUMMIT. Value exists only inside a declared boundary, netted against fully loaded cost, owned by someone.
    - Competencies: C18, C19. Anchor theorem: THM-006.
    - Craft: the value-boundary worksheet (the book's signature artifact); the boundary charter.

### Part IV: The Institution
Purpose: the discipline in a real organization. Integrative, unguided assessments throughout.

13. Diagnosis and Maturity
    - Big idea: the Founding Questions are a measurement instrument; maturity is which of them an organization can answer with records rather than opinions.
    - Competency: C20.
    - Craft: the maturity model (five stages, proposed: Unmanaged, Visible, Attributed, Governed, Accountable). NOTE: requires deliberate design session.
14. The Organized Buyer
    - Big idea: institutionalization has an inside (the function) and an outside (the market posture); leverage is records.
    - Competencies: C21, C22.
    - Craft: function charter + interface RACI incl. FinOps boundary treaty; sourcing dossier + term-sheet checklist.
15. Standing Up the Discipline
    - Big idea: the discipline is adopted in a sequence, and the sequence is derivable; the case must survive translation into the CFO's numbers.
    - Competencies: C23, C24.
    - Craft: three-exhibit briefing format; the ninety-day sequence.
    - Contains the book's final exam.

## The judgment call (resolved): function order

Manifesto order: sourcing, planning/budgeting, metering/attribution, allocation, value-boundary.
Book order: sourcing, metering, attribution, planning/budgeting, allocation, value-boundary.
Single deviation: metering/attribution before planning/budgeting.
Reason: a budget is a comparison of plan against records; records must exist first. The manifesto itself calls metering the function on which the other four depend, and the final exam (C24) grades metering-before-budgeting sequencing; the book's structure must embody the lesson it grades. Sourcing remains first among functions: its analytics consume only Part II science, not internal records, and THM-008 closes Part II pointing directly at it.
Action: Part III introduction states the reordering openly, one paragraph, as a teaching point: functions listed in the order the flow encounters them, learned in the order their dependencies require.

## Coverage map (Stage 1 -> chapters)

C1->1; C2->2; C3->2; C4->3; C5->4; C6->6; C7->7; C8->7; C9->5; C10->7; C11->10; C12->10; C13->8; C14->9; C15->9; C16->11; C17->11; C18->12; C19->12; C20->13; C21->14; C22->14; C23->15; C24->15.
All 24 covered. No orphaned competencies. No chapter without competencies.

## Theorem map (all 8, one-to-one)

THM-009 -> Ch1; THM-004 -> Ch2; THM-007 -> Ch4; THM-002 -> Ch5; THM-005 -> Ch6; THM-008 -> Ch7; THM-010 -> Ch8; THM-006 -> Ch12.
The one-to-one mapping was not forced; it emerged from the pedagogy. Chapters 3, 9, 10, 11, 13, 14, 15 run on lemmas, craft, and integration.
Reuse is permitted and expected (e.g., THM-004 in Ch10; THM-006 foreshadowed in Ch6).

## Capstone dataset thread

Introduced: top of Part III, with construction note (clearly labeled constructed data).
Records -> Ch8, Ch9 problems. Budget and actuals -> Ch10. Constraint scenarios -> Ch11. The netting -> Ch12 (C18 capstone). Compression to three exhibits -> Ch15 (C23).
The dataset needs a name (open item).

## Structural devices

- Fixed chapter skeleton in all 15 chapters, no exceptions: opening case, teaching body, craft section, chapter summary, key terms, discussion questions and problems.
- Part-closing cumulative cases (4 total), each reaching backward across parts (interleaving).
- Worked-example fading: Parts I-II fully worked; Part III completion -> unguided; Part IV integrative unguided.
- Founding Questions: posed Ch3; resolved one per function chapter (Ch7, Ch10, Ch8/9, Ch11, Ch12); instrumentalized Ch13; re-asked Ch15.
- Fifty-year rule: body prose timeless; perishable specifics quarantined in dated cases.

## Open items before outlining proceeds

1. Dan's review of this structure (approve, amend, or reorder).
2. Design session: the maturity model (Ch13's craft; the one major framework not yet designed).
3. Name the capstone dataset.
4. Case-bank research: documented episodes for Ch4 (provider mechanisms), Ch6 (value/ROI statements), opening cases for all 15 chapters.
5. Remaining publisher questions from the original fifteen never asked in v2 form: voice/tone ruling (manifesto taunts out, per university-press standard: to confirm), production (design system, series identity), front matter and appendix plan (registry reproduction, method note, glossary/index).
