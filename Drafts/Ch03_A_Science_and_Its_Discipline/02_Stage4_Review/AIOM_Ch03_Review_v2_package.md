# Review package: Chapter 3, "A Science and Its Discipline" (redesigned)

This is ONE self-contained file. Everything you need is inside it: your
instructions, the required output format, and all the material to review. Do not
ask for other files. Read the whole file before you begin.

---

## PART 1. Your task

You are reviewing one chapter of an academic textbook for business graduate
students, titled *AI Operations Management*. Chapter 3 is under review. It closes
Part I of the book. It has just been redesigned: an earlier version taught readers
to read formal claims from the book's underlying registry; this version keeps that
registry behind the scenes and teaches the discipline itself, its five functions
and its borders.

This file contains three documents, each between clear BEGIN and END markers in
Part 3 below:

- **Document 1: Chapter 3, the text under review.**
- **Document 2: the reference extract.** What the chapter is meant to do (its
  structure entry, its competency and assessment, its approved plan with the
  author's rulings) and the book's seven craft criteria, C1 to C7.
- **Document 3: Chapter 1 of the same book**, locked and published. It is the
  exemplar the craft standard was measured from. Calibrate against Chapter 1,
  not against how closely Chapter 3 resembles itself.

### Four warnings

1. **Sourcing is out of bounds.** Whether any figure or fact is true is checked
   separately, later, against the sources. You may still flag a sentence that
   makes an empirical claim with no visible support.
2. **Some wording is fixed elsewhere.** The one-sentence reading of THM-004 in
   Section 3.1 ("Once a deployment reaches scale ...") repeats Chapter 2's
   locked wording word for word. The opening case, Section 3.3, Section 3.4 and
   the Part I cumulative case were kept from the earlier version, which was
   fact-checked. You may judge all of them; say so if one no longer fits the
   redesigned chapter around it.
3. **Dated boxes are deliberate.** Perishable reporting (company names, dates,
   figures) is kept in dated boxes so that the body prose stays timeless. Judge
   whether each box earns its place, not whether the body should carry its facts.
4. **"No findings" is not an answer.** A review that says the chapter meets the
   criteria with no findings will be discarded as confirmatory.

The chapter is about 5,600 words, below the book's usual 6,000 to 7,500. The
author accepted that deliberately rather than pad it. If you find a real teaching
gap, say where; do not recommend length for its own sake.

### How to review

Review in three separate sections. In every section, do not report whether
something is met. Quote the WEAKEST evidence, say precisely what is wrong, and
say whether it is a defect, a deliberate choice serving something else, or noise.

**Section A, structure.** Does every slot serve the chapter's stated purpose?
Is competency C4 DELIVERED, meaning a reader could perform assessment 4 after
this chapter, unaided, on a real deployment the book has not worked? Does each
dated box show its function, or only sit beside it? Does the chapter front-run
anything a later chapter is meant to reveal? Does anything in the plan go
missing, and does anything appear that the plan does not call for? Now that the
registry is behind the scenes, does Section 3.1 still give the science enough
weight that the two-layer claim is believable?

**Section B, teaching.** Where would a sceptical, busy MBA-level reader stall,
lose the thread, or stop believing the argument? Judge clarity, pacing,
cognitive load, example fitness, and transitions. Name the single paragraph you
would cut first and the single place most in need of a concrete example.

**Section C, voice and craft.** One finding per criterion, C1 to C7, quoting the
weakest passage by section and the strongest, so your calibration is visible.

---

## PART 2. Required output format

Reply in Markdown, using exactly this structure and nothing else. No preamble.

```
# Second-model review: Chapter 3 (redesigned)

## Section A: Structure
## Section B: Teaching
## Section C: Voice and craft

## Findings

| ID | Sec | Where (section heading) | Quote (exact, under 30 words) | What is wrong | Type | Severity | Suggested fix |
|---|---|---|---|---|---|---|---|
| S-1 | A | ... | "..." | ... | defect | high | ... |

## Fix first
1. S-n: one line on why
2. S-n: ...
3. S-n: ...
```

Rules for the table:

- **ID**: S-1, S-2, and so on, numbered across all three sections.
- **Sec**: A, B or C. For Section C, start the "What is wrong" cell with the
  criterion (C1 to C7). Give every criterion at least one row.
- **Quote**: copied exactly from Document 1, so the author can find it.
- **Type**: one of `defect`, `deliberate`, `noise`.
- **Severity**: one of `high`, `medium`, `low`.
- Under each Section heading, write at most five sentences of overall judgment.
  The findings themselves go only in the table.
- Do not use em dashes or en dashes anywhere in your reply.

---

## PART 3. The material

<<<<< BEGIN DOCUMENT 1: CHAPTER 3, UNDER REVIEW >>>>>

Part I · The Argument

# A Science and Its Discipline

## [OPENING CASE]

## The discipline that changed its mission

*Dated: February 2026. Figures and the quotation checked against the Foundation’s report and announcement, October 2026.*

In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned the expansion of FinOps into AI spending. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of the survey’s respondents were managing it.

Asked whether AI was providing value, one practitioner stated what remained unknown. The report chose to quote the answer: “No one can answer that question yet.”

The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization’s AI consumption.

That work requires both a body of knowledge about what is true and a practice that turns that knowledge into action. A neighboring discipline cannot supply either on its behalf. Chapter 14 explains how FinOps and that practice divide the work. Until both exist, the practitioner’s question about whether AI is providing value remains unanswered.

### 3.1 The science and the practice

Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, careful execution does not repair the decisions built on them.

Claims like these can remain informal, held in experience, rules of thumb, or the slides of the last person to present. That knowledge is useful, but it has a cost: two managers can hold opposing beliefs about the same deployment without being able to identify where they disagree. One might treat Chapter 1’s Cursor licenses as a fixed software expense and the other as metered consumption. Without stating their claims, neither can identify the fact that would settle the disagreement, so the argument turns on confidence rather than evidence.

Chapters 1 and 2 each ended with an explicit result rather than an opinion. Chapter 1 stated the conditions under which deployed AI is a resource the organization consumes. Chapter 2 stated the conditions under which a scaled deployment cannot be controlled without a governing apparatus.

AI Business Economics is that body of knowledge. It is a science in a specific, limited sense: a set of claims about the business economics of consuming AI, each stating when it holds and expressed precisely enough to be checked. Here, science does not imply laboratory experiments or certainty. It means that every claim states when it applies, what it concludes, and which other claims it rests on.

> **DEFINITION CALLOUT · AI Business Economics**
>
> The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

A stated condition is what makes such a claim useful to a manager. Chapter 1’s result does not say that every use of AI is consumption. It says when deployed AI behaves as a resource the organization consumes, so a manager can check whether a given deployment meets those conditions before relying on the result. A claim that states when it applies can also be shown not to apply. That is what lets two managers who disagree find the fact that would settle the question.

The book shows the results of this science in numbered panels, as Chapters 1 and 2 did. Each panel states a result in its exact form and carries an identifier. A reading in plain business language follows each panel, and the reading is enough to use the result. The identifier lets a reader who doubts a result find its full statement and its supporting claims in Appendix A. A manager needs nothing more than the panel and its reading.

Chapter 2’s panel, THM-004, shows what such a result settles and what it leaves open. It formalizes the economic consequence of the third flow’s asymmetry. Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough. The theorem does not establish the three flows themselves. They are this book’s way of looking at a deployment, and the theorem’s conditions do not mention them.

### 3.2 The five functions

Knowledge alone does not change what an organization does. Medicine draws on physiology, but clinicians treat patients by applying that knowledge. Engineering draws on physics, but engineers build bridges using codes and procedures. In each case, a practice connects the knowledge to the result through its own methods, roles, and standards.

> **DEFINITION CALLOUT · AI Operations Management**
>
> The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

AI Operations Management is the practice of managing an organization’s AI consumption from week to week. An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns. Chapter 1 described the problem as a category error. Wherever that chapter’s conditions hold, AI Operations Management addresses the error by managing AI as a resource the organization consumes.

The discipline has five functions that follow AI capacity through the organization: buying it, planning its use, recording and assigning consumption, routing it to work, and judging the value it returns. Each function is a capability an organization either has or lacks. Part III teaches all five, with metering and attribution covered in two chapters.

The first function, sourcing, matches the AI capacity an organization buys to the requirements of its work. It determines which models and providers serve which work, and on what terms, so that the organization neither pays for capability it does not need nor deprives work of capability it requires. A company that sends every request to its most capable model, including requests a smaller model would answer just as well, is paying for capability its work does not use.

Sourcing decides more than the provider. A requirement can be accuracy, speed, cost per request, or how easily a model connects to the systems that feed it, and different pieces of work weigh these differently. Customer messages may need a fast, inexpensive model, while a contract review may need the most capable one available. An organization that buys one model for all of its work has still made a sourcing decision, whether or not anyone made it deliberately.

> **DATED EVIDENCE BOX · Dated: October 2025**
>
> In October 2025, Airbnb’s chief executive, Brian Chesky, said the company’s customer-service agent was built on 13 models, from OpenAI, Google, Alibaba, and open-source providers. He said the company relied heavily on Alibaba’s Qwen models, which he called “very good” and “also fast and cheap.” He also said OpenAI’s tools for connecting its models to Airbnb’s systems were not yet ready for the company’s needs.

The second function is planning and budgeting, whose absence proved costly in Chapter 2’s opening case. The organization must state how much AI it expects to consume in the coming period and detect when actual consumption departs from that expectation. A budget is a commitment made in advance that makes deviations visible as they happen, before the money is gone.

A budget for AI differs from a budget for licenses because the quantity is not fixed when the budget is set. The plan must therefore state the drivers it assumes, such as how many people or workflows will use the system and how heavily. A change in spending can then be traced to a change in a driver, while there is still time to act on it.

> **DATED EVIDENCE BOX · Dated: October 2026**
>
> Pigment, a company that sells financial planning software, surveyed about 2,000 finance leaders in the United States, the United Kingdom, France, and Germany for a report released in October 2026. Eighty-three percent said consumption-based pricing had pushed their AI spending above expectations. Thirteen percent said they had stayed within budget, and the average overrun was about 27 percent. The figures describe the survey’s respondents, reported by a vendor of planning software.

The third function, metering and attribution, builds what Chapter 2 called the record flow. The organization must record what was consumed and assign each unit of consumption to the team, product, or purpose it served. Without that assignment, managers can see a cost but cannot trace it to the work that caused it.

The record has two parts. Metering counts what was consumed, request by request. Attribution assigns each count to the work that caused it. A provider’s invoice supplies the first part in total. Only the organization can supply the second, because only the organization knows which team, product, or customer a request served.

> **DATED EVIDENCE BOX · Dated: February 2026**
>
> DoiT, a company that sells cloud cost-management services, commissioned a survey of 500 finance leaders at organizations in the United States and the United Kingdom with 1,000 or more employees. Sapio Research conducted it in February 2026. Seventy-nine percent reported AI-related cost overruns in the previous twelve months. Asked who was accountable for AI spending, 55 percent named technology leadership and 53 percent named finance, so at least 8 percent named both.

The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which. Allocation and routing make that choice deliberate by applying a rule.

Routing and allocation are two sides of one decision. Routing sends each piece of work to suitable capacity, such as a smaller model for routine requests and a larger one for difficult cases. Allocation decides who goes first when capacity is not enough for everyone. Both need a stated rule, because a stated rule can be checked against its results and changed.

> **DATED EVIDENCE BOX · Dated: July 2026**
>
> In July 2026, Bloomberg reported that Microsoft had begun sending some prompts from Copilot in Excel and Outlook to its own MAI models instead of models from OpenAI and Anthropic, citing the cost of the outside models. Reports put the volume at tens of thousands of prompts a week. Routine tasks moved to the in-house models, while complex reasoning tasks could still go to the outside models. The company’s head of AI, Mustafa Suleyman, said its goal was to reduce and ultimately eliminate what it paid Anthropic.

The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. That requires a boundary: the costs and value the evaluation counts, the period it covers, and the outcomes it measures against. The organization sets the boundary for each deployment before spending begins and names one person responsible for knowing the answer. This book calls it the value boundary.

The boundary matters because the choice of what to count changes the return. An evaluation that counts the assistant’s subscription but not the staff time spent checking its answers reports a higher return than one that counts both. So does an evaluation that measures the busiest month instead of the whole quarter. Setting the boundary in advance prevents the evaluation from choosing the version it prefers.

> **DATED EVIDENCE BOX · Dated: October 2025, with a later update**
>
> In October 2025, JPMorgan Chase’s chief executive, Jamie Dimon, told Bloomberg Television that the bank spent about $2 billion a year on AI and received about the same in benefits: “We have shown that for $2 billion of expense, we have about $2 billion of benefit.” When later asked for updated figures, the bank’s chief financial officer put annual AI spending closer to $700 million and called the earlier figure “a little stale.” The same report said the benefits were not yet visible in the bank’s quarterly earnings. The published accounts do not say which costs, benefits, or period either figure covered.

Figure 3.1 shows the relationship between the two layers: the science provides the foundation for the discipline’s five functions.

[FIGURE 3.1. Drawn figure, not reproduced here.]

**Figure 3.1.** The two layers. AI Business Economics states conditional claims about consuming AI and records what each one rests on. AI Operations Management acts on it through five functions, all taught in Part III.

A result about governance changes nothing until an organization builds the apparatus it describes. The science therefore depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

### 3.3 Where the discipline ends

Chapter 1 set aside three related subjects: how models work, prompt engineering, and finding uses for AI. Each has its own purpose and literature, and each ends before AI Operations Management begins.

The first subject concerns how models work, including their architectures, training, and internal behavior. It belongs to computer science and machine learning engineering, and ends where a model becomes a service an organization can call. AI Operations Management begins where a model is a service an organization can buy and call.

The second is prompt engineering, the craft of writing inputs that produce better outputs. It improves individual uses of AI, while AI Operations Management governs their combined consumption, cost, and value. A better prompt can lower the cost of one request. Only the discipline can determine whether the organization’s requests, taken together, are worth what they cost.

The third subject is finding uses for AI: deciding which business problems it might solve. That work belongs to strategy and innovation, and ends when a use is chosen. AI Operations Management begins with buying capacity for the chosen use and manages its consumption from then on.

Four established disciplines sit closer to AI Operations Management. Each manages an aspect of work related to AI consumption, but each lacks something needed to govern its economics. Table 3.1 compares them.

| Neighbor | What it is for | What it manages | What it lacks for this territory |
|---|---|---|---|
| AIOps | Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination | The health and performance of IT systems | It uses AI to watch systems. It does not govern what consuming AI costs or returns |
| MLOps | Building, deploying, and monitoring machine learning models in production | The lifecycle of models an organization builds | It ships models. It does not govern the consumption of capacity an organization buys |
| FinOps | Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams | Cloud and wider technology spending | It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value |
| Regulatory AI governance | Ensuring that uses of AI are lawful, safe, and accountable to regulators | Risk and compliance | It asks whether a use is permitted, not whether it is economically managed |

Table 3.1. The four neighboring disciplines. Each manages work related to AI consumption, but none was built to govern its economics.

FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

Regulatory governance determines whether an organization may use AI in a particular way. This book takes that determination as given and asks how the permitted use is managed.

### 3.4 Five questions the discipline exists to answer

Each of the five questions corresponds to one of the discipline’s functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

An organization that manages its AI consumption can answer five questions from its own records:

Question 1. “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7.

Question 2. “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10.

Question 3. “Who consumed what last month, in service of which work?” This is the metering and attribution question, answered across Chapters 8 and 9.

Question 4. “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11.

Question 5. “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12.

These are the Founding Questions, which an organization must answer “from its own records.” It can always produce an answer by asking the provider, estimating, or repeating the business case, but none of those methods produces knowledge the organization holds and can check.

At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II presents the science the functions rest on, Part III builds the five functions, and Part IV turns them into an institution.

## [CRAFT SECTION]

## The function audit

The **function audit** finds which of the five functions an organization performs for one deployment, and which no one performs. It builds on the two methods of Part I. Chapter 1’s consumption-event inventory lists what a deployment consumes, and Chapter 2’s three-flow mapping shows which flows are managed. The audit asks who does each job the discipline requires. The procedure has six steps.

Step 1. List the deployment’s AI activities: buying capacity, choosing models, forecasting spending, recording use, assigning costs, routing work, and judging the return. Start from the consumption-event inventory.

Step 2. For each activity, name the Founding Question it helps to answer, and assign the activity to that question’s function.

Step 3. Assign to a neighboring discipline any activity that answers a neighbor’s question instead, using Table 3.1.

Step 4. Mark each function that no activity performs.

Step 5. For each function that is performed, name who performs it. Write “no one” where the evidence shows no owner.

Step 6. State the first gap to close and the record that closing it requires.

Steps 2 and 4 do most of the work. Step 2 turns a list of activities into a map of the discipline. Step 4 shows what the map leaves empty: the functions where cost can arrive with no one watching it.

> **DATED EVIDENCE BOX · Dated: April to July 2026**
>
> Lindy is a company of about 25 people that sells AI assistants for email and calendars. In 2026 its founder, Flo Crivello, said the company’s largest expense was the AI models it bought from Anthropic: “Like, more than payroll.” In June 2026 he announced that Lindy had moved all of its traffic to DeepSeek V4, a model from a Chinese developer, and said the move would save millions of dollars. He called the switch “100x more work than we thought.” He said he would consider returning to Anthropic’s models if their prices fell, and he expected the company to keep spending more on AI than on payroll.

Applied to Lindy on the public record, the procedure works as follows.

Step 1. The record shows five activities: running the assistants that customers use; choosing a model provider; knowing the total cost of the models well enough to compare it with payroll; sending all traffic to one model; and keeping the former provider under review against its price.

Step 2. Choosing a provider and keeping it under review answer the sourcing question. Sending all traffic to one model is a routing rule, so allocation and routing is performed by a single decision. Knowing the total cost answers part of the metering and attribution question. The record does not show that cost assigned to customers or products.

Step 3. No activity in the record belongs to a neighbor. Whether a company may use a model from a particular developer or country is a question for regulatory governance, which this book takes as given.

Step 4. Planning and budgeting, and holding value to account, show no activity. Nothing reported shows a forecast of consumption, a comparison of spending against a plan, or a measure of whether each customer’s use pays for itself.

Step 5. The founder performs sourcing in public. The record names no one for the other functions. A public record cannot show work a company does without announcing it, so “no one” here means “not shown.”

Step 6. The first gap is attribution. A company whose largest cost is AI consumption needs that consumption recorded by customer account, so that it can compare each customer’s use with what that customer pays. The same record supplies the raw material for a budget and for a value boundary.

The audit took six steps and a few public facts. It showed a company changing its entire supply of AI capacity on grounds of cost, while the public record showed no one answering three of the five Founding Questions. The switch itself was sourcing done well. The audit shows what the switch could not tell the company: which customers its new costs belong to.

### Chapter summary

AI Business Economics is the science of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on. The claims are kept in a registry and linked by dependency. This book renders and cites only certified claims.

The book presents the results of the science in numbered panels. Each panel carries an identifier and a reading in plain business language, and the full statements are in Appendix A.

AI Operations Management applies the science through five functions: sourcing, planning and budgeting, metering and attribution, allocation and routing, and holding value to account at a boundary. It begins when a model becomes a service an organization consumes. It shares boundaries with AIOps, MLOps, FinOps, and regulatory governance, while remaining a distinct discipline.

The function audit assigns a deployment’s AI activities to the five functions or to a neighboring discipline and marks the functions no one performs. Its first output is the gap to close and the record that closing it requires.

The Founding Questions are the five questions the discipline exists to answer from an organization’s own records. By the end of Part I, readers understand the questions but do not yet have a method for answering them.

### Key terms

**AI Business Economics.** The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

**AI Operations Management.** The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

**Sourcing.** The function that matches the AI capacity an organization buys to the requirements of its work: which models and providers serve which work, and on what terms.

**Planning and budgeting.** The function that states how much AI an organization expects to consume in a period and detects when actual consumption departs from that expectation.

**Metering and attribution.** The function that records what was consumed and assigns each unit of consumption to the team, product, or purpose it served.

**Allocation and routing.** The function that decides what runs first when capacity is limited and sends each piece of work to suitable capacity, by a stated rule.

**Value boundary.** The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against. Holding value to account at this boundary is the fifth function.

**Founding Questions.** The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions.

**Function audit.** The six-step method for finding which of the five functions an organization performs for a deployment: list its AI activities; assign each to a function or a neighboring discipline; mark the functions no activity performs; name who performs each; and state the first gap to close.

### Discussion questions and problems

## [DISCUSSION QUESTIONS]

**1.** Choose one of the five dated boxes in Section 3.2. What would the organization in it have to record, in its own systems, to answer that function’s Founding Question? Name the record and who would keep it.

**2.** Of the four borders in Table 3.1, which is hardest to defend, and why? State what evidence would move that border.

**3.** Restate one Founding Question in language your chief financial officer would use, preserving all its content. Then identify the part you were most tempted to omit.

**4.** Chapter 2 diagnosed a deployment through its three flows. Match each flow to the functions in Section 3.2 that act on it, then explain which flow draws on the most functions and why.

## [PROBLEMS]

**P1 · Worked.** An audit of the budget that ran out

Chapter 2’s opening case described Uber’s deployment of Claude Code, which consumed the company’s annual AI budget by April 2026. Using only the facts reported there, apply the six steps of the function audit.

Step 1. The reported activities are: buying access to Claude Code; rolling it out to roughly 5,000 engineers from December 2025; setting an annual AI budget; tracking adoption, which reached 32 percent of the engineering organization in February and 84 percent in March; and totaling spending. Reported spending ran from $150 to $250 a month for the average engineer and from $500 to $2,000 for the heaviest users. A sixth activity is a question. The president and chief operating officer said the company could not yet connect its growing use of the tool to the consumer features it was producing: “That link is not there yet.”

Step 2. Buying access to one tool for all engineers is sourcing. Setting the annual budget is planning and budgeting. Tracking adoption and totaling spending are part of metering and attribution. The chief operating officer’s question belongs to holding value to account: it was asked, and the reporting shows no answer.

Step 3. Nothing reported places any of these activities with a neighboring discipline.

Step 4. Allocation and routing shows no activity. Nothing reported shows a rule for which work went to the tool or a limit on its heaviest users. Attribution shows none either: nothing reported assigns the consumption to teams.

Step 5. Engineering ran the rollout, and someone set the budget. The public account does not show anyone comparing spending with that budget before it ran out, so the audit writes “no one” against that comparison.

Step 6. The first gap is a monthly comparison of actual consumption with the plan. It requires consumption recorded by team, which is the metering and attribution function the audit found incomplete.

**P2 · Completion.** An audit with three steps left open

Chapter 2’s problem P3 described the Australian Government’s whole-of-government trial of Microsoft 365 Copilot, from January to June 2024. Around sixty agencies took part. Each agency nominated or approved the employees who would receive licences, and the government issued several thousand. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an evaluation, delivered it jointly with an external firm, and published the full report. Participants reported using the tool a few times a week or less and saving time when they used it. They assessed those effects themselves, and the published methodology reports no objective measure of task time or output from before the trial. Steps 1 to 3 are worked below. Complete steps 4 to 6.

Step 1. The activities are: buying several thousand per-seat licences; agencies choosing which employees receive them; commissioning an independent evaluation; publishing it in full; and collecting participants’ reports of their use and the time it saved.

Step 2. Buying per-seat licences is sourcing. Choosing which employees receive a licence is allocation: it decides who gets capacity, by agency nomination. Commissioning and publishing the evaluation is holding value to account, within a boundary the evaluation stated, including its own limits. Collecting participants’ reports of their use is a partial record of consumption, part of metering and attribution, without a record of each use.

Step 3. Any review of whether agencies were permitted to use the tool belongs to regulatory governance, and the audit sets it aside.

Step 4. Mark the functions that no activity performs. Consider how per-seat pricing changes which functions the trial needed.

Step 5. Name who performed each function, from the facts above. Write “no one” where the facts show no owner.

Step 6. State the first gap you would close if the trial became a permanent deployment, and the record that closing it requires.

**P3 · Independent.** Whose decision is it

Consider a constructed situation. A company’s FinOps lead and its new head of AI operations both claim the decision to commit to an annual volume contract with a model provider. The FinOps lead argues that the commitment is a spending decision, like reserving cloud capacity. The head of AI operations argues that it fixes which work the company can afford to run. Write one page assigning each part of the decision to one discipline, using Table 3.1 and the five functions. State the evidence that would move one part across the border.

*Interleaving: question 4 requires Chapter 2’s three flows, problems P1 and P2 audit Chapter 2’s cases, and the cumulative case below requires both earlier chapters.*

## [PART I CUMULATIVE CASE]

**Cumulative case · Part I.** One announcement, three readings

Dated: February 2024. The company’s own announcement, using its own figures. Only that announcement is used here.

In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

Work from this announcement alone.

First, apply Chapter 1’s consumption-event inventory. Identify the consumption events described in the announcement and where each would be metered.

Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and cost-and-value flows, identifying the evidence behind each diagnosis.

Third, apply each of the five Founding Questions to the announcement. For each question, state whether the announcement provides an answer from the organization’s own records and what record would be needed to answer it.

Keep your answers. The case returns in Chapter 6.

<<<<< END DOCUMENT 1 >>>>>

<<<<< BEGIN DOCUMENT 2: REFERENCE EXTRACT >>>>>

# Chapter 3 review: reference extract

Everything the reviewer grades against, extracted verbatim from the book's planning documents.

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
   - Competency: C4 (place an organization’s AI work in the five functions; tell the discipline from its neighbors). No single anchor, no set piece (Decision 85, 2026-10-14).
   - Also: five functions previewed; Founding Questions posed; borders drawn (not AIOps, not FinOps, not MLOps, not regulatory governance).
   - Craft section: the function audit (assign a deployment’s AI activities to the five functions or a neighboring discipline; mark the functions no one performs).

## 2. Competency C4 and assessment 4, from the exit competencies

Competency C4: Place an organization’s AI work in the discipline: assign each activity to one of the five functions, name the functions no one performs, and tell AI Operations Management apart from FinOps, MLOps, AIOps and regulatory governance.

Assessment 4: Function audit on a cited real deployment not worked in the book: list its AI activities, assign each to a function or a neighboring discipline, mark the functions no one performs, and defend one contested border in a paragraph a CFO would accept.

## 3. The approved chapter plan (version 2)

## The chapter in one line

AI Business Economics is the science; AI Operations Management is the discipline
that acts on it, through five functions, inside borders that separate it from
its neighbors. Competency C4, rewritten (decision 1 below). No anchor theorem and
no new panel. Closes Part I.

## Slots

| Slot | Content | Source or object |
|---|---|---|
| 1 Opening case | KEPT as locked and fact-checked: the FinOps Foundation's mission change, February 2026; the 2026 survey; the practitioner quotation | Verified at the 2026-10-13 fact check (finops-2026-mission, -state, -what-is, -definition-2024) |
| 2 Teaching body | **3.1 The science and the practice** (about 900 words): the business problem first; AI Business Economics as an ordered body of conditional claims; one short passage on how the book shows them (numbered panels such as Chapter 2's THM-004, each with a plain-English reading; the full statements are in Appendix A); how the two layers depend on each other; Figure 3.1, the two layers (the old Figure 3.2). **3.2 The five functions** (about 2,400): the definition of AI Operations Management, then each function in timeless prose followed by **one dated box of real reporting** (five boxes). **3.3 Where the discipline ends** (about 900): KEPT, the three subjects Chapter 1 set aside and Table 3.1, the four neighbors. **3.4 Five questions the discipline exists to answer** (about 700): KEPT, the Founding Questions verbatim | Dated boxes: candidates in `AIOM_Ch03_Redesign_examples.md`, all Grade C until read. Neighbors: the verified table sources |
| 3 Craft section | **The function audit**, six steps: (1) list the deployment's AI activities (Chapter 1's inventory); (2) for each, ask which question it answers and assign it to a function; (3) assign anything that answers a neighbor's question to that neighbor; (4) mark each function no activity performs; (5) name who performs each function, or "no one"; (6) state the first gap to close and the record it needs. Worked in full on one real deployment (decision 2) | Case per decision 2 |
| 4 Summary | The two layers; the five functions; the borders; the Founding Questions, unanswered | none |
| 5 Key terms | AI Business Economics; AI Operations Management; the five functions, each named; the value boundary; the Founding Questions; the function audit. Dropped: registry, theorem, lemma, proposition, certified claim, trace, dependency, condition, scope, non-claim, falsifying case, trace procedure | Inherited vocabulary for AI Business Economics terms |
| 6 Questions and problems | Discussion: the hardest border to defend (kept); a Founding Question in a CFO's language (kept); Chapter 2's flows mapped to the functions (kept); NEW, one dated box: what would the organization have to record to answer that function's question. Problems: **P1 worked** function audit; **P2 completion** audit, steps 4 to 6 open; **P3** an ownership dispute between FinOps and AI Operations Management over one named activity, argued in a page. Then the **Part I cumulative case, KEPT** (Klarna, February 2024 announcement only) | Cases per decision 2; Klarna verified 2026-10-13 |

**Removed:** the THM-004 trace (old 3.2) and Figure 3.1; how to read a formal
claim (old 3.3); the trace procedure; the dated registry-counts box; problems P1
and P2 on LEM-020 and THM-002; the four lemma and seven proposition citations.

**Continuity promises this chapter pays** (`AIOM_Continuity_Ledger.md`):
- Ch1 to Ch3: where each neighboring subject ends. Paid by 3.3, unchanged.
- Ch2 to Ch3: "As Chapter 3 explains, the theorem formalizes the economic
  consequence of the third flow's asymmetry; it does not establish the taxonomy
  itself." See decision 3.
- Ch2 to Ch3: Chapter 3 names the discipline that resolves the category error.
  Paid by 3.2.

**Promises it makes:** each Founding Question to its answering chapter; the
FinOps treaty to Chapter 14; the Klarna reveal to Chapter 6. **Withdrawn:** the
THM-008 trace in Chapter 7's assessment (C4 no longer asks for a trace).

**Ledgers, from the first lock:** Chapter 3's 14 claim-ledger rulings are
re-ruled at the new fact check (kept where the sentence survives, superseded
where it is cut); Chapter 3's continuity-ledger rows (16 terms, 21 forward
references, 13 glosses) are reconciled at the new lock, removing what the new
text no longer carries.

