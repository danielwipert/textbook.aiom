# AIOM Continuity Ledger

Owner: Dan (Chorus AI Systems). Maintained by `continuity.py`, the G3 gate.
Created 2026-08-05.

## What this is

The book is written one chapter at a time over a long period. Continuity drift
is therefore the default, not the exception: a term acquires a second definition
three chapters after its first, a promise made in Chapter 1 is never paid, a
lemma gloss is reworded because the earlier wording was not in front of the
drafter. Every one of those is cheap to prevent and expensive to discover at
manuscript integration, where the fix means reopening a locked chapter.

This ledger is the record G3 checks against. It holds, per chapter:

- **Terms owned.** The chapter that first defines a term owns it. A later
  chapter may use the term freely and may not redefine it.
- **Forward references made.** A promise that some later chapter will do
  something. Each is logged here when the promising chapter locks and marked
  paid when the promised chapter locks.
- **Registry glosses.** The wording used for a registry object. A recurring
  object is glossed identically every time.
- **Northmoor figures used**, so a figure can be diffed against generator
  output rather than trusted.
- **Founding Question and maturity-stage references**, checked verbatim against
  the canonical wording in section 2 below.

## Policy

1. **The ledger is appended at Stage 9, on lock, not at draft time.** A chapter
   still moving would write entries that later have to be retracted.
2. **G3 runs before lock and reads this file.** It fails on a redefinition, an
   unlogged forward reference, an unpaid promise assigned to the chapter under
   test, a reworded registry gloss, or a misquoted Founding Question or stage
   name.
3. **Entries are never edited to match a new chapter.** If a later chapter needs
   a different definition, that is a decision for Dan, recorded as a decision,
   and the earlier chapter is reopened. The ledger does not bend to make a gate
   pass.
4. **`continuity.py --update` writes the entries**, so the ledger reflects what
   the chapter actually contains rather than what someone remembered.

Usage:

```bash
python3 continuity.py <chapter.html> --chapter 1            # G3 check
python3 continuity.py <chapter.html> --chapter 1 --update   # append at lock
python3 continuity.py --pay 2                               # mark promises to Ch2 paid
```

---

## 1. Canonical invariants

These are copied from locked sources and are the reference G3 checks quotations
against. They are not editable here: change the source, then change this.

### The Founding Questions (locked, Decision 22; source: Workplan v5)

| # | Question | Function | Answered in | Maturity stage |
|---|----------|----------|-------------|----------------|
| 1 | Are you paying for capability you do not need, or starving work that needs more? | Sourcing | Ch7 | Governed |
| 2 | What do you expect the AI flow to consume next period, and how will you know when it deviates? | Planning and budgeting | Ch10 | Governed |
| 3 | Who consumed what last month, in service of which work? | Metering and attribution | Ch8, Ch9 | Visible, then Attributed |
| 4 | When capacity is constrained, who decides what runs first, and by what rule? | Allocation | Ch11 | Governed |
| 5 | Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing? | Value boundary | Ch12 | Accountable |

Structural device: posed at the end of Ch3, resolved once each across Ch7 to
Ch12, instrumentalized as the diagnostic in Ch13, re-asked as the ninety-day
plan's targets in Ch15.

### The maturity ladder (locked; source: AIOM_Maturity_Model_v1.md)

| Stage | Name | One-line test |
|---|---|---|
| 1 | Unmanaged | No Founding Question answerable with records. |
| 2 | Visible | The first half of Question 3: who consumed what. |
| 3 | Attributed | Question 3 fully answerable: in service of which work. |
| 4 | Governed | Questions 1, 2, and 4 answerable with records. |
| 5 | Accountable | Question 5 answerable: the flow answers for itself. |

Stage names are used exactly as written. "Governed" is cost governance in
THM-004's sense, and Chapter 13 fences off regulatory AI governance in one
sentence.

---

## 2. Terms owned

One row per term, owned by the chapter that first defines it. The definition is
recorded as given, whitespace normalized. A later chapter using the term does
not appear here; only the owner does.

| Term | Owner | Definition as given |
|---|---|---|

