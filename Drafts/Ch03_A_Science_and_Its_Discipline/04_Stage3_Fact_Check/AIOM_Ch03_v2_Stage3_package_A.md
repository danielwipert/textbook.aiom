# Fact-check package A: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file. Everything you need is inside it: your
instructions, the required output format, and the material, between BEGIN and
END markers in Part 3. Read the whole file before you begin.

---

## PART 1. Your task

You are fact checking one chapter of an academic textbook for business graduate
students, *AI Operations Management*, before it is typeset for good. Work to the
standard of a university press fact checker: a claim is verified when you have
seen the document that supports it, not when it sounds right.

**Your first line must say whether you have live web access in this session.**
If you do not, say so. **Do not simulate a lookup you cannot perform.** If you
cannot open a document, the answer is CANNOT CONFIRM, never a summary from
memory presented as a check.

### What you have

- **Document 1** is the chapter as it will print, as text extracted from the PDF.
- **Document 2** is the source packet: every passage carrying a citation, the
  source key it cites, and the register entry behind each key with its note
  verbatim. A note marked **UNVERIFIED, GRADE C** means nobody on this project
  has read that source: it was found by web search only. A note recording an
  earlier external check means that source was read then, against an earlier
  version of the sentence.

The packet's header says that 14 rulings are in force and that a ruled-form
check fails. That is expected: the chapter was redesigned and its author
rewrote it, so several earlier rulings no longer match the text word for word.
Your findings are what they will be re-ruled against.

### Your task, in priority order

For every item, give a verdict: **VERIFIED**, **CONTRADICTED**, **PARTLY
SUPPORTED** (say which part fails), or **CANNOT CONFIRM** (say why: no access,
paywall, page gone). Quote the source language you relied on and give the
exact URL you read it at.