**Length:** 6,000 to 7,500 words (Decision 82). One figure, one table, five
dated boxes.

## Rulings at sitting 1, 2026-10-15 (all A)

1. C4 and Assessment 4 take the wording below; C4 moves to Group 2 (Doing).
2. Craft example: Lindy.ai. P1: Uber. P2: the Australian Copilot trial.
3. Chapter 2's THM-004 promise is kept by one or two sentences in 3.1.
4. Five key-term entries, one per function.

## 4. The seven craft criteria, from the prose standard

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

<<<<< END DOCUMENT 2 >>>>>

<<<<< BEGIN DOCUMENT 3: CHAPTER 1, THE EXEMPLAR >>>>>

Part I · The Argument

# The Category Error

## [OPENING CASE]

## Two subscriptions, one correction

*Dated: June 2025 to June 2026. Vendor actions, dates, and figures are sourced. The buying organization is a composite.*

Twenty dollars per developer, per month. In the spring of 2025, that was the price of Cursor, an AI coding assistant. A software team bought one Cursor license for each developer who would use it, just as it did with every other software tool. The expense went into the budget beside the company’s ticketing system, design software, and password manager.

Cursor was useful, and it was cheap. Once the agreement was signed, nobody in finance had a reason to examine the line item again. Nothing about a twenty-dollar software seat demanded attention. But beneath every seat, a meter was running.

