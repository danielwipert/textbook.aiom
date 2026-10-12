# Chapter 3, Stage 3. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 3 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html`
RENDER         `Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_Stage3_render.pdf`, FAILING a print gate on this file: overflow: [(12, 419.3, ',')]; 1 definition callout(s) split across a page break; run place.py on this chapter; footnotes not on the page of their call: [(10, ['11']), (12, ['11'])].

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. Nothing yet. This chapter carries no
ruled claim narrowings, so every finding a checker raises here is new.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    7 keys defined, 7 cited, 0 orphans, 0 dangling. CORRECTED
                      BY HAND: the tool reads paragraphs only and reported
                      gartner-aiops and kreuzberger-2023-mlops as orphans. Both
                      are cited in Table 3.1, added below as T1 to T3.
  Citation markers    20 cited passages (17 paragraphs, 3 table cells), every
                      marker resolving to a key.
  Footnote build      21 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    nothing to check. No ruling is recorded for Ch03 yet.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> In February 2026, the FinOps Foundation revised its mission statement. For years, it said it existed to advance the people who manage cloud value. The new statement changed a single word: it now advances the people who manage technology value.

CITES: `finops-2026-mission`

IN-CHAPTER GLOSS: The mission statement before and after the change.

### C2

CLAIM TEXT AS IT STANDS

> The change accompanied the Foundation’s annual survey of practitioners: people inside companies who manage cloud spending. The 2026 survey included 1,192 respondents who collectively oversaw more than $83 billion in annual cloud spending. Its central finding concerned work the discipline was not originally created to do. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

CITES: `finops-2026-state`, `finops-2026-state`

IN-CHAPTER GLOSS: Survey size and the cloud spending its respondents manage.

### C3

CLAIM TEXT AS IT STANDS

> FinOps was built to solve a specific problem: engineers could buy cloud capacity with a few lines of code, but the bill arrived only after they had used it. The discipline emerged to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending as well, and by 2026, nearly all of them managed it.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The practice as the Foundation defines it.

### C4

CLAIM TEXT AS IT STANDS

> The report also recorded a question this work had not yet answered. Asked whether AI was delivering value, one practitioner replied in words the report chose to quote: “No one can answer that question yet.”

CITES: `finops-2026-state`

IN-CHAPTER GLOSS: Practitioner quotation as reproduced in the report.

### C5

CLAIM TEXT AS IT STANDS

> The registry also records which claims are complete. A claim is certified when every claim it depends on is itself certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status from the graph at each version; no one enters it manually. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every claim marked empirical has evidence attached, and that a reviewer has signed off on the claim’s current wording. These checks establish the structure and record of an argument, not its truth. If a claim has a gap in its support, the registry records what is missing. This book presents and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science does.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: What the validator checks.

### C6

CLAIM TEXT AS IT STANDS

> The propositions are small claims, each nearly obvious on its own. PROP-043 states: “If activity is metered, records describing measured activity are generated or maintained.” PROP-053 states: “If economic exposure exists, monitoring mechanisms may be used to observe the sources or magnitude of that exposure.” PROP-085 states: “If usage information becomes visible, decisions regarding management, allocation, optimization, or monitoring may reference that information.” No manager would dispute these claims; the work lies in combining them. PROP-043 says that metered activity leaves a record, PROP-085 allows management decisions to draw on visible usage, and PROP-053 adds that monitoring can be used to observe economic exposure. None of the three alone establishes that controls can be applied to what is visible. LEM-020 reaches that conclusion by combining them with four further propositions and LEM-002, a combination the registry records as its proof.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s proof record and its supporting propositions.

### C7

CLAIM TEXT AS IT STANDS

> The registry version used to write this book held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records of evidence the science still needs. It recorded 1,777 dependency links among them, and 397 of the 413 objects were certified. These figures describe one version of the registry, which is revised as the science develops, rather than the science itself.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: Object counts, links and certification at the pinned registry version.

### C8

CLAIM TEXT AS IT STANDS

> The scope defines which cases the claim addresses. As presented in this book, THM-004 states its scope before the word “if”: one defined deployment and its measurement boundary. The registry adds that the theorem applies where an organization seeks economic control over the resulting cost. The claim thus concerns one deployment within one boundary, rather than an organization’s AI activity in general. To apply it across a whole company, a manager must first show that each deployment meets the conditions.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-004’s scope condition.

### C9

CLAIM TEXT AS IT STANDS

> The non-claims identify what the claim deliberately does not establish. THM-004 says that governance is necessary for control, but it does not say that governance delivers control or is costless. It specifies neither the scale at which the requirement begins to apply nor the size of the exposure. It also does not establish Chapter 2’s three flows, which belong to this book’s framework rather than the registry’s. The registry records each claim’s non-claims. A reader with only the statement can identify most of them by asking whether a requirement is sufficient or merely necessary, whether the claim specifies an amount, and what it says about cost.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-004’s recorded exclusions.

### C10

CLAIM TEXT AS IT STANDS

> The most costly misreading confuses necessary with sufficient. A manager who reads THM-004 as “governance produces control” might buy a dashboard and expect costs to settle. The theorem makes no such promise: it says only that without governance, there is no route to control. One level down, LEM-020 makes the same limit explicit: it does not claim that management mechanisms are automatically effective.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s recorded exclusions.

