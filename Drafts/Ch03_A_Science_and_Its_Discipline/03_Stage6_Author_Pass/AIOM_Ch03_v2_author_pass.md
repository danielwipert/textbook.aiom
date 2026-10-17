# Chapter 3, A Science and Its Discipline: author pass

Edit the prose freely. Three things to keep:

1. The bracketed tag at the start of each paragraph, such as [BODY]. It tells
   the importer what the paragraph is.
2. One blank line between paragraphs, and the order of the paragraphs.
3. Plain text: no markdown formatting (no asterisks, no #). Typographic quotes
   and apostrophes are fine.

Splitting a paragraph, merging two, or adding a new one is fine: the importer
detects it and the change is made by hand. Blocks tagged THEOREM render a
locked registry statement; edits inside them are not applied. Footnotes carry
their source keys in parentheses after the tag; edit the footnote text, not the
keys. The source register is not in this file. Read the PDF beside this file
for layout and figures.

---

[PART LABEL] Part I · The Argument

[CHAPTER TITLE] A Science and Its Discipline

[SLOT] Opening case

[CASE TITLE] The discipline that changed its mission

[PROVENANCE] Dated: February 2026. Figures and the quotation checked against the Foundation’s report and announcement, October 2026.

[BODY] In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

[FOOTNOTE] (finops-2026-mission) The mission statement before and after the change.

[BODY] The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding concerned the expansion of FinOps into AI spending. Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier.

[FOOTNOTE] (finops-2026-state) Survey size and the cloud spending its respondents manage.

[FOOTNOTE] (finops-2026-state) Share of respondents managing AI spend, 2026 survey against 2024 survey.

[BODY] FinOps was built to address a specific problem: cloud consumption varied with use, and the bills arrived after capacity had been used. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all of the survey’s respondents were managing it.

[FOOTNOTE] (finops-definition-2024) Cloud consumption as variable and tracked after the fact.

[FOOTNOTE] (finops-what-is) The Foundation’s definition.

[BODY] Asked whether AI was providing value, one practitioner stated what remained unknown. The report chose to quote the answer: “No one can answer that question yet.”

[FOOTNOTE] (finops-2026-state) Practitioner quotation as reproduced in the report.

[BODY] The quotation names the gap Chapters 1 and 2 described, in the words of someone asked to close it. When an organization pays for a metered resource, costs accrue with use, but someone must build the means to measure the value it receives. FinOps is a capable neighboring discipline that has expanded into work it was not built to govern: the economics of an organization’s AI consumption.

[BODY] That work requires both a body of knowledge about what is true and a practice that turns that knowledge into action. This book sets out both. Chapter 14 explains how FinOps and that practice divide the work. Until both exist, the practitioner’s question about whether AI is providing value remains unanswered.

[SECTION HEAD] 3.1 The science and the practice

[BODY] Managers act on claims about how their business works. A budget assumes that costs follow usage. A pricing negotiation assumes that the provider has a reason to accept a lower price. A dashboard assumes that the information it displays will change someone’s decisions. When those claims are wrong, careful execution does not repair the decisions built on them.

[BODY] Claims like these can remain informal, held in experience, rules of thumb, or the slides of the last person to present. That knowledge is useful, but it has a cost: two managers can hold opposing beliefs about the same deployment without being able to identify where they disagree. One might treat Chapter 1’s Cursor licenses as a fixed software expense and the other as metered consumption. Without stating their claims, neither can identify the fact that would settle the disagreement, so the argument turns on confidence rather than evidence.

[BODY] Chapters 1 and 2 each ended with an explicit result rather than an opinion. Chapter 1 stated the conditions under which deployed AI is a resource the organization consumes. Chapter 2 stated the conditions under which a scaled deployment cannot be controlled without a governing apparatus.

[BODY] AI Business Economics is that body of knowledge. It is a science in a specific, limited sense: a set of claims about the business economics of consuming AI, each stating when it holds and expressed precisely enough to be checked. Here, science does not imply laboratory experiments or certainty. It means that every claim states when it applies, what it concludes, and which other claims it rests on.

[LABEL] Definition

[TERM] AI Business Economics

[BODY] The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

[BODY] A stated condition is what makes such a claim useful to a manager. Chapter 1’s result does not say that every use of AI is consumption. It says when deployed AI behaves as a resource the organization consumes, so a manager can check whether a given deployment meets those conditions before relying on the result. A claim that states when it applies can also be shown not to apply. That is what lets two managers who disagree find the fact that would settle the question.

[BODY] Chapter 1’s Cursor licenses show the check at work. Two of the result’s conditions are that the buyer’s cost extends beyond the access price and that measurement makes resource use visible. After June 2025, each request drew down a twenty-dollar monthly credit at the model provider’s rate, and further use was priced at the same rates, so both conditions held for a team on that plan. A manager who still budgeted the licenses as a fixed software expense was relying on a price the conditions said no longer described the cost. Two conditions settled what confidence could not.

[FOOTNOTE] (truell-2025-pricing) The Cursor post describing the plan change of June 16, 2025, as cited in Chapter 1.

[BODY] The book shows the results of this science in numbered panels, as Chapters 1 and 2 did. Each panel states a result in its exact form and carries an identifier. A reading in plain business language follows each panel, and the reading is enough to use the result. The identifier lets a reader who doubts a result find its full statement and its supporting claims in Appendix A. A manager needs nothing more than the panel and its reading.

[BODY] Chapter 2’s panel, THM-004, shows what such a result settles and what it leaves open. It formalizes the economic consequence of the third flow’s asymmetry. Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough. The theorem does not establish the three flows themselves. They are this book’s way of looking at a deployment, and the theorem’s conditions do not mention them.

[SECTION HEAD] 3.2 The five functions

[BODY] A manager can know that consumption drives cost and still have no forecast of next month’s use, no owner for the bill, and no record of which team used what. Knowledge alone does not change what an organization does. A practice connects knowledge to results through its own methods, roles, and standards, as clinical practice does for physiology and engineering codes do for physics.

[LABEL] Definition

[TERM] AI Operations Management

[BODY] The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

[BODY] Chapter 1 described the problem as a category error. Wherever that chapter’s conditions hold, AI Operations Management addresses the error by managing AI as a resource the organization consumes. The discipline has five functions that follow AI capacity through the organization: buying it, planning its use, recording and assigning consumption, routing it to work, and judging the value it returns. Each function is a capability an organization either has or lacks. An organization that lacks one does not stop consuming. It consumes without that function’s answer.

[BODY] The first function, sourcing, matches the AI capacity an organization buys to the requirements of its work. It determines which models and providers serve which work, and on what terms, so that the organization neither pays for capability it does not need nor deprives work of capability it requires. A company that sends every request to its most capable model, including requests a smaller model would answer just as well, is paying for capability its work does not use.

[BODY] Sourcing decides more than the provider. A requirement can be accuracy, speed, cost per request, or how easily a model connects to the systems that feed it, and different pieces of work weigh these differently. Customer messages may need a fast, inexpensive model, while a contract review may need the most capable one available. An organization that buys one model for all of its work has still made a sourcing decision, whether or not anyone made it deliberately.

[DATED] Dated: October 2025

[BODY] In October 2025, Airbnb’s chief executive, Brian Chesky, said the company’s customer-service agent was built on 13 models, from OpenAI, Google, Alibaba, and open-source providers. He said the company relied heavily on Alibaba’s Qwen models, which he called “very good” and “also fast and cheap.” He also said OpenAI’s tools for connecting its models to Airbnb’s systems were not yet ready for the company’s needs.

[FOOTNOTE] (airbnb-2025-qwen) The chief executive’s account of the models behind the agent.

[BODY] The second function is planning and budgeting, whose absence proved costly in Chapter 2’s opening case. The organization must state how much AI it expects to consume in the coming period and detect when actual consumption departs from that expectation. A budget is a commitment made in advance. When someone compares it with recorded consumption as the period runs, a deviation shows before the money is gone.

[BODY] A budget for AI differs from a budget for licenses because the quantity is not fixed when the budget is set. The plan must therefore state the drivers it assumes, such as how many people or workflows will use the system and how heavily. A change in spending can then be traced to a change in a driver, while there is still time to act on it.

[DATED] Dated: October 2026

[BODY] Pigment, a company that sells financial planning software, surveyed about 2,000 finance leaders in the United States, the United Kingdom, France, and Germany for a report released in October 2026. Eighty-three percent said consumption-based pricing had pushed their AI spending above expectations. Thirteen percent said they had stayed within budget, and the average overrun was about 27 percent. The figures describe the survey’s respondents, reported by a vendor of planning software.

[FOOTNOTE] (pigment-2026-cfo-index) Survey size, overruns, and the share within budget.

[BODY] The third function, metering and attribution, builds what Chapter 2 called the record flow. The organization must record what was consumed and assign each unit of consumption to the team, product, or purpose it served. Without that assignment, managers can see a cost but cannot trace it to the work that caused it.

[BODY] The record has two parts. Metering counts what was consumed, request by request. Attribution assigns each count to the work that caused it. An invoice priced by use supplies the first part in total. An invoice priced by seat supplies neither part. Only the organization can supply the second, because only the organization knows which team, product, or customer a request served. Without that record, no one can say whose work caused a cost, so responsibility for it can sit with several groups at once.

[DATED] Dated: February 2026

[BODY] DoiT, a company that sells cloud cost-management services, commissioned a survey of 500 finance leaders at organizations in the United States and the United Kingdom with 1,000 or more employees. Sapio Research conducted it in February 2026. Seventy-nine percent reported AI-related cost overruns in the previous twelve months. Asked who was accountable for AI spending, 55 percent named technology leadership and 53 percent named finance, so at least 8 percent named both.

[FOOTNOTE] (doit-2026-ai-spend) Survey size, overruns, and the split of accountability.

[BODY] The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to suitable capacity. These choices occur even when no one makes them deliberately. Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which. Allocation and routing make that choice deliberate by applying a rule.

[BODY] Routing and allocation are two sides of one decision. Routing sends each piece of work to suitable capacity, such as a smaller model for routine requests and a larger one for difficult cases. Allocation decides who goes first when capacity is not enough for everyone. Both need a stated rule, because a stated rule can be checked against its results and changed.

[DATED] Dated: July 2026

[BODY] In July 2026, Bloomberg reported that Microsoft had begun sending some prompts from Copilot in Excel and Outlook to its own MAI models instead of models from OpenAI and Anthropic, citing the cost of the outside models. Reports put the volume at tens of thousands of prompts a week. Routine tasks moved to the in-house models, while complex reasoning tasks could still go to the outside models. The company’s head of AI, Mustafa Suleyman, said its goal was to reduce and ultimately eliminate what it paid Anthropic.

[FOOTNOTE] (microsoft-2026-mai) The routing change, its scale, and the stated cost motive.

[BODY] The fifth function is holding value to account. Consider a constructed example in which a support team adds an AI assistant to its help desk. At the end of a quarter, the organization should be able to say whether the assistant paid for itself, identifying what it cost and returned, over which months, and against which outcome. That requires a boundary: the costs and value the evaluation counts, the period it covers, and the outcomes it measures against. The organization sets the boundary for each deployment before spending begins and names one person responsible for knowing the answer. This book calls it the value boundary.

[BODY] The boundary matters because the choice of what to count changes the return. An evaluation that counts the assistant’s subscription but not the staff time spent checking its answers reports a higher return than one that counts both. So can an evaluation that measures only its best month instead of the whole quarter. Setting the boundary in advance prevents the evaluation from choosing the version it prefers.

[DATED] Dated: October 2025, with a later update

[BODY] In October 2025, JPMorgan Chase’s chief executive, Jamie Dimon, told Bloomberg Television that the bank spent about $2 billion a year on AI and received about the same in benefits: “We have shown that for $2 billion of expense, we have about $2 billion of benefit.” When later asked for updated figures, the bank’s chief financial officer put annual AI spending closer to $700 million and called the earlier figure “a little stale.” The same report said the benefits were not yet visible in the bank’s quarterly earnings. The published accounts do not say which costs, benefits, or period either figure covered.

[FOOTNOTE] (jpmorgan-2025-dimon) The chief executive’s figures.

[FOOTNOTE] (jpmorgan-cfo-ai-spend) The later spending figure and the earnings observation.

[BODY] Figure 3.1 shows the relationship between the two layers: the science provides the foundation for the discipline’s five functions.

[FIGURE CAPTION] Figure 3.1 The two layers. AI Business Economics states conditional claims about consuming AI and records what each one rests on. AI Operations Management acts on it through five functions, all taught in Part III.

[FIGURE TEXT] AI OPERATIONS MANAGEMENT · THE DISCIPLINE

[FIGURE TEXT] AI BUSINESS ECONOMICS · THE SCIENCE

[FIGURE TEXT] Sourcing

[FIGURE TEXT] Planning and

[FIGURE TEXT] budgeting

[FIGURE TEXT] Metering and

[FIGURE TEXT] attribution

[FIGURE TEXT] Allocation

[FIGURE TEXT] and routing

[FIGURE TEXT] The value

[FIGURE TEXT] boundary

[FIGURE TEXT] Chapter 7

[FIGURE TEXT] Chapter 10

[FIGURE TEXT] Chapters 8, 9

[FIGURE TEXT] Chapter 11

[FIGURE TEXT] Chapter 12

[FIGURE TEXT] conditional claims about the economics of consuming AI

[BODY] A result about governance changes nothing until an organization builds the apparatus it describes. The science therefore depends on the discipline to put its findings into practice. The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim.

[SECTION HEAD] 3.3 Where the discipline ends

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

[FOOTNOTE] (gartner-aiops) Gartner’s definition of AIOps.

[TABLE CELL] The health and performance of IT systems

[TABLE CELL] It uses AI to watch systems. It does not govern what consuming AI costs or returns

[TABLE CELL] MLOps

[TABLE CELL] Building, deploying, and monitoring machine learning models in production

[FOOTNOTE] (kreuzberger-2023-mlops) Definition and scope of MLOps.

[TABLE CELL] The lifecycle of models an organization builds

[TABLE CELL] It ships models. It does not govern the consumption of capacity an organization buys

[TABLE CELL] FinOps

[TABLE CELL] Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams

[FOOTNOTE] (finops-what-is) The Foundation’s own definition of the practice.

[TABLE CELL] Cloud and wider technology spending

[TABLE CELL] It grew from managing cloud cost and usage. Its 2026 report quotes a practitioner saying that no one can yet answer whether AI is providing value

[TABLE CELL] Regulatory AI governance

[TABLE CELL] Ensuring that uses of AI are lawful, safe, and accountable to regulators

[TABLE CELL] Risk and compliance

[TABLE CELL] It asks whether a use is permitted, not whether it is economically managed

[BODY] Table 3.1. The four neighboring disciplines. Each manages work related to AI consumption, but none was built to govern its economics.

[BODY] FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. Their distinction concerns what each was built to do, rather than its intent. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

[FOOTNOTE] (finops-what-is) The Foundation’s definition, which names business value.

[BODY] Until Chapter 14 draws the full border, a provisional rule decides where an activity sits. An activity belongs to FinOps when it answers a question about the bill, and to AI Operations Management when it answers a Founding Question about the work the consumption served. Consider a constructed case. A company’s monthly AI invoice arrives at three times its forecast. Reconciling the invoice against the contract and charging it to cost centers answers a question about the bill, so it sits with FinOps. Tracing the increase to the workflow whose requests grew, and deciding whether that workflow’s output justifies its new cost, answers the third and fifth Founding Questions, so it sits with AI Operations Management. Both draw on the same record. Evidence that the FinOps team already traces consumption to work would move the second activity across the border.

[BODY] Regulatory governance determines whether an organization may use AI in a particular way. This book takes that determination as given and asks how the permitted use is managed.

[SECTION HEAD] 3.4 Five questions the discipline exists to answer

[BODY] Each of the five questions corresponds to one of the discipline’s functions and is answered in the chapter that teaches that function. Part III covers them in a different order, for reasons explained there.

[BODY] An organization that manages its AI consumption can answer five questions from its own records:

[BODY] Question 1. “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7.

[BODY] Question 2. “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10.

[BODY] Question 3. “Who consumed what last month, in service of which work?” This is the metering and attribution question, answered across Chapters 8 and 9.

[BODY] Question 4. “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11.

[BODY] Question 5. “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12.

[BODY] These are the Founding Questions, which an organization must answer “from its own records.” It can always produce an answer by asking the provider, estimating, or repeating the business case. Such an answer counts only when the organization keeps the evidence behind it and can check it: a provider’s figures reconciled against its own, or an estimate with its assumptions written down.

[BODY] At the end of Part I, readers do not yet have a method for answering these questions from records. Parts II through IV provide it: Part II presents the science the functions rest on, Part III builds the five functions, and Part IV turns them into an institution.

[SLOT] Craft section

[CASE TITLE] The function audit

[BODY] The function audit finds which of the five functions an organization performs for one deployment, and which the evidence does not show anyone performing. It builds on the two methods of Part I. Chapter 1’s consumption-event inventory lists what a deployment consumes, and Chapter 2’s three-flow mapping shows which flows are managed. The audit asks who does each job the discipline requires. The procedure has six steps.

[BODY] Step 1. List the deployment’s AI activities: buying capacity, choosing models, forecasting spending, recording use, assigning costs, routing work, and judging the return. Start from the consumption-event inventory.

[BODY] Step 2. For each activity, name the Founding Question it helps to answer, and assign the activity to that question’s function.

[BODY] Step 3. Assign to a neighboring discipline any activity that answers a neighbor’s question instead, using Table 3.1.

[BODY] Step 4. Mark each function as performed, partly performed, or not shown. A public record shows only what a company chose to report, so a function missing from it is not shown, not proven absent. Only an organization’s own records can show that no one performs a function.

[BODY] Step 5. For each function performed or partly performed, name who performs it. Write “not named” where the evidence names no one.

[BODY] Step 6. State the first gap to close and the record that closing it requires. Close first the gap where the largest cost goes unwatched, starting with the records the organization already holds.

[BODY] Steps 2 and 4 do most of the work. Step 2 turns a list of activities into a map of the discipline. Step 4 shows what the map leaves empty: the functions where cost can arrive with no one watching it.

[BODY] Two rules keep the assignment consistent. Choosing what capacity to buy is sourcing, even when one model serves all the work. Allocation and routing begins only when a stated rule sends different work to different capacity or decides what runs first.

[DATED] Dated: April to July 2026

[BODY] Lindy is a company of about 25 people that sells AI assistants for email and calendars. In 2026 its founder, Flo Crivello, said the company’s largest expense was the AI models it bought from Anthropic: “Like, more than payroll.” In June 2026 he announced that Lindy had moved all of its traffic to DeepSeek V4, a model from a Chinese developer, and said the move would save millions of dollars. He called the switch “100x more work than we thought.” He said he would consider returning to Anthropic’s models if their prices fell, and he expected the company to keep spending more on AI than on payroll.

[FOOTNOTE] (npr-2026-lindy) The founder’s statements on cost, payroll, and the work of switching.

[FOOTNOTE] (cnbc-2026-lindy) Company size, expected savings, and the outlook for AI spending.

[BODY] Applied to Lindy on the public record, the procedure works as follows.

[BODY] Step 1. The record shows five activities: running the assistants that customers use; choosing a model provider; knowing the total cost of the models well enough to compare it with payroll; sending all traffic to one model; and keeping the former provider under review against its price.

[BODY] Step 2. Choosing a provider and keeping it under review answer the sourcing question. Sending all traffic to one model is part of that sourcing choice: no rule sends different work to different capacity. Knowing the total cost answers part of the metering and attribution question. The record does not show that cost assigned to customers or products.

[BODY] Step 3. No activity in the record belongs to a neighbor. Whether a company may use a model from a particular developer or country is a question for regulatory governance, which this book takes as given.

[BODY] Step 4. Metering and attribution is partly performed. Planning and budgeting, allocation and routing, and holding value to account are not shown. Nothing reported shows a forecast of consumption, a rule for which work runs where, or a measure of whether each customer’s use pays for itself.

[BODY] Step 5. The founder performs sourcing in public. The record names no one for the other functions.

[BODY] Step 6. The first gap is attribution. A company whose largest cost is AI consumption needs that consumption recorded by customer account, so that it can compare each customer’s use with what that customer pays. The same record supplies the raw material for a budget and for a value boundary.

[BODY] The audit took six steps and a few public facts. It showed a company changing its entire supply of AI capacity on grounds of cost, while the public record showed no answer to three of the five Founding Questions and only part of an answer to a fourth. The switch was a sourcing decision made on cost. Whether it was made well depends on the new model’s quality and the cost of the move, which the record shows only in part. The audit shows what the switch could not tell the company: which customers its new costs belong to.

[SECTION HEAD] Chapter summary

[BODY] AI Business Economics is the science of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

[BODY] The book presents the results of the science in numbered panels. Each panel carries an identifier and a reading in plain business language, and the full statements are in Appendix A.

[BODY] AI Operations Management applies the science through five functions: sourcing, planning and budgeting, metering and attribution, allocation and routing, and holding value to account at a boundary. It begins when a model becomes a service an organization consumes. It shares boundaries with AIOps, MLOps, FinOps, and regulatory governance, while remaining a distinct discipline.

[BODY] The function audit assigns a deployment’s AI activities to the five functions or to a neighboring discipline and marks each function performed, partly performed, or not shown. Its first output is the gap to close and the record that closing it requires.

[BODY] The Founding Questions are the five questions the discipline exists to answer from an organization’s own records. By the end of Part I, readers understand the questions but do not yet have a method for answering them.

[SECTION HEAD] Key terms

[KEY TERM] AI Business Economics

[BODY] The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

[KEY TERM] AI Operations Management

[BODY] The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

[KEY TERM] Sourcing

[BODY] The function that matches the AI capacity an organization buys to the requirements of its work: which models and providers serve which work, and on what terms.

[KEY TERM] Planning and budgeting

[BODY] The function that states how much AI an organization expects to consume in a period and detects when actual consumption departs from that expectation.

[KEY TERM] Metering and attribution

[BODY] The function that records what was consumed and assigns each unit of consumption to the team, product, or purpose it served.

[KEY TERM] Allocation and routing

[BODY] The function that decides what runs first when capacity is limited and sends each piece of work to suitable capacity, by a stated rule.

[KEY TERM] Holding value to account

[BODY] The function that judges, at a value boundary set before spending begins, whether a deployment pays for itself, and names one person responsible for knowing.

[KEY TERM] Value boundary

[BODY] The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes it measures against.

[KEY TERM] Founding Questions

[BODY] The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions.

[KEY TERM] Function audit

[BODY] The six-step method for finding which of the five functions an organization performs for a deployment: list its AI activities; assign each to a function or a neighboring discipline; mark each function performed, partly performed, or not shown; name who performs each; and state the first gap to close.

[SECTION HEAD] Discussion questions and problems

[SLOT] Discussion questions

[BODY] Choose one of the five dated boxes in Section 3.2. What would the organization in it have to record, in its own systems, to answer that function’s Founding Question? Name the record and who would keep it.

[BODY] Of the four borders in Table 3.1, which is hardest to defend, and why? State what evidence would move that border.

[BODY] Restate one Founding Question in language your chief financial officer would use, preserving all its content. Then identify the part you were most tempted to omit.

[BODY] Chapter 2 diagnosed a deployment through its three flows. Match each flow to the functions in Section 3.2 that act on it, then explain which flow draws on the most functions and why.

[SLOT] Problems

[PROBLEM LABEL] P1 · Worked

[PROBLEM TITLE] An audit of the budget that ran out

[BODY] Chapter 2’s opening case described Uber’s deployment of Claude Code, which consumed the company’s annual AI budget by April 2026. Using only the facts reported there, apply the six steps of the function audit.

[BODY] Step 1. The reported activities are: buying access to Claude Code; rolling it out to roughly 5,000 engineers from December 2025; setting an annual AI budget; tracking adoption, which reached 32 percent of the engineering organization in February and 84 percent in March; and totaling spending. Reported spending ran from $150 to $250 a month for the average engineer and from $500 to $2,000 for the heaviest users. A sixth activity is a question. The president and chief operating officer said the company could not yet connect its growing use of the tool to the consumer features it was producing: “That link is not there yet.”

[FOOTNOTE] (uber-2026-budget) Rollout, adoption, and the cost per engineer.

[FOOTNOTE] (fortune-2026-uber-coo) The chief operating officer’s statement.

[BODY] Step 2. Buying access to one tool for all engineers is sourcing. Setting the annual budget is planning and budgeting. Tracking adoption and totaling spending are part of metering and attribution. The chief operating officer’s question belongs to holding value to account: it was asked, and the reporting shows no answer.

[BODY] Step 3. Nothing reported places any of these activities with a neighboring discipline.

[BODY] Step 4. Allocation and routing is not shown: nothing reported shows a rule for which work went to the tool or a limit on its heaviest users. Metering and attribution is partly performed: spending was totaled, but nothing reported assigns it to teams.

[BODY] Step 5. Engineering ran the rollout, and someone set the budget. The public account does not show anyone comparing spending with that budget before it ran out, so the audit writes “not named” against that comparison.

[BODY] Step 6. The first gap is a monthly comparison of total consumption with the plan. The spending totals already reported make that comparison possible without a new record. Recording consumption by team comes next, to show where a deviation came from.

[PROBLEM LABEL] P2 · Completion

[PROBLEM TITLE] An audit with three steps left open

[BODY] Chapter 2’s problem P3 described the Australian Government’s whole-of-government trial of Microsoft 365 Copilot, from January to June 2024. Around sixty agencies took part. Each agency nominated or approved the employees who would receive licences, and the government issued several thousand. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an evaluation, delivered it jointly with an external firm, and published the full report. Participants reported using the tool a few times a week or less and saving time when they used it. They assessed those effects themselves, and the published methodology reports no objective measure of task time or output from before the trial. Steps 1 to 3 are worked below. Complete steps 4 to 6.

[FOOTNOTE] (microsoft-2024-copilot-pricing) Per-seat pricing of the product.

[FOOTNOTE] (dta-copilot-2024) The trial, its evaluation, and the evaluation’s stated limits.

[BODY] Step 1. The activities are: buying several thousand per-seat licences; agencies choosing which employees receive them; commissioning an independent evaluation; publishing it in full; and collecting participants’ reports of their use and the time it saved.

[BODY] Step 2. Buying per-seat licences is sourcing. Choosing which employees receive a licence is allocation: it decides who gets capacity, by agency nomination. Commissioning and publishing the evaluation is holding value to account, within a boundary the evaluation stated, including its own limits. Collecting participants’ reports of their use is a partial record of consumption, part of metering and attribution, without a record of each use.

[BODY] Step 3. Any review of whether agencies were permitted to use the tool belongs to regulatory governance, and the audit sets it aside.

[BODY] Step 4. Mark each function as performed, partly performed, or not shown. Consider how per-seat pricing changes which functions the trial needed.

[BODY] Step 5. Name who performed each function, from the facts above. Write “not named” where the facts name no owner.

[BODY] Step 6. State the first gap you would close if the trial became a permanent deployment, and the record that closing it requires.

[PROBLEM LABEL] P3 · Independent

[PROBLEM TITLE] Whose decision is it

[BODY] Consider a constructed situation. A company’s FinOps lead and its new head of AI operations both claim the decision to commit to an annual volume contract with a model provider. The FinOps lead argues that the commitment is a spending decision, like reserving cloud capacity. The head of AI operations argues that it fixes which work the company can afford to run. Write one page assigning each part of the decision to one discipline, using Table 3.1 and the five functions. State the evidence that would move one part across the border.

[PROBLEM NOTE] Interleaving: question 4 requires Chapter 2’s three flows, problems P1 and P2 audit Chapter 2’s cases, and the cumulative case below requires both earlier chapters.

[SLOT] Part I cumulative case

[PROBLEM LABEL] Cumulative case · Part I

[PROBLEM TITLE] One announcement, three readings

[PROVENANCE] Dated: February 2024. The company’s own announcement, using its own figures. Only that announcement is used here.

[BODY] In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously. Klarna estimated that the assistant would improve its profit by $40 million in 2024.

[FOOTNOTE] (klarna-2024-assistant) All figures in this case are the company’s own, as announced.

[BODY] Work from this announcement alone.

[BODY] First, apply Chapter 1’s consumption-event inventory. Identify the consumption events the announcement implies and where each would be metered, marking what the announcement reports and what you assume.

[BODY] Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and cost-and-value flows, identifying the evidence behind each diagnosis.

[BODY] Third, apply each of the five Founding Questions to the announcement. For each question, state whether the announcement provides an answer from the organization’s own records and what record would be needed to answer it.

[BODY] Keep your answers. The case returns in Chapter 6.
