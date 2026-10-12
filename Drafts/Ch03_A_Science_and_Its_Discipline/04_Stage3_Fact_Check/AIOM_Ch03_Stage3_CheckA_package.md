# Fact-check package A: Chapter 3, the sources

This is ONE self-contained file: your instructions, the required output
format, and all the material, between BEGIN and END markers in Part 3. Do not
ask for other files. Read the whole file before you begin.

---

## PART 1. Your task

You are fact checking one chapter of an academic textbook for business
graduate students, *AI Operations Management*, before it locks. Chapter 3 is
"A Science and Its Discipline". Work to the standard of a university press
fact checker: **a claim is verified when you have seen the document that
supports it, not when it sounds right.**

**Your first line must say whether you have live web access in this session.**
If you do not, say so and treat every "verified" below as unavailable to you.
**Do not simulate a lookup you cannot perform.** If you cannot open a
document, the answer is CANNOT CONFIRM, never a summary from memory presented
as a check. Nobody on this project has yet read any of these sources; the
register notes record what search summaries said, nothing more.

Part 3 holds two documents:

- **Document 1: the chapter**, as typeset.
- **Document 2: the claim packet.** Every passage carrying a citation, the
  source keys it cites, and each source's register entry with its note
  verbatim. The notes say what each source must be checked for.

### Reading the chapter text

Document 1 is the text of the typeset PDF, page by page, extracted from the
render the book will print from. Three things in it are typesetting, not
errors, and must not be reported: words broken across a line end carry a
hyphen; small capitals come out letter-spaced ("D AT E D"); and footnotes sit
at the foot of the page that calls them, numbered to match the superscript in
the text. Table 3.1 is laid out in columns on its page. `[[ PAGE n ]]` marks
the start of each printed page.

The render also fails three print-layout checks (a line overflowing the
margin on page 12, a definition box split across a page break, and footnote
11 not on its calling page). These are pagination, booked to the design
review that follows this check. **Report none of them.**

### What to check, in priority order

For every item give a verdict: **VERIFIED, CONTRADICTED, or CANNOT CONFIRM**,
and quote the source language you relied on, with its location.

**1. The State of FinOps 2026 report** (`finops-2026-state`; packet C2, C4).
The opening case rests on it and its provenance line says it has not been
checked against the report itself. Verify, each separately:
- the survey had **1,192 respondents**;
- they oversaw **more than $83 billion** in annual cloud spending;
- **98 percent** of respondents managed AI spending;
- **31 percent** did "two years earlier": is that the 2024 survey's figure?
- the quotation **"No one can answer that question yet."** appears in the
  report itself, is attributed to a practitioner, and is worded exactly so;
  and the chapter's lead-in, "Asked whether AI was delivering value", is a fair
  account of the question it answered;
- the publication date, February 19, 2026.
Give the report's own title and location if you reach it.

**2. The mission change** (`finops-2026-mission`; packet C1). The chapter says
that in February 2026 the FinOps Foundation revised its mission from
advancing "the people who manage cloud value" to "the people who manage
technology value", and that the new statement "changed a single word". The
chapter paraphrases; it does not quote. Confirm both wordings from the
Foundation's own statement, the date, and that the paraphrase and "a single
word" are faithful. The cited source is a syndicated press release; if you find
the Foundation's own page stating the change, give its URL.

**3. The FinOps definition** (`finops-what-is`; packet C3, C12, T3). Confirm
the live wording of the Foundation's "What is FinOps?" page, and whether it
supports each of: (a) the Table 3.1 row "Financial accountability for
technology spending, through collaboration among engineering, finance, and
business teams"; (b) "defines its purpose in terms of maximizing technology's
business value"; (c) in C3, the account of the problem FinOps was built to
solve (engineers buying capacity in code, the bill arriving after use) and
"jointly accountable". **Also judge the citation itself:** C3 ends "by 2026,
nearly all of them managed it", and the footnote on that paragraph is the
definition page, not the survey. Say whether every sentence of C3 is supported
by the source its footnote names.

