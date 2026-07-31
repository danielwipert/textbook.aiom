# AI Operations Management: Backward Design Foundation v2.0

Textbook: *AI Operations Management* (founding text of the discipline)
Approved by Dan. Stage 1 locked; Stage 2 locked. Current date of record: July 19, 2026.

Naming note: the five diagnostic questions of the discipline (formerly "the Monday questions" in the manifesto) are pending a permanent name. Provisional label in this document: THE FIVE QUESTIONS. Update globally when the name is chosen.

Rules of use:
- Every competency is phrased as "the reader can..." and is observable.
- This list is the whole book. No chapter may exist that does not serve at least one competency.
- The registry justifies the book; it does not organize the book.

## Standing decisions

1. This book fully replaces the earlier AI Operations textbook (abandoned as premature).
2. Two-layer architecture, both named: AI Business Economics is the science; AI Operations Management is the discipline that acts on it.
3. Primary reader: MBA-level graduate student; must translate to C-suite. University-press standard. Fifty-year founding-document ambition: body prose written to outlive its examples; perishable market specifics quarantined inside dated case studies.
4. Buyer-side spine. Provider economics appears once, early, as "the playing field."
5. Registry objects tiered: theorems as chapter-anchoring callouts; lemmas quoted where load-bearing; propositions cited by ID; full registry as back-of-book appendix; one early trace set piece teaching registry literacy.
6. Evidence policy: straight spine. Every empirical claim cited, formalized as conditional, or cut. Limitations stated once, plainly. No hedging.
7. Many real cited case studies; no single narrative case. ONE recurring constructed DATASET (the capstone dataset, clearly labeled as constructed) threads the problem sets: its budget appears in budgeting problems, its actuals in variance problems, its records in attribution problems, culminating in the final netting. Cumulative practice without storybook narrative.
8. Fixed chapter skeleton, identical in every chapter: (1) Opening case, (2) Teaching body, (3) Craft section, (4) Chapter summary, (5) Key terms, (6) Discussion questions and problems.
9. THE FIVE QUESTIONS live at the part level, judiciously.
10. Pedagogy: backward design; worked-example fading (worked early, completion mid, unguided late); interleaved cumulative practice; self-explanation-style discussion questions; Mayer coherence and signaling; one strong figure per big idea at first exposure.
11. Book prose never uses em dashes.
12. Sequencing constraint discovered in Stage 2: the institutional layer (competencies 20-24) consumes all earlier material and must come last; the capstone dataset must be fully exercised before competency 23.

## Stage 1: Exit Competencies (LOCKED)

### Group 1: Thinking (theory layer, AI Business Economics)
1. Explain why deployed AI use is resource consumption rather than software access; defend against the flat-rate objection.
2. Identify the three flows (usage, records, cost-and-value) in any real deployment; diagnose which are unmanaged.
3. State the central asymmetry (cost by default, value by design) and derive its consequence: all of the cost, an unknown fraction of the value.
4. Read a formal claim: parse conditions, trace dependencies, state what it does and does not establish.
5. Model the provider side: why fixed revenue against variable cost is unstable; predict the rational mechanisms (meters, tiers, limits, priority pricing).
6. Distinguish claimed value, realized value, productivity, ROI; why a productivity claim never establishes ROI.
7. Distinguish technical capability from economic suitability; why the frontier model is not automatically correct.

### Group 2: Doing (practice layer, the five functions)
8. Decompose a task into performance requirements; evaluate models economically, not by benchmark rank.
9. Compute TCO beyond access price: integration, operation, review, error, governance.
10. Evaluate a switching decision: functional adequacy gate, transition costs, payback.
11. Build a usage-aware budget: driver-based forecast by workflow with pre-committed anomaly thresholds.
12. Perform variance analysis; classify causes (demand-driven, efficiency-driven, control-driven).
13. Specify a metering architecture: event record schema, consolidation, tagging enforcement, coverage test.
14. Choose and defend an attribution basis; compute under alternatives; understand incentive consequences.
15. Produce the one-page consolidated management report a CFO can act on.
16. Write a routing policy matching work classes to capacity classes on economic grounds.
17. Design priority and constraint rules with a stated generative rule (criticality tiers, degradation ladder).
18. Draw a value boundary and perform the netting: realized value against fully loaded cost, with limitations. [SUMMIT]
19. Assign boundary ownership: owner, cadence, decision thresholds. [SUMMIT]