**1. The five dated boxes and the Lindy box, never read by anyone (the
chapter's largest exposure).** Each is Grade C. Verify every figure, date,
name and quotation separately, against the primary where one exists:

- **Airbnb (October 2025)**: the customer-service agent built on **13 models**
  from OpenAI, Google, Alibaba and open-source providers; heavy reliance on
  Alibaba's **Qwen**, called **"very good"** and **"also fast and cheap"**; OpenAI's
  tools for connecting its models to Airbnb's systems **not yet ready**. Name the
  interview and its date.
- **Pigment (October 2026)**: about **2,000** finance leaders in the US, UK,
  France and Germany; **83 percent** said consumption-based pricing pushed AI
  spending above expectations; **13 percent** stayed within budget; average
  overrun about **27 percent**; the report's release date.
- **DoiT (February 2026)**: commissioned by DoiT, conducted by **Sapio
  Research** in February 2026; **500** finance leaders at US and UK organizations
  with **1,000 or more** employees; **79 percent** reported AI-related overruns in
  the previous twelve months; accountability named as technology leadership
  **55 percent** and finance **53 percent**. The chapter infers "at least 8
  percent named both": confirm that the question allowed more than one answer.
- **Microsoft (July 2026)**: Bloomberg reported that Microsoft began sending
  some Copilot prompts in **Excel and Outlook** to its own **MAI** models instead
  of OpenAI and Anthropic models, **citing cost**; **tens of thousands of prompts
  a week**; routine tasks moved, complex reasoning could still go outside;
  **Mustafa Suleyman** said the goal was to reduce and ultimately eliminate its
  payments to Anthropic. Find the Bloomberg report if you can.
- **JPMorgan (October 2025, with a later update)**: **Jamie Dimon** on Bloomberg
  Television, about **$2 billion** a year spent and about the same in benefit,
  quotation **"We have shown that for $2 billion of expense, we have about $2
  billion of benefit."**; then the **chief financial officer** putting annual AI
  spending **closer to $700 million**, calling the earlier figure **"a little
  stale"**, and the report saying the benefits were **not yet visible in quarterly
  earnings**. Name the CFO and the date of that later report. If the cited
  article does not carry the later update, say so plainly.
- **Lindy (April to July 2026)**: about **25 people**; **Flo Crivello**; the largest
  expense was Anthropic's models, **"Like, more than payroll."**; in **June 2026**
  all traffic moved to **DeepSeek V4**; the move would **save millions**; **"100x
  more work than we thought."**; open to returning if prices fell; expects to keep
  spending more on AI than on payroll. Say which outlet carries each item.

**2. Sentences rewritten since their last check.** Each of these was verified
against its source on 2026-10-13 in different words. Confirm the new words are
still supported, and say if the rewrite claims more:

- Opening case: "Its central finding was how far FinOps had expanded into AI
  spending: 98 percent of respondents now managed it, up from 31 percent two
  years earlier." Does the report make AI spending its central finding?
- Opening case: "FinOps was built to address a specific problem: cloud bills
  varied with use and arrived after capacity had been consumed."
- Opening case: "by 2026 nearly all respondents to the Foundation's survey were
  managing it."
- Section 3.1, the Cursor paragraph: "After June 2025, each request drew down a
  twenty-dollar monthly credit at the model provider's rate, and further use was
  priced at the same rates." Check against `truell-2025-pricing`; its note
  records what the post does and does not establish about billing.

**3. Carried sources, restated in this chapter.** Uber (C13), the Australian
Copilot trial (C14) and Klarna (C15) were verified in earlier checks. Confirm
only that this chapter's sentences match their sources; do not re-verify what
the notes already record.

**4. Table 3.1** (Part 1a of the packet): confirm the three cited cells still
match their sources as recorded.

**5. Anything else.** Name any sentence in Document 1 that states a fact about
the outside world (a date, a figure, a named organization's action, how often
organizations do something) and carries **no** citation. Do not report
sentences that are plainly the book's own argument or a labelled constructed
example.

### Rules for your findings

- **Number every finding** (A-1, A-2, ...).
- **Separate "the source contradicts this" from "I could not reach the source".**
  They get different rulings.
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

Start with one line: `WEB ACCESS: yes` or `WEB ACCESS: no`.

Then one block per finding, in this form:

```
A-<n>. <VERDICT>  [packet item, e.g. C2 or T1]
Sentence: "<the exact sentence from Document 1>"
Checked against: <document title, URL, date read>
Source says: "<quoted source language>"
Finding: <one or two sentences>
Proposed remedy: <exact replacement wording, or "none">
```

Report every priority item, including the ones you verify: a VERIFIED verdict
with its quotation is a result, and silence is not. End with a short list
headed `NOT CHECKED` naming anything in priorities 1 to 4 you could not reach.

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

<<<<< BEGIN DOCUMENT 2: SOURCE PACKET >>>>>

# Chapter 3, Stage 3. Claim inventory and source packet

Generated from the live text by `factcheck_packet.py` at the repo root.
Stage 3 is STRUCTURALLY external: no source host is reachable from the
Claude environment, verified 2026-08-06 against six of them, so nothing
below is a verification. It is the material a checker needs.

LIVE TEXT      `Drafts/Ch03_A_Science_and_Its_Discipline/00_Stage0_Draft/AIOM_Ch03_draft.html`
RENDER         `Drafts/Ch03_A_Science_and_Its_Discipline/04_Stage3_Fact_Check/AIOM_Ch03_v2_Stage3_render.pdf`, FAILING a print gate on this file: overflow: [(6, 420.0, ' ')]; 1 definition callout(s) split across a page break; run place.py on this chapter.

WHAT THIS IS. Every passage carrying a citation marker, with the keys it
cites and the register entry behind each key. The register note is
reproduced in full because it carries the verification history and, for
findings already ruled, the condition that would reverse the ruling.

WHAT A CHECKER SHOULD NOT RE-RAISE. This chapter carries 14 ruling(s) already
made and still in force, recorded in `AIOM_Claim_Ledger.md` and in the
register notes below. A checker who reaches one should say whether the
condition named in the note is now met, not restate the finding.

MECHANICAL CHECKS ALREADY RUN, so they need not be repeated:

  Register closure    20 keys defined, 18 cited. 2 orphan(s), 0 dangling.
                      orphans: gartner-aiops, kreuzberger-2023-mlops
  Citation markers    15 cited passages, every marker resolving to a key.
  Footnote build      24 footnote(s) generated. Gate 8 checks each sits on its calling page; its verdict on the shipped render is on the RENDER line above, where it is measured rather than assumed.
  Ruled-form check    14 ruling(s) in force for Ch03: 12 required, 16 forbidden,
                      1 by reading. `claimcheck.py` reports FAIL.

---

## Part 1. Cited passages, in document order

### C1

CLAIM TEXT AS IT STANDS

> In February 2026, the FinOps Foundation changed its mission statement. For years, it had described its purpose as “advancing the people who manage the value of cloud.” The new statement replaced one word: “advancing the people who manage the value of technology.”

CITES: `finops-2026-mission`

IN-CHAPTER GLOSS: The mission statement before and after the change.

### C2

CLAIM TEXT AS IT STANDS

> The change accompanied the Foundation’s annual survey of its practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 respondents responsible for more than $83 billion in annual cloud spending. Its central finding was how far FinOps had expanded into AI spending: 98 percent of respondents now managed it, up from 31 percent two years earlier.

CITES: `finops-2026-state`, `finops-2026-state`

IN-CHAPTER GLOSS: Survey size and the cloud spending its respondents manage.

### C3

CLAIM TEXT AS IT STANDS

> FinOps was built to address a specific problem: cloud bills varied with use and arrived after capacity had been consumed. The discipline developed to make engineering, finance, and business teams jointly accountable for that spending. Its practitioners later took on AI spending, and by 2026 nearly all respondents to the Foundation’s survey were managing it.

CITES: `finops-definition-2024`, `finops-what-is`

IN-CHAPTER GLOSS: Cloud consumption as variable and tracked after the fact.

### C4

CLAIM TEXT AS IT STANDS

> Asked whether AI was providing value, one practitioner acknowledged the uncertainty. The report quoted the answer: “No one can answer that question yet.”

CITES: `finops-2026-state`

IN-CHAPTER GLOSS: Practitioner quotation as reproduced in the report.

### C5

CLAIM TEXT AS IT STANDS

> Chapter 1’s Cursor licenses show this check in practice. Two of the result’s conditions are that the buyer’s cost extends beyond the access price and that measurement makes resource use visible. After June 2025, each request drew down a twenty-dollar monthly credit at the model provider’s rate, and further use was priced at the same rates. Both conditions therefore held for a team on that plan. A manager who still budgeted the licenses as a fixed software expense was treating the access price as the full cost, even though the conditions showed otherwise. Checking those conditions could settle what confidence alone could not.

CITES: `truell-2025-pricing`

IN-CHAPTER GLOSS: The Cursor post describing the plan change of June 16, 2025, as cited in Chapter 1.

### C6

CLAIM TEXT AS IT STANDS

> In October 2025, Airbnb’s chief executive, Brian Chesky, said the company’s customer-service agent was built on 13 models from OpenAI, Google, Alibaba, and open-source providers. He said the company relied heavily on Alibaba’s Qwen models, which he called “very good” and “also fast and cheap.” He also said OpenAI’s tools for connecting its models to Airbnb’s systems were not yet ready to meet the company’s needs.

CITES: `airbnb-2025-qwen`

IN-CHAPTER GLOSS: The chief executive’s account of the models behind the agent.

### C7

CLAIM TEXT AS IT STANDS

> Pigment, a company that sells financial planning software, surveyed about 2,000 finance leaders in the United States, the United Kingdom, France, and Germany for a report released in October 2026. Eighty-three percent said consumption-based pricing had pushed their AI spending above expectations. Thirteen percent said they had stayed within budget, and the average overrun was about 27 percent. These figures describe the survey’s respondents and were reported by a vendor of planning software.

CITES: `pigment-2026-cfo-index`

IN-CHAPTER GLOSS: Survey size, overruns, and the share within budget.

### C8

CLAIM TEXT AS IT STANDS

> DoiT, a company that sells cloud cost-management services, commissioned a survey of 500 finance leaders at organizations with at least 1,000 employees in the United States and the United Kingdom. Sapio Research conducted it in February 2026. Seventy-nine percent reported AI-related cost overruns in the previous twelve months. Asked who was accountable for AI spending, 55 percent named technology leadership and 53 percent named finance, meaning at least 8 percent named both.

CITES: `doit-2026-ai-spend`

IN-CHAPTER GLOSS: Survey size, overruns, and the split of accountability.

### C9

CLAIM TEXT AS IT STANDS

> In July 2026, Bloomberg reported that Microsoft had begun sending some prompts from Copilot in Excel and Outlook to its own MAI models instead of models from OpenAI and Anthropic, citing the cost of the outside models. Reports put the volume at tens of thousands of prompts a week. Routine tasks moved to the in-house models, while complex reasoning tasks could still go to the outside models. The company’s head of AI, Mustafa Suleyman, said its goal was to reduce and ultimately eliminate its payments to Anthropic.

CITES: `microsoft-2026-mai`

IN-CHAPTER GLOSS: The routing change, its scale, and the stated cost motive.

### C10

CLAIM TEXT AS IT STANDS

> In October 2025, JPMorgan Chase’s chief executive, Jamie Dimon, told Bloomberg Television that the bank spent about $2 billion a year on AI and received about the same in benefits: “We have shown that for $2 billion of expense, we have about $2 billion of benefit.” When later asked for updated figures, the bank’s chief financial officer put annual AI spending closer to $700 million and called the earlier figure “a little stale.” The same report said the benefits were not yet visible in the bank’s quarterly earnings. The published accounts do not say which costs, benefits, or period either figure covered.

CITES: `jpmorgan-2025-dimon`, `jpmorgan-cfo-ai-spend`

IN-CHAPTER GLOSS: The chief executive’s figures.

### C11

CLAIM TEXT AS IT STANDS

> FinOps is the closest neighboring discipline, making its boundary with AI Operations Management the hardest to define. It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology. Chapter 14 explains how the two divide the work. The distinction rests on what each was built to do, rather than what it intends to achieve. FinOps was built to make cloud spending accountable when bills arrived after capacity had been used. AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins.

CITES: `finops-what-is`

IN-CHAPTER GLOSS: The Foundation’s definition, which names business value.

### C12

CLAIM TEXT AS IT STANDS

> Lindy is a company of about 25 people that sells AI assistants for email and calendars. In 2026, its founder, Flo Crivello, said the company’s largest expense was the AI models it bought from Anthropic: “Like, more than payroll.” In June 2026, he announced that Lindy had moved all its traffic to DeepSeek V4, a model from a Chinese developer, and said the move would save millions of dollars. He called the switch “100x more work than we thought.” He said he would consider returning to Anthropic’s models if their prices fell and expected the company to keep spending more on AI than on payroll.

CITES: `npr-2026-lindy`, `cnbc-2026-lindy`

IN-CHAPTER GLOSS: The founder’s statements on cost, payroll, and the work of switching.

### C13

CLAIM TEXT AS IT STANDS

> Step 1. The reported activities are buying access to Claude Code; rolling it out to roughly 5,000 engineers from December 2025; setting an annual AI budget; tracking adoption, which reached 32 percent of the engineering organization in February and 84 percent in March; and totaling spending. Reported spending ranged from $150 to $250 a month for the average engineer and from $500 to $2,000 for the heaviest users. A sixth activity was asking about value. The president and chief operating officer said the company could not yet connect its growing use of the tool to the consumer features it was producing: “That link is not there yet.”

CITES: `uber-2026-budget`, `fortune-2026-uber-coo`

IN-CHAPTER GLOSS: Rollout, adoption, and the cost per engineer.

### C14

CLAIM TEXT AS IT STANDS

> Chapter 2’s problem P3 described the Australian Government’s whole-of-government trial of Microsoft 365 Copilot, which ran from January to June 2024. Around sixty agencies took part. Each agency nominated or approved the employees who would receive licenses, and the government issued several thousand. The product was priced per seat rather than by unit of use. The Digital Transformation Agency commissioned an evaluation, delivered it jointly with an external firm, and published the full report. Participants reported using the tool a few times a week or less and saving time when they used it. These were their own assessments, and the published methodology reports no objective measure of task time or output before the trial. Steps 1 to 3 are worked through below. Complete Steps 4 to 6.

CITES: `microsoft-2024-copilot-pricing`, `dta-copilot-2024`

IN-CHAPTER GLOSS: Per-seat pricing of the product.

### C15

CLAIM TEXT AS IT STANDS

> In February 2024, the payments company Klarna announced results from the first month of an AI assistant powered by OpenAI. The company reported that the assistant had handled 2.3 million conversations, accounting for two-thirds of its customer-service chats. It estimated that the assistant was doing the work of 700 full-time agents. Klarna also reported that customers resolved their questions in under two minutes during that month, compared with eleven minutes previously. It estimated that the assistant would improve its profit by $40 million in 2024.

CITES: `klarna-2024-assistant`

IN-CHAPTER GLOSS: All figures in this case are the company’s own, as announced.

---

## Part 2. Register entries, verbatim

### `airbnb-2025-qwen`

- **type**: news
- **title**: Airbnb CEO Brian Chesky says OpenAI’s tools are not ready, relies on Alibaba’s Qwen
- **container**: Fortune
- **date**: 2025-10-21
- **url**: https://fortune.com/2025/10/21/brian-chesky-openai-tools-not-ready
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage (Fortune, South China Morning Post, Bloomberg interview behind both) gives: the agent is built on 13 models from OpenAI, Alibaba, Google and open-source providers; Airbnb relies heavily on Qwen, which Chesky called ‘very good’ and ‘also fast and cheap’; OpenAI’s integration tools were not ‘quite ready’. Check A must confirm each, the date, and the exact quotations; the Bloomberg interview is the primary. The chapter does not use the later House inquiry.


### `cnbc-2026-lindy`

- **type**: news
- **title**: OpenAI and Anthropic face new AI reality as users shift from ‘tokenmaxxing’ to efficiency
- **container**: CNBC
- **date**: 2026-06-26
- **url**: https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: Lindy is a roughly 25-person company; Crivello expects the switch to save millions within months; he still expects to spend more on AI than on payroll. Check A must confirm each.


### `doit-2026-ai-spend`

- **type**: web
- **authors**: {"org": "DoiT"}
- **title**: Why 79% of Enterprises Overspent on AI in 2026
- **container**: DoiT blog
- **date**: 2026
- **url**: https://www.doit.com/blog/ai-spending-survey
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: commissioned by DoiT, conducted by Sapio Research, February 2026; 500 finance leaders at US and UK organizations with 1,000 or more employees; 79 percent reported AI-related cost overruns in the previous twelve months; accountability split, technology 55 percent and finance 53 percent. Check A must confirm each, and the survey dates. A 36 percent ‘unclear attribution’ figure seen in secondary coverage is NOT used: no primary was found for it.


### `dta-copilot-2024`

- **type**: report
- **authors**: {"org": "Digital Transformation Agency"}, {"org": "Nous Group"}
- **title**: Evaluation of the whole-of-government trial of Microsoft 365 Copilot
- **container**: Australian Government Digital Transformation Agency
- **date**: 2024
- **url**: https://www.digital.gov.au/initiatives/copilot-trial/microsoft-365-copilot-evaluation-report-full
- **perishable**: False
- **upgrade**: The published evaluation itself, which the Digital Transformation Agency released in full and which nobody on this project has read.

NOTE, verbatim:

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE REPORT HAS NOW BEEN READ AND THE GRADE C IS DISCHARGED. Of the four things this note called load bearing, TWO HELD AND TWO FAILED. Held: the licence is priced per seat rather than by unit of use (now also carried by microsoft-2024-copilot-pricing, since this report does not state the contrast), and agencies nominated participants (the chapter now says ’nominated or approved’, because Appendix B records a self-nomination route as well). FAILED 1, THE EVALUATION IS NOT INDEPENDENT: Appendix B says it was ’jointly delivered by the DTA and Nous’. This note asked Stage 3 to record whether Nous appears on the face of the report, and it does. The word ’independent’ is cut from BOTH sentences that carried it, which sit far apart, and FQ5 is amended in the claim ledger because one of them was its REQUIRED text. FAILED 2, THE REPORT NAMES FIVE LIMITS, NOT TWO: representativeness, positive selection bias, inconsistent rollout, evaluation fatigue and self-assessment. Only self-assessment was one of the chapter’s two. THE ABSENCE OF A PRE-TRIAL WORK BASELINE IS NOT ONE OF THE REPORT’S LIMITATIONS: it ran a pre-use survey that baselined sentiment and confidence rather than task time or output. The chapter was presenting its own inference as the report’s statement, which is Chapter 1’s FC9 shape. The sentence is split so the report’s finding and the chapter’s inference are visibly different things. THE COUNTS WERE RIGHT TO LEAVE LOOSE. Around sixty agencies holds, and the official record reports 7,600 staff, 5,765 licences and 7,769 licences in three places, so ’several thousand’ should NOT be replaced by a precise count until the agency resolves its own discrepancy. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch on 2026-08-22 for problem P3, after Dan ruled at Chapter 2 Stage 1 that competency C2 needs a mapping exercise on a cited real deployment and that the constructed insurer would not serve. Claude read search result summaries and did NOT read the evaluation, any article about it, or any agency page: WebFetch and curl are blocked by the container egress proxy. Grade C. THE SECONDARY COVERAGE DISAGREES WITH ITSELF ON EVERY COUNT, which is why the problem states none of them precisely. Agency counts of 56, almost 60 and more than 60 all appear; participant and licence counts of more than 5,000, 5,765, nearly 6,000 and 7,600 all appear. The problem says ’around sixty agencies’ and ’several thousand licences’ deliberately, so that a corrected count does not invalidate the exercise. WHAT IS LOAD BEARING IS NOT A COUNT. The problem rests on four things: that the licence is priced per seat rather than by unit of use, that agencies nominated their own participants, that an independent evaluation was commissioned and published, and that the evaluation stated both that participants self-assessed the effects and that no pre-trial measure of the work existed. STAGE 3 MUST CONFIRM THOSE FOUR AND MAY LEAVE THE COUNTS ALONE. It should also settle the publication date, which is recorded here as the year only because no source read gave a day, and record whether the evaluation is attributed to Nous Group on its face, since secondary coverage names that firm as the evaluator. ACCESS DATE NOT REQUIRED: a fixed published report, the same convention applied to mit-nanda-2025.


### `finops-2026-mission`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: A One Word Change: How the FinOps Community Made Our Mission Evolution Inevitable
- **date**: 2026-02-19
- **url**: https://www.finops.org/insights/mission-update/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). REPLACES the Yahoo Finance syndication cited at Stage 0 (A-4): the Foundation’s own announcement is the better source. VERIFIED: February 2026, a one-word change from ‘advancing the people who manage the value of cloud’ to ‘advancing the people who manage the value of technology’, released with the State of FinOps 2026 figures. RULING, Dan, sitting 3, A-1 and B-30: the chapter quoted the wording without ‘the value of’; both statements are now quoted exactly. REVERSES-IF: the Foundation’s page is changed to give a different wording.


### `finops-2026-state`

- **type**: report
- **authors**: {"org": "FinOps Foundation"}
- **title**: State of FinOps 2026
- **date**: 2026-02-19
- **url**: https://data.finops.org/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-2, A-5): ‘1,192 respondents’, ‘$83bn+ in annual cloud spend’, and ‘98% of respondents now manage AI spend (up from 63% in 2025 and 31% in 2024)’, so 31 percent is the 2024 figure for the same measure. The quotation is in the report itself: ‘As one practitioner framed it: “Is your AI providing value? No one can answer that question yet.”’ RULINGS, Dan, sitting 3: A-3 the sentence now reads ‘Its central finding concerned the expansion of FinOps into AI spending.’ (the report makes AI central but does not state the discipline’s history); B-10 ‘nearly all of the survey’s respondents’, and the gloss ‘Share of respondents’; B-9 one practitioner’s remark is not generalized to practitioners; B-2 the provenance banner now says the figures were checked against the report. REVERSES-IF: the report is revised, or a later reading finds the quotation outside the report body.


### `finops-definition-2024`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: 2024 Changes to the Definition of Cloud FinOps
- **url**: https://www.finops.org/insights/changes-to-finops-definition/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: ADDED AT SITTING 3 (A-6). Found and read by external check A with live web access: the page describes cloud’s ‘variable consumption tracked after the fact’. RULING, Dan: the opening case’s ‘cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it’ had no source for its first half and now reads ‘cloud consumption varied with use, and the bills arrived after capacity had been used.’ Section 3.5 matches (B-12). REVERSES-IF: a source describing provisioning by code is cited.


### `finops-what-is`

- **type**: web
- **authors**: {"org": "FinOps Foundation"}
- **title**: What is FinOps?
- **url**: https://www.finops.org/introduction/what-is-finops/
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-7): ‘FinOps is an operational framework and cultural practice which maximizes the business value of technology ... and creates financial accountability through collaboration between engineering, finance, and business teams.’ The page names AI among technology categories (A-8) and describes ‘a strong heritage in managing cloud cost and usage’ (A-13). RULINGS, Dan, sitting 3: B-11 Table 3.1’s purpose cell now carries the value purpose as well as accountability; A-13 the table’s ‘built around cloud billing’ is now ‘grew from managing cloud cost and usage’; A-8 ‘the hardest to define’ is the book’s judgment and stays. REVERSES-IF: the Foundation changes its definition.