| Category error | 1 | The error of managing a metered resource as if it were licensed software. It rests on a false assumption: that the access price fixes the total cost. The tool is the right one and the vendor is not at fault. The economic model applied to the tool is wrong. |
| Consumption event | 1 | A single use of an AI system that consumes metered computing resources and creates an underlying cost greater than zero, whether or not the buyer is charged for it separately. A consumption event may be measured in tokens, requests, credits, compute time, or another equivalent unit. It is the basic unit of consumption tracked in AI Operations Management. |
| Resource consumption model | 1 | The economic model in which deployed AI is consumed as a metered resource. Each use creates a consumption event, and cost accrues with each event. It contrasts with the software access model. |
| Software access model | 1 | A purchasing model in which an organization pays a fixed price for access to software, usually per seat or subscription. Because additional use creates little or no additional cost, the organization manages who has access rather than how much of the software each user consumes. |
| Access price | 1 | The stated amount an organization pays for the right to use an AI capability, usually per seat or subscription. It does not include additional costs based on how much AI the organization actually uses. |
| Metered resource | 1 | A resource whose consumption is measured per unit of use, here in tokens or their equivalents. |
| Flat-rate objection | 1 | The claim that a flat per-seat price makes AI equivalent to licensed software; answered by meter relocation. |
| Meter relocation | 1 | The placement of consumption metering on the provider’s side of a flat-rate subscription. The buyer pays a fixed price for access, while the provider continues to measure actual use. The provider sets the flat rate based on expected consumption and may change the price, allowance, or usage limits when actual consumption exceeds that expectation. |
| Flow | 2 | A continuous stream of related activity within a deployment, described by its rate, direction, and the records kept about it. An organization manages a flow by governing it over time rather than approving the deployment once. |
| Usage flow | 2 | The stream of consumption events a deployment generates, including requests made, work performed, and outputs returned. It is the only one of the three flows that an organization normally seeks to increase. |
| Record flow | 2 | The stream of information an organization keeps about its own usage, including which team or product consumed what, at what volume, and when. The provider always keeps a record because it must produce a bill. The buyer has a record only if it deliberately builds one. |
| Cost-and-value flow | 2 | The stream of money spent on a deployment together with the business return attributed to that spending. The two halves form one flow because neither can support an economic decision on its own. |
| Cost-value asymmetry | 2 | The condition in which metering records a deployment’s cost automatically, while its value is measured only when the organization has deliberately built a way to measure it. As a result, the organization may know precisely what the deployment costs without knowing what that spending produces. |
| Three-flow mapping | 2 | The diagnostic that establishes the condition of the usage, record, and cost-and-value flows in a named deployment. The mapping also identifies the evidence that would change each diagnosis. |
| AI Business Economics | 3 | The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on. |
| AI Operations Management | 3 | The management discipline that acts on AI Business Economics: the practice by which an organization buys AI capacity, plans its use, records and assigns consumption, allocates capacity, and holds that consumption to account. |
| Value boundary | 3 | The boundary within which an organization judges whether a deployment pays for itself, defined by the costs and value it counts, the period it covers, and the outcomes against which it measures performance. |
| Founding Questions | 3 | The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions. |
| Sourcing | 3 | The function that matches the AI capacity an organization buys to the requirements of its work: which models and providers serve which work, and on what terms. |
| Planning and budgeting | 3 | The function that states how much AI an organization expects to consume in a period and detects when actual consumption departs from that expectation. |
| Metering and attribution | 3 | The function that records what was consumed and assigns each unit of consumption to the team, product, or purpose it served. |
| Allocation and routing | 3 | The function that uses a stated rule to decide what runs first when capacity is limited and to send each piece of work to suitable capacity. |
| Holding value to account | 3 | The function that judges whether a deployment pays for itself within a value boundary set before spending begins and names one person responsible for knowing the answer. |
| Function audit | 3 | The six-step method for finding which of the five functions an organization performs for a deployment: list its AI activities; assign each to a function or a neighboring discipline; mark each function as performed, partly performed, or not shown; name who performs each; and state the first gap to close. |
<!-- CONTINUITY:TERMS -->

---

## 3. Forward references

A promise that a later chapter will do something. Logged when the promising
chapter locks; marked paid when the promised chapter locks and G3 confirms the
promise was kept.

| From | To | Promise | Status |
|---|---|---|---|

