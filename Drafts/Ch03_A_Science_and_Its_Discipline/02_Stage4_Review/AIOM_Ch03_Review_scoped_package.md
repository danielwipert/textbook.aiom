# Scoped review package: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file: your instructions, the required output format,
and all the material, between BEGIN and END markers in Part 3. Do not ask for
other files. Read the whole file before you begin.

---

## PART 1. Your task

You are reviewing part of one chapter of an academic textbook for business
graduate students, *AI Operations Management*. The whole chapter was reviewed
earlier and passed. Since then, a fact check led to 35 passages being changed,
mostly to make sentences claim no more than their sources or the book's formal
registry support. **Review only those 35 passages.** The rest of the chapter is
there for context and is out of scope.

- **Document 1** gives each changed passage BEFORE and AFTER, labelled with its
  section. Some passages are footnote glosses, table cells, a figure caption, or
  a key-term entry rather than body paragraphs.
- **Document 2** is the whole chapter as it now stands, as tagged blocks.
- **Document 3** is the reference extract: what the chapter must do, and the
  seven craft criteria C1 to C7.

### Three warnings

1. **The narrowing is settled.** Each change was ruled by the author for
   accuracy. A finding that a passage should claim more, or return to its
   BEFORE wording, will be discarded. A fix you propose must keep what the
   AFTER wording claims and does not claim. Fixing HOW it says it is in scope.
2. **Formal statements are not prose.** Statements of theorems, lemmas and
   propositions (THM-004, LEM-021, PROP-043 and so on) and their names are
   verbatim from the registry. Judge the prose around them.
3. **Sourcing is out of scope.** The fact check has closed.

### What to look for, in each changed passage

**Section A, structure.** Does the change disturb what its slot or section is
for? Does it front-run something a later chapter is meant to reveal, or add a
promise the chapter does not keep? Does an added sentence repeat what a nearby
sentence already says?

**Section B, teaching.** Read each AFTER passage with its neighbors in Document
2. Where does the edit leave a seam: a repeated word or idea, a pronoun whose
referent changed, a sentence that no longer follows from the one before, a
paragraph that now ends weakly? Would a sceptical, busy MBA reader stall here?

**Section C, voice and craft.** Grade the changed passages against C1 to C7.
Quote the WEAKEST changed passage for each criterion. If a criterion is met
everywhere, say so in one row and quote the passage that comes closest to
failing it. House rules: no em or en dashes, no contractions, no rhetorical
questions, no hedging ("perhaps", "some argue"); accurate qualification is not
hedging.

Read adversarially. A review that finds nothing will be discarded as
confirmatory; one that invents a defect will waste a round. Mark the
difference with the Type column.

---

## PART 2. Required output format

Reply in Markdown, using exactly this structure and nothing else. No preamble.

```
# Scoped review: Chapter 3

## Section A: Structure
## Section B: Teaching
## Section C: Voice and craft

## Findings

| ID | Sec | Passage (P-number) | Quote (exact, under 30 words) | What is wrong | Type | Severity | Suggested fix |
|---|---|---|---|---|---|---|---|
| SR-1 | B | P3 | "..." | ... | defect | medium | ... |

## Fix first
1. SR-n: one line on why
```

Rules for the table:

- **ID**: SR-1, SR-2, and so on, across all three sections.
- **Sec**: A, B or C. For Section C, start "What is wrong" with the criterion
  (C1 to C7), and give every criterion at least one row.
- **Quote**: copied exactly from the AFTER text in Document 1.
- **Type**: one of `defect`, `deliberate`, `noise`.
- **Severity**: one of `high`, `medium`, `low`.
- **Suggested fix**: exact replacement wording that keeps the AFTER claim.
- Under each Section heading, at most five sentences of overall judgment.
- Do not use em dashes or en dashes anywhere in your reply.

---

## PART 3. The material

<<<<< BEGIN DOCUMENT 1: THE 35 CHANGED PASSAGES, BEFORE AND AFTER >>>>>

### P1. The discipline that changed its mission  [BODY, PROVENANCE]

BEFORE:

> Dated: February 2026. Found by search. Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself. See the source register.
> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as advancing the people who manage cloud value. The new statement replaced one word: the Foundation now advances the people who manage technology value.

AFTER:

> Dated: February 2026. Figures and the quotation checked against the Foundation’s report and announcement, October 2026.
> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

### P2. The discipline that changed its mission  [BODY]

BEFORE:

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned work the discipline had not originally been created to do. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

AFTER:

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned the expansion of FinOps into AI spending. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

### P3. The discipline that changed its mission  [BODY, FOOTNOTE]

BEFORE:

> Share of practitioners managing AI spend, 2026 against 2024.
> FinOps was built to address a specific problem: cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of them were managing it.

AFTER:

> Share of respondents managing AI spend, 2026 survey against 2024 survey.
> FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of the survey’s respondents were managing it.
> Cloud consumption as variable and tracked after the fact.

### P4. The discipline that changed its mission  [BODY]

BEFORE:

> The report also recorded what practitioners had yet to establish. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

AFTER:

> The report also carried one practitioner’s statement of what remained unknown. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

### P5. The discipline that changed its mission  [BODY]

BEFORE:

> The survey reveals the gap Chapters 1 and 2 described, as reported by the people asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. Cloud cost management is a capable neighboring discipline that has expanded into work no discipline was designed to govern: the economics of an organization’s AI consumption.

