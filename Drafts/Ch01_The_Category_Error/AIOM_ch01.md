# Chapter 1. The Category Error

*Part I: The Argument. Content-first draft v1 (voice-lock review). Figures are described in place for the later render pass. Anchor theorem THM-009 is quoted verbatim from Locked Registry v1.3.*

---

## Opening case: Two subscriptions, one correction

::: provenance
Cursor pricing change, June 2025; GitHub Copilot billing transition, June 2025 to June 2026. Public sources, cited in full at the end of this chapter.
:::

In the spring of 2025, a software team at a mid-size company was doing what thousands of teams were doing: paying twenty dollars per developer per month for an AI coding assistant called Cursor, and treating that line on the budget the way it treated every other software line. The tool was useful. The price was small. The arrangement was, on its face, a subscription like any other, filed next to the ticketing system and the design software and the password manager. Nobody in finance thought about it again after signature, because nothing about a twenty-dollar seat asks to be thought about.

Then, in June 2025, the arrangement changed underneath them. Cursor revised its pricing so that the flat monthly allotment became metered usage billed at the underlying model rates. For light users the change was invisible. For the team's heaviest users, the people getting the most value, the monthly allowance was consumed in a matter of prompts, after which usage continued to bill against real rates. Charges arrived that no one had planned for. The company's chief executive published an apology and an explanation. The explanation was not an excuse. It was an account of arithmetic: the upstream cost of serving heavy users under a flat price had become untenable, and the flat price had to go (Truell, 2025).

The same pattern, in the same window, played out at a far larger scale and with no apology at all. GitHub Copilot, the most widely adopted AI coding assistant in the world, spent the year from June 2025 to June 2026 dismantling its own flat model in two acts. First it capped request types that had effectively been unlimited. Then, across a paid base reported at 4.7 million subscribers, it retired flat "premium requests" entirely and moved billing to token-denominated credits (GitHub, 2025; GitHub, 2026). One vendor corrected its pricing with a public apology. The other corrected its pricing in two quiet steps across millions of accounts. The correction was the same.

Set the two episodes side by side and the shared feature is not the apology, the timing, or the size of the vendor. The shared feature is what broke. In both cases a product had been sold, and bought, as software: a seat, a flat price, a cost fixed at signature. In both cases the thing underneath the seat turned out to obey a different law. It consumed a resource on every use, the resource had a real and variable cost, and heavy use ran that cost past the flat price. When the gap grew large enough, the price changed. It changed on the provider's schedule, not the buyer's, and it changed whether or not the buyer had ever looked at a meter.

The buyers in these stories did not make an error of vendor selection. Cursor and Copilot were, and are, excellent tools. The buyers made an error of category. They filed a metered resource under the mental model they use for licensed software, and the mental model held right up until the moment it did not. This chapter is about that error: what it is, why it was reasonable, and what the organization actually purchased when it thought it was buying software.

---

## Teaching body

### 1.1 The purchase that is not one

The buyer brought a model to the transaction, and it was a good model, refined over three decades of enterprise software procurement. In that model, software is a license. The organization buys the right for a defined number of people to use a program. The marginal cost of an additional use, once the seat is paid for, is approximately zero: a licensed user who runs the program a thousand times a day costs the vendor essentially the same as one who runs it once a week. Cost is therefore fixed at signature. The negotiation that matters happens once, at purchase, over the number of seats and the price per seat. After that, management of the software is management of access: who has a login, how many seats are active, when the contract renews.

This model is not wrong about licensed software. It is wrong about the thing now being sold under the same packaging. What the organization operates when it deploys an AI assistant is not a program that people are licensed to run. It is work that consumes a metered resource on every task. Each use sends a request to a model, the model performs computation to answer it, and that computation has a cost that scales with the size of the request and the size of the answer. The marginal cost of an additional use is not approximately zero. It is the central fact.

The consequence is a mismatch between what the organization manages and what the organization operates. Access management asks how many people may use the tool. Resource management asks how much of the resource the work consumes, at what cost, for what return. An organization that manages access while operating a metered resource is managing the wrong quantity. It counts seats while the bill is written in tokens. The mental model determines what gets managed, and the wrong model manages the wrong thing.

### 1.2 The consumption event

::: definition consumption event
A request that consumes computational resource, metered in tokens or their equivalents, at a per-event cost greater than zero.
:::