### `fortune-2026-uber-coo`

- **type**: news
- **title**: Uber burned through its entire 2026 AI budget in four months
- **container**: Fortune
- **date**: 2026-05-26
- **url**: https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/
- **perishable**: True
- **accessed**: 2026-08-30
- **upgrade**: Taken 2026-08-30. See rapidresponse-2026-macdonald.

NOTE, verbatim:

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. CHECK A OPENED THE ARTICLE AND THE FIRST-PARTY TRANSCRIPT BEHIND IT. The quotation ’That link is not there yet’ is confirmed in both, and the remark refers to Claude Code specifically rather than to AI spending generally, which the Stage 6 copy edit had narrowed it to and which was flagged for this step as a risk. It is cleared. THE UPGRADE THIS ENTRY ASKED FOR IS NOW TAKEN and lives at rapidresponse-2026-macdonald. One unresolved nuance, recorded rather than acted on: Fortune calls it the 2026 AI coding-tools budget while Forbes and Macdonald use the broader ’AI budget’, and the chapter follows Forbes. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS B1 TO B3 OF THE VERIFICATION SHEET, ALL PASS. The speaker is Andrew Macdonald, Uber’s PRESIDENT AND CHIEF OPERATING OFFICER, and the chapter said only ‘chief operating officer’ until this ruling; both sentences carrying the title were corrected the same day. THE VENUE IS THE RAPID RESPONSE PODCAST, which Fortune reports: the article is therefore SECONDARY to a recorded interview, and that is the level the chapter cites. MACDONALD’S WORDS, QUOTED HERE BECAUSE A NOTE THAT QUOTES THE SENTENCE IS WHAT CAUGHT SF7 AND SF11: he said it is hard to draw a connection between the company’s rising use of Claude Code and innovations meant to serve consumers. ‘That link is not there yet. Maybe implicitly there’s more that is getting shipped, but it’s very hard to draw a line between one of those stats and “Okay now we’re actually producing like 25% more useful consumer features.”’ B2 PASSES ON DAN’S READING that he questions the value of the spend repeatedly in the interview, not on this quotation alone. REVERSES IF the interview is shown to postdate or otherwise not bear on the April budget exhaustion, or if the title changes again. RULED THE SAME DAY: DAN CHOSE THE DIRECT QUOTATION AND THE NAME. The paraphrase was supported and stood, and the quoted words are narrower and stronger, namely that the link between usage and consumer value cannot be drawn, which is the cost-value asymmetry in the executive’s own words. The opening case now names him in Chapter 1’s form, title then full name then ‘said publicly that’, and carries ‘That link is not there yet,’ he said. THIS IS THE BOOK’S FIRST DIRECT QUOTATION IN BODY PROSE; Chapter 1 names Sam Altman and quotes nobody. THE SHORT LINE WAS CHOSEN OVER THE LONGER ONE DELIBERATELY: the longer quotation carries three contractions, body prose bans them, and the opening case is not a voiced block, so quoting it would have failed Stage 4 mechanical. The 2.6 back-reference is unchanged and is supported by B2. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Supports the claim that a senior executive publicly questioned whether the spending was justified. THE CHAPTER’S ARGUMENT LEANS ON THIS MORE THAN ON ANY FIGURE, because the executive’s question is the evidence that the value half of the flow was unbuilt. If Stage 3 cannot confirm it, the paragraph and problem P1 both need rework rather than a looser number.