On June 16, 2025, the twenty dollars stopped being a price and became a balance. Cursor replaced the Pro plan’s monthly allowance of five hundred requests to external models with a twenty-dollar credit for frontier-model usage. Each request now drew down that credit at the model provider’s API rate. The subscription still cost twenty dollars a month, but what that price bought had changed completely.

Light users barely noticed the change because their activity remained within the included credit. Heavy users had a different experience. A handful of prompts could exhaust the credit, after which additional usage was billed at the underlying API rates. The change therefore affected the customers who relied on the product most and often received the most value from it. Many faced charges they had not anticipated or budgeted for.

On July 4, less than three weeks after the change, Michael Truell apologized and promised refunds for charges incurred during the transition. Truell is chief executive of Anysphere, the company behind Cursor. His explanation reduced the dispute to arithmetic. The newest models consumed far more tokens on long-horizon tasks than a flat monthly price could cover.

On June 18, 2025, two days after Cursor changed its plan, GitHub began enforcing monthly premium-request allowances for Copilot and letting customers pay for usage beyond them. It then spent the next year preparing a larger change.

On June 1, 2026, GitHub stopped measuring standard usage in requests and began measuring it in credits. Those credits reflected the tokens each customer consumed and the published rate of the model that customer selected. Customers received advance notice and could preview their charges before the bill arrived. Every plan included an allowance, and annual subscribers kept premium-request pricing until their subscriptions expired. The subscription price did not change by a dollar. What changed was what that dollar bought.