AFTER:

> The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization’s AI consumption.

### P6. 3.1 Why name a science  [BODY]

BEFORE:

> Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, management based on them fails, however carefully managers carry it out.

AFTER:

> Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, careful execution does not repair the decisions built on them.

### P7. 3.1 Why name a science  [BODY]

BEFORE:

> These links are the registry’s most important feature. Every higher claim names the lower claims it depends on, which in turn name their own supporting claims. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader with the registry can start at any theorem and follow its supporting claims down to definitions and axioms. Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier. Readers can therefore trace any claim to the lemma level using the book alone. Below that level, they work from the propositions supplied in a chapter or exercise.
> For a manager, the graph resolves one practical concern: no conclusion rests on circular reasoning. A manager can therefore trace a doubt down to a smaller claim and examine it. Whether that smaller claim is true is a separate question the graph does not answer.
> The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status from the graph at each version; no one enters it manually. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

AFTER:

> These links are the registry’s most important feature. Every higher claim names the lower claims it depends on, which in turn name their own supporting claims. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader with the registry can start at any certified theorem and follow its supporting claims down to definitions and axioms. Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier. Readers can therefore trace any certified theorem to the lemma level using the book alone. Below that level, they work from the propositions supplied in a chapter or exercise.
> For a manager, the graph resolves one practical concern: no conclusion rests on a circular chain of recorded support. A manager can therefore trace a doubt down to a smaller claim and examine it. Whether that smaller claim is true is a separate question the graph does not answer.
> The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status at each version; no one enters the status by hand. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

### P8. 3.1 Why name a science  [BODY]

BEFORE:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. Chapters follow the order in which a manager needs to learn, which differs from the order in which the science derives its results. The registry supports each result the book teaches so that a reader who doubts a claim can trace its basis. Organizing the chapters by proof would leave a manager reading definitions for many pages before reaching a recognizable decision.

AFTER:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. Chapters follow the order in which a manager needs to learn, which differs from the order in which the science derives its results. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis. Organizing the chapters by proof would leave a manager reading definitions for many pages before reaching a recognizable decision.

### P9. 3.2 Tracing a result the reader already accepts  [BODY]

BEFORE:

> Tracing the theorem changes how a manager can use it. Initially, THM-004 is a conclusion to accept or reject as a whole. The trace reveals a set of smaller claims that can be examined individually, allowing a manager to identify which supporting claim they doubt. A disagreement over an entire conclusion has no obvious way to end. A disagreement over a specific proposition can be settled.

AFTER:

> Tracing the theorem changes how a manager can use it. Initially, THM-004 is a conclusion to accept or reject as a whole. The trace reveals a set of smaller claims that can be examined individually, allowing a manager to identify which supporting claim they doubt. A disagreement over an entire conclusion has no obvious way to end. A disagreement over a specific proposition concerns one stated claim, so the two sides can name the fact that would decide it.

### P10. 3.2 Tracing a result the reader already accepts  [BODY]

BEFORE:

> In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

AFTER:

> In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified, including 9 of the 11 theorems and 20 of the 21 lemmas. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

### P11. 3.3 How to read a formal claim  [BODY]

BEFORE:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records every claim’s non-claims. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

AFTER:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records the non-claims of every certified claim. The record is not exhaustive: the exclusion of Chapter 2’s three flows comes from this book, not from the registry. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

### P12. 3.3 How to read a formal claim  [BODY]

BEFORE:

> The most costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

AFTER:

> A costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

### P13. 3.3 How to read a formal claim  [BODY]

BEFORE:

> The falsifying case describes what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition but lacks the conclusion. The second and third conditions describe what measurement and management would make possible, rather than an apparatus already in place. A deployment with no instruments installed can therefore meet all four conditions. For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not provide such a case. If the fee covers every cost, the fourth condition fails. If it does not, the organization would have to control the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

AFTER:

> The falsifying case describes what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition but lacks the conclusion. The second and third conditions describe what measurement and management would make possible, rather than an apparatus already in place. A deployment with no instruments installed can therefore meet all four conditions.
> For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

### P14. 3.4 The discipline that acts on the science  [BODY]

BEFORE:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. The organization buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management resolves it by managing AI as a resource the organization consumes rather than as software it has bought.

AFTER:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management addresses it by managing AI as a resource the organization consumes wherever Chapter 1’s conditions hold.

### P15. 3.4 The discipline that acts on the science  [BODY]

BEFORE:

> The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. If two workflows share a provider account with a fixed rate limit, one waits whenever the other is busy. Allocation and routing make that choice deliberate by applying a rule.
> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” The organization must set that boundary for each deployment and name the person responsible for knowing the answer. This book calls it the value boundary.

AFTER:

> The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which. Allocation and routing make that choice deliberate by applying a rule.
> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary.

### P16. 3.4 The discipline that acts on the science  [FIGURE CAPTION]

BEFORE:

> Figure 3.2 The two layers. AI Business Economics states what is true about consuming AI. AI Operations Management acts on it through five functions, all taught in Part III.

AFTER:

> Figure 3.2 The two layers. AI Business Economics states conditional claims about consuming AI and records what each one rests on. AI Operations Management acts on it through five functions, all taught in Part III.

### P17. 3.4 The discipline that acts on the science  [BODY]

BEFORE:

> The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because a practice built on incorrect claims fails however well it is run.

AFTER:

> The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

### P18. 3.5 Where the discipline ends  [BODY]

BEFORE:

> The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins with that call, when each use consumes resources and costs money.

AFTER:

> The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins where a model is a service an organization can buy and call.

### P19. 3.5 Where the discipline ends  [FOOTNOTE, TABLE CELL]

BEFORE:

> Applying machine learning to run IT operations: correlating events, detecting anomalies, finding causes
> The originating definition of AIOps.

AFTER:

> Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination
> Gartner’s definition of AIOps.

### P20. 3.5 Where the discipline ends  [TABLE CELL]

BEFORE:

> Financial accountability for technology spending, through collaboration among engineering, finance, and business teams

AFTER:

> Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams

### P21. 3.5 Where the discipline ends  [TABLE CELL]

BEFORE:

> It was built around cloud billing. A practitioner told its own survey that no one could yet say whether AI provides value

AFTER:

> It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value

### P22. 3.5 Where the discipline ends  [BODY]

BEFORE:

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

AFTER:

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

### P23. 3.6 Five questions the discipline exists to answer  [BODY]

BEFORE:

> AI Operations Management exists to answer five questions that an organization cannot answer without the discipline. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

AFTER:

> AI Operations Management exists to answer five questions from an organization’s own records. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

### P24. 3.6 Five questions the discipline exists to answer  [BODY]

BEFORE:

> At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II establishes what is true, Part III builds the five functions, and Part IV turns them into an institution.

AFTER:

> At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II presents the certified claims the functions rest on, Part III builds the five functions, and Part IV turns them into an institution.

### P25. The trace procedure  [BODY]

BEFORE:

> Step 1. Locate the claim in the registry by its identifier and record its name exactly as the registry gives it.

AFTER:

> Step 1. Locate the claim in the registry by its identifier and record its name exactly as the registry gives it. A claim’s name is a label; only its statement says what the claim establishes.

### P26. The trace procedure  [BODY]

BEFORE:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team, and the theorem says nothing about it. Like the pilot in Section 3.3 that fails the first condition, the team falls outside the theorem’s coverage. The trace reveals a limit not stated in the theorem’s own wording.

AFTER:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team. The trace reveals a limit not stated in the theorem’s own wording.

### P27. Chapter summary  [BODY]

BEFORE:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. The registry supports each result so that readers who doubt a claim can trace its basis.

AFTER:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis.

### P28. Key terms  [BODY]

BEFORE:

> The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. LEM-021 states that any evaluation of return on AI requires such a boundary.

AFTER:

> The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. LEM-021 requires such a boundary whenever return on AI is evaluated. Setting one for each deployment before spending begins is this book’s practice.

### P29. A trace of LEM-020  [BODY]

BEFORE:

> Step 2. When the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

AFTER:

> Step 2. Scope: the relevant actor has reliable visibility and the authority to apply management mechanisms. Within that scope, when the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

### P30. A trace of LEM-020  [BODY]

BEFORE:

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. It adds a condition: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

AFTER:

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. Its scope adds a requirement: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

### P31. A trace with two steps left open  [BODY]

BEFORE:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that the cost is understated holds without it.

AFTER:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that treating access price as total cost creates underestimation risk holds without it.

### P32. A trace with two steps left open  [BODY]

BEFORE:

> Step 6. The falsifying case is a buyer whose adoption cost includes categories beyond the access price and who evaluates the return within a boundary covering cost and value. The buyer treats the access price as the total cost, yet the cost is not understated.

AFTER:

> Step 6. The falsifying case is a buyer whose adoption cost includes categories beyond the access price and who evaluates the return within a boundary covering cost and value. The buyer treats the access price as the total cost, yet doing so creates no risk of understating the cost within the evaluation boundary.

### P33. One announcement, three readings  [BODY]

BEFORE:

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

AFTER:

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

### P34. One announcement, three readings  [BODY]

BEFORE:

> First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each is metered.

AFTER:

> First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each would be metered.

### P35. One announcement, three readings  [BODY]

BEFORE:

> Third, apply each of the five Founding Questions to the announcement. For each question, state whether the public record provides an answer from the organization’s own records and what record would be needed to answer it.

AFTER:

> Third, apply each of the five Founding Questions to the announcement. For each question, state whether the announcement provides an answer from the organization’s own records and what record would be needed to answer it.

<<<<< END DOCUMENT 1 >>>>>

<<<<< BEGIN DOCUMENT 2: CHAPTER 3 AS IT NOW STANDS >>>>>

[PART LABEL] Part I · The Argument

[CHAPTER TITLE] A Science and Its Discipline

[SLOT] Opening case

[CASE TITLE] The discipline that changed its mission

[PROVENANCE] Dated: February 2026. Figures and the quotation checked against the Foundation’s report and announcement, October 2026.

[BODY] In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

[FOOTNOTE] The mission statement before and after the change.

[BODY] The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned the expansion of FinOps into AI spending. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

[FOOTNOTE] Survey size and the cloud spending its respondents manage.

[FOOTNOTE] Share of respondents managing AI spend, 2026 survey against 2024 survey.

[BODY] FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of the survey’s respondents were managing it.

[FOOTNOTE] Cloud consumption as variable and tracked after the fact.

[FOOTNOTE] The practice as the Foundation defines it.

