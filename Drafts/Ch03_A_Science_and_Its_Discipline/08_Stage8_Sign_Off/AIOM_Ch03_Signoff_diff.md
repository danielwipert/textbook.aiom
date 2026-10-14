# Chapter 3 sign-off (Sitting 4): what changed since your author pass

Two files: this diff, and `AIOM_Ch03_Signoff_render.pdf`, the final 27-page
render (all fifteen print gates and all seventeen web gates pass).

Your author pass closed at commit b56819c. Since then, 45 passages
changed, every one by a ruling you made at a gate. They are listed below in
three groups, by the step that made them, each passage BEFORE and AFTER.
Layout-only changes (a definition box moved, Figure 3.2 moved and moved back,
two CSS rules) change no words and are not listed; they are in the checklist.

What you decide: approve the chapter as a whole, or name ONE structural
reason, and the chapter returns to the step that owns it. The full read
already happened in your author pass, so this is a check of the changes and
the render, not a second read.

## 1. Sitting 3, fact check: 34 change(s)

Rulings recorded in: checklist S3 lines; 04_Stage3_Fact_Check/AIOM_Ch03_Sitting3_rulings.md.

**1.1  The discipline that changed its mission**  (body, provenance)

Before:

> Dated: February 2026. Found by search. Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself. See the source register.
> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as advancing the people who manage cloud value. The new statement replaced one word: the Foundation now advances the people who manage technology value.

After:

> Dated: February 2026. Figures and the quotation checked against the Foundation’s report and announcement, October 2026.
> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

**1.2  The discipline that changed its mission**  (body)

Before:

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned work the discipline had not originally been created to do. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

After:

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned the expansion of FinOps into AI spending. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

**1.3  The discipline that changed its mission**  (body, footnote)

Before:

> Share of practitioners managing AI spend, 2026 against 2024.
> FinOps was built to address a specific problem: cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of them were managing it.

After:

> Share of respondents managing AI spend, 2026 survey against 2024 survey.
> FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of the survey’s respondents were managing it.
> Cloud consumption as variable and tracked after the fact.

**1.4  The discipline that changed its mission**  (body)

Before:

> The report also recorded what practitioners had yet to establish. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

After:

> The report also carried one practitioner’s statement of what remained unknown. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

**1.5  The discipline that changed its mission**  (body)

Before:

> The survey reveals the gap Chapters 1 and 2 described, as reported by the people asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. Cloud cost management is a capable neighboring discipline that has expanded into work no discipline was designed to govern: the economics of an organization’s AI consumption.

After:

> The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization’s AI consumption.

**1.6  3.1 Why name a science**  (body)

Before:

> Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, management based on them fails, however carefully managers carry it out.

After:

> Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, careful execution does not repair the decisions built on them.

**1.7  3.1 Why name a science**  (body)

Before:

> These links are the registry’s most important feature. Every higher claim names the lower claims it depends on, which in turn name their own supporting claims. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader with the registry can start at any theorem and follow its supporting claims down to definitions and axioms. Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier. Readers can therefore trace any claim to the lemma level using the book alone. Below that level, they work from the propositions supplied in a chapter or exercise.
> For a manager, the graph resolves one practical concern: no conclusion rests on circular reasoning. A manager can therefore trace a doubt down to a smaller claim and examine it. Whether that smaller claim is true is a separate question the graph does not answer.
> The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status from the graph at each version; no one enters it manually. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

After:

> These links are the registry’s most important feature. Every higher claim names the lower claims it depends on, which in turn name their own supporting claims. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader with the registry can start at any certified theorem and follow its supporting claims down to definitions and axioms. Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier. Readers can therefore trace any certified theorem to the lemma level using the book alone. Below that level, they work from the propositions supplied in a chapter or exercise.
> For a manager, the graph resolves one practical concern: no conclusion rests on a circular chain of recorded support. A manager can therefore trace a doubt down to a smaller claim and examine it. Whether that smaller claim is true is a separate question the graph does not answer.
> The registry also records which claims are complete. A claim is certified when every claim it depends on is certified and its supporting argument meets the registry’s fixed conditions. The registry’s validator computes that status at each version; no one enters the status by hand. The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim’s current wording. It checks the structure and record of an argument, not its truth. A claim with a gap in its supporting claims carries a record of what is missing. This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes.

**1.8  3.1 Why name a science**  (body)

