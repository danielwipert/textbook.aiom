# Chapter 3, Stage 3. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 3 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html`
RENDER         `Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_Stage3_render.pdf`, FAILING a print gate on this file: footnotes not on the page of their call: [(7, ['7']), (8, ['7'])].

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. Nothing yet. This chapter carries no
ruled claim narrowings, so every finding a checker raises here is new.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    7 keys defined, 5 cited. 2 orphan(s), 0 dangling.
                      orphans: gartner-aiops, kreuzberger-2023-mlops
  Citation markers    17 cited passages, every marker resolving to a key.
  Footnote build      21 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    nothing to check. No ruling is recorded for Ch03 yet.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as advancing the people who manage cloud value. The new statement replaced one word: the Foundation now advances the people who manage technology value.

CITES: `finops-2026-mission`

IN-CHAPTER GLOSS: The mission statement before and after the change.

### C2

CLAIM TEXT AS IT STANDS

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned work the discipline had not originally been created to do. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

CITES: `finops-2026-state`, `finops-2026-state`

IN-CHAPTER GLOSS: Survey size and the cloud spending its respondents manage.

### C3

CLAIM TEXT AS IT STANDS

> FinOps was built to address a specific problem: cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of them were managing it.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The practice as the Foundation defines it.

### C4

CLAIM TEXT AS IT STANDS

> The report also recorded what practitioners had yet to establish. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

CITES: `finops-2026-state`

IN-CHAPTER GLOSS: Practitioner quotation as reproduced in the report.

### C5

CLAIM TEXT AS IT STANDS

> The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status from the graph at each version; no one enters it manually. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: What the validator checks.

### C6

CLAIM TEXT AS IT STANDS

> The propositions are small claims that appear nearly self-evident in isolation. PROP-043 states: “If activity is metered, records describing measured activity are generated or maintained.” PROP-053 states: “If economic exposure exists, monitoring mechanisms may be used to observe the sources or magnitude of that exposure.” PROP-085 states: “If usage information becomes visible, decisions regarding management, allocation, optimization, or monitoring may reference that information.” Their contribution becomes clearer when they are combined. PROP-043 establishes that metered activity leaves a record. PROP-085 allows management decisions to draw on visible usage, and PROP-053 establishes that monitoring can be used to observe economic exposure. None of the three alone says that controls can be applied to visible activity. LEM-020 reaches that conclusion by combining them with four further propositions and LEM-002, a combination the registry records as its proof.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s proof record and its supporting propositions.

### C7

CLAIM TEXT AS IT STANDS

> In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: Object counts, links and certification at the pinned registry version.

### C8

CLAIM TEXT AS IT STANDS

> The scope defines which cases the claim covers. As presented in this book, THM-004 states its scope before the word “if”: one defined deployment and its measurement boundary. The registry adds that the theorem applies when an organization seeks economic control over the resulting cost. The claim concerns one deployment within one boundary, rather than an organization’s AI activity in general. Before applying it across a company, a manager must show that each deployment meets the conditions.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-004’s scope condition.

### C9

CLAIM TEXT AS IT STANDS

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records every claim’s non-claims. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-004’s recorded exclusions.

### C10

CLAIM TEXT AS IT STANDS

> The most costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s recorded exclusions.

### C11

CLAIM TEXT AS IT STANDS

> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” The organization must set that boundary for each deployment and name the person responsible for knowing the answer. This book calls it the value boundary.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-021’s statement.

### C12

CLAIM TEXT AS IT STANDS

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The Foundation’s definition, which names business value.

### C13

CLAIM TEXT AS IT STANDS

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team, and the theorem says nothing about it. Like the pilot in Section 3.3 that fails the first condition, the team falls outside the theorem’s coverage. The trace reveals a limit not stated in the theorem’s own wording.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s scope condition.

### C14

CLAIM TEXT AS IT STANDS

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. It adds a condition: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-002’s scope condition.

### C15

CLAIM TEXT AS IT STANDS

> Step 5. LEM-020 establishes that visibility makes management mechanisms available. It does not establish that the mechanisms work automatically or that visibility alone determines the right policy or price.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s recorded exclusions.

### C16

CLAIM TEXT AS IT STANDS

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that the cost is understated holds without it.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-002’s dependencies and their recorded roles.

### C17

CLAIM TEXT AS IT STANDS

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

CITES: `klarna-2024-assistant`

IN-CHAPTER GLOSS: All figures in this case are the company’s own, as announced.

---

## Part 2. Register entries, verbatim

### `aibe-registry-2026`

- **type**: web
- **authors**: {"org": "AI Business Economics registry"}
- **title**: dag.aiom, commit 9d7ee50
- **date**: 2026-08-21

NOTE, verbatim:

> The registry version pinned in AIOM_Registry_Manifest.json. Counts in the dated box are read from the manifest’s counts, certified_counts and edge count, not from search. If the manifest is refreshed, the dated box is updated or left describing this version, never silently mixed.


### `finops-2026-mission`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures Across Technology Value
- **date**: 2026-02-19
- **url**: https://finance.yahoo.com/news/state-finops-survey-ai-value-160000371.html
- **perishable**: True
- **accessed**: 2026-10-01
- **upgrade**: The Foundation’s own release or mission page, if one states the before and after wording.

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C. Search coverage gives the old mission as advancing the people who manage the value of cloud and the new one as advancing the people who manage the value of technology, changed February 2026. Check A must confirm both wordings and the date. One summary says the change was the first in the Foundation’s history; the chapter does not claim that.


### `finops-2026-state`

- **type**: report
- **authors**: {"org": "FinOps Foundation"}
- **title**: State of FinOps 2026
- **date**: 2026-02-19
- **url**: https://data.finops.org/
- **perishable**: True
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C. Search coverage converges on: 1,192 respondents; more than $83 billion in annual cloud spend; 98 percent managing AI spend, against 31 percent two years earlier; the quotation ’Is your AI providing value? No one can answer that question yet.’ Check A must confirm each figure, that the quotation appears in the report itself and is attributed to a practitioner, and that the 31 percent figure is the 2024 survey’s. The spec also cites 63 percent for 2025; the chapter does not use it.


### `finops-what-is`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: What is FinOps?
- **url**: https://www.finops.org/introduction/what-is-finops/
- **perishable**: True
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C. Search summary of the definition: an operational framework and cultural practice which maximizes the business value of technology, enables timely data-driven decision making, and creates financial accountability through collaboration between engineering, finance, and business teams. Table 3.1 paraphrases it and section 3.5 says it names business value. Check A must confirm the wording on the live page.


### `klarna-2024-assistant`

- **type**: web
- **authors**: {"org": "Klarna"}
- **title**: Klarna AI assistant handles two-thirds of customer service chats in its first month
- **date**: 2024-02-27
- **url**: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- **perishable**: True
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED. Grade A in the case bank as a primary, but nobody on this project has read it from this container. Figures used: 2.3 million conversations; two-thirds of customer-service chats; work of 700 full-time agents; resolution under two minutes against eleven; estimated $40 million profit improvement in 2024. Check A must confirm each against the release. PROTECT THE CHAPTER 6 REVEAL: the case uses this announcement only and must not cite or allude to any later reporting.