The discipline that follows in this book is built on a single atomic unit, and it is worth defining precisely before anything is built on top of it. A **consumption event** is a request that consumes computational resource, metered in tokens or their equivalents, at a per-event cost greater than zero. Every deployed use of AI, at bottom, is a stream of these events. They are the thing the meter counts, the thing the invoice sums, and the thing every later chapter learns to source, record, attribute, budget, allocate, and hold accountable.

The anatomy of one event is simple and worth holding in view. Something goes in: a prompt, a document, a conversation history, retrieved reference material. The model performs computation. Something comes back: a completion, a suggestion, an answer, a tool call. A meter records what was consumed, typically the count of input tokens and output tokens, and sometimes the calls to retrieval or tools that the event triggered. And a record of that consumption is held somewhere. In the ordinary case, it is held by the provider, and the buyer sees only its monthly summation on an invoice.

::: figure 1.1
caption: Two purchase models.
src:

A two-panel figure. Left panel, "Seat model": a horizontal line, cost flat against rising usage, labeled to show that a licensed user who uses the software heavily costs the same as one who barely uses it. Right panel, "Event model": a rising line, cost as the accumulating integral of consumption, each consumption event adding area under the curve, labeled to show that total cost is the sum of events, not a property of headcount. The two panels share a horizontal usage axis so the reader sees the same usage producing a flat cost on the left and a rising cost on the right.
:::

::: figure 1.2
caption: Anatomy of a consumption event.
src:

A single event drawn as a pipeline: inputs on the left (prompt, context, retrieved material), the model in the center, outputs on the right (the returned response), and beneath the pipeline a meter capturing the resource drivers (input tokens, output tokens, calls, retrieval, tool invocations). A callout marks who holds the record: the provider, with the buyer receiving an invoice.
:::

The seat model and the event model are not two views of the same economics. They are two different economics, and Figure 1.1 draws the difference the invoice hides. Under the seat model, cost is a horizontal line: usage rises and cost does not follow. Under the event model, cost is the area under the usage curve: every event adds to the total, and heavy use is expensive by construction. A buyer operating on the left panel while the right panel governs the bill will be surprised, and the surprise will arrive as a number, on a schedule the buyer did not set.

### 1.3 The flat-rate objection, answered

::: evidence
tag: Vendor disclosure
date: January 2025

The chief executive of the largest provider disclosed that the flat-rate Pro plan was losing money because subscribers used it more than the price had assumed (Altman, 2025).
:::

There is a strong objection to everything said so far, and it deserves to be stated at full strength rather than in a weakened form built to be knocked down. The objection is this: "We pay thirty dollars per seat per month. The price is flat. We are never billed by the token. For us, this simply is software, and your consumption framing is an abstraction that describes someone else's problem."

The objection is not confused, and the answer is not that the buyer is billed by the token after all. The answer is that a flat rate relocates the meter; it does not abolish it. When a provider offers a flat price for a metered resource, the provider does not stop metering. The provider meters exactly what the buyer has declined to see, and prices the flat rate against an assumption about how much the average buyer will consume. That assumption is a bet. It holds while usage stays near the average the price assumed. It fails when usage is skewed, when a minority of heavy users consume a majority of the resource, because the flat price collected from everyone no longer covers the resource consumed by the few. At that point the arrangement is unstable, and the instability resolves in one direction: the provider corrects the price. The correction arrives on the provider's schedule, because the provider holds the meter and the buyer does not.

This is not a claim about badly run vendors. It is a structural result, and the registry states it as a theorem.

::: theorem THM-009
AI Use Is Resource Consumption, Not Merely Software Access

If an AI activity requires compute and executing that activity consumes resources, production scaling expands the usage surface of AI deployment, buyer total cost extends beyond access price, and measurement enables visibility into resource use or cost-bearing activity, then AI use in a deployed business context is resource-consuming operating activity, not merely software access, within the relevant deployment and cost boundary.
:::

The theorem does not say that a flat rate is impossible or that every subscription will be repriced tomorrow. It says something narrower and more durable: that in a deployed business context, where the activity requires compute, where scaling expands the surface of use, and where total cost runs past the access price, the thing being operated is a resource-consuming activity rather than software access. The flat rate is a way of packaging that activity for sale. It is not evidence that the activity is something else. The buyer who reads the flat rate as proof of software access has mistaken the packaging for the contents.