[BODY] The report also carried one practitioner’s statement of what remained unknown. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

[FOOTNOTE] Practitioner quotation as reproduced in the report.

[BODY] The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization’s AI consumption.

[BODY] That work requires both a body of knowledge about what is true and a practice that turns that knowledge into action. A neighboring discipline cannot supply either on its behalf. Chapter 14 explains how FinOps and that practice divide the work. Until both exist, the practitioner’s question about whether AI is providing value remains unanswered.

[SECTION HEAD] 3.1 Why name a science

[BODY] Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, careful execution does not repair the decisions built on them.

[BODY] Claims like these can remain informal, held in experience, rules of thumb, or the slides of the last person to present. That knowledge is useful, but it has a cost: two managers can hold opposing beliefs about the same deployment without being able to identify where they disagree. One might treat Chapter 1’s Cursor licenses as a fixed software expense and the other as metered consumption. Without stating their claims, neither can identify the fact that would settle the disagreement, so the argument turns on confidence rather than evidence.

[BODY] Chapters 1 and 2 each ended with an explicit result rather than an opinion. Chapter 1 stated the conditions under which deployed AI is a resource the organization consumes. Chapter 2 stated the conditions under which a scaled deployment cannot be controlled without a governing apparatus. Each result appeared in a panel with an identifier that points to the larger body of claims supporting it.

[BODY] AI Business Economics is that body of knowledge. It is a science in a specific, limited sense: a set of claims about the business economics of consuming AI, each stating when it holds and expressed precisely enough to be checked. Here, science does not imply laboratory experiments or certainty. It means that every claim states when it applies, what it concludes, and which other claims it rests on.

[LABEL] Definition

[TERM] AI Business Economics

[BODY] The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

[BODY] The claims are kept in a registry, a structured record of every definition, assumption, and result in the science. Each result is linked to the claims that support it. A definition fixes what a term means, and an axiom states an assumption the science accepts without proof. A proposition states a single claim, accepted on the basis of the definitions, axioms, or earlier claims it names as support. A lemma combines propositions, and sometimes other lemmas, into an intermediate result. A theorem combines lemmas into a result with direct consequences for management.

[BODY] These links are the registry’s most important feature. Every higher claim names the lower claims it depends on, which in turn name their own supporting claims. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader with the registry can start at any certified theorem and follow its supporting claims down to definitions and axioms. Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier. Readers can therefore trace any certified theorem to the lemma level using the book alone. Below that level, they work from the propositions supplied in a chapter or exercise.

[BODY] For a manager, the graph resolves one practical concern: no conclusion rests on a circular chain of recorded support. A manager can therefore trace a doubt down to a smaller claim and examine it. Whether that smaller claim is true is a separate question the graph does not answer.

[BODY] The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status at each version; no one enters the status by hand. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

[FOOTNOTE] What the validator checks.

[BODY] The registry provides the book’s justification, while the manager’s learning needs determine its organization. Chapters follow the order in which a manager needs to learn, which differs from the order in which the science derives its results. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis. Organizing the chapters by proof would leave a manager reading definitions for many pages before reaching a recognizable decision.

[SECTION HEAD] 3.2 Tracing a result the reader already accepts

[BODY] Once a deployment reaches scale, economic control requires a governing apparatus; the diligence of the people running it is no longer enough. Chapter 2 ended with that result, which a reader who accepted its argument already believes. Tracing the result through the registry offers a clear way to learn how the registry works. The conclusion is familiar, so a reader can focus on how its supporting claims are arranged.

[BODY] The registry states that result as THM-004:

[LABEL] Theorem 2 · THM-004

[THEOREM STATEMENT] Scaled AI Deployment Requires Cost Governance for Economic Control

[THEOREM SCOPE] Within the defined deployment and measurement boundary, if:

[THEOREM ANTECEDENT] production scaling expands the usage surface of AI deployment;

[THEOREM ANTECEDENT] measurement enables visibility into measurable cost-bearing activity;

[THEOREM ANTECEDENT] visibility enables management mechanisms; and

[THEOREM ANTECEDENT] buyer total cost extends beyond access price;

[THEOREM CONSEQUENT] then scaled AI deployment requires cost governance for economic control.

[BODY] Each condition has a plain meaning a manager can check against a deployment. The first says the deployment has moved from a pilot into daily operations, multiplying the places where usage can occur. The second says that measuring usage makes the activity that costs money visible. The third says that monitoring, limits, attribution, or other management mechanisms can be applied to visible activity. The fourth says the organization’s total cost exceeds the price of access. When all four hold, an organization that wants economic control over the deployment needs cost governance.

[BODY] THM-004 names four certified lemmas as its support, one for each condition. LEM-016, “Production Scaling Expands Usage Surface,” supports the first. LEM-002, “Measurement Enables Visibility,” supports the second. LEM-020, “Visibility Enables Management Mechanisms,” supports the third. LEM-006, “Buyer Total Cost Extends Beyond Access Price,” supports the fourth.

[BODY] The registry also records the theorem’s proof, which combines the lemmas in two pairs. The first and fourth establish that economic exposure grows with the deployment and cannot be determined from the access price alone. The second and third establish the only route to managing that exposure: measurement makes it visible, allowing management mechanisms to be applied. Economic control therefore requires an apparatus for both measurement and management, which the theorem calls cost governance.

