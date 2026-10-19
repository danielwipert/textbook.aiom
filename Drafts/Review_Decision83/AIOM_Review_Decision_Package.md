# Decision package: review of Chapters 1 to 3 (Decision 87)

Built 2026-10-19, after Dan pulled and Claude read eleven articles (pull list
numbers 1 to 10 and 13). The exact quotes behind every item are in
`research/pulled_sources.md` and `research/ch01_research.md` to
`ch03_research.md`. Nothing here is applied yet. Each item is ruled by Dan,
then applied in one `amend.py` run per chapter. The chapters stay locked.

How to read this: six group gates. Each group has a recommendation. Reply
"A" to accept the whole group, or pull items ("A, but not 2-C").

The path:

1. Red flags in the published text
2. Chapter 1: new dated evidence
3. Chapter 2: new dated evidence
4. Chapter 3: new dated evidence
5. Items NOT recommended (confirm they stay out)
6. The outside check before anything goes into type

House rules kept in every proposed sentence: no dashes, no contractions, dated
material only inside dated boxes or the dated opening case, no reserved case
(Klarna, MIT NANDA beyond its existing box, provider pricing or limit changes,
shadow AI, Air Canada).

---

## Group 1. Red flags in the published text

**Result of the sweep: nothing in the three chapters has been disproven.** The
new reporting supports every central claim. One sentence in Chapter 2 now reads
narrower than the public record, and one source upgrade is available.

### R-1. Chapter 2 opening case: "nothing ... changed the course of the spending" (recommended: narrow it)

Published text (opening case, eleventh paragraph):

> It does show that nothing in the public account identifies a control that
> changed the course of the spending, or a measure that connected the use to a
> return.