Microsoft’s scale changed how the pricing correction arrived, but not whether the underlying economics required it. On January 28, 2026, four months before that change, the company told investors on its earnings call that Copilot had passed 4.7 million paid subscribers and was growing 75 percent year over year. If a provider can fund the gap between a flat price and the cost of the resource that price buys, then it controls the timing and the form of the correction. That control is what buys advance notice, a published schedule, and tooling that shows customers the effect before it lands. If a provider cannot fund the gap, the gap sets the timing instead. Scale made the correction orderly. It did not make the variable cost disappear.

From the buyer’s side, the two pricing corrections looked very different. Cursor changed its plan without warning, then apologized and issued refunds after customers objected. GitHub announced its change in advance, published a schedule, and gave customers tools to preview the effect on their bills. The execution differed. The economic correction was the same.

Both products had been sold and purchased like conventional software: one seat, one flat price, and a cost fixed when the contract was signed. Beneath that subscription, however, the provider carried a variable cost. Every request consumed computing resources, and heavier use increased that cost while the revenue from each seat remained fixed. Once the cost of serving heavy users exceeded what the subscription could support, the provider changed the terms.

The provider determined when and how that correction occurred. Customers did not have to approve the change, or even know how many tokens they were consuming, for it to affect them. In both cases, the movement was in one direction: away from unlimited use at a flat price and toward plans that tied allowances, credits, and additional charges to consumption.