The public record already contains the correction running its course. In January 2025, the chief executive of the largest provider disclosed that the flat-rate Pro plan was losing money because subscribers used it more than the price had assumed (Altman, 2025). In July 2025, Anthropic introduced and then tightened usage limits on its Claude Code offering, adjusting the constraints during the cycle rather than at renewal (Anthropic, 2025). And the two episodes that opened this chapter, Cursor and GitHub Copilot, are the same result reached across the two most widely used AI coding subscriptions inside twelve months. The flat rate did not make the meter disappear. It moved the meter to the provider's side of the table and moved the correction to the provider's calendar.

### 1.4 What follows if this is true

Accept the category, and a great deal follows without further argument. Resources that flow through an organization have long been the object of a mature management discipline, and the reader already knows its shape from physical goods. A manufacturer does not manage its steel by counting the people licensed to touch it. It sources the steel against requirements, plans and budgets its consumption, tracks where it goes, allocates it under constraint when supply is tight, and holds the finished output accountable for the material it consumed. Sourcing, planning, metering, allocation, accountability: these are the functions any organization performs on a resource that flows and costs money as it flows.

Deployed AI is such a resource. It flows through the organization as a stream of consumption events, it costs money as it flows, and its cost accrues by default while its value accrues only by design. Yet no equivalent discipline exists for it. Organizations that would never let a material flow through the plant unmetered let the AI flow through the work unmetered, because the packaging told them it was software and software does not flow. The gap between the resource and the discipline it lacks is the reason this book exists. The remaining chapters build the discipline, function by function, on the foundation this chapter has just laid.

### 1.5 What this book is not

A word on the borders of the subject, stated once and briefly here, with the full treatment reserved for Chapter 3. This book is not about the internals of models, and the reader will find no account here of architectures, training, or weights. It is not about prompt engineering, and it offers no techniques for extracting better outputs from a given model. It is not about use-case ideation, and it will not help the reader decide which problems to point AI at. Those are real subjects with their own literatures. This book is about the economics of the resource once the decision to deploy has been made: what it consumes, what it costs, and how an organization governs both. The neighbors of that subject, and the exact line this book draws against each of them, are the business of Chapter 3.

---

## Craft section: The consumption-event inventory

The reader has now met the consumption event as a definition. The first craft artifact of the book turns the definition into a procedure the reader can run against any deployment. The **consumption-event inventory** takes a description of an AI deployment and produces a structured account of what that deployment consumes, where the meter sits, and what the organization's seat count conceals. It is the first artifact the reader produces, and every later artifact in the book assumes it.

The procedure has four steps.

**Step 1. Enumerate the event types.** Given a deployment description, list the distinct kinds of consumption event the deployment generates. A deployment rarely produces one kind of event; it produces several, each with its own trigger and its own resource profile.

**Step 2. Identify each type's resource drivers.** For each event type, name what actually consumes resource: input tokens, output tokens, the number of calls, retrieval operations, and tool invocations. The driver is what the bill scales with, and it is almost never the number of people.

**Step 3. Locate the meter.** State where the metering happens and who holds the record. In the ordinary case the meter is on the provider's side, and what the buyer receives instead of a meter is an invoice.

**Step 4. State what the inventory reveals that the seat count conceals.** Name the quantity that actually drives cost, and contrast it with the quantity the organization currently tracks.

### Worked example: a contact-center assistant