[BODY] This pairing explains Chapter 2’s statement that THM-004 formalizes the economic consequence of the third flow’s asymmetry. Costs accrue with use and grow with scale, as the first and fourth conditions describe. Control requires deliberate measurement and management, as the second and third conditions describe.

[BODY] Each lemma, in turn, rests on propositions. LEM-020 offers a useful example of how the registry is built. Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.” It rests on seven propositions and one other lemma.

[BODY] The propositions are small claims that appear nearly self-evident in isolation. PROP-043 states: “If activity is metered, records describing measured activity are generated or maintained.” PROP-053 states: “If economic exposure exists, monitoring mechanisms may be used to observe the sources or magnitude of that exposure.” PROP-085 states: “If usage information becomes visible, decisions regarding management, allocation, optimization, or monitoring may reference that information.” Their contribution becomes clearer when they are combined. PROP-043 establishes that metered activity leaves a record. PROP-085 allows management decisions to draw on visible usage, and PROP-053 establishes that monitoring can be used to observe economic exposure. None of the three alone says that controls can be applied to visible activity. LEM-020 reaches that conclusion by combining them with four further propositions and LEM-002, a combination the registry records as its proof.

[FOOTNOTE] LEM-020’s proof record and its supporting propositions.

[BODY] LEM-020 also rests on LEM-002, which directly supports THM-004’s second condition. Figure 3.1 shows the branch through LEM-020 and makes this shared support visible. The registry is a graph in which one claim can support several others, rather than a tree in which each claim has one parent.

[FIGURE CAPTION] Figure 3.1 One branch of the trace. THM-004 rests on four lemmas, one for each condition. LEM-020 rests in turn on LEM-002, which also supports the theorem directly, and on seven propositions, three of which are shown.

[BODY] Tracing the theorem changes how a manager can use it. Initially, THM-004 is a conclusion to accept or reject as a whole. The trace reveals a set of smaller claims that can be examined individually, allowing a manager to identify which supporting claim they doubt. A disagreement over an entire conclusion has no obvious way to end. A disagreement over a specific proposition concerns one stated claim, so the two sides can name the fact that would decide it.

[DATED] Dated: August 2026

[BODY] In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified, including 9 of the 11 theorems and 20 of the 21 lemmas. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

[FOOTNOTE] Object counts, links and certification at the pinned registry version.

[SECTION HEAD] 3.3 How to read a formal claim

[BODY] A manager who cites a formal claim for more than it establishes bases a decision on something the claim never stated. To avoid that error, read the claim in four parts: its conditions, its scope, its non-claims, and the falsifying case that would defeat it. A manager who can state all four can use the claim without being misled by it.

[BODY] The conditions are the “if” clauses, each of which is true or false for a given case. In THM-004, they are the four numbered clauses. If a deployment fails any one of them, the theorem says nothing about it. A pilot used by one team for a few weeks has not been scaled into daily operations, so it fails the first condition. The theorem neither requires governance for that pilot nor rules it out. Reading the conditions first prevents a basic misuse: applying a formal claim to a case it does not cover.

[BODY] The scope defines which cases the claim covers. As presented in this book, THM-004 states its scope before the word “if”: one defined deployment and its measurement boundary. The registry adds that the theorem applies when an organization seeks economic control over the resulting cost. The claim concerns one deployment within one boundary, rather than an organization’s AI activity in general. Before applying it across a company, a manager must show that each deployment meets the conditions.

[FOOTNOTE] THM-004’s scope condition.

[BODY] The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records the non-claims of every certified claim. The record is not exhaustive: the exclusion of Chapter 2’s three flows comes from this book, not from the registry. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

[FOOTNOTE] THM-004’s recorded exclusions.

[LABEL] Definition

[TERM] Non-claim

[BODY] A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating non-claims prevents a claim from being cited for more than it says.

[BODY] A costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

[FOOTNOTE] LEM-020’s recorded exclusions.

[BODY] The falsifying case describes what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition but lacks the conclusion. The second and third conditions describe what measurement and management would make possible, rather than an apparatus already in place. A deployment with no instruments installed can therefore meet all four conditions.

[BODY] For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

[BODY] These four parts answer an objection to the formal style: that the registry offers word games, dressing obvious points in numbered clauses. The common-sense version of THM-004 says that big deployments need cost controls, but gives no answer for the one-team pilot because it never defines “big.” The formal version does: the pilot fails the first condition, so the theorem is silent about it. The manager must first check whether the deployment has moved into daily operations. The common-sense version also allows readers to slide from “needs controls” to “controls deliver control,” a misreading the non-claims rule out. A formal statement fixes in advance what would count as the claim being wrong. Stating its conditions makes it possible to test and improve it.

[SECTION HEAD] 3.4 The discipline that acts on the science

[BODY] Knowledge alone does not change what an organization does. Medicine draws on physiology, but clinicians treat patients by applying that knowledge. Engineering draws on physics, but engineers build bridges using codes and procedures. In each case, a practice connects the knowledge to the result through its own methods, roles, and standards.

[BODY] AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management addresses it by managing AI as a resource the organization consumes wherever Chapter 1’s conditions hold.

[LABEL] Definition

[TERM] AI Operations Management

[BODY] The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

[BODY] The discipline has five functions that follow AI capacity through the organization: buying it, planning its use, recording and assigning consumption, routing it to work, and judging the value it returns. Each function is a capability an organization either has or lacks. Part III teaches all five, with metering and attribution covered in two chapters.