The buyers had not chosen the wrong vendors, and the tools had not failed. They made an **error of category**. They bought access to a metered resource but managed it as conventional licensed software, assuming that the subscription price fixed the cost. What had looked like fixed-price software became a consumption-based resource all at once.

### 1.1 The purchase that is not one

> **DEFINITION CALLOUT · Access price**
>
> The stated amount an organization pays for the right to use an AI capability, usually per seat or subscription. It does not include additional costs based on how much AI the organization actually uses.

> **DEFINITION CALLOUT · Software access model**
>
> A purchasing model in which an organization pays a fixed price for access to software, usually per seat or subscription. Because additional use creates little or no additional cost, the organization manages who has access rather than how much of the software each user consumes.

The buyer understood the transaction through the conventional software model. Under that model, an organization buys licenses that give a defined number of employees access to a program. Once the organization pays for a seat, additional use creates almost no additional cost. An employee who opens the program a thousand times a day costs the same as one who opens it once a week.

The organization therefore fixes its cost when it signs the contract. Procurement negotiates the number of seats and the price of each seat. That per-seat amount is the **access price**. After the purchase, the organization manages access rather than consumption: who has a login, how many seats are active, and when the contract renews.

**The software access model** is not flawed. It accurately describes licensed software, and organizations have refined it through decades of enterprise purchasing. The problem begins when buyers apply that model to AI.

An AI assistant may be sold as a program licensed by the seat, but each task calls a model and consumes computing resources. The amount consumed depends on factors such as the model selected and the size of the request and response. Each additional use therefore creates an additional underlying cost, whether the provider charges the buyer immediately or absorbs that cost for a time. AI access may be packaged like licensed software, but AI use behaves like a metered resource.

The result is a mismatch between what the organization manages and what its AI systems consume. Access management asks who can use the tool and how many seats are active. Resource management asks how much AI the work consumes, what that consumption costs, and what value the work returns.

An organization that manages only access to a metered resource is measuring the wrong quantity. It counts seats even though usage and cost are determined by tokens, requests, and credits. The organization is managing the right tool through the wrong economic model.

### 1.2 The consumption event

> **DEFINITION CALLOUT · Consumption event**
>
> A single use of an AI system that consumes metered computing resources and creates an underlying cost greater than zero, whether or not the buyer is charged for it separately. A consumption event may be measured in tokens, requests, credits, compute time, or another equivalent unit. It is the basic unit of consumption tracked in AI Operations Management.

The discipline developed in this book begins with a single unit of measurement: **the consumption event**. Each time an employee, workflow, or product calls an AI model, the system consumes computing resources and creates one of these events. The meter records them, and the invoice sums their cost.

The anatomy of a consumption event is simple, and Figure 1.1 shows its parts. Something enters the model: a prompt, a document, or a conversation history. The model performs a computation. Something returns: a completion, a suggestion, an answer, or a tool call.

As this work occurs, a meter records the resources consumed. Providers typically measure this consumption in input and output tokens, the units into which the model divides the material it reads and generates. The provider records those units in a usage ledger, even when the buyer never sees the individual event.

This creates an important difference in visibility. The provider sees a stream of metered consumption. The buyer may see only a flat subscription charge at the end of the month. Token counts can rise into the millions while remaining hidden behind that fixed price. The buyer often has no reason to examine the underlying consumption until usage exceeds an allowance or additional charges begin to appear.

[FIGURE 1.1. Drawn figure, not reproduced here.]

**Figure 1.1.** Anatomy of a consumption event. The system assembles an input, the model performs the computation, and the system returns an output. A meter records the resources consumed by the event. In most cases, the provider retains this event-level record, while the buyer receives only an aggregate usage total or charge.

AI Operations Management must measure cost in the same unit used to record consumption. Three units appear possible: the seat, the task, and the consumption event.

A seat measures access, not use. Two employees with identical seats can consume vastly different amounts of AI. A task is the right unit for measuring business value, because it connects AI use to completed work. It cannot, however, measure cost reliably, because one task may require a single model call while another requires hundreds.

The consumption event provides the necessary unit for cost. It is the smallest recorded use of AI that consumes computing resources and creates an underlying cost. It is also the unit captured by the provider’s usage meter. The organization can attribute costs to users, tasks, workloads, and workflows only by connecting those categories to the events that produced the costs. Later chapters group individual events into these larger operating units. Because each total begins with recorded events, the organization can trace it back to actual consumption and reconcile it with the provider’s invoice.