### C11

CLAIM TEXT AS IT STANDS

> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself by identifying what it cost, what it returned, the months covered, and the outcome used to judge it. The registry’s LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” The organization must set that boundary for each deployment and identify who is responsible for knowing whether it paid for itself. This book calls it the value boundary.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-021’s statement.

### C12

CLAIM TEXT AS IT STANDS

> FinOps is the nearest neighbor, making its border with AI Operations Management the hardest to draw. It already manages spending, has moved toward AI, and defines its purpose in terms of maximizing technology’s business value. Chapter 14 examines how the two divide the work. Their border rests on what each was built to do, rather than on intent: FinOps was built to make cloud bills accountable after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The Foundation’s definition, which names business value.

### C13

CLAIM TEXT AS IT STANDS

> Step 4 also asks what each dependency adds. LEM-020’s scope requires the organization to have reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, not to the third condition. A team that can see its costs but has no authority to cap them falls outside LEM-020’s scope. The lemma therefore does not support THM-004’s third condition for that team, and the theorem says nothing about it. The team is in the same position as the pilot in Section 3.3, which fails the first condition. The trace has revealed a limit that the theorem’s wording does not show.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s scope condition.

### C14

CLAIM TEXT AS IT STANDS

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. It adds a condition: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says that compute use can be measured. PROP-039 says that measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it, while PROP-042 says that measured activity can be distinguished by quantity. PROP-043 says that metering produces records of what was metered. PROP-053 says that monitoring can be used to observe economic exposure, adding the condition that there is exposure to observe. PROP-085 says that once usage is visible, management decisions can draw on it. Together, these claims explain why visibility makes management possible.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-002’s scope condition.

### C15

CLAIM TEXT AS IT STANDS

> Step 5. LEM-020 establishes that visibility makes management mechanisms available. It does not claim that those mechanisms work automatically or that visibility alone determines the right policy or price.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: LEM-020’s recorded exclusions.

### C16

CLAIM TEXT AS IT STANDS

> Step 3. The theorem has four dependencies: LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates how a contextual dependency contributes: it bears on what a buyer can do about an understated cost once that cost is visible, but the claim that the cost is understated holds without it.

CITES: `aibe-registry-2026`

IN-CHAPTER GLOSS: THM-002’s dependencies and their recorded roles.

### C17

CLAIM TEXT AS IT STANDS

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

CITES: `klarna-2024-assistant`

IN-CHAPTER GLOSS: All figures in this case are the company’s own, as announced.

### T1 (Table 3.1, AIOps row; added by hand)

CLAIM TEXT AS IT STANDS

> AIOps. What it is for: Applying machine learning to run IT operations: correlating events, detecting anomalies, finding causes. What it manages: The health and performance of IT systems. What it lacks for this territory: It uses AI to watch systems. It does not govern what consuming AI costs or returns

CITES: `gartner-aiops`

IN-CHAPTER GLOSS: The originating definition of AIOps.

### T2 (Table 3.1, MLOps row; added by hand)

CLAIM TEXT AS IT STANDS

> MLOps. What it is for: Building, deploying, and monitoring machine learning models in production. What it manages: The lifecycle of models an organization builds. What it lacks for this territory: It ships models. It does not govern the consumption of capacity an organization buys

CITES: `kreuzberger-2023-mlops`

IN-CHAPTER GLOSS: Definition and scope of MLOps.

### T3 (Table 3.1, FinOps row; added by hand)

CLAIM TEXT AS IT STANDS

> FinOps. What it is for: Financial accountability for technology spending, through collaboration among engineering, finance, and business teams. What it manages: Cloud and wider technology spending. What it lacks for this territory: It was built around cloud billing. A practitioner told its own survey that no one could yet say whether AI provides value

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The Foundation’s own definition of the practice.

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

### `gartner-aiops`

- **type**: web
- **authors**: {"org": "Gartner"}
- **title**: AIOps (Artificial Intelligence for IT Operations)
- **container**: Gartner Information Technology Glossary
- **url**: https://www.gartner.com/en/information-technology/glossary/aiops-artificial-intelligence-operations
- **perishable**: True
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C, AND THE URL IS A CANDIDATE. Search coverage attributes to the Gartner glossary: AIOps combines big data and machine learning to automate IT operations processes, including event correlation, anomaly detection and causality determination. Table 3.1 paraphrases it. Check A must find the live glossary page, confirm the wording, and correct the URL.

### `kreuzberger-2023-mlops`

- **type**: article
- **authors**: Dominik Kreuzberger, Niklas Kühl, Sebastian Hirschl
- **title**: Machine Learning Operations (MLOps): Overview, Definition, and Architecture
- **container**: IEEE Access
- **volume**: 11
- **date**: 2023
- **pages**: 31866-31879
- **doi**: 10.1109/ACCESS.2023.3262138

NOTE, verbatim:

> STAGE 0, 2026-10-01, UNVERIFIED, GRADE C. Bibliographic details from search results. Table 3.1 paraphrases the scope of MLOps as building, deploying and monitoring machine learning models in production. Check A must confirm the paper’s own definition supports that paraphrase, and the volume, pages and DOI.