Consider a customer-support organization that has deployed a generative AI assistant across its contact center. For each incoming customer message, the assistant drafts a suggested reply that the agent may edit and send; the assistant draws on a knowledge base and on the conversation so far. The deployment covers a large agent population, on the order of five thousand agents, and the organization currently accounts for it as a per-seat tool. (This is the deployment studied by Brynjolfsson, Li, and Raymond, 2025, which returns in Chapter 6 as the book's anchor case on realized value. Here it serves only as a deployment to inventory.)

**Step 1. Event types.** The deployment generates at least three: (a) a suggested-reply generation, triggered each time an agent asks the assistant to draft a response to a customer message; (b) a knowledge retrieval, triggered when the assistant pulls reference material to ground a suggestion; and (c) a conversation-close operation, where the deployment summarizes or tags the resolved conversation.

**Step 2. Resource drivers.** For suggested-reply generation, the drivers are input tokens (the system instructions, the retrieved knowledge, and the conversation history assembled into the prompt) and output tokens (the drafted reply). The volume driver is the number of customer messages that receive a drafted reply, which scales with contacts multiplied by the number of turns per contact. For knowledge retrieval, the drivers are the number of retrieval calls and the tokens those calls embed and return. For the conversation-close operation, the drivers are input tokens (the full conversation) and output tokens (the summary or tags), scaling with the number of resolved conversations.

**Step 3. The meter.** All three event types are metered on the provider's side, by token for the generation and close operations and by call and token for retrieval. What the organization receives is a monthly invoice, and beneath its per-seat plan, a seat count.

**Step 4. What the seat count conceals.** The seat count treats the agent population as a set of equal units, five thousand seats at one price. The bill does not behave that way. Cost scales with the number of customer messages drafted, the length of the conversations, and the token footprint assembled per turn, none of which the seat count records. Two agents on identical seats can consume very different amounts of resource: a high-volume agent handling long, reference-heavy conversations generates many times the consumption of a low-volume agent, at the same seat cost. The quantity that drives the bill is tokens per resolved contact. It does not appear on the seat line, and until the inventory names it, the organization is managing a number that does not govern its cost.

The inventory has done its work when the organization can see, for the first time, the shape of what it is buying: not five thousand seats, but a flow of consumption events whose volume and intensity, not whose headcount, determine the bill.

---

## Chapter summary

The reader can now name the category error at the root of AI cost surprise, distinguishing the software access model, in which cost is fixed at signature and management is management of seats, from the resource consumption model, in which cost is the accumulating sum of metered events and management is management of a flow. The reader can define the consumption event as the discipline's atomic unit, answer the flat-rate objection by showing that a flat price relocates the meter to the provider rather than abolishing it, and cite the structural result, THM-009, that a deployed AI activity is resource-consuming operating activity rather than software access. And the reader can run the consumption-event inventory against a deployment description, producing the event types, their resource drivers, the location of the meter, and the cost driver the seat count conceals. What the reader cannot yet do is manage the flow the inventory reveals. That requires seeing the deployment as flows rather than events, which is the work of Chapter 2.

---

## Key terms

Consumption event
: A request that consumes computational resource, metered in tokens or their equivalents, at a per-event cost greater than zero. The atomic unit of the discipline.

Resource consumption (model)
: The economic model in which deployed AI is a metered resource consumed on every task, with cost accruing per event; contrasted with the software access model.

Software access model
: The economic model, inherited from licensed software, in which cost is fixed at signature and the marginal cost of additional use is approximately zero; management is management of access.

Access price
: The stated price of access to an AI capability, per seat or per subscription, distinct from the total cost of consuming the resource behind it.

Metered resource
: A resource whose consumption is measured per unit of use, here in tokens or their equivalents.

Flat-rate objection
: The claim that a flat per-seat price makes AI equivalent to licensed software; answered by meter relocation.

Meter relocation
: The principle that a flat rate does not abolish the meter but moves it to the provider's side, where the provider prices the flat rate against assumed consumption and corrects it on its own schedule when usage is skewed.

---

## Discussion questions and problems

### Discussion questions

1. A colleague argues that because your organization pays a flat per-seat price and never sees a token bill, AI is a seat-priced good for you and the consumption framing does not apply. Explain, without appealing to any specific vendor's future behavior, why the per-seat contract does not make AI a seat-priced good.

2. The Cursor and GitHub Copilot episodes are often read as stories about two particular companies changing their prices. Explain what the two episodes, taken together, reveal about where the meter was all along, and why the pairing is harder to dismiss than either episode alone.

3. Construct the strongest version of the flat-rate objection yourself, in the voice of a capable skeptic who has read this chapter. Then answer it. Your answer should not depend on predicting that any particular subscription will be repriced.

### Problems

::: problem P1
The CIO memo. (worked)

A board member has written to the chief information officer arguing that the company is overcomplicating a simple software purchase and should stop tracking AI usage "like it's a utility." Write the CIO's one-page reply defending consumption economics against the flat-rate objection.

*Model reply.*
*Model reply.* "Thank you for the note. I want to agree with the part of it that is right and then explain the part that will cost us if we accept it. You are right that our current AI tools are billed to us at a flat per-seat price, and that this looks exactly like the software we have always bought. The reason I am tracking usage anyway is that the flat price is not a statement about our costs; it is a bet the vendor has made about our consumption. Behind the flat price, every use of these tools consumes a metered resource that costs the vendor real money, and the vendor prices the flat rate against an assumption about how much we will use. While our usage stays near that assumption, nothing happens. When our heaviest teams pull usage above it, the vendor's arrangement stops covering its costs, and it corrects the price. We have watched this happen across the two most widely used AI coding subscriptions inside a single year. Tracking our own usage is not utility theater. It is how we see the correction coming before it arrives as a number we did not plan for, and how we keep the timing of that correction from being entirely the vendor's to choose. I am not asking us to manage AI like plumbing. I am asking us to stop managing a metered resource as if it were a license, because the two behave differently exactly when the stakes are highest."
:::

*Annotated reasoning.* The reply concedes the true premise (the price is flat and looks like software) before contesting the inference, which disarms the objection rather than dodging it. It relocates the meter (the flat price is a bet against assumed consumption) rather than claiming a token bill the reader knows does not exist. It grounds the structural claim in the documented pattern rather than in a prediction about a specific vendor, satisfying the evidence standard. And it closes on the buyer's actual interest, the timing of the correction, which is the concrete thing consumption tracking buys.

**P2 (worked). Inventory a coding-assistant deployment.** A software organization has deployed an AI coding assistant to three hundred developers. The assistant offers inline code completions as developers type, answers chat questions in the editor, and runs multi-step agentic tasks on request. Produce the consumption-event inventory.

*Model inventory.* **Event types:** (a) inline completion, triggered continuously as developers type; (b) editor chat query, triggered when a developer asks a question; (c) agentic task run, triggered when a developer delegates a multi-step task. **Resource drivers:** inline completion is driven by input tokens (the surrounding code context sent for each completion) and output tokens (the suggested code), with a very high call count because completions fire constantly; chat query is driven by input tokens (the question plus code context) and output tokens (the answer); agentic task run is driven by input and output tokens across many model calls per task, plus tool invocations, and is the highest-intensity event by a wide margin. **Meter:** provider side, per token, with agentic runs additionally consuming tool calls; the buyer receives an invoice, and under a seat plan, a seat count. **What the seat count conceals:** cost is driven by completion frequency and, above all, by agentic run volume and length, not by the number of developer seats. A single developer who leans on agentic runs can consume more resource than a dozen who use only inline completion, at the same seat cost. The cost driver is tokens per developer per day, concentrated in agentic runs, and the seat line shows none of it.

**P3 (completion). Inventory a document-review deployment.** A legal operations team has deployed an AI assistant that, for each contract submitted, extracts key clauses, compares them against a policy playbook, and drafts a redline memo. Complete the inventory below by filling the blank column.

| Event type | Resource drivers | Meter location | What the seat count conceals |
|---|---|---|---|
| _______________ | Input tokens (full contract text), output tokens (extracted clauses); scales with contract length | Provider side, per token | Cost scales with document length, not reviewer headcount |
| _______________ | Input tokens (extracted clauses plus playbook), output tokens (comparison result); retrieval calls against the playbook | Provider side, per token and per call | A long playbook inflates every comparison regardless of seat count |
| _______________ | Input tokens (clauses, comparison, contract context), output tokens (the drafted memo); highest output-token event | Provider side, per token | The drafting step, not the reviewer, is the dominant cost driver |

*(Interleaving: none. This is the first chapter; problem sets begin reaching back to earlier chapters in Chapter 2.)*

---

## Sources referenced (this chapter)

- Altman, S. (2025, January). Public statement on OpenAI Pro subscription economics. [Primary source to be archived at citation pass; chase-list item.]
- Anthropic. (2025, July). Claude Code usage-limit announcement and mid-cycle tightening. [Primary source to be archived at citation pass; chase-list item.]
- Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *Quarterly Journal of Economics.* [Deployment description used for the craft worked example; returns as the Chapter 6 anchor case.]
- GitHub. (2025, 2026). Copilot pricing and request-model changes, including the migration from premium requests to credit-denominated billing. [Primary sources to be archived at citation pass; chase-list item.]
- Truell, M. (2025, June–July). Cursor pricing-change apology and explanation. [Primary source to be archived at citation pass; chase-list item.]

*Registry: THM-009 quoted verbatim from AI Business Economics Locked Registry v1.3 (Locked_Registry sheet).*