A seat measures access. A task measures value. A consumption event measures use and cost.

[FIGURE 1.2. Drawn figure, not reproduced here.]

**Figure 1.2.** Two purchase models. Under the seat model, the buyer pays a fixed price for access, so cost remains flat as usage rises. Under the event model, each consumption event adds to the total, so cost rises with usage.

The seat model and the event model do not describe the same cost in different ways. They describe two different cost structures. The seat model is the software access model defined in 1.1. The event model is the **resource consumption model**, in which each use is a metered consumption event. Figure 1.2 makes visible the difference that a flat subscription price can hide. Under the software access model, the buyer pays a fixed price for access, regardless of how much the software is used. Under the resource consumption model, every use adds to the total cost.

A contract may package AI as fixed-price software, but that packaging does not make the underlying cost fixed. If the buyer manages seats while consumption governs the economics, the mismatch remains invisible until the provider changes the terms or additional charges appear. The correction then arrives on the provider’s schedule, not the buyer’s.

### 1.3 The flat-rate objection, answered

One objection stands against everything said so far: “We pay twenty dollars per seat each month. Our price is fixed, and the provider never bills us by the token. From our perspective, this is simply software.”

The objection is valid. A buyer who pays a flat monthly price is not secretly being billed by the token. But this does not mean that the underlying resource is unmetered. Flat pricing relocates the meter from the buyer to the provider. It does not abolish it. This is **meter relocation**.

The provider continues to measure what each customer consumes. It sets the flat price based on an estimate of how much the average customer will use and what that usage will cost. The price is therefore built on an assumption. It remains viable while subscription revenue covers the total cost of serving the customer base.

The arrangement becomes unstable when actual usage departs from that assumption. If a small group of heavy users consumes a disproportionate share of the resource, the flat price collected across all customers may no longer cover the provider’s cost. The provider must then bring the price or the product limits back into line with consumption.

It can raise the subscription price, charge for usage above an allowance, redefine the allowance in tokens or credits, or cap consumption outright. Chapter 4 examines these instruments in detail. The method may vary, but the direction does not: what the customer receives becomes more closely tied to what the customer consumes.

The buyer does not choose when this correction occurs. The provider holds the meter, bears the variable cost, and decides when the existing terms have become unsustainable. A flat price can hide the meter from the buyer. It cannot prevent the provider from acting when the numbers no longer work.

This result does not depend on a vendor being careless or badly managed. It follows from the economics of deployed AI, and the AI Business Economics registry states it as a theorem.

> **THEOREM PANEL · Theorem 1 · THM-009**
>
> *AI Use Is Resource Consumption, Not Merely Software Access*
>
> Within a defined deployment and cost boundary, if:
>
>   (i) an AI activity requires compute, and executing it consumes resources;
>
>   (ii) production scaling expands the surface over which that activity is used;
>
>   (iii) the buyer’s total cost extends beyond the access price; and
>
>   (iv) measurement makes resource use, or the cost-bearing activity, visible;
>
> then that AI use is a resource-consuming operating activity, not merely software access.

A theorem in this book is a statement established within a defined system from earlier propositions and lemmas. It is not a generalization drawn from the Cursor and Copilot episodes. Those cases illustrate the result; they do not prove it. Like every theorem in this book, Theorem 1 applies only when its stated conditions hold.

Its claim is deliberately narrow. The theorem does not say that flat-rate AI subscriptions are impossible, nor does it predict that every provider will reprice them. It says that when an AI activity requires computation, each execution consumes resources. As employees, workflows, and products use that activity at greater scale, its resource consumption grows. When the stated cost boundary includes the cost of those resources, the economics of the activity cannot be described by the access price alone.

The fourth condition asks only that the resource use be measured somewhere, not that the buyer can see it. A provider’s meter satisfies that condition even when the invoice shows a single flat charge. The business is operating a resource-consuming activity, not merely accessing software.

> **DEFINITION CALLOUT · Meter relocation**
>
> The placement of consumption metering on the provider’s side of a flat-rate subscription. The buyer pays a fixed price for access, while the provider continues to measure actual use. The provider sets the flat rate based on expected consumption and may change the price, allowance, or usage limits when actual consumption exceeds that expectation.

A flat monthly subscription to ChatGPT does not contradict this conclusion. The subscription price states what the buyer pays for access under a particular plan. It does not show how much computing capacity the buyer consumes, what that consumption costs, or whether the provider absorbs the cost within the subscription. Buyers may classify the charge as another SaaS expense because that is how it appears on the invoice. But the invoice describes the commercial arrangement, not the operating economics beneath it. The subscription buys access. Each use still consumes a resource.

The public record already shows this pattern running its course in several forms. Some providers have moved directly to usage-based pricing. Others have retained a flat subscription while adding allowances, credits, or hard limits on consumption. The commercial instrument differs, but the correction is the same: what the buyer receives is brought back into line with what the buyer consumes.

> **DATED EVIDENCE BOX · Dated: January 2025**
>
> OpenAI provided an early example. Chief executive Sam Altman said publicly that the company was losing money on its two-hundred-dollar Pro subscriptions because subscribers used them more than the price had assumed. He also acknowledged that he had personally set the price. The problem was not the price of access. Actual consumption had exceeded the assumption built into it.

> **DATED EVIDENCE BOX · Dated: July 2025**
>
> Claude Code customers encountered the same economic correction through tighter limits rather than a higher subscription price. Subscribers reported that they were reaching their plans’ usage limits sooner, although Anthropic had given no notice of a change. Many had not realized that their subscriptions were subject to such limits at all. Anthropic acknowledged the reports but did not confirm that it had altered the plans. Those reports were published on July 17, 2025.
>
> Eleven days later, the company announced two new weekly usage caps in addition to its existing five-hour limits. The caps would take effect the following month for all Pro and Max subscribers. Max subscribers could continue using Claude Code beyond those limits by purchasing additional usage at standard API rates. The subscription price remained intact, but the amount of consumption included within it now had a clearer boundary.

The Cursor and GitHub Copilot episodes that opened this chapter show the same pattern. Within twelve months, two widely used AI coding products revised their subscriptions so that what customers received more closely reflected what they consumed. Cursor made the correction abruptly and responded to complaints with an apology and refunds. GitHub announced its change in advance and introduced it with billing tools and a transition period. The method differed. The economic correction did not.

In both cases, the provider continued to measure usage beneath the flat subscription price. The provider determined when the existing terms no longer worked and changed the arrangement on its own schedule. The flat rate had not removed the meter. It had placed the meter, and control over the correction, on the provider’s side of the transaction.

### 1.4 What follows if this is true

Once an organization recognizes deployed AI as a resource it consumes, the management requirements become familiar. Businesses already know how to manage resources used in daily operations. Consider a manufacturer that relies on steel. Counting how many employees are authorized to order steel would measure access to the resource, but it would not manage the resource itself. The company must determine how much steel its operations require, what specifications it must meet, what it costs, where it is used, and what value it helps create. The same management logic applies to AI.

Before purchasing steel, the company forecasts demand, sets a budget, and evaluates suppliers against its requirements. During production, it compares actual consumption with the plan and tracks how much steel each product line uses. If supply becomes limited, it allocates the available steel according to business priorities. It then includes the cost of that steel when calculating the profitability of each finished product. If a product consumes more steel than its margins can support, management can see the problem and respond.

These practices are not unique to manufacturing. They apply to any resource that costs money as it moves through an organization. To manage such a resource, leaders must be able to answer five questions:

What is the organization buying, and what requirement must it meet?

How much does it expect to consume, and how will it know when actual use departs from the plan?

Where is the resource being used?

Who decides how it is allocated when there is not enough?

What value does the organization receive in return?

If an organization cannot answer these questions, it is not managing the resource, regardless of what its organizational chart or policies suggest. It is simply receiving invoices and paying them.