[BODY] The first function, sourcing, matches the AI capacity an organization buys to the requirements of its work. It determines which models and providers serve which work, and on what terms, so that the organization neither pays for capability it does not need nor deprives work of capability it requires. A company that sends every request to its most capable model, including requests a smaller model would answer just as well, is paying for capability its work does not use.

[BODY] The second function is planning and budgeting, whose absence proved costly in Chapter 2’s opening case. The organization must state how much AI it expects to consume in the coming period and detect when actual consumption departs from that expectation. A budget is a commitment made in advance that makes deviations visible as they happen, before the money is gone.

[BODY] The third function, metering and attribution, builds what Chapter 2 called the record flow. The organization must record what was consumed and assign each unit of consumption to the team, product, or purpose it served. Without that assignment, managers can see a cost but cannot trace it to the work that caused it.

[BODY] The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which. Allocation and routing make that choice deliberate by applying a rule.

[BODY] The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary.

[FOOTNOTE] LEM-021’s statement.

[BODY] Figure 3.2 shows the relationship between the two layers: the science provides the foundation for the discipline’s five functions.

[FIGURE CAPTION] Figure 3.2 The two layers. AI Business Economics states conditional claims about consuming AI and records what each one rests on. AI Operations Management acts on it through five functions, all taught in Part III.

[BODY] The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

[SECTION HEAD] 3.5 Where the discipline ends

[BODY] Chapter 1 set aside three related subjects: how models work, prompt engineering, and finding uses for AI. Each has its own purpose and literature, and each ends before AI Operations Management begins.

[BODY] The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins where a model is a service an organization can buy and call.

[BODY] The second is prompt engineering, the craft of writing inputs that produce better outputs. It improves individual uses of AI, while AI Operations Management governs their combined consumption, cost, and value. A better prompt can lower the cost of one request. Only the discipline can determine whether the organization’s requests, taken together, are worth what they cost.

[BODY] The third subject is finding uses for AI: deciding which business problems it might solve. That work belongs to strategy and innovation, and ends when a use is chosen. AI Operations Management begins with buying capacity for the chosen use and manages its consumption from then on.

[BODY] Four established disciplines sit closer to AI Operations Management. Each manages an aspect of work related to AI consumption, but each lacks something needed to govern its economics. Table 3.1 compares them.

[TABLE HEADING] Neighbor

[TABLE HEADING] What it is for

[TABLE HEADING] What it manages

[TABLE HEADING] What it lacks for this territory

[TABLE CELL] AIOps

[TABLE CELL] Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination

[FOOTNOTE] Gartner’s definition of AIOps.

[TABLE CELL] The health and performance of IT systems

[TABLE CELL] It uses AI to watch systems. It does not govern what consuming AI costs or returns

[TABLE CELL] MLOps

[TABLE CELL] Building, deploying, and monitoring machine learning models in production

[FOOTNOTE] Definition and scope of MLOps.

[TABLE CELL] The lifecycle of models an organization builds

[TABLE CELL] It ships models. It does not govern the consumption of capacity an organization buys

[TABLE CELL] FinOps

[TABLE CELL] Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams

[FOOTNOTE] The Foundation’s own definition of the practice.

[TABLE CELL] Cloud and wider technology spending

[TABLE CELL] It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value

[TABLE CELL] Regulatory AI governance

[TABLE CELL] Ensuring that uses of AI are lawful, safe, and accountable to regulators

[TABLE CELL] Risk and compliance

[TABLE CELL] It asks whether a use is permitted, not whether it is economically managed

[BODY] Table 3.1. The four neighboring disciplines. Each manages work related to AI consumption, but none was built to govern its economics.

[BODY] FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

[FOOTNOTE] The Foundation’s definition, which names business value.

[BODY] Regulatory governance determines whether an organization may use AI in a particular way. This book takes that determination as given and asks how the permitted use is managed.

[SECTION HEAD] 3.6 Five questions the discipline exists to answer

[BODY] AI Operations Management exists to answer five questions from an organization’s own records. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

[BODY] An organization that manages its AI consumption can answer five questions from its own records:

[BODY] Question 1. “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7.

[BODY] Question 2. “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10.

[BODY] Question 3. “Who consumed what last month, in service of which work?” This is the metering and attribution question, answered across Chapters 8 and 9.

[BODY] Question 4. “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11.

[BODY] Question 5. “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12.

[BODY] These are the Founding Questions, which an organization must answer “from its own records.” It can always produce an answer by asking the provider, estimating, or repeating the business case, but none of those methods produces knowledge the organization holds and can check.

[BODY] At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II presents the certified claims the functions rest on, Part III builds the five functions, and Part IV turns them into an institution.

[SLOT] Craft section

[CASE TITLE] The trace procedure

[BODY] The trace procedure helps a manager examine a formal claim before relying on it. It breaks a theorem into smaller supporting claims that can be checked individually, allowing the manager to assess more than the conclusion as a whole. The procedure has six steps.

[BODY] Step 1. Locate the claim in the registry by its identifier and record its name exactly as the registry gives it. A claim’s name is a label; only its statement says what the claim establishes.

[BODY] Step 2. State its scope, then restate each condition in ordinary business language. Retain every antecedent and add none.

[BODY] Step 3. List the claims it depends on by identifier and name.

