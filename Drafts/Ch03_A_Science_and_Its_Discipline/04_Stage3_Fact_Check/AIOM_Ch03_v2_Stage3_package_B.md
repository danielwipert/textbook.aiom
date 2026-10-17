# Fact-check package B: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file: your instructions, the required output format,
and the chapter, between BEGIN and END markers in Part 3. Read the whole file
before you begin.

**You have the chapter and nothing else, on purpose.** Another checker is reading
the sources. You get no source notes, no register, and not that checker's
output. A claim that survives only because the reader trusts a footnote they
cannot open is the failure this check exists to find.

---

## PART 1. Your task

You are reading one chapter of an academic textbook for business graduate
students, *AI Operations Management*. **Do not look anything up, and do not tell
us whether its facts are true.** Your question is different: **does this chapter
claim more than it has shown?**

### What to look for

**1. A dated box and the prose around it.** Six dated boxes report real
companies (Airbnb, Pigment, DoiT, Microsoft, JPMorgan, Lindy). For each, does
the body prose next to it, or a later worked example, draw a conclusion the box
does not support? Quote both.

**2. Quantities and their scope.** For every figure, proportion, count and range
(the FinOps survey, "nearly all", the two finance-leader surveys, the JPMorgan
figures, Uber's costs, the Klarna figures), ask what population or period it
covers, whether the sentence says so, and whether a later sentence reuses it as
though it covered something broader. Two surveys come from vendors: is that
said where it matters?

**3. The function audit's verdicts.** The craft section and problem P1 mark
functions as performed, partly performed, or not shown, from public reporting.
Find any verdict that says more than the reporting quoted in the chapter shows,
or any place where "not shown" slides into "not done".

**4. One organization, described consistently.** FinOps appears in the opening
case, Section 3.3, Table 3.1 and problem P3. Check that what the chapter says
FinOps is, was built for, and now does is the same everywhere, and that a
quotation and its paraphrase say the same thing. Do the same for Klarna in the
Part I cumulative case and for Cursor in Section 3.1.

**5. Statements about what organizations generally do.** Quote every sentence
claiming or implying how often, how commonly, or how typically organizations,
managers, or practitioners do something, including ones with no frequency word
that imply frequency through a generic plural ("companies ...", "managers
...").

**6. Constructed examples.** For each example and problem, say whether it rests
on facts the chapter established, facts it labelled as constructed, or facts it
neither established nor labelled. **Report the third kind.**

### Rules for your findings

- **Number every finding** (B-1, B-2, ...). Quote the exact sentence and give its
  section.
- **Say what a reader would wrongly conclude.** A finding with no wrong
  conclusion attached is a style note, and style is not this step.
- **Rank your findings** and name the single one you would fix if you could fix
  only one.
- **Formal statements are not prose.** A theorem identifier such as THM-004 names
  a formal result; do not judge its wording.
- **A proposed remedy is welcome and will be judged separately from the
  finding.** House rules a remedy must obey, or it is rejected while the finding
  stands: **no em dashes or en dashes** anywhere; **no hedging** ("perhaps",
  "some argue"); **no contractions**. Accurate qualification is not hedging.
  Making a sentence narrower is a good remedy; making it vaguer is not.
- **Do not comment on prose quality, structure, or teaching.** Other steps own
  those.
- **Ignore page layout.** The render has known layout defects (an overflowing
  line, a definition box split across a page, a footnote on the wrong page);
  they belong to the design step.

---

## PART 2. Required output format

One block per finding, in this form:

```
B-<n>. Rank <r>  [section]
Sentence: "<the exact sentence>"
Conflicts with: "<the other sentence, if any>"   [section]
A reader would wrongly conclude: <one sentence>
Proposed remedy: <exact replacement wording, or "none">
```

End with one line: `FIX FIRST: B-<n>`, and one sentence saying why.

---

## PART 3. The material

<<<<< BEGIN DOCUMENT 1: CHAPTER 3, AS IT WILL PRINT >>>>>

The chapter text below was extracted from the typeset PDF, so it
carries typesetting artifacts that are NOT in the text. Do not report them:

- Running heads, page numbers and small capitals set with spaces between the
  letters ("PA R T I", "D AT E D").
- Words broken at a line end, shown with a hyphen and a line break, or joined.
- Footnotes printed at the foot of each page, in the middle of the running
  text. Footnote numbers appear as plain digits after a word or a period.
- Figure 3.1 is a drawing; only its caption and labels survive extraction.
  Table 3.1 may come out as broken columns.

If a finding depends on one of these, it is an artifact. When in doubt, quote
it and say you are unsure, rather than reporting a defect.

---

PA R T I · T H E A R G U M E N T

A Science and Its Discipline
OPENING CASE

The discipline that changed its mission
D AT E D : F E B R U A R Y 2 0 2 6 . F I G U R E S A N D T H E Q U O TAT I O N C H E C K E D A G A I N S T T H E
F O U N D AT I O N ’ S R E P O R T A N D A N N O U N C E M E N T, O C T O B E R 2 0 2 6 .

In February 2026, the FinOps Foundation changed its mission state‐
ment. For years, it had described its purpose as “advancing the people
who manage the value of cloud.” The new statement replaced one word:
“advancing the people who manage the value of technology.”1
The change accompanied the Foundation’s annual survey of its practi‐
tioners, the people inside companies who manage cloud spending for a
living. The 2026 survey reached 1,192 respondents responsible for
more than $83 billion in annual cloud spending.2 Its central finding was
how far FinOps had expanded into AI spending: 98 percent of respon‐
dents now managed it, up from 31 percent two years earlier.3
FinOps was built to address a specific problem: cloud bills varied with
use and arrived after capacity had been consumed.4 The discipline de‐
veloped to make engineering, finance, and business teams jointly
accountable for that spending.5 Its practitioners later took on AI spend‐

1.

FinOps Foundation, “A One Word Change: How the FinOps Community Made Our Mission
Evolution Inevitable,” February 19, 2026, accessed October 13, 2026. The mission statement
before and after the change.
2.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 13, 2026.
Survey size and the cloud spending its respondents manage.
3.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 13, 2026.
Share of respondents managing AI spend, 2026 survey against 2024 survey.
4.

FinOps Foundation, “2024 Changes to the Definition of Cloud FinOps,” accessed October 13,
2026. Cloud consumption as variable and tracked after the fact.
5.

FinOps Foundation, “What is FinOps?,” accessed October 13, 2026. The Foundation’s definition.

1


A I O P E R AT I O N S M A N A G E M E N T

ing, and by 2026 nearly all respondents to the Foundation’s survey were
managing it.
Asked whether AI was providing value, one practitioner acknowledged
the uncertainty. The report quoted the answer: “No one can answer that
question yet.”6
The quotation expresses the gap Chapters 1 and 2 described, in the
words of someone asked to close it. When an organization pays for a
metered resource, costs accrue with use, but someone must build a way
to measure the value that use returns. FinOps is a capable neighboring
discipline that has expanded into work it was not built to govern: the
economics of an organization’s AI consumption.
That work requires both a body of knowledge about what is true and a
practice that turns that knowledge into action. This book sets out both.
Chapter 14 explains how FinOps and that practice divide the work. Until
both exist, the practitioner’s question about whether AI is providing
value remains unanswered.

3.1 The science and the practice
Managers act on claims about how their businesses work. A budget as‐
sumes that costs follow usage. A pricing negotiation assumes that the
provider has a reason to accept a lower price. A dashboard assumes that
the information it displays will change someone’s decisions. When those
claims are wrong, careful execution cannot repair the decisions built on
them.
Claims like these can remain informal, drawn from experience, rules of
thumb, or the last presentation’s slides. That knowledge is useful, but
leaving it unstated has a cost: two managers can hold opposing beliefs
about the same deployment without being able to identify where they
disagree. One might treat Chapter 1’s Cursor licenses as a fixed software
6.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 13, 2026.
Practitioner quotation as reproduced in the report.

2


A SCIENCE AND ITS DISCIPLINE

expense and the other as metered consumption. Unless they state their
claims, neither can identify the fact that would settle the disagreement,
so the argument turns on confidence rather than evidence.
Chapters 1 and 2 each ended with an explicit result rather than an opin‐
ion. Chapter 1 stated the conditions under which deployed AI is a re‐
source the organization consumes. Chapter 2 stated the conditions un‐
der which a scaled deployment cannot be controlled without a
governing apparatus.
AI Business Economics is that body of knowledge. It is a science in a
specific, limited sense: a set of claims about the business economics of
consuming AI, each stated precisely enough to be checked. Here, sci‐
ence does not imply laboratory experiments or certainty. It means that
every claim states when it applies, what it concludes, and which other
claims it rests on.
Stating when a claim applies makes it
useful to a manager. Chapter 1’s re‐
sult does not say that every use of AI
is consumption. It identifies the con‐
ditions under which deployed AI be‐
haves as a resource the organization
consumes, so a manager can check a
deployment against those conditions

DEFINITION

AI Business Economics
The science of the business
economics of consuming AI: an
ordered body of conditional
claims, each stating when it
applies, what it concludes, and
which other claims it depends on.

before relying on the result. Stating
those conditions also makes it possible to show when the claim does
not apply. Two managers who disagree can then identify the fact that
would settle the question.
Chapter 1’s Cursor licenses show this check in practice. Two of the re‐
sult’s conditions are that the buyer’s cost extends beyond the access
price and that measurement makes resource use visible. After June
2025, each request drew down a twenty-dollar monthly credit at the
model provider’s rate, and further use was priced at the same rates.

3


A I O P E R AT I O N S M A N A G E M E N T

Both conditions therefore held for a team on that plan.7 A manager who
still budgeted the licenses as a fixed software expense was treating the
access price as the full cost, even though the conditions showed other‐
wise. Checking those conditions could settle what confidence alone
could not.
The book presents the results of this science in numbered panels, as
Chapters 1 and 2 did. Each panel states a result in its exact form and
carries an identifier, followed by an explanation in plain business lan‐
guage. The panel and its explanation give a manager enough to use the
result. Readers who want to examine it further can use the identifier to
find its full statement and supporting claims in Appendix A.
Chapter 2’s panel, THM-004, shows what such a result settles and what
it leaves open. It formalizes the economic consequence of the third
flow’s asymmetry. Once a deployment reaches scale, economic control
requires a governing apparatus. Diligence from the people running the
deployment is no longer enough. The theorem does not establish the
three flows themselves. They are this book’s way of examining a deploy‐
ment, and the theorem’s conditions do not mention them.

3.2 The five functions
A manager can know that consumption drives cost and still have no
forecast of next month’s use, no owner for the bill, and no record of
which team used what. Knowledge alone does not change what an orga‐
nization does. A practice connects knowledge to results through meth‐
ods, roles, and standards, as clinical practice does for physiology and
engineering codes do for physics.
Chapter 1 described the problem as a
category error. Wherever that chap‐
ter’s conditions hold, AI Operations

7.

DEFINITION

AI Operations
Management

Michael Truell, “Clarifying Our Pricing,” Cursor, July 4, 2025, accessed July 29, 2026. The Cursor
post describing the plan change of June 16, 2025, as cited in Chapter 1.

4


A SCIENCE AND ITS DISCIPLINE

Management addresses the error by
managing AI as a resource the or‐
ganization consumes. The discipline
has five functions that follow AI ca‐
pacity through the organization:
buying it, planning its use, recording
and assigning consumption, routing

The management discipline that
acts on AI Business Economics:
the practice by which an
organization buys AI capacity,
plans its use, records and assigns
consumption, allocates capacity,
and holds that consumption to
account.

it to work, and judging the value it
returns. Each function is a capability an organization either has or lacks.
Without one, the organization continues consuming but cannot answer
the question that function addresses.
The first function, sourcing, matches the AI capacity an organization
buys to the requirements of its work. It determines which models and
providers serve which work, and on what terms, so the organization nei‐
ther pays for capability it does not need nor deprives work of capability
it requires. A company that sends every request to its most capable
model, including requests a smaller model would answer just as well, is
paying for capability that work does not need.
Sourcing involves more than choosing a provider. Requirements may in‐
clude accuracy, speed, cost per request, and ease of connection to the
systems that feed a model. Different kinds of work place different
weight on each requirement: customer messages may need a fast, inex‐
pensive model, while a contract review may need the most capable one
available. An organization that buys one model for all its work has still
made a sourcing decision, whether or not anyone made it deliberately.

5


A I O P E R AT I O N S M A N A G E M E N T

D AT E D : O C T O B E R 2 0 2 5

In October 2025, Airbnb’s chief executive, Brian Chesky, said the company’s
customer-service agent was built on 13 models from OpenAI, Google,
Alibaba, and open-source providers. He said the company relied heavily on
Alibaba’s Qwen models, which he called “very good” and “also fast and
cheap.” He also said OpenAI’s tools for connecting its models to Airbnb’s
systems were not yet ready to meet the company’s needs.8

The second function is planning and budgeting, whose absence proved
costly in Chapter 2’s opening case. The organization must state how
much AI it expects to consume in the coming period and detect when
actual consumption departs from that expectation. A budget is a com‐
mitment made in advance. Comparing it with recorded consumption
throughout the period makes deviations visible before the money runs
out.
An AI budget differs from a license budget because the quantity con‐
sumed is not fixed when the budget is set. The plan must therefore state
its assumptions about what drives consumption, including how many
people or workflows will use the system and how heavily. Managers can
then trace a change in spending to a change in one of those drivers while
there is still time to act.
D AT E D : O C T O B E R 2 0 2 6

Pigment, a company that sells financial planning software, surveyed about
2,000 finance leaders in the United States, the United Kingdom, France, and
Germany for a report released in October 2026. Eighty-three percent said
consumption-based pricing had pushed their AI spending above expecta‐
tions. Thirteen percent said they had stayed within budget, and the average
overrun was about 27 percent. These figures describe the survey’s respon‐
dents and were reported by a vendor of planning software.9

8.

“Airbnb CEO Brian Chesky says OpenAI’s tools are not ready, relies on Alibaba’s Qwen,” Fortune,
October 21, 2025, accessed October 15, 2026. The chief executive’s account of the models behind
the agent.
9.

Pigment, “CFO Index, Q3 2026,” October 7, 2026, accessed October 15, 2026. Survey size,
overruns, and the share within budget.

6


A SCIENCE AND ITS DISCIPLINE

The third function, metering and attribution, builds what Chapter 2
called the record flow. The organization must record what was con‐
sumed and assign each unit of consumption to the team, product, or
purpose it served. Without that assignment, managers can see a cost
but cannot trace it to the work that caused it.
The record has two parts: metering counts what was consumed, request
by request, while attribution assigns that consumption to the work that
caused it. A usage-based invoice supplies an aggregate count; a seatbased invoice supplies neither consumption counts nor attribution. Only
the organization can attribute consumption, because only it knows
which team, product, or customer a request served. Without that record,
no one can say whose work caused a cost, and responsibility can remain
divided among several groups.
D AT E D : F E B R U A R Y 2 0 2 6

DoiT, a company that sells cloud cost-management services, commissioned
a survey of 500 finance leaders at organizations with at least 1,000 employ‐
ees in the United States and the United Kingdom. Sapio Research conducted
it in February 2026. Seventy-nine percent reported AI-related cost overruns
in the previous twelve months. Asked who was accountable for AI spending,
55 percent named technology leadership and 53 percent named finance,
meaning at least 8 percent named both.10

The fourth function is allocation and routing. When capacity is limited,
the organization must decide what runs first and send each piece of
work to suitable capacity. These choices occur even when no one makes
them deliberately. Consider a constructed example: two workflows
share a provider account with a fixed rate limit. When their combined
demand exceeds the limit, one must wait, even though no one has de‐
cided which should take priority. Allocation and routing make that
choice deliberate by applying a rule.

10.

DoiT, “Why 79% of Enterprises Overspent on AI in 2026,” DoiT blog, 2026, accessed October
15, 2026. Survey size, overruns, and the split of accountability.

7


A I O P E R AT I O N S M A N A G E M E N T

Routing and allocation are two sides of one decision. Routing sends
each piece of work to suitable capacity, such as a smaller model for
routine requests and a larger one for difficult cases. Allocation decides
who goes first when capacity is insufficient for everyone. Both require a
stated rule that managers can check against the results and change.
D AT E D : J U LY 2 0 2 6

In July 2026, Bloomberg reported that Microsoft had begun sending some
prompts from Copilot in Excel and Outlook to its own MAI models instead of
models from OpenAI and Anthropic, citing the cost of the outside models.
Reports put the volume at tens of thousands of prompts a week. Routine
tasks moved to the in-house models, while complex reasoning tasks could
still go to the outside models. The company’s head of AI, Mustafa Suleyman,
said its goal was to reduce and ultimately eliminate its payments to
Anthropic.11

The fifth function is holding value to account. Consider a constructed
example in which a support team adds an AI assistant to its help desk.
At the end of a quarter, the organization should be able to say whether
the assistant paid for itself, identifying its costs and returns, the months
covered, and the outcome used to judge it. That requires a boundary
specifying the costs and value the evaluation counts, the period it
covers, and the outcomes against which it measures performance. The
organization sets this value boundary for each deployment before
spending begins and names one person responsible for knowing the an‐
swer.
The boundary matters because the choice of what to count changes the
reported return. An evaluation that counts the assistant’s subscription
but excludes staff time spent checking its answers reports a higher
return than one that counts both. An evaluation that measures only the
assistant’s best month rather than the whole quarter can also report a

11.

“Microsoft begins replacing third-party AI models with its own in Office apps,” Redmond
Magazine, July 9, 2026, accessed October 15, 2026. The routing change, its scale, and the stated
cost motive.

8


A SCIENCE AND ITS DISCIPLINE

higher return. Setting the boundary in advance prevents those conduct‐
ing the evaluation from choosing the version they prefer.
D AT E D : O C T O B E R 2 0 2 5 , W I T H A L AT E R U P D AT E

In October 2025, JPMorgan Chase’s chief executive, Jamie Dimon, told
Bloomberg Television that the bank spent about $2 billion a year on AI and
received about the same in benefits: “We have shown that for $2 billion of
expense, we have about $2 billion of benefit.”12 When later asked for updat‐
ed figures, the bank’s chief financial officer put annual AI spending closer to
$700 million and called the earlier figure “a little stale.” The same report
said the benefits were not yet visible in the bank’s quarterly earnings. The
published accounts do not say which costs, benefits, or period either figure
covered.13

Figure 3.1 shows the relationship between the two layers: the science
provides the foundation for the discipline’s five functions.

12.

“JPMorgan’s Dimon says AI cost savings now match money spent,” Bloomberg, via Yahoo
Finance, October 7, 2025, accessed October 15, 2026. The chief executive’s figures.
13.

“JPMorgan CEO Dimon warns customers of ‘liability transfer’ with AI,” Banking Dive, accessed
October 15, 2026. The later spending figure and the earnings observation.

9


A I O P E R AT I O N S M A N A G E M E N T

AI OPERATIONS MANAGEMENT · THE DISCIPLINE

Sourcing

Planning and
budgeting

Metering and
attribution

Allocation
and routing

The value
boundary

Chapter 7

Chapter 10

Chapters 8, 9

Chapter 11

Chapter 12

AI BUSINESS ECONOMICS · THE SCIENCE

conditional claims about the economics of consuming AI

Figure 3.1 The two layers. AI Business Economics states conditional claims about
consuming AI and records what each one rests on. AI Operations Management acts on it
through five functions, all taught in Part III.

A result about governance changes nothing until an organization builds
the apparatus it describes. The science therefore depends on the disci‐
pline to put its findings into practice. The discipline depends on the
science because careful practice cannot repair a decision built on an
incorrect claim.

3.3 Where the discipline ends
Chapter 1 set aside three related subjects: how models work, prompt
engineering, and finding uses for AI. Each has its own purpose and liter‐
ature, and each ends before AI Operations Management begins.
The first subject concerns how models work, including their architec‐
tures, training, and internal behavior. It belongs to computer science
and machine learning engineering and ends where a model becomes a
service an organization can call. AI Operations Management begins
when the organization can buy and call that service.
The second is prompt engineering, the craft of writing inputs that pro‐
duce better outputs. It improves individual uses of AI, while AI Opera‐
tions Management governs their combined consumption, cost, and val‐
ue. A better prompt can lower the cost of one request. Determining

10


A SCIENCE AND ITS DISCIPLINE

whether the organization’s requests, taken together, are worth what
they cost requires the discipline.
The third subject is finding uses for AI: deciding which business prob‐
lems it might solve. That work belongs to strategy and innovation and
ends when a use is chosen. AI Operations Management begins with buy‐
ing capacity for the chosen use and manages its consumption from then
on.
Four established disciplines overlap more directly with AI Operations
Management. Each manages an aspect of work related to AI consump‐
tion, but each lacks something needed to govern its economics. Table
3.1 compares them.

11


A I O P E R AT I O N S M A N A G E M E N T

WHAT IT
MANAGES

WHAT IT L ACKS FOR
THIS TERRITORY

The health and
performance of
IT systems

It uses AI to watch
systems. It does not
govern what
consuming AI costs or
returns

The lifecycle of
models an
organization
builds

It ships models. It does
not govern the
consumption of
capacity an
organization buys

Maximizing the business
Cloud and wider
value of technology through technology
financial accountability and spending
collaboration among
engineering, finance, and

It grew from managing
cloud cost and usage.
Its 2026 report quotes
a practitioner saying
that no one can yet
answer whether AI is
providing value

NEIGHBOR

WHAT IT IS FOR

AIOps

Applying big data and
machine learning to
automate IT operations,
including event correlation,
anomaly detection, and
causality determination14

MLOps

Building, deploying, and
monitoring machine
learning models in
production15

FinOps

business teams16
Regulatory AI
governance

Ensuring that uses of AI are
lawful, safe, and
accountable to regulators

Risk and
compliance

It asks whether a use is
permitted, not whether
it is economically
managed

Table 3.1. The four neighboring disciplines. Each manages work related to AI
consumption, but none was built to govern its economics.

FinOps is the closest neighboring discipline, making its boundary with AI
Operations Management the hardest to define. It already manages
spending, has expanded into AI, and defines its purpose in terms of

14.

Gartner, “AIOps (Artificial Intelligence for IT Operations),” Gartner Information Technology
Glossary, accessed October 1, 2026. Gartner’s definition of AIOps.
15.

Dominik Kreuzberger, Niklas Kühl, and Sebastian Hirschl, “Machine Learning Operations
(MLOps): Overview, Definition, and Architecture,” IEEE Access 11 (2023): 31866-31879. Definition
and scope of MLOps.
16.

FinOps Foundation, “What is FinOps?,” accessed October 13, 2026. The Foundation’s own
definition of the practice.

12


A SCIENCE AND ITS DISCIPLINE

maximizing the business value of technology.17 Chapter 14 explains how
the two divide the work. The distinction rests on what each was built to
do, rather than what it intends to achieve. FinOps was built to make
cloud spending accountable when bills arrived after capacity had been
used. AI Operations Management manages consumption metered by
the request and judges it against a value boundary set before spending
begins.
Until Chapter 14 defines the full boundary, a provisional rule assigns
activities to the two disciplines. An activity belongs to FinOps when it
answers a question about the bill, and to AI Operations Management
when it answers a Founding Question about the work the consumption
served. Consider a constructed case in which a company’s monthly AI
invoice is three times the forecast. Reconciling the invoice against the
contract and charging it to cost centers answers a question about the
bill, so it belongs to FinOps. Tracing the increase to the workflow whose
requests grew and deciding whether that workflow’s output justifies its
new cost answers the third and fifth Founding Questions, so it belongs
to AI Operations Management. Both activities draw on the same record.
Evidence that the FinOps team already traces consumption to work
would move the second activity across the boundary.
Regulatory governance determines whether an organization may use AI
in a particular way. This book takes that determination as given and asks
how the permitted use is managed.

3.4 Five questions the discipline exists to answer
Each of the five questions corresponds to one of the discipline’s func‐
tions and is answered in the chapter that teaches it. Part III covers the
functions in a different order, for reasons explained there.

17.

FinOps Foundation, “What is FinOps?,” accessed October 13, 2026. The Foundation’s definition,
which names business value.

13


A I O P E R AT I O N S M A N A G E M E N T

An organization that manages its AI consumption can answer five
questions from its own records:
Question 1. “Are you paying for capability you do not need, or starving
work that needs more?” This is the sourcing question, answered in
Chapter 7.
Question 2. “What do you expect the AI flow to consume next period,
and how will you know when it deviates?” This is the planning and
budgeting question, answered in Chapter 10.
Question 3. “Who consumed what last month, in service of which
work?” This is the metering and attribution question, answered across
Chapters 8 and 9.
Question 4. “When capacity is constrained, who decides what runs first,
and by what rule?” This is the allocation question, answered in Chapter
11.
Question 5. “Where, exactly, does this AI flow pay for itself, and who is
on the hook for knowing?” This is the value boundary question,
answered in Chapter 12.
These are the Founding Questions, which an organization must answer
“from its own records.” It can always produce an answer by asking the
provider, estimating, or repeating the business case. But the answer
counts only when the organization retains enough evidence to check it,
such as a provider’s figures reconciled against its own or an estimate
with its assumptions written down.
At the end of Part I, readers do not yet have a method for answering
these questions from records. Parts II through IV provide it: Part II
presents the science the functions rest on, Part III builds the five
functions, and Part IV turns them into an institution.

14


A SCIENCE AND ITS DISCIPLINE

CRAFT SECTION

The function audit
The function audit identifies which of the five functions an organization
performs for a deployment and which the available evidence does not
show anyone performing. It builds on Part I’s two earlier methods:
Chapter 1’s consumption-event inventory lists what a deployment con‐
sumes, and Chapter 2’s three-flow mapping shows which flows are
managed. The audit asks who performs each job the discipline requires,
using the following six steps.
Step 1. List the deployment’s AI activities: buying capacity, choosing
models, forecasting spending, recording use, assigning costs, routing
work, and judging the return. Start from the consumption-event invento‐
ry.
Step 2. For each activity, name the Founding Question it helps answer
and assign it to that question’s function.
Step 3. Use Table 3.1 to assign any activity that answers a neighboring
discipline’s question to that discipline.
Step 4. Mark each function as performed, partly performed, or not
shown. A public record shows only what a company chose to report. If a
function is missing from that record, the evidence does not show it; the
omission does not prove the function absent. Only an organization’s own
records can establish that no one performs a function.
Step 5. For each function performed or partly performed, name who per‐
forms it. Write “not named” where the evidence identifies no one.
Step 6. State the first gap to close and the record needed to close it.
Begin with the gap where the largest cost goes unmonitored, using the
records the organization already holds.
Steps 2 and 4 do most of the work. Step 2 turns a list of activities into a
map of the discipline, while Step 4 identifies the gaps: functions in
which costs can accrue without anyone monitoring them.

15


A I O P E R AT I O N S M A N A G E M E N T

Two rules keep the assignments consistent. Choosing what capacity to
buy is sourcing, even when one model serves all the work. The alloca‐
tion and routing function begins only when a stated rule sends different
work to different sources of capacity or decides what runs first.
D AT E D : A P R I L T O J U LY 2 0 2 6

Lindy is a company of about 25 people that sells AI assistants for email and
calendars. In 2026, its founder, Flo Crivello, said the company’s largest ex‐
pense was the AI models it bought from Anthropic: “Like, more than pay‐
roll.” In June 2026, he announced that Lindy had moved all its traffic to
DeepSeek V4, a model from a Chinese developer, and said the move would
save millions of dollars. He called the switch “100x more work than we
thought.”18 He said he would consider returning to Anthropic’s models if
their prices fell and expected the company to keep spending more on AI
than on payroll.19

Applied to Lindy using the public record, the procedure works as fol‐
lows.
Step 1. The record shows five activities: running the assistants that
customers use; choosing a model provider; knowing the total cost of the
models well enough to compare it with payroll; sending all traffic to one
model; and reviewing the former provider’s prices to judge whether to
return.
Step 2. Choosing a provider and keeping it under review answer the
sourcing question. Sending all traffic to one model is part of that sourc‐
ing choice: no rule sends different work to different sources of capacity.
Knowing the total cost answers part of the metering and attribution
question, but the record does not show how that cost is assigned to
customers or products.

18.

“American AI is expensive. Some startups are turning to cheap Chinese models,” NPR, July 15,
2026, accessed October 15, 2026. The founder’s statements on cost, payroll, and the work of
switching.
19.

“OpenAI and Anthropic face new AI reality as users shift from ‘tokenmaxxing’ to efficiency,”
CNBC, June 26, 2026, accessed October 15, 2026. Company size, expected savings, and the
outlook for AI spending.

16


A SCIENCE AND ITS DISCIPLINE

Step 3. No activity in the record belongs to a neighboring discipline.
Whether a company may use a model from a particular developer or
country is a question for regulatory governance, whose determination
this book takes as given.
Step 4. Metering and attribution is partly performed. Planning and bud‐
geting, allocation and routing, and holding value to account are not
shown. The public record contains no forecast of consumption, no rule
for which work runs where, and no measure of whether each customer’s
use pays for itself.
Step 5. The founder publicly performs the sourcing function. The record
names no one responsible for the other functions.
Step 6. The first gap is attribution. A company whose largest cost is AI
consumption needs to record that consumption by customer account so
it can compare each customer’s use with what that customer pays. The
same record provides the basis for a budget and a value boundary.
Using six steps and a few public facts, the audit showed a company
changing its entire supply of AI capacity because of cost. The public
record provided no answer to three of the five Founding Questions and
only part of an answer to a fourth. Whether the sourcing decision was
sound depends on the new model’s quality and the cost of the move,
which the record shows only in part. The audit also identifies what the
switch alone could not establish: which customers account for the
company’s new costs.

Chapter summary
AI Business Economics is the science of consuming AI: an ordered body
of conditional claims, each stating when it applies, what it concludes,
and which other claims it depends on.
The book presents the results of the science in numbered panels. Each
panel carries an identifier and is followed by an explanation in plain
business language. The full statements are in Appendix A.

17


A I O P E R AT I O N S M A N A G E M E N T

AI Operations Management applies the science through five functions:
sourcing, planning and budgeting, metering and attribution, allocation
and routing, and holding value to account within a value boundary. It
begins when a model becomes a service an organization consumes and
shares boundaries with AIOps, MLOps, FinOps, and regulatory gover‐
nance, while remaining a distinct discipline.
The function audit assigns a deployment’s AI activities to the five func‐
tions or to a neighboring discipline and marks each function as per‐
formed, partly performed, or not shown. Its first output identifies the
gap to close and the record needed to close it.
The Founding Questions are the five questions the discipline exists to
answer from an organization’s own records. By the end of Part I, readers
understand the questions but do not yet have a method for answering
them.

Key terms
AI Business Economics
The science of the business economics of consuming AI: an ordered body of
conditional claims, each stating when it applies, what it concludes, and which
other claims it depends on.

AI Operations Management
The management discipline that acts on AI Business Economics: the practice
by which an organization buys AI capacity, plans its use, records and assigns
consumption, allocates capacity, and holds that consumption to account.

Sourcing
The function that matches the AI capacity an organization buys to the
requirements of its work: which models and providers serve which work, and
on what terms.

18


A SCIENCE AND ITS DISCIPLINE

Planning and budgeting
The function that states how much AI an organization expects to consume in a
period and detects when actual consumption departs from that expectation.

Metering and attribution
The function that records what was consumed and assigns each unit of
consumption to the team, product, or purpose it served.

Allocation and routing
The function that uses a stated rule to decide what runs first when capacity is
limited and to send each piece of work to suitable capacity.

Holding value to account
The function that judges whether a deployment pays for itself within a value
boundary set before spending begins and names one person responsible for
knowing the answer.

Value boundary
The boundary within which an organization judges whether a deployment pays
for itself, defined by the costs and value it counts, the period it covers, and the
outcomes against which it measures performance.

Founding Questions
The five questions AI Operations Management exists to answer from an
organization’s own records, one for each of its five functions.

19


A I O P E R AT I O N S M A N A G E M E N T

Function audit
The six-step method for finding which of the five functions an organization
performs for a deployment: list its AI activities; assign each to a function or a
neighboring discipline; mark each function as performed, partly performed, or
not shown; name who performs each; and state the first gap to close.

Discussion questions and problems
DISCUSSION QUESTIONS

1

Choose one of the five dated boxes in Section 3.2. What would the
organization described there have to record in its own systems to answer
that function’s Founding Question? Name the record and who would keep
it.

2

Of the four borders in Table 3.1, which is hardest to defend, and why?
State what evidence would move that border.

3

Restate one Founding Question in language your chief financial officer
would use, preserving all its content. Then identify the part you were most
tempted to omit.

4

Chapter 2 diagnosed a deployment through its three flows. Match each
flow to the functions in Section 3.2 that act on it, then explain which flow
draws on the most functions and why.

PROBLEMS
P1 · WORKED

An audit of the budget that ran out
Chapter 2’s opening case described Uber’s deployment of Claude Code, which
consumed the company’s annual AI budget by April 2026. Using only the facts
reported there, apply the six steps of the function audit.
Step 1. The reported activities are buying access to Claude Code; rolling it out
to roughly 5,000 engineers from December 2025; setting an annual AI budget;
tracking adoption, which reached 32 percent of the engineering organization in

20


A SCIENCE AND ITS DISCIPLINE

February and 84 percent in March; and totaling spending. Reported spending
ranged from $150 to $250 a month for the average engineer and from $500 to
$2,000 for the heaviest users.20 A sixth activity was asking about value. The
president and chief operating officer said the company could not yet connect its
growing use of the tool to the consumer features it was producing: “That link is
not there yet.”21
Step 2. Buying access to one tool for all engineers is sourcing, and setting the
annual budget is planning and budgeting. Tracking adoption and totaling
spending are part of metering and attribution. The chief operating officer’s
question belongs to holding value to account, though the reporting provides no
answer.
Step 3. The reporting does not place any of these activities within a neighboring
discipline.
Step 4. Allocation and routing is not shown: the reporting describes no rule for
which work went to the tool or any limit on its heaviest users. Metering and
attribution is partly performed: spending was totaled, but the reporting does
not assign it to teams.
Step 5. Engineering ran the rollout, and someone set the budget. The public
account does not identify anyone who compared spending with that budget
before it ran out, so the audit records “not named” for that task.
Step 6. The first gap is a monthly comparison of total consumption with the
plan. The reported spending totals already make that comparison possible
without a new record. Recording consumption by team comes next, to show
where a deviation originated.
P2 · COMPLETION

An audit with three steps left open
Chapter 2’s problem P3 described the Australian Government’s whole-ofgovernment trial of Microsoft 365 Copilot, which ran from January to June
2024. Around sixty agencies took part. Each agency nominated or approved the

20.

Janakiram MSV, “Uber burns its 2026 AI budget in four months on Claude Code,” Forbes, May
17, 2026, accessed August 30, 2026. Rollout, adoption, and the cost per engineer.
21.

“Uber burned through its entire 2026 AI budget in four months,” Fortune, May 26, 2026,
accessed August 30, 2026. The chief operating officer’s statement.

21


A I O P E R AT I O N S M A N A G E M E N T

employees who would receive licenses, and the government issued several
thousand. The product was priced per seat rather than by unit of use.22 The
Digital Transformation Agency commissioned an evaluation, delivered it jointly
with an external firm, and published the full report. Participants reported using
the tool a few times a week or less and saving time when they used it. These
were their own assessments, and the published methodology reports no
objective measure of task time or output before the trial.23 Steps 1 to 3 are
worked through below. Complete Steps 4 to 6.
Step 1. The activities are buying several thousand per-seat licenses; agencies
choosing which employees receive them; commissioning an independent evalu‐
ation; publishing it in full; and collecting participants’ reports of their use and
the time it saved.
Step 2. Buying per-seat licenses is sourcing. Choosing which employees receive
a license is allocation: agency nomination determines who gets capacity. Com‐
missioning and publishing the evaluation is holding value to account within the
boundary the evaluation stated, including its limits. Collecting participants’
reports of their use provides a partial record of consumption and is part of
metering and attribution, though it does not record each use.
Step 3. Any review of whether agencies were permitted to use the tool belongs
to regulatory governance, and the audit sets it aside.
Step 4. Mark each function as performed, partly performed, or not shown. Con‐
sider how per-seat pricing changes which functions the trial needed.
Step 5. Use the facts above to name who performed each function. Write “not
named” where the facts identify no owner.
Step 6. State the first gap you would close if the trial became a permanent
deployment and the record needed to close it.

22.

Microsoft, “Expanding Copilot for Microsoft 365 to businesses of all sizes,” Microsoft 365 Blog,
January 15, 2024. Per-seat pricing of the product.
23.

Digital Transformation Agency and Nous Group, “Evaluation of the whole-of-government trial of
Microsoft 365 Copilot,” Australian Government Digital Transformation Agency, 2024. The trial, its
evaluation, and the evaluation’s stated limits.

22


A SCIENCE AND ITS DISCIPLINE

P3 · INDEPENDENT

Whose decision is it
Consider a constructed situation. A company’s FinOps lead and its new head of
AI operations both claim the right to decide whether to commit to an annual
volume contract with a model provider. The FinOps lead argues that the com‐
mitment is a spending decision, like reserving cloud capacity. The head of AI
operations argues that it determines which work the company can afford to run.
Write one page assigning each part of the decision to one discipline, using Table
3.1 and the five functions. State the evidence that would move one part across
the boundary.
Interleaving: question 4 requires Chapter 2’s three flows, problems P1 and P2 audit
Chapter 2’s cases, and the cumulative case below requires both earlier chapters.
PA R T I C U M U L AT I V E C A S E
C U M U L AT I V E C A S E · PA R T I

One announcement, three readings
D AT E D : F E B R U A R Y 2 0 2 4 . T H E C O M PA N Y ’ S O W N A N N O U N C E M E N T, U S I N G I T S O W N
F I G U R E S . O N LY T H AT A N N O U N C E M E N T I S U S E D H E R E .

In February 2024, the payments company Klarna announced results from the
first month of an AI assistant powered by OpenAI. The company reported that
the assistant had handled 2.3 million conversations, accounting for two-thirds
of its customer-service chats. It estimated that the assistant was doing the
work of 700 full-time agents. Klarna also reported that customers resolved
their questions in under two minutes during that month, compared with eleven
minutes previously. It estimated that the assistant would improve its profit by
$40 million in 2024.24
Work from this announcement alone.
First, apply Chapter 1’s consumption-event inventory. Identify the consumption
events the announcement implies and where each would be metered. Distin‐
guish what the announcement reports from what you assume.

24.

Klarna, “Klarna AI assistant handles two-thirds of customer service chats in its first month,”
February 27, 2024, accessed October 13, 2026. All figures in this case are the company’s own, as
announced.

23


A I O P E R AT I O N S M A N A G E M E N T

Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and
cost-and-value flows, identifying the evidence behind each diagnosis.
Third, apply each of the five Founding Questions to the announcement. For each
question, state whether the announcement provides an answer from the orga‐
nization’s own records and what record would be needed to answer it.
Keep your answers. The case returns in Chapter 6.

24

<<<<< END DOCUMENT 1 >>>>>

END OF PACKAGE. Now produce your findings in the format given in Part 2.