Deployed AI is one of these resources. Every time an employee, workflow, or product uses AI, the organization consumes computing resources and incurs a cost. Total consumption rises with the volume of work, and as a deployment succeeds, that volume usually grows.

Most organizations, however, do not manage AI usage through a single, coordinated discipline. Responsibility is divided across several existing functions. Procurement negotiates the contract. Cloud cost management monitors infrastructure spending. Engineering tracks the systems it operates. Finance allocates the costs it can trace. Each function manages one part of the resource, but none manages it from purchase through consumption to business return.

These functions were designed before deployed AI created a resource that crossed all of their boundaries. As a result, AI usage touches several owners but belongs fully to none. Chapter 14 distinguishes the subject of this book from these neighboring disciplines. What is missing is not attention. It is a management system that brings the separate responsibilities together.

Organizations that would never allow material to move through a plant without a record often allow AI consumption to pass through daily work unrecorded. The five questions therefore go unanswered, and the reason is visible in three places.

First, the organization tracks the wrong quantities. A company accustomed to seat-based software tracks headcount, license utilization, and renewal dates. None of these measures shows how much AI the organization consumes or what produces the bill.

Second, the organization lacks a record of use. Under a seat-based contract, each additional use costs nothing at the margin, so the buyer has little reason to record it. Under an event-based model, every use consumes resources and can add to the bill. Yet a company that has not built a meter cannot show which work produced that consumption. The invoice does not provide this record. It reports the total cost, not the uses that created it.

Third, the organization has no basis for accountability. Finance cannot assign a cost to the team, workflow, or product that incurred it unless the company can trace the cost back to the work. A cost assigned to no one is defended by no one.

It would be a mistake to treat these gaps as negligence. The organization inherited them from the seat-based software model, just as it inherited the absence of a clear owner. It did not decide to stop metering software use. It never began, because the software it had purchased for three decades did not require it. Enterprise software procurement built a management system around the economics of the license: count the seats, track utilization, and manage renewals. That system worked.

AI often entered the organization in familiar packaging. It came through the same vendors and procurement channels, initially at a price low enough to approve without much debate. The organization therefore managed it as another software license. The existing system did not fail. It did exactly what it was built to do, continuing to report seats, utilization, and renewal dates even after those measures had stopped explaining consumption and cost.

Scale makes this inherited arrangement untenable. While AI remains a pilot, the organization can afford to manage it as a software license. One team uses a few seats, and the bill is too small to matter against the larger software budget.

This all changes when the pilot enters production. AI usage then grows with the volume of work the system performs. A contact center does not merely add licensed users. It applies AI across the conversations and workflows those users handle, generating a new consumption event each time the system performs work.

The contact-center deployment examined later in this chapter illustrates the difference. It operates with roughly five thousand seats but generates tens of millions of consumption events each month. The craft section calculates this ratio in full. At pilot scale, seat count is a harmless simplification. At production scale, it is a blindfold.

The problem established in this chapter defines the work of the rest of the book. Once AI consumption moves through daily operations and produces variable cost, the organization needs a system for measuring, assigning, and governing it. No existing management practice provides that system in assembled form. The remaining chapters build it.

### 1.5 What this book is not

This book addresses what happens after an organization decides to deploy AI. It does not explain how models work internally, so it carries no account of architectures, training, or weights. It does not teach prompt engineering or offer techniques for improving a model’s output. It also does not help leaders identify problems that AI might solve. Each of these subjects has its own purpose and literature, and Chapter 3 explains where each ends and AI Operations Management begins.

The subject of this book is the deployed resource itself. It examines what AI consumes as employees, workflows, and products use it; what that consumption costs; and how the organization measures, assigns, and governs both. The decision to deploy establishes the need. This book explains how to manage what follows.

## [CRAFT SECTION]

## The consumption-event inventory

*The contact-center setting and approximate agent population are drawn from the cited study. The event architecture and all volume assumptions are stipulated for this exercise.*

A seat count shows how many people can use an AI system. It does not show how much AI activity their work generates. **The consumption-event inventory** replaces that administrative count with an operating view of the deployment. It identifies each kind of consumption event, what resources the event consumes, where that consumption is measured, and what the seat count leaves hidden.

This is the first artifact the reader produces in this book. Later artifacts use it to trace consumption, assign costs, and compare those costs with the value created. The inventory therefore needs to be specific enough to run against an actual deployment.

The procedure has four steps.

**Step 1: Enumerate the event types.** List every distinct kind of consumption event generated by the deployment. Begin with the work the system performs, not with the number of employees who have access. A single deployment may classify a request, retrieve information, generate several responses, call a tool, and summarize the completed interaction. Each is a separate event type when it triggers its own measurable use of resources.

**Step 2: Identify the resource drivers.** For each event type, state what causes its resource consumption to rise. Common drivers include input tokens, output tokens, model calls, retrieval operations, tool invocations, and the amount of context processed. Do not assume that two events consume the same resources merely because they occur inside the same workflow.

**Step 3: Locate the meter.** State which system records the consumption and which party controls that record. The meter may sit with the model provider, the application vendor, the organization’s cloud environment, or an internal platform. A flat-rate contract does not remove this step. It means only that the provider may hold the operational meter while the customer sees a fixed price.

**Step 4: State what the seat count conceals.** Estimate the volume of each event type over a defined period. Show the operating assumptions used in the calculation, then compare the resulting activity with the number of seats. The purpose is not merely to produce a larger number. It is to reveal the work, consumption, and cost drivers that cannot be seen from the seat count alone.

Consider a customer-support organization that has deployed a generative AI assistant across its contact center. For each incoming customer message, the assistant drafts a suggested reply that the agent may edit and send; the assistant draws on a knowledge base and on the conversation so far. The deployment covers a large agent population, on the order of five thousand agents, and the organization currently accounts for it as a per-seat tool.

Model inventory

**Step 1. Event types.** The deployment generates at least three: (a) a suggested-reply generation, triggered each time an agent asks the assistant to draft a response to a customer message; (b) a knowledge retrieval, triggered when the assistant pulls reference material to ground a suggestion; and (c) a conversation-close operation, in which the deployment summarizes or tags the resolved conversation.

**Step 2. Resource drivers.** For suggested-reply generation, the drivers are input tokens (the system instructions, the retrieved knowledge, and the conversation history assembled into the prompt) and output tokens (the drafted reply). The volume driver is the number of customer messages that receive a drafted reply, which scales with contacts multiplied by the number of turns per contact. For knowledge retrieval, the drivers are the number of retrieval calls and the tokens those calls embed and return. For the conversation-close operation, the drivers are input tokens (the full conversation) and output tokens (the summary or tags); their volume scales with the number of resolved conversations.

**Step 3. The meter.** The generation and close operations are metered on the provider’s side, by token. Retrieval is metered wherever the retrieval service runs. In the architecture stipulated here, the retrieval service is the provider’s managed index, metered by call and by token; an organization that operates its own vector store meters that step itself. Meter location is a property of the architecture rather than of the event type, which is why Step 3 directs the reader to locate the meter instead of assuming it. Under its per-seat plan, the organization receives a monthly invoice that shows only a seat count.

**Step 4. What the seat count conceals.** The seat count treats the agent population as a set of equal units: five thousand seats at one price. Put the volume drivers from Step 2 against it and the two quantities separate immediately. Stipulate, for this exercise, five thousand agents, each handling forty contacts on a working day, with six drafted replies per contact, one retrieval per drafted reply, and twenty-one working days in the month. Suggested-reply generations then run at 5,000 × 40 × 6 × 21, or 25.2 million events a month. Retrievals match them one for one at 25.2 million. Conversation-close operations run once per contact, at 4.2 million. The deployment generates roughly 54.6 million consumption events a month, which is about 10,900 events behind every seat.