**4. AIOps** (`gartner-aiops`; packet T1). The URL is a candidate. Find the
live Gartner glossary entry, confirm the wording, and say whether the Table 3.1
paraphrase ("Applying machine learning to run IT operations: correlating
events, detecting anomalies, finding causes") is faithful. Give the correct URL.

**5. MLOps** (`kreuzberger-2023-mlops`; packet T2). Confirm the paper's own
definition supports "Building, deploying, and monitoring machine learning
models in production", and confirm volume 11, pages 31866-31879, and the DOI.

**6. Klarna** (`klarna-2024-assistant`; packet C17, Problem P3). Against the
February 27, 2024 press release only, verify each: built on OpenAI's models;
first month; **2.3 million** conversations; **two-thirds** of customer-service
chats; the work of **700** full-time agents; resolution in **under two
minutes** against **eleven**; an estimated **$40 million** profit improvement
in 2024. Note which figures the release presents as estimates and whether the
chapter's sentences attribute them accordingly.
**Use the release and nothing later.** The problem deliberately uses the
announcement alone, and a later chapter takes up what happened afterwards. Do
not cite, summarize, or recommend adding later reporting on Klarna, and do not
raise its absence as a finding.

**Out of scope: `aibe-registry-2026`.** The registry is not public; its counts
and statements are checked mechanically against a pinned version. Do not mark
those passages CANNOT CONFIRM. You may check internal arithmetic only (C7: do
the six object counts sum to the total?).

### Rules for your findings

- **Number every finding** (A-1, A-2, ...). Give the exact sentence from the
  chapter, its page, what you checked it against, and your verdict.
- **Separate "the source contradicts this" from "I could not reach the
  source".** They get different rulings, and conflating them wastes a round.
- **Nothing has been ruled on this chapter yet**, so every finding you raise
  is new.
- **A proposed remedy is welcome and will be judged separately from the
  finding.** Two house rules constrain remedies, and a remedy breaking either
  is rejected while the finding stands: body prose carries **no hedging
  language** ("perhaps", "some argue", "one might say"), and **no em dashes or
  en dashes anywhere**. Accurate qualification is not hedging. Making a sentence
  narrower is an acceptable fix; making it vaguer is not.
- **Do not comment on prose quality, rhythm, structure, or teaching.** Other
  steps own those and have closed.
- **Formal statements are out of bounds.** Quoted statements of theorems,
  lemmas and propositions (IDs such as THM-004, LEM-020, PROP-043) are verbatim
  from a formal registry and are checked mechanically against it. Do not judge
  their wording.

---

## PART 2. Required output format

Reply in Markdown, exactly this structure. No preamble.

```
# Fact check A: Chapter 3

Web access in this session: YES / NO (one line, first)

## Findings

| ID | Packet | Page | Chapter sentence (exact) | Checked against (title, location) | Verdict | Source language (quoted) | Proposed remedy |
|---|---|---|---|---|---|---|---|
| A-1 | C2 | 1 | "..." | ... | VERIFIED | "..." | none |

## Sources I could not reach
One line each: key, what you tried.

## Corrected bibliographic details
One line each: key, field, register value, correct value, where seen.

## Fix first
1. A-n: one line on why
```

---

## PART 3. The material

<<<<< BEGIN DOCUMENT 1: CHAPTER 3, AS TYPESET >>>>>

[[ PAGE 1 ]]

PA R T I · T H E A R G U M E N T

A Science and Its Discipline
OPENING CASE

The discipline that changed its mission
D AT E D : F E B R U A R Y 2 0 2 6 . F O U N D B Y S E A R C H . F I G U R E S A N D T H E Q U O TAT I O N A G R E E
A C R O S S S E C O N D A R Y C O V E R A G E A N D H AV E N O T Y E T B E E N C H E C K E D A G A I N S T T H E
R E P O R T I T S E L F. S E E T H E S O U R C E R E G I S T E R .

In February 2026, the FinOps Foundation revised its mission statement.
For years, it said it existed to advance the people who manage cloud
value. The new statement changed a single word: it now advances the
people who manage technology value.1
The change accompanied the Foundation’s annual survey of practition‐
ers: people inside companies who manage cloud spending. The 2026
survey included 1,192 respondents who collectively oversaw more than
$83 billion in annual cloud spending.2 Its central finding concerned work
the discipline was not originally created to do. Ninety-eight percent of
respondents now managed AI spending, up from 31 percent two years
earlier.3
FinOps was built to solve a specific problem: engineers could buy cloud
capacity with a few lines of code, but the bill arrived only after they had
used it. The discipline emerged to make engineering, finance, and
business teams jointly accountable for that spending.4 Its practitioners
1.

FinOps Foundation, “State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures
Across Technology Value,” February 19, 2026, accessed October 1, 2026. The mission statement
before and after the change.
2.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 1, 2026.
Survey size and the cloud spending its respondents manage.
3.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 1, 2026.
Share of practitioners managing AI spend, 2026 against 2024.
4.

FinOps Foundation, “What is FinOps?,” accessed October 1, 2026. The practice as the
Foundation defines it.

1

[[ PAGE 2 ]]

A I O P E R AT I O N S M A N A G E M E N T

later took on AI spending as well, and by 2026, nearly all of them
managed it.
The report also recorded a question this work had not yet answered.
Asked whether AI was delivering value, one practitioner replied in words
the report chose to quote: “No one can answer that question yet.”5
The survey reveals the gap Chapters 1 and 2 described among the very
people expected to close it. For an organization using a metered re‐
source, cost arrives by default with the bill, while value becomes visible
only when someone builds a way to measure it. Cloud-cost management
is a neighboring discipline, but it has been drawn, reluctantly, into work
it was never designed to do: managing the economics of an
organization’s AI use.
FinOps can show who is using AI and what the organization pays for it.
On its own, however, it cannot determine whether the system produces
accurate, useful work or build the management practice that turns that
evidence into decisions. That work requires both a body of knowledge
for judging what is true and a practice for acting on those judgments.
Chapter 14 explains how FinOps and that practice divide the work. Until
both exist, the practitioner’s question about whether AI provides value
remains unanswered.

3.1 Why name a science
Managers act on claims about how their business works. A budget as‐
sumes that cost follows usage, a pricing negotiation assumes the
provider has a reason to accept a lower price, and a dashboard assumes
that the information it shows will change someone’s actions. When
those claims are wrong, the management built on them fails, however
carefully managers carry it out.

5.

FinOps Foundation, “State of FinOps 2026,” February 19, 2026, accessed October 1, 2026.
Practitioner quotation as reproduced in the report.

2

[[ PAGE 3 ]]

A SCIENCE AND ITS DISCIPLINE

These claims can remain informal, held in experience, rules of thumb, or
the slides of whoever presented last. Informal knowledge is useful, but
it has a cost: two managers can hold opposite beliefs about the same
deployment without being able to identify where they disagree. One
might treat Chapter 1’s Cursor licenses as a fixed software expense and
the other as metered consumption. Unless each states the claim behind
that view, neither can identify the fact that would settle the disagree‐
ment, and the argument turns on confidence rather than evidence.
Chapters 1 and 2 each ended with a stated result rather than an opinion.
Chapter 1 set out the conditions under which deployed AI is a resource
the organization consumes, while Chapter 2 set out the conditions under
which a scaled deployment cannot be controlled without a governing
apparatus. Each result appeared in a panel with an identifier that points
to the larger body of claims supporting it.
That body of claims is AI Business Economics. It is a science in a specif‐
ic and limited sense: a set of claims about the business economics of
consuming AI, each stating when it holds and precise enough to be
checked. Here, science means neither laboratory experiments nor cer‐
tainty. It means that every claim states when it applies, what it
concludes, and which other claims it rests on.
The claims are kept in a registry: a
structured record of every definition,
assumption, and result in the science,
with each result linked to the claims
that support it. A definition fixes what
a term means, while an axiom states
an assumption the science accepts
without proof. A proposition states a

DEFINITION

AI Business Economics
The science of the business
economics of consuming AI: an
ordered body of conditional
claims, each stating when it
applies, what it concludes, and
which other claims it depends on.

single claim, accepted on the basis of
the definitions, axioms, or earlier claims it names as support. A lemma
combines propositions, and sometimes other lemmas, into an interme‐
diate result. A theorem combines lemmas into a result with direct
consequences for management.
3

[[ PAGE 4 ]]

A I O P E R AT I O N S M A N A G E M E N T

Those links are the registry’s most important feature. Every higher claim
names the lower claims it depends on, which in turn name their own
supporting claims. Together, the links form a dependency graph: a map
in which no claim can rest, directly or indirectly, on itself. Anyone with
the registry can start at a theorem and follow its supporting claims down
to definitions and axioms. Appendix A reproduces every certified theo‐
rem and lemma, while the book cites propositions by identifier. Readers
can therefore trace any claim to the lemma level unaided. Below that
level, they work from the propositions supplied by a chapter or exercise.
For a manager, the graph rules out circular reasoning: no conclusion
depends on itself. A manager who doubts a conclusion can therefore
trace that doubt to a smaller claim and examine it. The graph does not,
however, establish whether that smaller claim is true.
The registry also records which claims are complete. A claim is certified
when every claim it depends on is itself certified and its supporting
argument meets the registry’s fixed conditions. The registry’s validator
computes that status from the graph at each version; no one enters it
manually. The validator checks that every dependency is recorded and
certified, that no chain of support loops back on itself, that every claim
marked empirical has evidence attached, and that a reviewer has signed
off on the claim’s current wording.6 These checks establish the structure
and record of an argument, not its truth. If a claim has a gap in its
support, the registry records what is missing. This book presents and
cites only certified claims, because presenting an uncertified claim as a
theorem would assert more than the science does.
The registry justifies this book, but it does not organize it. The chapters
follow the order in which a manager needs to learn, which differs from
the order in which the science derives its results. The registry supports
each result the book teaches, allowing a reader who doubts a claim to
trace its support. If the chapters instead followed the order of proof,
6.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. What the
validator checks.

4

[[ PAGE 5 ]]

A SCIENCE AND ITS DISCIPLINE

managers would spend many pages on definitions before reaching a
decision they recognize.

3.2 Tracing a result the reader already accepts
Once a deployment reaches scale, economic control requires a govern‐
ing apparatus; diligence from the people running it is no longer enough.
Chapter 2 ended with that result, so a reader who accepted the chap‐
ter’s argument already accepts the conclusion. Tracing that familiar
result through the registry is the clearest way to learn how the registry
works. The only new task is to understand how its supporting claims are
arranged.
The registry states that result as THM-004:

THEOREM 2 · THM-004

Scaled AI Deployment Requires Cost Governance for
Economic Control
Within the defined deployment and measurement boundary, if:
(i) production scaling expands the usage surface of AI deployment;
(ii) measurement enables visibility into measurable cost-bearing
activity;
(iii) visibility enables management mechanisms; and
(iv) buyer total cost extends beyond access price;
then scaled AI deployment requires cost governance for economic
control.

Each condition has a plain meaning a manager can check against a de‐
ployment. The first says that the deployment has moved from a pilot
into daily operations, multiplying the places where usage can occur. The
second says that measuring usage makes activity that costs money visi‐
ble. The third says that managers can apply monitoring, limits, attribu‐

5

[[ PAGE 6 ]]

A I O P E R AT I O N S M A N A G E M E N T

tion, or other management mechanisms to visible activity. The fourth
says that the organization’s total cost exceeds the price of access. When
all four hold, an organization seeking control over the deployment’s
economics needs cost governance.
THM-004 rests on four certified lemmas, one for each condition.
LEM-016, “Production Scaling Expands Usage Surface,” supports the
first; LEM-002, “Measurement Enables Visibility,” supports the second.
LEM-020, “Visibility Enables Management Mechanisms,” supports the
third, and LEM-006, “Buyer Total Cost Extends Beyond Access Price,”
supports the fourth.
The registry also records the theorem’s proof, which combines the four
lemmas in two pairs. The first and fourth describe economic exposure
that grows with the deployment and cannot be determined from the ac‐
cess price alone. The second and third describe the only route to man‐
aging that exposure: measurement makes it visible, allowing managers
to apply management mechanisms. Control therefore requires an appa‐
ratus for both measurement and management, which the theorem calls
cost governance.
This pairing explains Chapter 2’s claim that THM-004 formalizes the
economic consequence of the third flow’s asymmetry. The first and
fourth conditions describe cost that arrives by default and grows with
scale. The second and third describe the measurement and manage‐
ment that an organization must deliberately build to control it.
One level down, each lemma rests on propositions. LEM-020 offers a
useful example of how the registry is built. Its statement reads: “If
economic exposure or usage activity is visible to the relevant actor, then
monitoring, limits, attribution, or management mechanisms can be ap‐
plied within the relevant scope.” The lemma rests on seven propositions
and one other lemma.
The propositions are small claims, each nearly obvious on its own.
PROP-043 states: “If activity is metered, records describing measured
activity are generated or maintained.” PROP-053 states: “If economic
6

[[ PAGE 7 ]]

A SCIENCE AND ITS DISCIPLINE

exposure exists, monitoring mechanisms may be used to observe the
sources or magnitude of that exposure.” PROP-085 states: “If usage in‐
formation becomes visible, decisions regarding management, allocation,
optimization, or monitoring may reference that information.” No manag‐
er would dispute these claims; the work lies in combining them.
PROP-043 says that metered activity leaves a record, PROP-085 allows
management decisions to draw on visible usage, and PROP-053 adds
that monitoring can be used to observe economic exposure. None of the
three alone establishes that controls can be applied to what is visible.
LEM-020 reaches that conclusion by combining them with four further
propositions and LEM-002, a combination the registry records as its
proof.7
LEM-020 also rests on LEM-002, which directly supports THM-004’s
second condition. Figure 3.1 shows the branch through LEM-020 and
makes that shared support visible. The registry is therefore a graph, in
which one claim can support several others, rather than a tree, in which
each claim has one parent.

7.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-020’s
proof record and its supporting propositions.

7

[[ PAGE 8 ]]

A I O P E R AT I O N S M A N A G E M E N T

THEOREM

THM-004
Scaled AI Deployment Requires Cost
Governance for Economic Control

LEMMAS

LEM-016

LEM-002

LEM-020

LEM-006

Production Scaling
Expands Usage Surface

Measurement Enables
Visibility

Visibility Enables
Management Mechanisms

Buyer Total Cost Extends
Beyond Access Price

LEM-020 also rests on LEM-002

PROPOSITIONS

PROP-043

PROP-053

PROP-085

Metered Activity
Produces Usage
Records

Economic Exposure
Creates Incentives
For Monitoring

Usage Visibility
Enables Management
Decisions

Figure 3.1 One branch of the trace. THM-004 rests on four lemmas, one for each
condition. LEM-020 rests in turn on LEM-002, which also supports the theorem directly,
and on seven propositions, three of which are shown.

Tracing the theorem changes how a manager can assess it. Before the
trace, THM-004 is a conclusion to accept or reject as a whole. Afterward,
the manager can examine its smaller supporting claims individually and
identify which one they doubt. That gives the disagreement a point that
can be checked: a dispute over an entire conclusion has no obvious res‐
olution, but a dispute over one proposition can be settled.
D AT E D : A U G U S T 2 0 2 6

The registry version used to write this book held 413 objects: 140 defini‐
tions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records
of evidence the science still needs. It recorded 1,777 dependency links
among them, and 397 of the 413 objects were certified.8 These figures de‐
scribe one version of the registry, which is revised as the science develops,
rather than the science itself.

8.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. Object counts,
links and certification at the pinned registry version.

8

[[ PAGE 9 ]]

A SCIENCE AND ITS DISCIPLINE

3.3 How to read a formal claim
A manager who cites a formal claim for more than it says bases a deci‐
sion on something the claim never established. To avoid that error, read
the claim in four parts: its conditions, its scope, its non-claims, and the
falsifying case that would defeat it. A manager who can state all four can
use the claim without being misled by it.
The conditions are the “if” clauses, each of which is true or false in a
given case. THM-004 has four numbered conditions, and if a deploy‐
ment fails any one of them, the theorem says nothing about it. A pilot
used by one team for a few weeks has not been scaled into daily opera‐
tions, so it fails the first condition. The theorem therefore neither
requires governance for the pilot nor rules it out. Reading the conditions
first prevents a basic error: applying a formal claim where it was never
stated to hold.
The scope defines which cases the claim addresses. As presented in this
book, THM-004 states its scope before the word “if”: one defined de‐
ployment and its measurement boundary. The registry adds that the
theorem applies where an organization seeks economic control over the
resulting cost.9 The claim thus concerns one deployment within one
boundary, rather than an organization’s AI activity in general. To apply it
across a whole company, a manager must first show that each
deployment meets the conditions.
The non-claims identify what the claim deliberately does not establish.
THM-004 says that governance is necessary for control, but it does not
say that governance delivers control or is costless. It specifies neither
the scale at which the requirement begins to apply nor the size of the
exposure.10 It also does not establish Chapter 2’s three flows, which
belong to this book’s framework rather than the registry’s. The registry
9.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. THM-004’s
scope condition.
10.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. THM-004’s
recorded exclusions.

9

[[ PAGE 10 ]]

A I O P E R AT I O N S M A N A G E M E N T

records each claim’s non-claims. A reader with only the statement can
identify most of them by asking whether a requirement is sufficient or
merely necessary, whether the claim specifies an amount, and what it
says about cost.
The most costly misreading confuses
necessary with sufficient. A manager
who reads THM-004 as “governance
produces control” might buy a dash‐
board and expect costs to settle. The
theorem makes no such promise: it
says only that without governance,
there is no route to control. One level

DEFINITION

Non-claim
A conclusion a formal claim
deliberately does not establish,
though a reader might be
tempted to draw it. Stating the
non-claims prevents a claim from
being cited for more than it says.

down, LEM-020 makes the same limit
explicit: it does not claim that management mechanisms are
automatically effective.11
The falsifying case identifies what would show the claim to be wrong.
For a conditional claim, the test is precise: a case that meets every
condition but does not satisfy the conclusion. The second and third con‐
ditions describe what measurement and management would make pos‐
sible, rather than an apparatus already in place, so a deployment with
no instruments installed can still meet all four. For THM-004, the falsify‐
ing case would be a scaled deployment that meets all four conditions
and whose organization controls its cost without any measurement and
management apparatus. A flat-fee contract does not provide such a
case. If the fee covers every cost, the fourth condition fails; if it does
not, the organization would have to control the costs beyond the fee
without measuring them. A claim that names no falsifying case cannot
be wrong, and a claim that cannot be wrong tells a manager nothing.
These four parts answer an objection the formal style invites: that the
registry consists of word games, dressing obvious points in numbered
clauses. The common-sense version of THM-004 says that big deploy‐

10

[[ PAGE 11 ]]

A SCIENCE AND ITS DISCIPLINE

ments need cost controls, but it offers no answer for the one-team pilot
above because it never defines how big is big. The formal version gives
the manager a clear first task: check whether the deployment has
moved into daily operations. The pilot fails that condition, so the
theorem says nothing about it. The common-sense version also slides
easily from “needs controls” to “controls deliver control,” a misreading
the non-claims rule out. A formal statement fixes in advance what would
count as the claim being wrong. By stating its conditions, it makes the
claim testable and therefore open to improvement.

3.4 The discipline that acts on the science
Knowing what is true does not, by itself, change what an organization
does. Medicine depends on physiology, but clinicians must apply that
knowledge to treat patients. Engineering depends on physics, but engi‐
neers must work to codes and procedures to build a bridge. In each
case, a practice connects knowledge to results through its own
methods, roles, and standards.
AI Operations Management is that practice for AI consumption: the
work an organization does each week to manage what it consumes. The
organization buys AI capacity, plans its use, records that use, and
assigns it to the work it serves. It decides what runs when capacity is
short and holds spending accountable for what it returns. Chapter 1 de‐
scribed the problem as a category error. AI Operations Management re‐
solves that error by managing AI as a resource the organization
consumes rather than as software it has bought.
The discipline has five functions that
follow AI capacity through its life in
the organization: buying it, planning
its use, recording and assigning that
use, routing capacity to work, and
judging what it returns. Each function

11

DEFINITION

AI Operations
Management
The management discipline that
acts on AI Business Economics:
the practice by which an

[[ PAGE 12 ]]

A I O P E R AT I O N S M A N A G E M E N T

is a capability an organization either has
or lacks. Part III teaches all five, with
metering and attribution covered in two
chapters.

organization buys, plans, records,
assigns, allocates, and holds
accountable its consumption of
AI.

The first function, sourcing, matches the AI capacity an organization
buys to the work it needs to do. The organization must avoid both paying
for capability the work does not use and providing too little for work that
needs more. Sourcing determines which models and providers serve
which work, and on what terms. A company that sends every request to
its most capable model, including requests a smaller model would an‐
swer just as well, pays for capability its work does not use.
The second function is planning and budgeting, whose absence proved
costly in Chapter 2’s opening case. The organization must be able to
state how much AI it expects to consume in the coming period and rec‐
ognize when actual consumption departs from that expectation. In this
sense, a budget is a commitment made in advance that makes a devia‐
tion visible as it happens, rather than after the money is gone.
The third function, metering and attribution, builds what Chapter 2
called the record flow. The organization must record what was con‐
sumed and assign each unit of consumption to the team, product, or
purpose it served. Without that assignment, managers can see a cost
but cannot trace it to the work that caused it.
The fourth function is allocation and routing. When capacity is limited,
the organization must decide what runs first and direct each piece of
work to capacity that suits it. These decisions occur even when no one
makes them deliberately. If two workflows share a provider account
with a fixed rate limit, one waits whenever the other is busy. Allocation
and routing make that choice a matter of rule rather than accident.

11.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-020’s
recorded exclusions.

12

[[ PAGE 13 ]]

A SCIENCE AND ITS DISCIPLINE

The fifth function is holding value to account. Consider a constructed
example in which a support team adds an AI assistant to its help desk.
At the end of a quarter, the organization should be able to say whether
the assistant paid for itself by identifying what it cost, what it returned,
the months covered, and the outcome used to judge it. The registry’s
LEM-021, “ROI Evaluation Requires Measurement Boundary,” states the
requirement: “If ROI is evaluated for AI adoption, the evaluation re‐
quires a defined boundary for relevant costs, value, time period, and
observed or expected outcomes.”12 The organization must set that
boundary for each deployment and identify who is responsible for know‐
ing whether it paid for itself. This book calls it the value boundary.
Figure 3.2 shows the two layers together: the science forms the founda‐
tion, and the discipline builds on it through its five functions.
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

definitions, axioms, propositions, lemmas, theorems, linked by dependency

Figure 3.2 The two layers. AI Business Economics states what is true about consuming
AI. AI Operations Management acts on it through five functions, all taught in Part III.

The two layers depend on each other in different ways. A result about
governance changes nothing until an organization builds the apparatus
it describes, so the science needs the discipline to put its results into
practice. The discipline, in turn, needs the science because a practice
built on wrong claims fails however well it is run.
12.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-021’s
statement.

13

[[ PAGE 14 ]]

A I O P E R AT I O N S M A N A G E M E N T

3.5 Where the discipline ends
Chapter 1 set aside three subjects that lie close to AI but outside this
book: how models work, prompt engineering, and finding uses for AI.
Each has its own purpose and literature, and each ends before AI
Operations Management begins.
The first subject is how models work, including their architectures,
training, and internal behavior. It belongs to computer science and
machine learning engineering and ends where a model becomes a ser‐
vice an organization can call. AI Operations Management begins with
that call, where each use consumes resources and costs money.
The second subject is prompt engineering, the craft of writing inputs
that produce better outputs. It improves individual uses of AI, while AI
Operations Management governs those uses together: how many there
are, what they cost, and what they return. A better prompt can lower the
cost of one request, but only the discipline can say whether the organi‐
zation’s requests, taken together, are worth their cost.
The third subject is finding uses for AI: deciding which business prob‐
lems it might solve. That work belongs to strategy and innovation and
ends when a use is chosen. AI Operations Management begins with buy‐
ing capacity for that use and continues to manage it thereafter.
Four established disciplines lie closer still. Each manages work adjacent
to AI consumption, but each lacks something needed to govern its
economics. Table 3.1 compares them.

14

[[ PAGE 15 ]]

A SCIENCE AND ITS DISCIPLINE

                                                      WHAT IT             WHAT IT L ACKS FOR
NEIGHBOR             WHAT IT IS FOR                   MANAGES             THIS TERRITORY

AIOps                Applying machine learning    The health and          It uses AI to watch
                     to run IT operations:        performance of          systems. It does not
                     correlating events,          IT systems              govern what
                     detecting anomalies, finding                         consuming AI costs or
                     causes13                                             returns

MLOps                Building, deploying, and         The lifecycle of    It ships models. It does
                     monitoring machine               models an           not govern the
                     learning models in               organization        consumption of
                     production14                     builds              capacity an
                                                                          organization buys

FinOps               Financial accountability for Cloud and wider         It was built around
                     technology spending,         technology              cloud billing. A
                     through collaboration        spending                practitioner told its
                     among engineering, finance,                          own survey that no one
                     and business teams15                                 could yet say whether
                                                                          AI provides value

Regulatory AI        Ensuring that uses of AI are     Risk and            It asks whether a use is
governance           lawful, safe, and                compliance          permitted, not whether
                     accountable to regulators                            it is economically
                                                                          managed

Table 3.1. The four neighboring disciplines. Each manages something
adjacent to AI consumption, and none was built to govern its economics.

FinOps is the nearest neighbor, making its border with AI Operations
Management the hardest to draw. It already manages spending, has
moved toward AI, and defines its purpose in terms of maximizing
technology’s business value.16 Chapter 14 examines how the two divide
the work. Their border rests on what each was built to do, rather than on

13.
    Gartner, “AIOps (Artificial Intelligence for IT Operations),” Gartner Information Technology
Glossary, accessed October 1, 2026. The originating definition of AIOps.
14.
   Dominik Kreuzberger, Niklas Kühl, and Sebastian Hirschl, “Machine Learning Operations
(MLOps): Overview, Definition, and Architecture,” IEEE Access 11 (2023): 31866-31879. Definition
and scope of MLOps.
15.
    FinOps Foundation, “What is FinOps?,” accessed October 1, 2026. The Foundation’s own
definition of the practice.
16.
   FinOps Foundation, “What is FinOps?,” accessed October 1, 2026. The Foundation’s definition,
which names business value.

                                                 15

[[ PAGE 16 ]]

A I O P E R AT I O N S M A N A G E M E N T

intent: FinOps was built to make cloud bills accountable after capacity
had been used. AI Operations Management manages consumption me‐
tered by the request and judges it against a value boundary set before
spending begins.
Regulatory governance determines whether an organization may use AI
in a given way. This book takes that answer as given and asks how the
organization manages the permitted use.

3.6 Five questions the discipline exists to answer
AI Operations Management exists to answer five questions an organiza‐
tion cannot answer without the discipline. Each question belongs to one
of the five functions and is answered in the chapter that teaches it. Part
III presents the functions in a different order, for reasons explained
there.
An organization that manages its AI consumption can answer these five
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

16

[[ PAGE 17 ]]

A SCIENCE AND ITS DISCIPLINE

Question 5. “Where, exactly, does this AI flow pay for itself, and who is
on the hook for knowing?” This is the value boundary question,
answered in Chapter 12.
These are the Founding Questions, and their essential qualification is
“from its own records.” An organization can produce an answer by ask‐
ing the provider, making an estimate, or repeating the business case.
Each approach produces a number, but none produces knowledge the
organization holds and can check.
A reader who has finished Part I has no method yet for answering these
questions from records. Parts II through IV provide that method: Part II
establishes what is true, Part III builds the five functions, and Part IV
turns them into an institution.
CRAFT SECTION

The trace procedure
The trace procedure guides a manager through a formal claim before re‐
lying on it. In six steps, it turns a theorem from a conclusion to accept or
reject as a whole into a set of smaller claims that can each be checked.
Step 1. Locate the claim in the registry by its identifier and record its
name exactly as the registry gives it.
Step 2. State its scope, then restate each condition in ordinary business
language, retaining every antecedent and adding none.
Step 3. List the claims it depends on by identifier and name.
Step 4. Move one level down. Restate each dependency in one sentence
and note any condition it adds that the claim above did not state.
Step 5. State what the claim establishes and, separately, what it does
not.
Step 6. Name the falsifying case: a case that meets every condition but
does not satisfy the conclusion.

17

[[ PAGE 18 ]]

A I O P E R AT I O N S M A N A G E M E N T

Steps 2 and 6 do most of the work. Step 2 is where an antecedent can
be lost in restatement, producing a claim the registry does not make.
Step 6 tests whether the reader has understood the claim: anyone who
cannot describe the case that would defeat it cannot say what it rules
out.
Applied to THM-004, the procedure reveals a requirement of authority
at step 4 that the theorem’s wording does not show. The following trace
demonstrates how.
Step 1 records THM-004, “Scaled AI Deployment Requires Cost
Governance for Economic Control.”
Step 2 restates the conditions. Within one deployment and its measure‐
ment boundary, the theorem applies when four conditions hold: scaling
expands the places where usage can occur; measurement makes activi‐
ty that costs money visible; management mechanisms can be applied to
that visible activity; and total cost exceeds the price of access.
Step 3 lists the four dependencies: LEM-016, LEM-002, LEM-020, and
LEM-006, one for each condition. The registry marks all four as required.
Some claims also have contextual dependencies, which bear on the
claim without being conditions of it. Problem P2 provides an example.
Step 3 records which kind each dependency is.
Step 4 restates each dependency. LEM-016 says that moving from iso‐
lated use into repeated operations can increase the number of usage
events and demand points. LEM-002 says that measured and recorded
activity becomes observable enough to support analysis, attribution,
monitoring, or management. LEM-020 says that monitoring, limits, attri‐
bution, or other management mechanisms can be applied to visible us‐
age or exposure. LEM-006 says that a buyer who incurs several kinds of
cost pays more in total than the access price.

18

[[ PAGE 19 ]]

A SCIENCE AND ITS DISCIPLINE

Step 4 also asks what each dependency adds. LEM-020’s scope requires
the organization to have reliable visibility and the authority to apply
management mechanisms.17 That requirement belongs to the scope, not
to the third condition. A team that can see its costs but has no authority
to cap them falls outside LEM-020’s scope. The lemma therefore does
not support THM-004’s third condition for that team, and the theorem
says nothing about it. The team is in the same position as the pilot in
Section 3.3, which fails the first condition. The trace has revealed a limit
that the theorem’s wording does not show.
Step 5 separates what the claim establishes from what a reader might
infer. THM-004 establishes that cost governance is necessary for eco‐
nomic control of a scaled deployment. It does not establish that gover‐
nance is sufficient or costless, specify the scale at which the require‐
ment applies or the size of the exposure, or establish that a deployment
has three flows.
Step 6 names the falsifying case: a scaled deployment that meets all
four conditions and whose organization controls its cost without a mea‐
surement and management apparatus. Finding such a case would show
the theorem to be false.
The procedure is deliberately slow: tracing a theorem takes longer than
reading it and agreeing with it. That time is worth spending once for
each claim a decision rests on, because the trace shows a manager
exactly what supports the decision.

Chapter summary
AI Business Economics is the science of consuming AI: an ordered body of
conditional claims, each stating when it applies, what it concludes, and
which other claims it depends on. The claims are linked by dependency in a
registry, and this book presents and cites only certified claims.
17.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-020’s
scope condition.

19

[[ PAGE 20 ]]

A I O P E R AT I O N S M A N A G E M E N T

The registry justifies this book, but it does not organize it. The chapters
follow the order in which a manager needs to learn. The registry supports
each result, allowing a reader who doubts a claim to trace its support.
A trace follows a claim down through the registry, from a theorem to its
supporting lemmas and propositions. It turns a conclusion into a set of
smaller claims that can each be examined.
Read a formal claim in four parts: its conditions, its scope, its non-claims,
and the falsifying case that would defeat it. A formal statement fixes in
advance what would count as the claim being wrong.
AI Operations Management acts on the science through five functions:
sourcing, planning and budgeting, metering and attribution, allocation and
routing, and holding value to account at a boundary. It begins where a
model becomes a service an organization consumes and borders AIOps,
MLOps, FinOps, and regulatory governance, while remaining distinct from
each.
The Founding Questions are the five questions the discipline exists to
answer from an organization’s own records. At the end of Part I, the reader
has no method yet for answering them.

Key terms
AI Business Economics
The science of the business economics of consuming AI: an ordered body of
conditional claims, each stating when it applies, what it concludes, and which
other claims it depends on.

AI Operations Management
The management discipline that acts on AI Business Economics: the practice
by which an organization buys, plans, records, assigns, allocates, and holds
accountable its consumption of AI.

20

[[ PAGE 21 ]]

A SCIENCE AND ITS DISCIPLINE

Registry
The structured record of every definition, assumption, and result in AI Business
Economics, with each result linked to the claims that support it.

Theorem
A registry result that combines lemmas into a conclusion with direct
consequences for management. The book presents each theorem it relies on in
a numbered panel.

Lemma
An intermediate registry result that combines propositions, and sometimes
other lemmas, to support one or more theorems.

Proposition
A single registry claim, accepted on the basis of the definitions, axioms, or
earlier claims it names as support. Lemmas combine propositions.

Certified claim
A registry claim that passes the validator’s fixed conditions and whose
dependencies are all certified. The book presents and cites only certified
claims.

Trace
Following a registry claim down through the claims it depends on, from a
theorem to its lemmas and from a lemma to its propositions.

Dependency
A claim that another claim rests on. A required dependency is one the claim
cannot hold without. A contextual dependency bears on the claim without
being one of its conditions.

21

[[ PAGE 22 ]]

A I O P E R AT I O N S M A N A G E M E N T

Condition
A requirement a deployment must meet for a formal claim to apply to it. A claim
says nothing about a case that fails any of its conditions.

Scope
The part of a formal claim that defines which cases it addresses, such as one
deployment within one boundary. A case outside that scope is outside the
claim, regardless of whether it meets the conditions.

Non-claim
A conclusion a formal claim deliberately does not establish, though a reader
might be tempted to draw it. Stating the non-claims prevents a claim from
being cited for more than it says.

Falsifying case
A case that meets every condition of a formal claim but does not satisfy its
conclusion. Finding such a case would show the claim to be wrong.

Value boundary
The boundary within which an organization judges whether a deployment pays
for itself, defined by the costs and value it counts, the period it covers, and the
outcomes used to judge it. LEM-021 states that any evaluation of return on AI
requires such a boundary.

Founding Questions
The five questions AI Operations Management exists to answer from an
organization’s own records, one for each of its five functions.

22

[[ PAGE 23 ]]

A SCIENCE AND ITS DISCIPLINE

Trace procedure
The six-step method for reading a formal claim before relying on it: locate it,
state its scope and restate its conditions, list its dependencies, move one level
down, distinguish what it establishes from what it does not, and name the case
that would defeat it.

Discussion questions and problems
DISCUSSION QUESTIONS

1

The book insists that the registry justifies the book but does not organize
it. Describe what a reader would lose if the chapters instead followed the
order in which the registry derives its results.

2

Of the four borders in Table 3.1, which is hardest to defend, and why?
State what evidence would move that border.

3

Restate one Founding Question in the language your chief financial officer
would use, without losing any of its content. Then identify which part of
the question you were most tempted to drop.

4

Chapter 2 diagnosed a deployment through its three flows. Match each
flow to the functions in Section 3.4 that act on it, then explain which flow
draws on the most functions and why.

PROBLEMS
P1 · WORKED

A trace of LEM-020
The craft section traced a theorem. Use the same six steps to trace one of its
lemmas, LEM-020, as a model for problem P2.
Step 1. LEM-020, “Visibility Enables Management Mechanisms.” Its statement
reads: “If economic exposure or usage activity is visible to the relevant actor,
then monitoring, limits, attribution, or management mechanisms can be
applied within the relevant scope.”

23

[[ PAGE 24 ]]

A I O P E R AT I O N S M A N A G E M E N T

Step 2. When the people responsible for a deployment can see its usage or its
cost, they can apply monitoring, limits, attribution, or other management
mechanisms to it.
Step 3. The lemma has eight dependencies, all required: LEM-002 and seven
propositions, PROP-032, PROP-039, PROP-041, PROP-042, PROP-043,
PROP-053, and PROP-085.
Step 4. LEM-002 says that recorded activity becomes observable enough to
support analysis, attribution, monitoring, or management. It adds a condition:
the record must be detailed enough for the relevant person to observe the ac‐
tivity.18 PROP-032 says that compute use can be measured. PROP-039 says
that measured compute use can inform methods for assigning cost. PROP-041
says that metering a resource or activity records one or more measurements of
it, while PROP-042 says that measured activity can be distinguished by quanti‐
ty. PROP-043 says that metering produces records of what was metered.
PROP-053 says that monitoring can be used to observe economic exposure,
adding the condition that there is exposure to observe. PROP-085 says that
once usage is visible, management decisions can draw on it. Together, these
claims explain why visibility makes management possible.
Step 5. LEM-020 establishes that visibility makes management mechanisms
available. It does not claim that those mechanisms work automatically or that
visibility alone determines the right policy or price.19
Step 6. The falsifying case is an organization that can see a deployment’s usage
and has the authority to manage it, yet cannot apply any monitoring, limit, or
attribution to it.
P2 · COMPLETION

A trace with two steps left open
THM-002, “AI Adoption Cost Is Underestimated When Access Price Is Treated
as Total Cost,” states a result that Part II will teach. Its statement reads: “If
buyer AI adoption cost includes cost categories beyond access price, and ROI
evaluation requires a defined measurement boundary for cost and value, then
18.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-002’s
scope condition.
19.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. LEM-020’s
recorded exclusions.

24

[[ PAGE 25 ]]

A SCIENCE AND ITS DISCIPLINE

treating access price as total adoption cost creates underestimation risk within
the evaluation boundary.” Steps 1, 2, 3, and 6 are worked below. Complete
steps 4 and 5.
Step 1. THM-002, as named above.
Step 2. When a buyer’s cost of adopting AI includes costs beyond the access
price, and evaluating the return requires a boundary covering both cost and
value, treating the access price as the whole cost risks understating adoption
cost.
Step 3. The theorem has four dependencies: LEM-006 and LEM-021 are re‐
quired, while LEM-002 and LEM-020 are contextual. LEM-006 appears in the
craft section. LEM-021, “ROI Evaluation Requires Measurement Boundary,”
reads: “If ROI is evaluated for AI adoption, the evaluation requires a defined
boundary for relevant costs, value, time period, and observed or expected out‐
comes.” LEM-020 illustrates how a contextual dependency contributes: it bears
on what a buyer can do about an understated cost once that cost is visible, but
the claim that the cost is understated holds without it.20
Step 4. Restate each dependency in one sentence and note any condition it
adds.
Step 5. State what THM-002 establishes and what it does not. Then use the
treatment of LEM-020 in step 3 as a model to explain what LEM-002 contrib‐
utes, given that the theorem does not depend on it as a condition.
Step 6. The falsifying case is a buyer whose adoption cost includes categories
beyond the access price and who evaluates the return within a boundary cover‐
ing cost and value. The buyer treats the access price as the total adoption cost,
yet the cost is not understated.
P3 · INDEPENDENT

A reply to the word-games objection
A senior colleague reads THM-004 and says: “This is common sense in num‐
bered clauses. Anyone who has run a large deployment knows you need con‐
trols. Formalizing it adds nothing.” Write a one-page reply using the four parts
of a formal claim from Section 3.3. Identify at least one thing the formal state‐
20.

AI Business Economics registry, “dag.aiom, commit 9d7ee50,” August 21, 2026. THM-002’s
dependencies and their recorded roles.

25

[[ PAGE 26 ]]

A I O P E R AT I O N S M A N A G E M E N T

ment allows the colleague to do that the common-sense version does not. Do
not argue that the colleague is wrong about the conclusion.
Interleaving: question 4 requires Chapter 2’s three flows, and the cumulative case below
requires both earlier chapters.
PA R T I C U M U L AT I V E C A S E
C U M U L AT I V E C A S E · PA R T I

One announcement, three readings
D AT E D : F E B R U A R Y 2 0 2 4 . T H E C O M PA N Y ’ S O W N
A N N O U N C E M E N T, U S I N G I T S O W N F I G U R E S . O N LY T H AT
ANNOUNCEMENT IS USED HERE.
In February 2024, the payments company Klarna announced results from the
first month of an AI assistant built on OpenAI’s models. The company reported
that the assistant had handled 2.3 million conversations, accounting for twothirds of its customer-service chats. It estimated that the assistant was doing
the work of 700 full-time agents. Customers resolved their questions in under
two minutes, compared with eleven minutes previously. Klarna estimated that
the assistant would improve its profit by $40 million in 2024.21
Work from this announcement alone.
First, apply Chapter 1’s consumption-event inventory. Identify the consumption
events the announcement describes and where each is metered.
Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and
cost-and-value flows, identifying the evidence behind each diagnosis.
Third, apply each of the five Founding Questions to the announcement. For each
question, state whether the public record provides an answer drawn from the
organization’s own records and identify the record needed to answer it.
Keep your answers, as the case returns in Chapter 6.

21.

Klarna, “Klarna AI assistant handles two-thirds of customer service chats in its first month,”
February 27, 2024, accessed October 1, 2026. All figures in this case are the company’s own, as
announced.

26

<<<<< END DOCUMENT 1 >>>>>

<<<<< BEGIN DOCUMENT 2: CLAIM PACKET >>>>>

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


<<<<< END DOCUMENT 2 >>>>>

END OF PACKAGE. Now produce your fact check in the format given in Part 2.