### Group 3: Leading (institutional layer)
20. Diagnose an organization with THE FIVE QUESTIONS; locate it on the maturity path.
21. Design the AIOM function: placement, roles, RACI, the FinOps boundary treaty.
22. Negotiate with a provider from an organized position: their economics, our leverage inventory, ranked term sheet.
23. Brief a C-suite in the organization's own numbers: three exhibits, 400 words, specific ask.
24. Stand up the discipline from zero: the ninety-day sequence with stated logic.

### Deliberate exclusions (confirmed)
No ML internals; no prompt engineering; no AI strategy/use-case ideation; no regulatory AI governance beyond boundary-drawing.

### Summit judgment
Competencies 18 and 19 are the summit. Everything else exists so the reader can do those two.

## Stage 2: Assessment Evidence (LOCKED)

Register: MBA-final-exam caliber, numerically real, no gentle versions (fading policy supplies the on-ramps). Every Group 3 assessment produces an artifact with consequences, graded on whether it survives the room it is written for.

1. CIO memo reply: defend consumption economics against the strongest flat-rate objection.
2. Three-flow mapping on a cited real deployment; marked-up flow diagram plus per-flow diagnosis. Recurs across the book (interleaving).
3. Two parts: prose derivation of the asymmetry consequence (why "unknown" is the damning word); spot-the-error on three real quotes (claimed-as-realized, netting-against-access-price, adoption-as-value).
4. Registry literacy on THM-008: restate conditions; state non-claims; trace one lemma to propositions; answer the "word games" objection. Requires the trace set piece earlier in the book.
5. Stylized provider model: compute unprofitable subscribers under flat rate given a skewed usage distribution; predict next three mechanisms ranked; map one documented episode (cited, dated) onto the mechanism menu.
6. Sort-and-repair: classify eight real cited statements (claimed/realized/productivity claim/measurement/ROI); rewrite two into true ROI claims by supplying boundary elements.
7. Essay pair: the category error explained to a board member; then the reversal test (construct the scenario where frontier IS economically correct, and state the conditions).
8. Legal-ops contract review: requirements decomposition; score three models against requirements; cost-at-volume recommendation. Built-in trap: frontier wins benchmark, mid-tier clears requirements at fraction of cost.
9. TCO assembly from scattered internal facts; first-year vs steady-state; multiple over access price.
10. Switching payback: per-task savings vs transition costs; volume threshold below which switching never pays; partial-switch wrinkle (Model B inadequate on one workflow).
11. Usage budget from six months of history (seasonal, steady, headcount-driven, erratic) plus business events; driver per line; numeric pre-committed anomaly thresholds.
12. Variance decomposition of a 62% overage into three causes (business growth / silent prompt change tripling tokens / test loop on production account); different prescription per cause.
13. Metering specification: minimum event schema (timestamp, actor, workflow tag, model, volumes, rate reference); consolidation point; tagging enforcement; coverage test including shadow usage estimate.
14. Attribution under three bases (per-token, per-request, per-seat) on twelve weeks of records; rankings reorder by construction; CFO memo defending the choice; answer the tripled team's objection.
15. One-page monthly AI operations report from a half-cleaned multi-provider export; graded: would a CFO act on it.
16. Routing policy document: five task classes across three capacity tiers; defaults, escalation and demotion triggers; projected cost vs everything-on-frontier baseline.
17. Constraint response: provider cuts rate limit 40% for two weeks; then budget-ceiling variant; graded on the stated generative rule, not the answers.
18. CAPSTONE: two quarters of a customer-service workflow; full messy picture including vendor "30% productivity" claim and two confounds (product change, attrition). Boundary declaration, loaded cost, realized-only value, netting with limitations. The 30% claim evaporates; a smaller defensible number survives.
19. Boundary charter following 18: owner (defended against alternatives), reporting cadence, pre-agreed expansion and kill thresholds. Fails if owner lacks authority.
20. Diagnostic packet (org chart, budget lines, dashboard screenshots, three stakeholder transcripts): score each of THE FIVE QUESTIONS as answerable/partial/unanswerable with packet evidence; place on maturity path; name the single highest-yield next move. Full-transformation prescriptions fail.
21. Org design under constraint (4,000-person firm, ~2% opex, existing FinOps team, two roles only): placement argument (CFO vs CIO vs COO), role charters, RACI, and the FinOps boundary treaty (graded hardest).
22. Negotiation dossier vs a realistic composite proposal (flat rate, buried soft-cap, unilateral repricing, no export commitment): provider-exposure analysis, leverage inventory (records, routing optionality, switching analysis), ranked term sheet, walk-away line. Thesis: leverage IS the AIOM records.
23. Compression: capstone dataset to three exhibits + 400 words for a 10-minute CFO slot; every number traces; no vendor statistics; specific ask. CFO-chair rubric: cost, benefit, verification, accountability.
24. FINAL EXAM: first Head of AI Operations inherits the Unmanaged-stage packet; ninety-day plan in three tranches; sequencing logic graded (metering before budgeting; one rough boundary in first thirty days; routing deferred; explicit not-doing list); day-90 self-assessment defined on day one. Standing up all five functions at once fails.