[BODY] Step 4. Follow the dependencies one level down. Restate each in one sentence and note any condition it adds that the claim above did not state.

[BODY] Step 5. State what the claim establishes and, separately, what it does not establish.

[BODY] Step 6. Name the falsifying case: one that meets every condition but lacks the conclusion.

[BODY] Steps 2 and 6 do most of the work. Dropping an antecedent in step 2 produces a claim the registry does not make. Step 6 tests whether the reader has understood the claim: a reader who cannot describe the case that would defeat it cannot say what it rules out.

[BODY] Applied to THM-004, the procedure reveals a requirement of authority at step 4 that the theorem’s wording does not state. The following trace shows how.

[BODY] Step 1 records THM-004, “Scaled AI Deployment Requires Cost Governance for Economic Control.”

[BODY] Step 2 restates the conditions. Within one deployment and its measurement boundary, the theorem applies when four conditions hold: scaling expands where usage can occur; measurement makes the activity that costs money visible; management mechanisms can be applied to visible activity; and total cost exceeds the access price.

[BODY] Step 3 lists the four dependencies: LEM-016, LEM-002, LEM-020, and LEM-006, one for each condition. The registry marks all four as required. Some claims also have contextual dependencies, which bear on a claim without being conditions of it. Problem P2 provides an example. Step 3 records whether each dependency is required or contextual.

[BODY] Step 4 restates each dependency. LEM-016 says that moving from isolated use into repeated operations can increase the number of usage events and demand points. LEM-002 says that measured and recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. LEM-020 says that monitoring, limits, attribution, or other management mechanisms can be applied to visible usage or exposure. LEM-006 says that a buyer who incurs several kinds of cost pays more in total than the access price.

[BODY] Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team. The trace reveals a limit not stated in the theorem’s own wording.

[FOOTNOTE] LEM-020’s scope condition.

[BODY] Step 5 separates what the claim establishes from what a reader might infer. THM-004 establishes that cost governance is necessary for economic control of a scaled deployment. It does not establish that governance is sufficient or costless, specify the scale at which governance becomes necessary or the size of the exposure, or establish that a deployment has three flows.

[BODY] Step 6 names the falsifying case: a scaled deployment that meets all four conditions and whose organization controls its cost without a measurement and management apparatus. Finding such a case would show the theorem to be false.

[BODY] The procedure is deliberately slow. Tracing a theorem takes longer than reading it and agreeing with it, but the time is worth spending once for each claim on which a decision depends. The trace shows a manager exactly what supports the decision.

[SECTION HEAD] Chapter summary

[BODY] AI Business Economics is the science of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on. The claims are kept in a registry and linked by dependency. This book renders and cites only certified claims.

[BODY] The registry provides the book’s justification, while the manager’s learning needs determine its organization. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis.

[BODY] A trace follows a claim through the registry to its supporting lemmas and propositions. It breaks a conclusion into smaller claims that can be examined individually.

[BODY] A formal claim must be read in four parts: its conditions, its scope, its non-claims, and the falsifying case that would defeat it. Stating a claim formally fixes in advance what would count as being wrong.

[BODY] AI Operations Management applies the science through five functions: sourcing, planning and budgeting, metering and attribution, allocation and routing, and holding value to account at a boundary. It begins when a model becomes a service an organization consumes. It shares boundaries with AIOps, MLOps, FinOps, and regulatory governance, while remaining a distinct discipline.

[BODY] The Founding Questions are the five questions the discipline exists to answer from an organization’s own records. By the end of Part I, readers understand the questions but do not yet have a method for answering them.

[SECTION HEAD] Key terms

[KEY TERM] AI Business Economics

[BODY] The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

[KEY TERM] AI Operations Management

[BODY] The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

[KEY TERM] Registry

[BODY] The structured record of every definition, assumption, and result in AI Business Economics, with each result linked to the claims that support it.

[KEY TERM] Theorem

[BODY] A registry result that combines lemmas into a conclusion with direct consequences for management. The book presents each theorem it relies on in a numbered panel.

[KEY TERM] Lemma

[BODY] An intermediate registry result that combines propositions, and sometimes other lemmas, to support one or more theorems.

[KEY TERM] Proposition

[BODY] A single registry claim, accepted because of the definitions, axioms, or earlier claims it names as its support. Lemmas combine propositions.

[KEY TERM] Certified claim

[BODY] A registry claim that meets the validator’s fixed conditions and whose dependencies are all certified. The book renders and cites only certified claims.

[KEY TERM] Trace

[BODY] The process of following a registry claim through its supporting claims, from a theorem to its lemmas and from a lemma to its propositions.

[KEY TERM] Dependency

[BODY] A claim that another claim rests on. A required dependency is one without which the claim cannot hold. A contextual dependency bears on the claim without being one of its conditions.

[KEY TERM] Condition

[BODY] A requirement a deployment must meet for a formal claim to apply to it. A claim says nothing about a case that fails any of its conditions.

[KEY TERM] Scope

[BODY] The part of a formal claim that defines which cases it covers, such as one deployment within one boundary. A case outside that scope is not covered, regardless of whether it meets the conditions.

[KEY TERM] Non-claim

[BODY] A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating non-claims prevents a claim from being cited for more than it says.

[KEY TERM] Falsifying case

[BODY] A case that meets every condition of a formal claim but lacks its conclusion. Finding such a case would show the claim to be wrong.