### `jpmorgan-2025-dimon`

- **type**: news
- **title**: JPMorgan’s Dimon says AI cost savings now match money spent
- **container**: Bloomberg, via Yahoo Finance
- **date**: 2025-10-07
- **url**: https://finance.yahoo.com/news/jpmorgan-dimon-says-ai-cost-160516333.html
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of a Bloomberg Television interview gives the quotation ‘We have shown that for $2 billion of expense, we have about $2 billion of benefit.’ Fortune’s report is dated October 8, 2025, so the interview is placed on October 7, 2025. Check A must confirm the date and the quotation.


### `jpmorgan-cfo-ai-spend`

- **type**: news
- **title**: JPMorgan CEO Dimon warns customers of ‘liability transfer’ with AI
- **container**: Banking Dive
- **url**: https://www.bankingdive.com/news/jpmorgan-dimon-ai-agents-bank-customers-liability-transfer/832870/
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search summary of this article gives: asked for updated figures, the bank’s CFO put annual AI spending closer to $700 million, calling the earlier figure ‘a little stale’; AI benefits were not yet observable in quarterly earnings. The date and the CFO’s name were not visible in the summary. Check A must confirm all of it; if the article does not carry it, the box’s second half is cut.


### `klarna-2024-assistant`

- **type**: web
- **authors**: {"org": "Klarna"}
- **title**: Klarna AI assistant handles two-thirds of customer service chats in its first month
- **date**: 2024-02-27
- **url**: https://www.prnewswire.com/news-releases/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month-302072740.html
- **perishable**: True
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). URL changed to the PR Newswire copy of the release, which is the copy check A read. VERIFIED (A-11): ‘2.3 million conversations’, ‘two-thirds’, ‘700 full-time agents’, ‘less than 2 mins compared to 11 mins previously’, ‘$40 million USD in profit improvement to Klarna in 2024’, dated February 27, 2024. RULINGS, Dan, sitting 3: A-12 ‘built on OpenAI’s models’ is now ‘powered by OpenAI’, the release’s words; B-28 the resolution time is attributed to the company; B-29 the case tasks work from the announcement alone. PROTECT THE CHAPTER 6 REVEAL: the case uses this announcement only and must not cite or allude to any later reporting. REVERSES-IF: none expected; the release is fixed.