## Craft inventory: the book's named machinery (17 items)

Generated by Stage 2; these are the book's original contributions, to be named as a set.

1. Requirements decomposition worksheet + capability-vs-suitability scoring grid (C8)
2. The TCO ledger: standard cost-category checklist (C9)
3. The switching-cost model with adequacy gate (C10)
4. The usage budget: driver-based forecast + pre-committed deviation rule (C11)
5. The variance decomposition: volume/intensity/rate + cause classification (C12)
6. The event record schema + consolidation reference architecture (C13)
7. The attribution decision framework: bases, incentives, gaming, fit test (C14)
8. The one-page AI operations report (canonical format) (C15)
9. The routing policy format: classes, defaults, escalation/demotion triggers, cadence (C16)
10. The priority schema: criticality tiers + degradation ladder (C17)
11. The value-boundary worksheet (the book's signature artifact) (C18)
12. The boundary charter: one-page ownership document (C19)
13. The maturity model: five stages (proposed: Unmanaged, Visible, Attributed, Governed, Optimized), each defined by which of THE FIVE QUESTIONS the organization can answer with records rather than opinions. Requires deliberate design. (C20)
14. The function charter + interface RACI, incl. the FinOps boundary treaty (C21)
15. The sourcing dossier + term-sheet checklist for AI capacity contracts (C22)
16. The three-exhibit briefing format: flow picture, netting, ask (C23)
17. The ninety-day standing-up sequence (canonical adoption path) (C24)

## Research obligations logged

- Case bank: documented, citable market episodes for C5 (provider mechanism episodes) and C6 (real value/ROI statements); real deployment descriptions for C2 and chapter opening cases.
- FinOps Foundation framework: engage honestly and by name for the C21 boundary treaty.
- The capstone dataset: construct once, thread everywhere, label as constructed.

## Next: Stage 3

Derive the chapter structure as the shortest well-sequenced path through the competencies, honoring: institutional layer last; trace set piece early; metering-before-budgeting logic; worked-example fading; cumulative part-level cases; the summit (C18/C19) as the structural climax.