Before:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. Chapters follow the order in which a manager needs to learn, which differs from the order in which the science derives its results. The registry supports each result the book teaches so that a reader who doubts a claim can trace its basis. Organizing the chapters by proof would leave a manager reading definitions for many pages before reaching a recognizable decision.

After:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. Chapters follow the order in which a manager needs to learn, which differs from the order in which the science derives its results. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis. Organizing the chapters by proof would leave a manager reading definitions for many pages before reaching a recognizable decision.

**1.9  3.2 Tracing a result the reader already accepts**  (body)

Before:

> Tracing the theorem changes how a manager can use it. Initially, THM-004 is a conclusion to accept or reject as a whole. The trace reveals a set of smaller claims that can be examined individually, allowing a manager to identify which supporting claim they doubt. A disagreement over an entire conclusion has no obvious way to end. A disagreement over a specific proposition can be settled.

After:

> Tracing the theorem changes how a manager can use it. Initially, THM-004 is a conclusion to accept or reject as a whole. The trace reveals a set of smaller claims that can be examined individually, allowing a manager to identify which supporting claim they doubt. A disagreement over an entire conclusion has no obvious way to end. A disagreement over a specific proposition concerns one stated claim, so the two sides can name the fact that would decide it.

**1.10  3.2 Tracing a result the reader already accepts**  (body)

Before:

> In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

After:

> In the version used to write this book, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records identifying evidence the science still needs. It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified, including 9 of the 11 theorems and 20 of the 21 lemmas. The registry changes as the science develops, so these figures describe a single version rather than the science itself.

**1.11  3.3 How to read a formal claim**  (body)

Before:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records every claim’s non-claims. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

After:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records the non-claims of every certified claim. The record is not exhaustive: the exclusion of Chapter 2’s three flows comes from this book, not from the registry. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

**1.12  3.3 How to read a formal claim**  (body)

Before:

> The most costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

After:

> A costly misreading confuses necessary with sufficient. A manager who interprets THM-004 as “governance produces control” might buy a dashboard and expect costs to come under control. The theorem promises no such result; it states only that control requires governance. LEM-020 makes the same limit explicit one level down: it does not establish that management mechanisms are automatically effective.

**1.13  3.3 How to read a formal claim**  (body)

Before:

> The falsifying case describes what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition but lacks the conclusion. The second and third conditions describe what measurement and management would make possible, rather than an apparatus already in place. A deployment with no instruments installed can therefore meet all four conditions. For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not provide such a case. If the fee covers every cost, the fourth condition fails. If it does not, the organization would have to control the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

After:

> The falsifying case describes what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition but lacks the conclusion. The second and third conditions describe what measurement and management would make possible, rather than an apparatus already in place. A deployment with no instruments installed can therefore meet all four conditions.
> For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

**1.14  3.4 The discipline that acts on the science**  (body)

Before:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. The organization buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management resolves it by managing AI as a resource the organization consumes rather than as software it has bought.

After:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management addresses it by managing AI as a resource the organization consumes wherever Chapter 1’s conditions hold.

**1.15  3.4 The discipline that acts on the science**  (body)

Before:

> The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. If two workflows share a provider account with a fixed rate limit, one waits whenever the other is busy. Allocation and routing make that choice deliberate by applying a rule.
> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” The organization must set that boundary for each deployment and name the person responsible for knowing the answer. This book calls it the value boundary.

After:

> The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which. Allocation and routing make that choice deliberate by applying a rule.
> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary.

**1.16  3.4 The discipline that acts on the science**  (body, figure caption)

Before:

> Figure 3.2 The two layers. AI Business Economics states what is true about consuming AI. AI Operations Management acts on it through five functions, all taught in Part III.
> The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because a practice built on incorrect claims fails however well it is run.

After:

> Figure 3.2 The two layers. AI Business Economics states conditional claims about consuming AI and records what each one rests on. AI Operations Management acts on it through five functions, all taught in Part III.
> The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

**1.17  3.5 Where the discipline ends**  (body)

Before:

> The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins with that call, when each use consumes resources and costs money.

After:

> The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins where a model is a service an organization can buy and call.

**1.18  3.5 Where the discipline ends**  (footnote, table cell)

Before:

> Applying machine learning to run IT operations: correlating events, detecting anomalies, finding causes
> The originating definition of AIOps.

After:

> Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination
> Gartner’s definition of AIOps.

**1.19  3.5 Where the discipline ends**  (table cell)

Before:

> Financial accountability for technology spending, through collaboration among engineering, finance, and business teams

After:

> Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams

**1.20  3.5 Where the discipline ends**  (table cell)

Before:

> It was built around cloud billing. A practitioner told its own survey that no one could yet say whether AI provides value

After:

> It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value

**1.21  3.5 Where the discipline ends**  (body)

Before:

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

After:

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

**1.22  3.6 Five questions the discipline exists to answer**  (body)

Before:

> AI Operations Management exists to answer five questions that an organization cannot answer without the discipline. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

After:

> AI Operations Management exists to answer five questions from an organization’s own records. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

**1.23  3.6 Five questions the discipline exists to answer**  (body)

Before:

> At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II establishes what is true, Part III builds the five functions, and Part IV turns them into an institution.

After:

> At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II presents the certified claims the functions rest on, Part III builds the five functions, and Part IV turns them into an institution.

**1.24  The trace procedure**  (body)

Before:

> Step 1. Locate the claim in the registry by its identifier and record its name exactly as the registry gives it.

After:

> Step 1. Locate the claim in the registry by its identifier and record its name exactly as the registry gives it. A claim’s name is a label; only its statement says what the claim establishes.

**1.25  The trace procedure**  (body)

Before:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team, and the theorem says nothing about it. Like the pilot in Section 3.3 that fails the first condition, the team falls outside the theorem’s coverage. The trace reveals a limit not stated in the theorem’s own wording.

After:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team. The trace reveals a limit not stated in the theorem’s own wording.

**1.26  Chapter summary**  (body)

Before:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. The registry supports each result so that readers who doubt a claim can trace its basis.

After:

> The registry provides the book’s justification, while the manager’s learning needs determine its organization. The registry supports each formal result the book presents, so that a reader who doubts one can trace its basis.

**1.27  Key terms**  (body)

Before:

> The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. LEM-021 states that any evaluation of return on AI requires such a boundary.

After:

> The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. LEM-021 requires such a boundary whenever return on AI is evaluated. Setting one for each deployment before spending begins is this book’s practice.

**1.28  A trace of LEM-020**  (body)

Before:

> Step 2. When the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

After:

> Step 2. Scope: the relevant actor has reliable visibility and the authority to apply management mechanisms. Within that scope, when the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

**1.29  A trace of LEM-020**  (body)

Before:

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. It adds a condition: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

After:

> Step 4. LEM-002 says that recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. Its scope adds a requirement: the record must be detailed enough for the relevant person to observe the activity. PROP-032 says compute use can be measured. PROP-039 says measured compute use can inform methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be distinguished by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says monitoring can be used to observe economic exposure, adding the condition that exposure exists. PROP-085 says management decisions can draw on visible usage. Together, these claims explain how visibility makes management possible.

**1.30  A trace with two steps left open**  (body)

Before:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that the cost is understated holds without it.

After:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that treating access price as total cost creates underestimation risk holds without it.

**1.31  A trace with two steps left open**  (body)

Before:

> Step 6. The falsifying case is a buyer whose adoption cost includes categories beyond the access price and who evaluates the return within a boundary covering cost and value. The buyer treats the access price as the total cost, yet the cost is not understated.

After:

> Step 6. The falsifying case is a buyer whose adoption cost includes categories beyond the access price and who evaluates the return within a boundary covering cost and value. The buyer treats the access price as the total cost, yet doing so creates no risk of understating the cost within the evaluation boundary.

**1.32  One announcement, three readings**  (body)

Before:

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

After:

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

**1.33  One announcement, three readings**  (body)

Before:

> First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each is metered.

After:

> First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each would be metered.

**1.34  One announcement, three readings**  (body)

Before:

> Third, apply each of the five Founding Questions to the announcement. For each question, state whether the public record provides an answer from the organization’s own records and what record would be needed to answer it.

After:

> Third, apply each of the five Founding Questions to the announcement. For each question, state whether the announcement provides an answer from the organization’s own records and what record would be needed to answer it.


## 2. Scoped re-review: 9 change(s)

Rulings recorded in: checklist SR lines; 02_Stage4_Review/AIOM_Ch03_Scoped_review_rulings.md.

**2.1  The discipline that changed its mission**  (body)

Before:

> The report also carried one practitioner’s statement of what remained unknown. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.”

After:

> Asked whether AI was providing value, one practitioner stated what remained unknown. The report chose to quote the answer: “No one can answer that question yet.”

**2.2  3.3 How to read a formal claim**  (body)

Before:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. Nor does it establish Chapter 2’s three flows, which belong to this book’s framework. The registry records the non-claims of every certified claim. The record is not exhaustive: the exclusion of Chapter 2’s three flows comes from this book, not from the registry. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

After:

> The non-claims identify conclusions the claim deliberately does not establish. THM-004 states that governance is necessary for control, but does not establish that governance delivers control or is costless. It does not specify the scale at which governance becomes necessary or the size of the economic exposure. The registry records non-claims for every certified claim, but its lists are not exhaustive. THM-004 also does not establish Chapter 2’s three flows; that exclusion comes from this book’s framework, rather than the registry. A reader with only the statement can identify most of them by asking whether it establishes that a requirement is necessary or sufficient, whether it specifies an amount, and whether it accounts for cost.

**2.3  3.3 How to read a formal claim**  (body)

Before:

> For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

After:

> For THM-004, the falsifying case would be a scaled deployment that meets all four conditions and whose organization controls its cost without any measurement and management apparatus. A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, a deployment under that contract is a falsifying case only if it meets all four conditions and the organization controls the costs beyond the fee without measuring them. A claim that identifies no possible falsifying case cannot be shown to be wrong and tells a manager nothing.

**2.4  3.4 The discipline that acts on the science**  (body)

Before:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. AI Operations Management addresses it by managing AI as a resource the organization consumes wherever Chapter 1’s conditions hold.

After:

> AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. Wherever that chapter’s conditions hold, AI Operations Management addresses the error by managing AI as a resource the organization consumes.

**2.5  3.4 The discipline that acts on the science**  (body)

Before:

> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary.

After:

> The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the requirement: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary.

**2.6  3.4 The discipline that acts on the science**  (body)

Before:

> The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus it describes, so the science depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

After:

> A result about governance changes nothing until an organization builds the apparatus it describes. The science therefore depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

**2.7  3.6 Five questions the discipline exists to answer**  (body)

Before:

> AI Operations Management exists to answer five questions from an organization’s own records. Each corresponds to one of its five functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

After:

> Each of the five questions corresponds to one of the discipline’s functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

**2.8  The trace procedure**  (body)

Before:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team. The trace reveals a limit not stated in the theorem’s own wording.

After:

> Step 4 also examines what each dependency adds. LEM-020’s scope requires reliable visibility and the authority to apply management mechanisms. That requirement belongs to the scope, rather than the third condition. A team that can see its costs but lacks authority to cap them falls outside LEM-020’s scope. The support for THM-004’s third condition therefore does not extend to that team. The trace reveals where the lemma’s support stops, a limit not stated in the theorem’s own wording.

**2.9  A trace with two steps left open**  (body)

Before:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 illustrates the role of a contextual dependency: it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that treating access price as total cost creates underestimation risk holds without it.

After:

> Step 3. The theorem has four dependencies. LEM-006 and LEM-021 are required, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,” reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined boundary for relevant costs, value, time period, and observed or expected outcomes.” LEM-020 concerns what a buyer can do about an understated cost once that cost is visible. It is contextual: the claim that treating access price as total cost creates underestimation risk holds without it.


## 3. Production (Stage 5, G2, G3): 2 change(s)

Rulings recorded in: checklist P, G2 and G3 lines.

Also 1 passage(s) moved with no words changed (a paragraph swapped order with a definition box).

**3.1  The discipline that changed its mission**  (footnote)

Before:

> The practice as the Foundation defines it.

After:

> The Foundation’s definition.

**3.2  3.2 Tracing a result the reader already accepts**  (body)

Before:

> Once a deployment reaches scale, economic control requires a governing apparatus; the diligence of the people running it is no longer enough. Chapter 2 ended with that result, which a reader who accepted its argument already believes. Tracing the result through the registry offers a clear way to learn how the registry works. The conclusion is familiar, so a reader can focus on how its supporting claims are arranged.

After:

> Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough. Chapter 2 ended with that result, which a reader who accepted its argument already believes. Tracing the result through the registry offers a clear way to learn how the registry works. The conclusion is familiar, so a reader can focus on how its supporting claims are arranged.