### `microsoft-2024-copilot-pricing`

- **type**: web
- **authors**: {"org": "Microsoft"}
- **title**: Expanding Copilot for Microsoft 365 to businesses of all sizes
- **container**: Microsoft 365 Blog
- **date**: 2024-01-15
- **url**: https://www.microsoft.com/en-us/microsoft-365/blog/2024/01/15/expanding-copilot-for-microsoft-365-to-businesses-of-all-sizes/
- **accessed**: 2026-08-30
- **upgrade**: Nothing outstanding. This is the vendor’s own announcement.

NOTE, verbatim:

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. ADDED BECAUSE THE DTA EVALUATION DOES NOT ESTABLISH THE PRICING CONTRAST. It records agencies purchasing licences; it does not state that the product is priced per seat rather than by unit of use, which is the sentence problem P3 rests on. Microsoft’s own announcement prices it at $30 per user per month, which settles it. Check A raised the gap and it is closed here rather than by leaving one source carrying two claims.


### `microsoft-2026-mai`

- **type**: news
- **title**: Microsoft begins replacing third-party AI models with its own in Office apps
- **container**: Redmond Magazine
- **date**: 2026-07-09
- **url**: https://redmondmag.com/articles/2026/07/09/microsoft-begins-replacing-third-party-ai-models.aspx
- **perishable**: True
- **accessed**: 2026-10-15
- **upgrade**: The Bloomberg report of July 7, 2026, which the coverage cites.

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of a Bloomberg report (July 7, 2026) gives: Microsoft routes some Excel and Outlook Copilot prompts to its in-house MAI models instead of OpenAI and Anthropic models, to cut cost; tens of thousands of prompts a week (one source says 10K+); routine tasks to MAI, complex reasoning still to frontier models; Suleyman: the goal is to ‘reduce and ultimately eliminate’ what Microsoft pays Anthropic. The chapter paraphrases the Suleyman remark because the coverage quotes it with an em dash. Check A must confirm each against Bloomberg.