What changed: on June 2, 2026, Bloomberg reported that Uber had since put caps,
a per-employee dashboard and an exception process in place (pull #3). On its
May 6, 2026 earnings call, the chief financial officer said management had
underestimated the budget and deliberately "re-upped" the investment. The
sentence was true when written (the case is dated to May 2026), but a reader now
could take it to mean Uber never responded.

Proposed replacement:

> It does show that nothing in the public account identifies a control that
> changed the course of the spending before the budget was gone, or a measure
> that connected the use to a return.

### R-2. Chapter 2 opening case: add the chief financial officer's own account (recommended)

After "Public reporting does not explain how Uber calculated its AI budget."
insert one sentence:

> On the company's earnings call in May 2026, its chief financial officer,
> Balaji Krishnamurthy, said that when Uber set its 2026 budgets in November,
> it had "underestimated the amount of impact the AI tools could have," and
> that the company had since "re-upped" its investment.

Why: it is first-party, it confirms the budget was set in advance, and it shows
management chose to keep spending, which keeps the case fair to Uber (C6).
Source: Uber Q1 2026 earnings call transcript, Uber investor relations.

Note: the following sentence ("The outcome, however, is consistent with ...")
still reads correctly after the insertion, because the call says WHEN the
budget was set, not HOW it was calculated.

### R-3. Chapter 2 opening case: cite the primary interview (recommended)

The provenance line says "The primary account behind that reporting remains
paywalled." Dan has now pulled it: The Information, "Uber CTO Shows How Claude
Code Can Blow Up AI Budgets", Laura Bratton, April 14, 2026 (pull #5). It
confirms the budget was gone "just a few months into 2026", so "By April 2026"
holds.

Proposed:

- Add the primary as a second citation on the first sentence (timing only; it
  does not carry the engineer count or the adoption percentages, which stay on
  the existing source).
- Provenance line becomes: "Dated: December 2025 to May 2026. Figures and dates
  were checked against the cited reporting, and the timing against the primary
  interview, read in October 2026. See the source register."

### Considered, no change proposed

- "just four months into the year": the sources say "a few months" (The
  Information), "not long after the first quarter ended" (the earnings call)
  and "middle of March" (Macdonald, podcast). "By April" is true. Minor, so
  left alone, per your "do not nitpick".
- "no one appears to have noticed until the annual budget was gone": consistent
  with the CTO ("the budget I thought I would need is blown away already").
- Chapter 3's Microsoft box (July 2026): later reporting (pull #9) points the
  same way. Holds.
- Chapter 1: nothing found that contradicts it. The one fair counterexample
  (the US government's $1 ChatGPT Enterprise deal, 2025) is time-limited and
  promotional, which is what Chapter 1's flat-rate section already explains.

## Gate 1 of 6: Red flags

**A. Accept R-1, R-2 and R-3** *(recommended)*
One narrowed sentence, one first-party sentence, one added citation. The case
becomes fairer to Uber and better sourced.

**B. Accept R-1 only**
The minimum fix: the sentence stops overreaching. No new material.

**C. Change nothing**
The case is dated to May 2026, so it was true when written.

---

## Group 2. Chapter 1: new dated evidence

### 1-A. New dated box in section 1.4 (recommended)

Placed after the paragraph beginning "This all changes when the pilot enters
production." That paragraph says use grows with the volume of work; the box shows
it at two large companies, neither of which is a later chapter's case.

> **Dated: June to September 2026**
>
> In June 2026, Meta told about 6,000 employees in a memo that internal AI use
> had grown exponentially and that the company was "tracking to spend billions
> on internal use alone in 2026." In September 2026, the chief technology
> officer of Tinder, Vinay Kuruvila, said the company's AI spending had run at
> a rate of $1 million a year in January and had climbed to $10 million a year
> by July.

Sources: The Information, Jyoti Mann, June 12, 2026 (pull #2, memo reviewed by
the reporter); Financial Times, McMorrow and Hammond, September 27, 2026
(pull #1). Note: "billions" is Meta's projection for the year, and the box says
"tracking to spend", not "spent".

### 1-B. New dated box in section 1.3 (recommended)

Placed after the July 2025 box. Section 1.3 answers the flat-rate objection: a
flat price does not remove the meter, it moves who bears it. Duolingo is the
case of a company that sells a flat subscription and pays the meter itself, in
its own SEC filings.

> **Dated: February to May 2025**
>
> Duolingo, the language-learning company, sells a premium subscription tier,
> Duolingo Max, with features built on generative AI. In its letter to
> shareholders for the fourth quarter of 2024, the company reported that gross
> margin had fallen by about 120 basis points from a year earlier, to 71.9
> percent, "due to lower subscription margins from increased generative AI
> costs due to the increased adoption of Duolingo Max." Its letter for the
> first quarter of 2025 said the features came "with variable costs that we are
> actively managing."

Sources: Duolingo Q4 2024 and Q1 2025 shareholder letters, SEC Form 8-K
(first party, open, read by Claude).

Layout note: this makes three dated boxes in section 1.3. The page read at
production will tell us whether that crowds the section.

## Gate 2 of 6: Chapter 1

**A. Add 1-A and 1-B** *(recommended)*
Two boxes, both strong: one shows cost growing with use, one shows a flat price
carrying a meter, in a company's own SEC filings.

**B. Add 1-A only**
Keeps section 1.3 at two boxes; loses the cleanest first-party item.

**C. Add nothing to Chapter 1**
Chapter 1 already carries two dated boxes; the new evidence goes to Chapters 2
and 3 only.

---

## Group 3. Chapter 2: new dated evidence

### 2-A. New dated box in section 2.4 (recommended)

Placed after the paragraph beginning "An unmanaged usage flow expands wherever
the tool makes work easier." Meta's memo states the chapter's mechanism in the
company's own words: use grew, visibility and control did not, and the answer
is budgets and tools.

> **Dated: June 2026**
>
> In June 2026, Meta told employees in a memo that "individuals and teams have
> limited visibility into and control over how they use AI." The company said
> it was building an internal platform to track AI use and spending in real
> time, set budgets, and limit each employee's token spending. It expected to
> manage AI use "in a more structured way" in 2027, "with budgets, allocation
> decisions, and supporting tools." An internal leaderboard had shown employees
> using 60.2 trillion tokens in a 30-day period, and use later reached 73.7
> trillion tokens before the leaderboard was taken down.

Source: The Information, Jyoti Mann, June 12, 2026 (pull #2). The memo text has
a dash at one point; the quotation is trimmed so none enters the book.

### 2-B. New dated box in section 2.6 (recommended)

Placed after the paragraph beginning "The substitution is easy to spot once it
has a name." That paragraph says usage data gets used to answer the value
question. Amazon found the cost of doing so and changed the measure.

> **Dated: May 2026**
>
> In May 2026, the Financial Times reported that Amazon had shut down an
> internal leaderboard that scored engineers on their AI activity, after some
> inflated their scores with unnecessary activity that raised the company's
> computing costs. Amazon said the leaderboard "was not a formal or approved
> tool." A senior vice president, Dave Treadwell, told staff: "Please don't use
> AI just for the sake of using AI." According to people familiar with the
> matter, Amazon had begun measuring the success of its AI tools with a metric
> called "normalised deployments," evidence that engineers were using AI to
> produce useful code, rather than with token consumption.

Source: Financial Times, Rafe Rosner-Uddin, May 28, 2026 (pull #10). The
contraction "don't" is inside a quotation, which the standard permits.

### 2-C. New dated box in section 2.7 (recommended)

Placed after the paragraph beginning "The first element is a record". Section
2.7 says a governing apparatus needs three elements: a record, attribution and a
constraint. Uber's response has all three, so the box closes the loop on the
opening case without the prose having to say so.

> **Dated: June 2026**
>
> In June 2026, Uber told Bloomberg News that it had set usage caps on some AI
> tools after exhausting its AI budget earlier in the year. Each employee was
> limited to $1,500 a month in token spending for each AI coding tool. Every
> employee had a dashboard showing their own use across tools, and an employee
> could ask permission to exceed the cap.

Source: Bloomberg News, Natalie Lung, June 2, 2026 (pull #3). A spokesperson
gave the cap on the record.

## Gate 3 of 6: Chapter 2

**A. Add 2-A, 2-B and 2-C** *(recommended)*
Three boxes, one per section, each showing a large company living the section's
mechanism. 2-C also tells the reader how the opening case ended.

**B. Add 2-C only**
The one box that completes the opening case; the chapter stays lean.

**C. Add 2-A and 2-C, not 2-B**
Drops Amazon, whose metric change rests on unnamed people.

---

## Group 4. Chapter 3: new dated evidence

### 3-A. New dated box in section 3.2, at allocation and routing (recommended)

Placed after the paragraph beginning "The fourth function is allocation and
routing", before the existing Microsoft box. AT&T is the strongest single item
found: one organization, on the record, deliberately sourcing, budgeting,
metering and routing.

> **Dated: August to September 2026**
>
> AT&T, which processes about 45 billion tokens a day through its internal AI
> service, began moving work from closed models to open models it could tune
> and run at lower cost. In August 2026, a vice president, Mark Austin, said
> open models powered 40 percent of employees' AI queries, that the company
> planned to keep its employees' spending on Anthropic and OpenAI models flat
> in the coming years, and that developers' spending was capped. After AT&T
> began using a router that sends each query to a cheaper model when the task
> allows, the cost of some advanced tasks such as coding fell by as much as 56
> percent, while the quality of the results fell 2 percent. In September 2026,
> the company's chief data and AI officer, Andy Markus, said AT&T aimed to run
> 70 percent of its AI workloads on open models within a year.

Sources: The Information, Aaron Holmes, August 20, 2026 (pull #7);
Financial Times, September 27, 2026 (pull #1). The 45 billion tokens a day
appears in every source, including AT&T's own blog and the AMD newsroom.

Kept apart on purpose: the open-model share differs by source, date and scope
(25 percent in the WSJ, August 12; 40 percent in the NYT, September 4; 40
percent of "employees' AI queries" in The Information; 40 percent of "AI
workloads" in the FT). The box gives each figure with its own speaker and date
and never merges them. The savings figures (56, 80, 90 percent) also differ in
scope, so the box uses only the one tied to a stated mechanism.

### 3-B. New dated box in section 3.2, at metering and attribution (recommended)

Placed after the existing DoiT box. Chapter 3 says only the organization can
attribute consumption, because only it knows which team a request served.
ServiceNow had to build that record itself.

> **Dated: May 2026**
>
> In May 2026, ServiceNow said it had used up its full-year budget for
> Anthropic's AI tools early in the year. Its chief digital information
> officer, Kellie Romack, said the provider did not automatically show
> customers which of their users consumed which tools, or how much. ServiceNow
> tracked its employees' daily use of the tools through its own monitoring
> application and assigned a member of her team to watch the data. "I want more
> transparency," she said.

Source: The Information, Laura Bratton, May 14, 2026 (pull #6), confirmed by
pull #2 ("Uber and ServiceNow used up their entire annual budgets").
Neutrality check (C6): the box states what the buyer could and could not see;
it does not fault the provider. Provider pricing in the same article belongs to
Chapter 4 and is not used.

Layout note: 3-A and 3-B each sit next to an existing box, so two pairs of
boxes appear in section 3.2. Production reads those pages.

## Gate 4 of 6: Chapter 3

**A. Add 3-A and 3-B** *(recommended)*
AT&T shows the discipline working; ServiceNow shows why attribution must be the
buyer's own.

**B. Add 3-A only**
The single strongest item; section 3.2 gains one box, not two.

**C. Add 3-A as a new discussion problem instead of a box**
"Apply the function audit to AT&T's public record." Strong teaching, no new box
in 3.2, but the problem set grows and the problem needs its own answer notes.

---

## Group 5. Items NOT recommended (confirm they stay out)

Read and verified, but held back. Each can come back on your word.

| ID | Item | Why it is held back |
|---|---|---|
| N-1 | Meta's "Switchboard" router document: "We pay top-model prices for every coding request, including the easy ones." (The Information, July 21, 2026) | An early-stage internal proposal that "may never be launched". Strong words, weak standing. |
| N-2 | Microsoft: "each division is managing a token budget"; per-employee monthly limit cut from $100,000 to about $10,000 (The Information, Oct 5, 2026) | Most facts rest on unnamed people, and Microsoft pays nothing for OpenAI models, so its routing reflects its own position, not a general lesson. |
| N-3 | Meta spent over $105 million on Claude Code in 28 days (same article) | Unnamed internal data; Chapter 1 box 1-A already makes the scale point on the record. |
| N-4 | JPMorgan, Dimon: "150,000 people use it every week ... That's not in an NPV." (2026 Company Update) | Chapter 3 already has a JPMorgan box; a second crowds it. |
| N-5 | Bosworth (Meta): "token usage alone is not a measure of impact of any kind." | Excellent line, but 2-B already makes the point with Amazon on the record. Could swap into 2-B if you prefer Meta. |
| N-6 | Industry figures: Vercel (open models 71.5% of gateway tokens, 23% of spend), Ramp, FinOps Foundation (98% now manage AI spend), AlphaSense (sixfold mentions) | Aggregates and vendor data; the chapters do not claim a market trend, so they would add a claim rather than support one. |
| N-7 | Pichai at Google I/O: "many companies are already blowing through their annual token budgets, and it's only May." | A provider selling a cheaper model. Context only. |

Counter-evidence weighed and not needing a change: the FT says "the two frontier
AI labs capture the bulk of AI spending", and Ramp finds the open-model shift
concentrated among the heaviest spenders. No chapter claims spending has moved
to open models, and box 3-A says only what AT&T did, so nothing needs
narrowing. The US government's $1 ChatGPT Enterprise deal is answered by Chapter
1's section 1.3 as written.

## Gate 5 of 6: Held-back items

**A. Keep all seven out** *(recommended)*
The boxes above already carry each point with better-standing sources.

**B. Keep them out, but swap Bosworth (N-5) into 2-B in place of Amazon**
Same point, one company the reader has already met in 2-A.

**C. Name the items to bring back**
Reply with the IDs.

---

## Group 6. The outside check before anything goes into type

The rule is that Claude does not fact-check its own draft. Every box above was
written by Claude from sources Claude read. Before applying, an outside checker
with web access should check two things: (1) each proposed sentence against its
source, and (2) a fresh sweep of the published chapters for anything major
Claude missed. You hold copies of the paywalled articles, so the checker can be
given those too.

## Gate 6 of 6: Outside check

**A. One outside check on the approved wording, then apply** *(recommended)*
Claude rebuilds the package to hold only the wording you approve plus the source
quotes and a short red-flag sweep. You run it, rule anything it finds, and then
Claude applies all three chapters in one batch.

**B. Apply now, check afterwards**
Faster, but a wrong word would be published and then amended again.

**C. Apply now, no outside check**
Treats Claude's reading as the check. Not consistent with the standing rule.

---

## What applying looks like (after Gate 6)

1. One `amend.py` run per chapter, each batching that chapter's approved items.
   The run renders the PDF, runs the fifteen print gates, the web build and
   voicecheck, and reports before committing.
2. New source register entries for each new source, and new lines in
   `AIOM_Claim_Ledger.md`, written from the chapter's sentence.
3. Claude rasterizes and reads every page that moved, because new boxes reflow
   the chapter.
4. A push to `main` publishes the new locks.
