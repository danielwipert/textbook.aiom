# The Northland Dataset v1.0 (LOCKED DESIGN)

Textbook: *AI Operations Management*. The book's single recurring constructed dataset, threaded through the problem sets of Chapters 8-12 and 15, and supplying the Chapter 13 diagnostic packet.
Approved by Dan, July 19, 2026. Design locked; numerical build deferred to a dedicated session when outlining reaches Part III.

## The company

NORTHLAND APPAREL: a mid-size apparel brand, roughly 4,000 employees (matching the Ch14 org-design problem), selling through direct-to-consumer e-commerce and a wholesale account channel. Mature, conventional supply chain function (sourcing, inventory, freight) already in place.

Why apparel (Dan's selection, ratified): universally understood; nobody needs the industry explained; rich layered seasonality (SS/FW drops, holiday peak, campaign spikes); real complications (returns, sizing, SKU breadth, channel mix); physical goods; and decisively, apparel is the canonical supply chain teaching industry (Zara et al.), so the manifesto's central analogy (the mature goods-flow discipline vs the absent AI-flow discipline) is mirrored inside an industry where MBA readers already learned what a mature flow discipline looks like.

Name diligence: run a trade-name collision check before print; include the standard fictional-entity disclaimer in the construction note regardless.

## Structural ruling: one company, two moments

The Ch13 diagnostic packet and the Part III dataset are the SAME company at two points in time.
- T0: Northland is Unmanaged (maturity model Stage 1). This state IS the Ch13 diagnostic packet (org chart, budget lines, dashboard screenshots, three stakeholder transcripts).
- The Ch15 final exam (the ninety-day plan) is the plan that stood up Northland's metering.
- Part III's dataset is the twelve months of records that resulted.
No narrative, no characters, no story (per Dan's ruling against a running case): one dataset with a timestamp axis. Payoff: the reader's final exam produces the plan that explains where the numbers they have worked all book came from; the Ch15 CFO briefing compresses a year they personally analyzed.

## The workflow portfolio (five, each engineered to its assessment job)

1. INQUIRY AND RETURNS TRIAGE
   - Classifying inbound contacts (order status, sizing, returns initiation). High-volume, cheap per event. The boring workflow quietly carrying the program. Routing class: bulk tier.
   - Forecast texture: steady base with one known post-holiday bump (deliberately more instructive than flat).
2. CUSTOMER SERVICE ASSIST  [THE CAPSTONE WORKFLOW]
   - Direct-to-consumer service center, two quarters into production at netting time. Carries the vendor's "30% productivity improvement" claim.
   - Confound 1: a size-guide overhaul (or sizing revision on a top-selling line) that cut sizing-related contacts. Physical, visible, undeniable.
   - Confound 2: agent attrition (two agents departed in the netting period).
   - Engineered outcome (C18): the 30% claim evaporates under boundary discipline; a smaller, real, defensible number survives.
3. SUPPLIER CONTRACT AND COMPLIANCE REVIEW
   - Sourcing agreements and factory compliance documents. Lumpy around the sourcing calendar. Few users, enormous documents (heavy tokens per request). Attribution triangle corner 1.
4. WHOLESALE SALES COPILOT
   - Quoting, assortment, account support for the wholesale team. Grows with a planned account-expansion hiring wave (the Ch10 headcount driver). Many users, moderate usage. Corner 2.
5. MARKETING CONTENT STUDIO
   - Seasonal drops and campaigns make this genuinely erratic and bursty. Small team, token monsters. Corner 3. Home of the silent prompt-change efficiency failure (a template change tripling tokens per task).

Supporting strands:
- Control failure: an e-commerce engineering team's test loop running against a production API key (Ch10's third variance cause; also Ch8 metering texture).
- Shadow usage: designers and marketers on personal accounts for creative work (Ch8 coverage-test texture; realistic for apparel).
- Providers: two external AI providers plus one internal gateway, imperfect workflow tagging (Ch9's half-cleaned multi-provider export).

## Engineered pedagogical properties (assertions the numerical build must satisfy)

A. ATTRIBUTION REORDERING (Ch9, C14): workflows 3, 4, 5 share one account; cost rankings must REORDER under per-token, per-request, and per-seat bases (few-users/huge-requests vs many-users/moderate vs small-team/bursty are the levers). Each basis crowns a different "most expensive team."
B. THE 62% QUARTER (Ch10, C12): one quarter runs 62% over aggregate budget from three causes in three workflows: wholesale copilot demand surge from the account expansion (healthy, value question open); marketing studio silent prompt change tripling tokens per task (efficiency failure); engineering test loop on production key (control failure). Decomposition: volume vs intensity vs rate effects.
C. SEASONAL FORECASTABILITY (Ch10, C11): drops, holiday peak, and hiring wave produce a forecast an attentive reader can defend driver-by-driver, with pre-committed anomaly thresholds that the 62% quarter then trips.
D. ROUTING ECONOMICS (Ch11, C16/C17): five task classes map to three capacity tiers; an everything-on-frontier baseline vs policy cost gap large enough to motivate, small enough to be honest. Constraint scenarios: a mid-quarter provider rate-limit cut (40%, two weeks) and a budget-ceiling variant.
E. THE NETTING (Ch12, C18): capstone workflow's fully loaded cost (usage + review labor + error incidents + governance) netted against realized-only value (handle-time and deflection changes with both confounds removed). The vendor claim dies; a smaller true number survives; limitations statable in two sentences.
F. COMPRESSIBILITY (Ch15, C23): the year must reduce honestly to three exhibits and 400 words.

## Build specification (deferred session)

- Implement as a seeded Python generator script, not a hand-made spreadsheet: parameters at top; every property A-F asserted by automated checks; regenerate and retune at will during drafting.
- Outputs: raw event records (Ch8/9 problems), the half-cleaned multi-provider export (Ch9), budget and actuals tables (Ch10), task-class and tier tables (Ch11), the capstone workflow panel (Ch12), the T0 diagnostic packet artifacts (Ch13), and answer keys.
- Construction note for the book: data is synthetic, how it was generated, fictional-entity disclaimer.

## Status

Structure document open item 3: CLOSED. Remaining before chapter outlining: case-bank research (open item 4).
