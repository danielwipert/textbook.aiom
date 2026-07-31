# The AIOM Maturity Model v1.0 (LOCKED)

Textbook: *AI Operations Management*. Framework home: Chapter 13 (Diagnosis and Maturity), craft item 13 of 17.
Approved by Dan, July 19, 2026. All four design rulings accepted.

## Definition

An organization's AI Operations maturity, within a declared scope, is the highest stage for which it can produce all required evidence artifacts on demand, together with all artifacts of the stages below.

Maturity is a claim about records, not intentions. The evidence artifacts are the book's own craft templates; a maturity claim is therefore checkable in an afternoon.

## Design principles (rulings, locked)

1. STRICT LADDER. Stages are strictly ordered because the ordering is a dependency fact about records: no other Founding Question is answerable with records until Question 3 (metering and attribution) is. Jagged organizational profiles are preserved in the per-question diagnostic beneath the stage label; the label is the honest compression.
2. NAMES: Unmanaged, Visible, Attributed, Governed, Accountable. Each names what the organization HAS. "Accountable" replaces the placeholder "Optimized": optimization is an unending activity, not a state, and the discipline's summit is the value boundary, not efficiency. Accountable is Question 5's own word.
3. GOVERNED IS A STRICT BUNDLE. All three control artifacts (budget, sourcing memo, routing policy) or the stage is not claimed. Sub-stages rejected: memorability is the stage model's job; precision is the diagnostic's job. A strict bundle converts partial progress into a to-do list rather than self-congratulation.
4. ONE BOUNDARY SUFFICES for Accountable, per the manifesto's standard: "somewhere specific, someone is accountable." Coverage fractions rejected as arbitrary. Expanding boundary coverage is continuous work WITHIN Stage 5, never finished, and the model does not pretend otherwise.

## The five stages

### Stage 1: Unmanaged
No Founding Question answerable with records. The flow runs, cost accrues by default, opinions circulate. The manifesto's opening condition.
Evidence: none exists.

### Stage 2: Visible
The first half of Question 3: the organization can say who consumed what.
Evidence artifacts: the consolidated usage record with its coverage test, including a shadow-usage estimate (Ch8 template: event schema + consolidation + coverage test).

### Stage 3: Attributed
Question 3 fully answerable: who consumed what, in service of which work. Responsibility has an address.
Evidence artifacts: a chosen and defended attribution basis; the attributed cost statement, i.e. the one-page AI operations report (Ch9 templates).

### Stage 4: Governed
Questions 1, 2, and 4 answerable with records. The three control functions are live. ("Governed" is cost governance in THM-004's sense; one sentence in Ch13 fences off regulatory AI governance.)
Evidence artifacts, ALL required:
- Forecast-versus-actual by workflow with pre-committed deviation thresholds (Ch10 template).
- A sourcing decision memo showing requirements decomposition and cost-at-volume (Ch7 templates).
- A written routing/priority policy plus at least one documented instance of the policy deciding something under a binding constraint (Ch11 templates).

### Stage 5: Accountable
Question 5 answerable: somewhere specific, the flow answers for itself.
Evidence artifacts: at least one live value boundary with a completed netting (realized value against fully loaded cost, limitations stated) and a signed boundary charter naming the owner, cadence, and decision thresholds (Ch12 templates).
Work within Stage 5: expanding boundary coverage, tightening nettings, pruning workflows the nettings condemn. This work does not end.

## The scope rule

Maturity is assessed within a declared scope (enterprise, division, workflow portfolio). Different scopes may legitimately sit at different stages, and precise mixed statements are the intended usage: "Claims processing is Accountable; the enterprise is Visible." This is boundary discipline applied to the model itself.

## Registry grounding (the ladder is proven, not asserted)

- Onto the ladder: LEM-002 (measurement enables visibility); LEM-011 (recorded tokenized activity produces measurable usage).
- Up through Attributed: PROP-046/047 (measured usage associates to entities; attribution enables responsibility assignment); LEM-003 (measured, attributed usage enables rule-based differentiated treatment).
- Opening Governed: LEM-020 (visibility enables management mechanisms); THM-004 (scaled deployment requires cost governance for economic control); THM-010 (economic control requires visibility into the managed boundary).
- The summit: LEM-021 (ROI evaluation requires a measurement boundary); THM-006 (AI ROI requires both a cost boundary and a value boundary).
Design note for Ch13 prose: the stages were designed from pedagogy; the registry proves the ordering is necessary. State this relationship explicitly; it models the science-discipline architecture the book teaches.

## Chapter 13 implications

- Opening case: the false-maturity confrontation. An organization with an "AI budget" but no metering believes it is Governed; the artifact test shows an access budget that cannot detect deviation by workflow; verdict Unmanaged or Visible. (Case to be sourced or constructed per evidence policy.)
- Craft section: the diagnostic procedure (competency 20): score each Founding Question answerable / partially answerable / unanswerable WITH cited artifacts; declare scope; assign stage; name the single highest-yield next move (which the strict ladder makes derivable: it is always the lowest missing artifact).
- The diagnostic packet assessment (Stage 2 of backward design, C20) grades evidentiary discipline; full-transformation prescriptions fail.
- Ch15 dependency: the ninety-day sequence is the ladder walked deliberately (metering first, one rough boundary early for political capital); the day-90 self-assessment uses this model.

## Status

Open item 2 (structure document): CLOSED. Remaining before chapter outlining: capstone dataset (name + design), case-bank research.