Change any stipulated figure and the total moves; change none of them and the seat count still does not move, because the seat count is not a function of any of these quantities. Two agents on identical seats can consume amounts of the resource that differ by an order of magnitude: a high-volume agent handling long, reference-heavy conversations generates many times the consumption of a low-volume agent, at the same seat cost. The quantity that drives the bill is tokens per resolved contact. It does not appear on the seat line, and until the inventory names it, the organization is managing a number that does not govern its cost.

The inventory has done its work when the organization can see, for the first time, the shape of what it is buying. Not five thousand seats. A flow of tens of millions of consumption events whose volume and intensity, not headcount, determine the bill.

### Chapter summary

The category error is now clear. Under the software access model, the organization fixes its cost when it signs the contract and manages the number of seats. Under the resource consumption model, each metered event adds to total cost, and the organization must manage the resulting flow of consumption. These are different operating models, even when the provider packages both as software subscriptions.

The consumption event is the atomic unit of the second model. It is the smallest use of AI that consumes resources and creates an underlying cost. It is also the smallest unit whose consumption the provider’s meter records. Seats measure access. Consumption events measure use and cost.

A flat price does not erase this distinction. It relocates the meter to the provider, which continues to measure consumption and decides when the commercial terms must change. This conclusion does not require a prediction about any particular vendor. It follows from Theorem 1: deployed AI is a resource-consuming operating activity, not merely software access.

The reader can now apply the consumption-event inventory to a deployment description. The inventory identifies the types of events the deployment produces, the resources each event consumes, where that consumption is metered, and which cost drivers the seat count conceals. It makes the flow visible. It does not yet explain how to manage that flow. Seeing it whole comes first.

### Key terms

**Category error.** The error of managing a metered resource as if it were licensed software. It rests on a false assumption: that the access price fixes the total cost. The tool is the right one and the vendor is not at fault. The economic model applied to the tool is wrong.

**Consumption event.** A single use of an AI system that consumes metered computing resources and creates an underlying cost greater than zero, whether or not the buyer is charged for it separately. A consumption event may be measured in tokens, requests, credits, compute time, or another equivalent unit. It is the basic unit of consumption tracked in AI Operations Management.

**Resource consumption model.** The economic model in which deployed AI is consumed as a metered resource. Each use creates a consumption event, and cost accrues with each event. It contrasts with the software access model.

**Software access model.** A purchasing model in which an organization pays a fixed price for access to software, usually per seat or subscription. Because additional use creates little or no additional cost, the organization manages who has access rather than how much of the software each user consumes.

**Access price.** The stated amount an organization pays for the right to use an AI capability, usually per seat or subscription. It does not include additional costs based on how much AI the organization actually uses.

**Metered resource.** A resource whose consumption is measured per unit of use, here in tokens or their equivalents.

**Flat-rate objection.** The claim that a flat per-seat price makes AI equivalent to licensed software; answered by meter relocation.

**Meter relocation.** The placement of consumption metering on the provider’s side of a flat-rate subscription. The buyer pays a fixed price for access, while the provider continues to measure actual use. The provider sets the flat rate based on expected consumption and may change the price, allowance, or usage limits when actual consumption exceeds that expectation.

### Discussion questions and problems

## [DISCUSSION QUESTIONS]

**1.** A colleague argues that your organization pays a flat per-seat price and never receives a token bill, so AI is a seat-priced good and the consumption model does not apply. Explain why the contract does not change the underlying economic model. Your answer should not depend on predicting how any specific vendor will price its product in the future.

**2.** The Cursor and GitHub Copilot episodes can be read as two companies changing their prices. Taken together, what do they reveal about where consumption was being measured all along? Why does the evidence become stronger when the two cases are considered together?

**3.** Section 1.2 treats the consumption event, rather than the user or the task, as the discipline’s atomic unit. Make the strongest case for using the task instead. What could a task-based discipline explain or manage more effectively? What would it lose by moving away from the event?

**4.** Construct the strongest flat-rate objection a capable skeptic could make after reading this chapter. Then answer it. Your response should explain why flat-rate pricing does not eliminate the underlying consumption problem without assuming that any particular subscription will eventually be repriced.

## [PROBLEMS]

**P1 · Worked.** Five hundred seats, one meter

A company purchases an AI coding assistant for five hundred employees at a fixed annual price per seat. The contract contains no token charges, and the finance team records the entire purchase as software expense. Over the next year, some employees use the assistant occasionally while others use it throughout the workday.

Using the resource consumption model, explain why the absence of a usage-based charge on the company’s invoice does not make seat count the underlying unit of AI consumption. Identify where the meter is likely to reside, what it measures, and what the per-seat price conceals.

Model answer

The company pays for the AI coding assistant by the seat, but the seat is the commercial pricing unit, not the underlying unit of consumption. The five hundred employees do not consume the same amount of AI simply because the company purchases five hundred licenses. An employee who uses the assistant several times a month generates far less activity than one who relies on it throughout the workday.

The underlying meter therefore sits behind the seat price. Each time an employee uses the assistant, the system processes a request and consumes computing resources. The provider can measure those consumption events even when it does not expose them as separate charges on the customer’s invoice. The flat annual price is built around assumptions about how much consumption the average seat will generate.

Seat count therefore conceals the actual cost driver. Two companies may each purchase five hundred seats while generating very different levels of AI consumption. The same difference can exist inside one company: a small group of heavy users may account for a disproportionate share of total consumption even though every employee carries the same accounting cost per seat.

Under the resource consumption model, the meter has not disappeared. It has moved to the provider’s side of the transaction. The company sees a fixed software price, while the provider sees the flow of consumption events that the price must cover.

Annotated reasoning

The response begins by separating the commercial pricing unit from the underlying consumption unit. The company buys five hundred seats, but equal seat count does not imply equal AI use. It then makes the hidden mechanism visible: each request consumes computing resources, and the provider can measure those events even when the customer never sees a usage-based charge. From there, the response explains what the seat price conceals. Users, teams, and companies with the same number of seats can generate very different levels of consumption. The conclusion follows directly: flat pricing changes where the meter is visible, not whether consumption exists.

**P2 · Worked.** Inventory a coding-assistant deployment

A software company has deployed an AI coding assistant to three hundred developers. The assistant provides inline code completions, answers questions in the editor, and can perform multi-step agentic tasks. Produce the consumption-event inventory for the deployment.

Model inventory

**Event types:**

(a) Inline completion: triggered as a developer types and the assistant generates a code suggestion.

(b) Editor chat query: triggered when a developer asks the assistant a question.

(c) Agentic task run: triggered when a developer delegates a multi-step task to the assistant.

**Resource drivers:**

Inline completions consume input tokens from the surrounding code context and output tokens from the generated suggestion. Each event may be small, but the total volume can be high because completions occur repeatedly throughout the workday.

Editor chat queries consume input tokens from the developer’s question and any code or file context supplied with it. They also consume output tokens from the assistant’s response.

Agentic task runs consume resources across multiple model calls rather than a single request. They may also invoke tools, inspect files, generate code, and repeat steps before the task is complete. For that reason, one agentic run can consume substantially more resources than a single completion or chat query.

**Meter:** The meter sits primarily on the provider’s side. The provider can measure token consumption and, for agentic tasks, additional activity such as tool calls or repeated model requests. Under a seat-priced plan, the buyer may see only the number of seats and the resulting subscription charge.

**What the seat count conceals:** Seat count does not show how much AI the developers actually consume. Two developers with identical seats may generate very different levels of usage. A developer who runs long agentic tasks throughout the day may consume far more resources than several developers who use only occasional inline completions.

The important cost drivers are therefore the number, type, and intensity of consumption events. In this deployment, agentic task volume and length are likely to be especially important. The seat count reveals none of that variation.

**P3 · Completion.** Inventory a document-review deployment

A legal operations team has deployed an AI assistant that extracts key clauses from each contract submitted, compares them against a policy playbook, and drafts a redline memo. Complete the inventory below by filling the blank column.

*Interleaving: none. This is the first chapter; problem sets begin reaching back to earlier chapters in Chapter 2.*

<<<<< END DOCUMENT 3 >>>>>