[KEY TERM] Value boundary

[BODY] The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. LEM-021 requires such a boundary whenever return on AI is evaluated. Setting one for each deployment before spending begins is this book’s practice.

[KEY TERM] Founding Questions

[BODY] The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions.

[KEY TERM] Trace procedure

[BODY] The six-step method for examining a formal claim before relying on it: locate the claim; state its scope and restate its conditions; list its dependencies; follow them one level down; separate what the claim establishes from what it does not; and name the case that would defeat it.

[SECTION HEAD] Discussion questions and problems

[SLOT] Discussion questions

[BODY] The book states that the registry provides its justification but does not determine its organization. Describe what a reader would lose if the chapters followed the registry’s order of derivation.

[BODY] Of the four borders in Table 3.1, which is hardest to defend, and why? State what evidence would move that border.

[BODY] Restate one Founding Question in language your chief financial officer would use, preserving all its content. Then identify the part you were most tempted to omit.

[BODY] Chapter 2 diagnosed a deployment through its three flows. Match each flow to the functions in Section 3.4 that act on it, then explain which flow draws on the most functions and why.

[SLOT] Problems

[PROBLEM LABEL] P1 · Worked

[PROBLEM TITLE] A trace of LEM-020

[BODY] The craft section traced a theorem. Use the same six steps to trace one of its lemmas, LEM-020, as a model for Problem P2.

[BODY] Step 1. LEM-020, “Visibility Enables Management Mechanisms.” Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.”

[BODY] Step 2. Scope: the relevant actor has reliable visibility and the authority to apply management mechanisms. Within that scope, when the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

[BODY] Step 3. Eight dependencies, all required: the lemma LEM-002 and seven propositions, PROP-032, PROP-039, PROP-041, PROP-042, PROP-043, PROP-053, and PROP-085.

[BODY] Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. Its scope adds a requirement: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

[FOOTNOTE] LEM-002’s scope condition.

[BODY] Step 5. LEM-020 establishes that visibility makes management mechanisms available. It does not establish that the mechanisms work automatically or that visibility alone determines the right policy or price.

[FOOTNOTE] LEM-020’s recorded exclusions.

[BODY] Step 6. The falsifying case is an organization that can see a deployment’s usage and has authority to manage it, but still cannot apply any monitoring, limit, or attribution to it.

[PROBLEM LABEL] P2 · Completion

[PROBLEM TITLE] A trace with two steps left open

[BODY] THM-002, “AI Adoption Cost Is Underestimated When Access Price Is Treated as Total Cost,” states a result taught in Part II. Its statement reads: “If buyer AI adoption cost includes cost categories beyond access price, and ROI evaluation requires a defined measurement boundary for cost and value, then treating access price as total adoption cost creates underestimation risk within the evaluation boundary.” Steps 1, 2, 3, and 6 are worked below. Complete steps 4 and 5.

[BODY] Step 1. THM-002, as named above.

[BODY] Step 2. When a buyer’s cost of adopting AI includes more than the access price, and evaluating the return requires a boundary that includes both cost and value, treating the access price as the whole cost risks understating it.

[BODY] Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that treating access price as total cost creates underestimation risk holds without it.

[FOOTNOTE] THM-002’s dependencies and their recorded roles.

[BODY] Step 4. Restate each dependency in one sentence and note any condition it adds.

[BODY] Step 5. State what THM-002 establishes and what it does not. Then use the treatment of LEM-020 in step 3 as a model to explain what LEM-002 contributes, given that the theorem does not depend on it as a condition.

[BODY] Step 6. The falsifying case is a buyer whose adoption cost includes categories beyond the access price and who evaluates the return within a boundary covering cost and value. The buyer treats the access price as the total cost, yet doing so creates no risk of understating the cost within the evaluation boundary.

[PROBLEM LABEL] P3 · Independent

[PROBLEM TITLE] A reply to the word-games objection

[BODY] A senior colleague reads THM-004 and says: “This is common sense in numbered clauses. Anyone who has run a large deployment knows you need controls. Formalizing it adds nothing.” Write a one-page reply using the four parts of a formal claim from Section 3.3. Identify at least one thing the formal statement lets the colleague do that the common-sense version does not. Do not argue that the colleague’s conclusion is wrong.

[PROBLEM NOTE] Interleaving: question 4 requires Chapter 2’s three flows, and the cumulative case below requires both earlier chapters.

[SLOT] Part I cumulative case

[PROBLEM LABEL] Cumulative case · Part I

[PROBLEM TITLE] One announcement, three readings

[PROVENANCE] Dated: February 2024. The company’s own announcement, using its own figures. Only that announcement is used here.

[BODY] In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

[FOOTNOTE] All figures in this case are the company’s own, as announced.

[BODY] Work from this announcement alone.

[BODY] First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each would be metered.

[BODY] Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and cost-and-value flows, identifying the evidence behind each diagnosis.

[BODY] Third, apply each of the five Founding Questions to the announcement. For each question, state whether the announcement provides an answer from the organization’s own records and what record would be needed to answer it.

[BODY] Keep your answers. The case returns in Chapter 6.

<<<<< END DOCUMENT 2 >>>>>

<<<<< BEGIN DOCUMENT 3: REFERENCE EXTRACT >>>>>

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

<<<<< END DOCUMENT 3 >>>>>

END OF PACKAGE. Now produce your review in the format given in Part 2.
