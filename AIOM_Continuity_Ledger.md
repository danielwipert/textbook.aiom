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
<!-- CONTINUITY:TERMS -->

---

## 3. Forward references

A promise that a later chapter will do something. Logged when the promising
chapter locks; marked paid when the promised chapter locks and G3 confirms the
promise was kept.

| From | To | Promise | Status |
|---|---|---|---|

| 1 | 2 | This is the first chapter; problem sets begin reaching back to earlier chapters in Chapter 2. | paid |
| 1 | 3 | Each of these subjects has its own purpose and literature, and Chapter 3 explains where each ends and AI Operations Management begins. | open |
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
| 2 | 3 | As Chapter 3 explains, the theorem formalizes the economic consequence of the third flow’s asymmetry; it does not establish the taxonomy itself. | open |
| 2 | 3 | Chapter 1 described the problem as a category error, and Chapter 3 names the discipline that resolves it. | open |
| 2 | 8 | Chapter 8 builds the record flow, and Chapter 10 turns that record into a budget. | open |
| 2 | 8 | It returns in Chapter 8, which builds the record flow that organizations are structurally most likely to skip. | open |
| 2 | 10 | Chapter 8 builds the record flow, and Chapter 10 turns that record into a budget. | open |
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
<!-- CONTINUITY:LOG -->