| 1 | 2 | This is the first chapter; problem sets begin reaching back to earlier chapters in Chapter 2. | paid |
| 1 | 3 | Each of these subjects has its own purpose and literature, and Chapter 3 explains where each ends and AI Operations Management begins. | paid |
| 1 | 4 | Chapter 4 examines these instruments in detail. | open |
| 1 | 6 | It returns in Chapter 6 as the book’s anchor case on realized value. | open |
| 1 | 14 | Chapter 14 distinguishes the subject of this book from these neighboring disciplines. | open |
| 2 | 1 | 4 Chapter 1 argued that a flat price relocates the meter to the provider rather than abolishing it. | paid |
| 2 | 1 | Chapter 1 defined its basic unit: the consumption event, a single use of an AI system that consumes metered computing resources. | paid |
| 2 | 1 | Chapter 1 described the problem as a category error, and Chapter 3 names the discipline that resolves it. | paid |
| 2 | 1 | Chapter 1 established that the provider always holds a meter, because the provider must bill and must manage its own capacity. | paid |
| 2 | 1 | Interleaving: question 4 and problem P2 require Chapter 1’s results. | paid |
| 2 | 1 | Public reporting does not establish whether Uber made the category error described in Chapter 1 or understood the cost model but failed to carry that understanding into its forecast. | paid |
| 2 | 1 | Uber’s experience makes the problem from Chapter 1 concrete. | paid |
| 2 | 3 | As Chapter 3 explains, the theorem formalizes the economic consequence of the third flow’s asymmetry; it does not establish the taxonomy itself. | paid |
| 2 | 3 | Chapter 1 described the problem as a category error, and Chapter 3 names the discipline that resolves it. | paid |
| 2 | 8 | Chapter 8 builds the record flow, and Chapter 10 turns that record into a budget. | open |
| 2 | 8 | It returns in Chapter 8, which builds the record flow that organizations are structurally most likely to skip. | open |
| 2 | 10 | Chapter 8 builds the record flow, and Chapter 10 turns that record into a budget. | open |
| 3 | 1 | Chapter 1 described the problem as a category error. | paid |
| 3 | 1 | Chapter 1 stated the conditions under which deployed AI is a resource the organization consumes. | paid |
| 3 | 1 | First, apply Chapter 1’s consumption-event inventory. | paid |
| 3 | 1 | One might treat Chapter 1’s Cursor licenses as a fixed software expense and the other as metered consumption. | paid |
| 3 | 2 | 4 Chapter 2 diagnosed a deployment through its three flows. | paid |
| 3 | 2 | Chapter 2 stated the conditions under which a scaled deployment cannot be controlled without a governing apparatus. | paid |
| 3 | 2 | Second, apply Chapter 2’s three-flow mapping. | paid |
| 3 | 2 | The second function is planning and budgeting, whose absence proved costly in Chapter 2’s opening case. | paid |
| 3 | 2 | The third function, metering and attribution, builds what Chapter 2 called the record flow. | paid |
| 3 | 6 | The case returns in Chapter 6. | open |
| 3 | 7 | “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7. | open |
| 3 | 10 | “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10. | open |
| 3 | 11 | “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11. | open |
| 3 | 12 | “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12. | open |
| 3 | 14 | Chapter 14 explains how FinOps and that practice divide the work. | open |
| 3 | 14 | Chapter 14 explains how the two divide the work. | open |
| 3 | 1 | 3.3 Where the discipline ends Chapter 1 set aside three related subjects: how models work, prompt engineering, and finding uses for AI. | paid |
| 3 | 1 | Chapter 1’s Cursor licenses show this check in practice. | paid |
| 3 | 1 | Chapter 1’s result does not say that every use of AI is consumption. | paid |
| 3 | 1 | It builds on Part I’s two earlier methods: Chapter 1’s consumption-event inventory lists what a deployment consumes, and Chapter 2’s three-flow mapping shows which flows are managed. | paid |
| 3 | 1 | [truell-2025-pricing] The Cursor post describing the plan change of June 16, 2025, as cited in Chapter 1. | paid |
| 3 | 2 | Chapter 2’s panel, THM-004, shows what such a result settles and what it leaves open. | paid |
| 3 | 2 | Interleaving: question 4 requires Chapter 2’s three flows, problems P1 and P2 audit Chapter 2’s cases, and the cumulative case below requires both earlier chapters. | paid |
| 3 | 2 | It builds on Part I’s two earlier methods: Chapter 1’s consumption-event inventory lists what a deployment consumes, and Chapter 2’s three-flow mapping shows which flows are managed. | paid |
| 3 | 2 | P2 · Completion An audit with three steps left open Chapter 2’s problem P3 described the Australian Government’s whole-of-government trial of Microsoft 365 Copilot, which ran from January to June 2024. | paid |
| 3 | 2 | Problems P1 · Worked An audit of the budget that ran out Chapter 2’s opening case described Uber’s deployment of Claude Code, which consumed the company’s annual AI budget by April 2026. | paid |
| 3 | 14 | Until Chapter 14 defines the full boundary, a provisional rule assigns activities to the two disciplines. | open |
<!-- CONTINUITY:FORWARD -->

---

## 4. Registry glosses

The wording used for each registry object cited in prose. A recurring object is
glossed identically every time it appears, so the reader meets one statement of
it rather than three paraphrases. Verbatim registry statements are verified
separately by `aiom_registry.py` against Locked Registry v1.3; this table
tracks the surrounding prose gloss.

| Object | First used | Gloss as given |
|---|---|---|

| THM-009 | Ch1 | deployed AI is a resource-consuming operating activity, not merely software access |
| THM-004 | Ch2 | Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough. |
<!-- CONTINUITY:REGISTRY -->

---

## 5. Northmoor figures used

Every Northmoor number that appears in a chapter, so it can be diffed against
generator output rather than trusted. The generator is `Northmoor/northmoor_gen.py`.

| Chapter | Figure | Value as printed | Source file |
|---|---|---|---|

<!-- CONTINUITY:NORTHMOOR -->

---

## 6. Chapter log

One line per chapter as it locks, so the ledger's own currency is visible.

| Chapter | Locked | Terms owned | Forward refs made | Registry objects |
|---|---|---|---|---|

| 1 | 2026-08-13 | 8 | 5 | 1 |
| 2 | 2026-08-31 | 6 | 12 | 1 |
| 3 | 2026-10-14 | 16 | 21 | 14 |
| 3 | 2026-10-17 | 6 | 11 | 1 |
<!-- CONTINUITY:LOG -->