### `npr-2026-lindy`

- **type**: news
- **title**: American AI is expensive. Some startups are turning to cheap Chinese models
- **container**: NPR
- **date**: 2026-07-15
- **url**: https://www.npr.org/2026/07/15/nx-s1-5886476/startups-cheap-chinese-ai-models
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage gives: Crivello, ‘By far, our No. 1 expense was Anthropic ... Like, more than payroll’; Lindy moved 100 percent of its traffic to DeepSeek V4, announced in June 2026; ‘100x more work than we thought’; open to returning to Claude if prices fall. Check A must confirm each quotation and which outlet carries it, and the month of the announcement.


### `pigment-2026-cfo-index`

- **type**: report
- **authors**: {"org": "Pigment"}
- **title**: CFO Index, Q3 2026
- **date**: 2026-10-07
- **url**: https://www.pigment.com/reports/cfo-index/q3-2026
- **perishable**: True
- **accessed**: 2026-10-15

NOTE, verbatim:

> STAGE 0, 2026-10-15, UNVERIFIED, GRADE C. Found by WebSearch; no source read. Search coverage of the report and its press release gives: about 2,000 finance leaders in the US, UK, France and Germany; 83 percent say consumption-based costs pushed spending above expectations; 13 percent stayed within budget; average overrun about 27 percent; released October 7, 2026. Check A must confirm each against the report. Vendor survey: the box says so.


### `truell-2025-pricing`

- **type**: blog
- **authors**: Michael Truell
- **title**: Clarifying Our Pricing
- **container**: Cursor
- **date**: 2025-07-04
- **url**: https://cursor.com/blog/june-2025-pricing
- **perishable**: True
- **accessed**: 2026-07-29

NOTE, verbatim:

> FROM CHAPTER 1, verified there (note follows). Chapter 3 uses it for the plan change only, in the ruled form: further use was PRICED at the same rates; no billing mechanism is asserted (SF2, SF8). NOTE ADDED 2026-07-29 (Stage 2, items A5, A6, A7). This entry previously carried no note despite being the most load-bearing source in the chapter. Verified by direct reading on the access date. DATE: July 4, 2025, stated on the page and corroborated by the post's own timeline, which reads June 16 for the original change, June 30 for a clarity revision to that post and the pricing page, and July 4 for the apology. Three fact-check rounds have proposed July 3; all three are wrong. Do not change it. REQUEST ARITHMETIC: for external models Cursor had previously charged by request count, with a limit of 500 requests per month and Sonnet models costing two requests, which is why the chapter says five hundred requests against external models rather than 'fast requests'. The phrase 'fast requests' is TechCrunch's gloss, not Cursor's term, and must not be reintroduced. NEW PLAN TERMS: unlimited use of Tab and of models in Auto, 20 dollars of frontier model usage per month at API pricing, and the option to purchase more at cost. ORDER OF MAGNITUDE: the post states verbatim that although most users' costs stayed fairly constant, the hardest requests cost an order of magnitude more than simple ones. A raise calling this unsupported has been rejected once and should be rejected again. COVERAGE: the post gives median Pro coverage as roughly 225 Sonnet 4 requests and states that the vast majority of Pro users do not exhaust the allowance, so the chapter's depletion sentence is scoped to a labelled composite team's heaviest users on long-horizon frontier work, not to Pro users generally. REFUNDS: offered for unexpected usage between June 16 and July 4, 2025. BYLINE: the post is bylined Michael Truell with no role stated on the page; his role as chief executive of Anysphere rests on techcrunch-2025-cursor-apology, not on this post. CLAIM NARROWED 2026-08-06 (Stage 3, SF2). The chapter formerly said the allowance was consumed 'after which usage continued to bill against real rates', which asserts that billing continued automatically. This entry does not establish that. What it establishes is the price of further use: twenty dollars of frontier-model usage per month at API pricing, with the option to purchase more at cost. Whether continuation was the default or required usage-based pricing or a spend limit to have been enabled is not settled here, and no Claude session can reach the post to settle it. RULED by Dan: state the price and assert no mechanism. The sentence now reads 'after which additional usage was priced at the same rates'. Do not restore a mechanism claim without a passage from this post that describes the default billing behaviour on exhaustion. The sentence that follows, that charges arrived which no one had planned for, is scoped to the labelled composite team and is separately supported by the refund offer for unexpected usage between June 16 and July 4, 2025. MECHANISM AND SCOPE BOTH REGRESSED AND ARE RESTORED 2026-08-10 (Stage 3, SF8 and SF9). The Stage 6 copy-edit rounds of 2026-08-08 rewrote this paragraph and undid both rulings while leaving every date and figure intact, so no check on values could see it. SF8: the chapter had come to read 'Once the credit ran out, Cursor billed each additional request at API rates', which is the automatic-continuation mechanism the SF2 ruling removed, restored in different words and with no new passage from the post to support it. SF9: the depletion claim had been generalized from the case team to 'Heavy users', dropping the scoping the COVERAGE entry above exists to require, since the post states that the vast majority of Pro users do not exhaust the allowance. The sentence read, as ruled on 2026-08-10, 'For the team's heaviest users, the people getting the most value, the credit was consumed in a handful of prompts, after which additional usage was priced at the same rates.' Both halves were the ruled form. UPDATED 2026-08-12 (CE11). That sentence was restructured to remove a mid-clause interrupter, per prose style guide Part 5 rule 3, and now reads 'The credit was consumed in a handful of prompts for the team's heaviest users, the people getting the most value. Additional usage was then priced at the same rates.' THE SF9 SCOPING SURVIVES: the depletion is still scoped to the team's heaviest users and is still not a claim about Pro users generally, which is the whole point of the COVERAGE entry above. Only the clause order changed; no value, date or claim moved. Recorded here rather than left to a later checker because this note's quotation of the exact sentence is what caught SF8 to SF10, and a quotation that silently goes stale is the failure SF7 and SF11 already are. What would reverse SF8 is unchanged and stated above: a passage from this post describing the default billing behaviour on exhaustion. What would reverse SF9: a passage scoping exhaustion to Pro users generally, which this post contradicts. CARRY TO EVERY LATER CHAPTER: a ruled claim narrowing does not survive a copy edit on its own. This one was recoverable only because the ruled sentence was quoted here and could be diffed against the render the external checks audited. CLAIM CUT 2026-08-13 (Stage 7, external check 2, FC9). The chapter formerly closed the paragraph with 'Cursor had been paying the difference, but the difference had become too expensive to absorb.' This entry does not carry it: the words absorb, paying the difference and too expensive appear nowhere in this note, and what the post supplies is the order-of-magnitude spread between hardest and simple requests plus the statement that most users' costs stayed fairly constant. The sentence was an inferred economic mechanism presented as Truell's explanation, which is the SF2 shape a second time. Cut. The supported sentence before it now carries the point alone: 'The newest models consumed far more tokens on long-horizon tasks than a flat monthly price could cover.' REVERSING CONDITION: a passage in which Cursor states it had been absorbing the difference would license restoring it.


### `uber-2026-budget`

- **type**: news
- **authors**: Janakiram MSV
- **title**: Uber burns its 2026 AI budget in four months on Claude Code
- **container**: Forbes
- **date**: 2026-05-17
- **url**: https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/
- **perishable**: True
- **accessed**: 2026-08-30
- **upgrade**: The Information’s original report, which carries the CTO confirmation. Paywalled.

NOTE, verbatim:

> FROM CHAPTER 2, verified there (note follows). STAGE 7, 2026-08-30: EXTERNAL CHECK A READ THE PRIMARY DOCUMENTS. It is the first check on this book with live web access, so this is the first entry here verified against the source rather than against a summary of it. THE COST RANGE WAS WRONG AND STAGE 3 PASSED IT. The article gives an average of $150 to $250 and heavy-user spending of $500 to $2,000. The chapter said ’several hundred to several thousand’ and, before the Stage 6 copy edit, ’a few thousand’: BOTH endpoints were unsupported in both forms, so the copy edit did not cause this. The looseness was deliberate, recorded here as protection against a corrected figure, and it concealed the error from every checker who could not read the article. THE RATIONALE FOR LOOSENESS IS RETIRED and the chapter now carries the exact figures, which the fifty-year rule permits because the opening case is dated. THE COMPLEXITY CLAUSE IS CUT: the article does not attribute the range to the complexity of the work, and the workload mechanism is already carried by the two sentences after it. THE ADOPTION PERCENTAGES NOW LIVE HERE, 32 per cent in February and 84 per cent in March, which retires uber-2026-adoption and with it rulings S3-1 and S3-2. BYLINE CORRECTED to its published form, Janakiram MSV, which the register had inverted. STILL SECONDARY, and the upgrade is unchanged: The Information’s original carries the CTO confirmation and stayed paywalled to check A as well. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: VERIFIED BY DAN 2026-08-29 AT STAGE 3, ROWS A1 TO A6 OF THE VERIFICATION SHEET, ALL PASS. That covers the budget exhaustion and its April timing, that no contract was renegotiated and no vendor raised a price, the roughly five thousand engineers from December 2025, the per-engineer monthly cost range, the attribution of the variation to workload, and the usage-based commercial terms. A2 AND A5 WERE CHECKED SEPARATELY FROM THE FIGURES AND BOTH HOLD, which matters because each could have been the chapter’s inference rather than the article’s statement, and that is the shape of Chapter 1’s FC9. STILL SECONDARY. The chapter’s cost range remains deliberately loose, and the upgrade is unchanged: The Information’s original report carries the CTO confirmation and is paywalled. Verifying Forbes establishes that the reporting says what the chapter says it says, not that the underlying facts hold. REVERSES IF the article is corrected or withdrawn. PRIOR NOTE, KEPT AS HISTORY: UNVERIFIED. Found by WebSearch 2026-08-21; the article itself has not been read by Claude, and the container cannot fetch it. Carries the budget exhaustion timing, the engineer count, the rollout date, and the per-engineer monthly cost range. Grade C until a primary is read. The chapter states the cost range as ’several hundred to a few thousand dollars’ rather than as exact bounds, deliberately, so that a corrected figure does not invalidate the sentence.

## Part 1a. Table 3.1 citations, added from the live text

`factcheck_packet.py` does not read inside tables, so these cited cells
are missing from Part 1. They are quoted from Table 3.1 as it stands,
and their register entries follow.

### T1 (Table 3.1, AIOps row, "What it is for")

> Applying big data and machine learning to automate IT operations, including event correlation, anomaly detection, and causality determination

CITES: `gartner-aiops`. IN-CHAPTER GLOSS: Gartner’s definition of AIOps.

### T2 (Table 3.1, MLOps row, "What it is for")

> Building, deploying, and monitoring machine learning models in production

CITES: `kreuzberger-2023-mlops`. IN-CHAPTER GLOSS: Definition and scope of MLOps.

### T3 (Table 3.1, FinOps row, "What it is for")

> Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams

CITES: `finops-what-is`. IN-CHAPTER GLOSS: The Foundation’s own definition of the practice.

### `gartner-aiops`

- **type**: web
- **title**: AIOps (Artificial Intelligence for IT Operations)
- **container**: Gartner Information Technology Glossary
- **url**: https://www.gartner.com/en/information-technology/glossary/aiops-artificial-intelligence-operations
- **accessed**: 2026-10-01

NOTE, verbatim:

> STAGE 3, 2026-10-13: CANNOT CONFIRM, GRADE C. Check A could not open the glossary (Gartner blocks retrieval). Cisco (developer.cisco.com/articles/what-is-aiops/what-is-aiops/) reproduces Gartner’s definition as ‘AIOps combines big data and machine learning to automate IT operations processes, including event correlation, anomaly detection, and causality determination’, says Gartner coined the term, and links this URL, so the URL is no longer a guess. RULINGS, Dan, sitting 3, A-9 and B-36: Table 3.1’s cell now follows the reproduced wording, and the gloss says ‘Gartner’s definition’ instead of ‘the originating definition’. REVERSES-IF: a reader of the live glossary finds different wording.

### `kreuzberger-2023-mlops`

- **type**: article
- **title**: Machine Learning Operations (MLOps): Overview, Definition, and Architecture
- **container**: IEEE Access
- **date**: 2023
- **doi**: 10.1109/ACCESS.2023.3262138

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-10): the paper defines MLOps as including ‘end-to-end conceptualization, implementation, monitoring, deployment, and scalability of machine learning products’, ‘aimed at productionizing machine learning systems’, so Table 3.1’s paraphrase is supported; IEEE Access 11, 31866-31879, 2023, and the DOI are correct. Read at epub.uni-bayreuth.de/7577/. REVERSES-IF: none expected; the paper is a fixed publication.

### `finops-what-is`

- **type**: web
- **title**: What is FinOps?
- **url**: https://www.finops.org/introduction/what-is-finops/
- **accessed**: 2026-10-13

NOTE, verbatim:

> STAGE 3, 2026-10-13: EXTERNAL CHECK A READ THE SOURCE WITH LIVE WEB ACCESS (04_Stage3_Fact_Check/AIOM_Ch03_Stage3_externalcheck_A.md). VERIFIED (A-7): ‘FinOps is an operational framework and cultural practice which maximizes the business value of technology ... and creates financial accountability through collaboration between engineering, finance, and business teams.’ The page names AI among technology categories (A-8) and describes ‘a strong heritage in managing cloud cost and usage’ (A-13). RULINGS, Dan, sitting 3: B-11 Table 3.1’s purpose cell now carries the value purpose as well as accountability; A-13 the table’s ‘built around cloud billing’ is now ‘grew from managing cloud cost and usage’; A-8 ‘the hardest to define’ is the book’s judgment and stays. REVERSES-IF: the Foundation changes its definition.

<<<<< END DOCUMENT 2 >>>>>

END OF PACKAGE. Now produce your findings in the format given in Part 2.
