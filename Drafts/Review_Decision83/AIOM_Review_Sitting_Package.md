# Sitting package: outside check findings, Chapters 1 to 3 (Decision 87)

Built 2026-10-19 from the seven outside check results in `check_results/`.
Every listed source (S1 to S11) was checked by an outside model with web access.

**Headline: the sweep found no major red flags in the three chapters.** All ten
approved additions are supported by their sources. Seven need wording fixes,
mostly about WHO said a thing (the company, or the newspaper). Two touch the
published opening case of Chapter 2.

Three gates:

1. The wording fixes to the seven new boxes (one group)
2. R-1: the narrowed sentence in Chapter 2's opening case
3. The first sentence of Chapter 2's opening case

After the gates, Claude applies everything in one batch: one `amend.py` run per
chapter.

---

## Group 1. The new boxes, final wording

Each box below is the wording that would go into the book. Where it differs
from what you approved, the reason is given in one line. "Checker's wording"
means the outside checker wrote it; "assembled" means Claude joined sentences
the checker had approved.

### 1-A. Chapter 1, section 1.4. Dated: June to September 2026

> In June 2026, Meta told about 6,000 employees in a memo that internal AI use
> had grown exponentially and that the company was "tracking to spend billions
> on internal use alone in 2026." In September 2026, the Financial Times
> reported that Tinder's chief technology officer, Vinay Kuruvila, said the
> company's AI spending had risen from an annual rate of $1 million in January
> to $10 million by July.

Change: the Tinder sentence now says the FT reported it (the article does not
say when the interview took place). Checker's wording.

### 1-B. Chapter 1, section 1.3. Dated: February to May 2025

> Duolingo, the language-learning company, sells a premium subscription tier,
> Duolingo Max, with features built on generative AI. In its fourth-quarter 2024
> shareholder letter, the company reported that quarterly gross margin had
> fallen by about 120 basis points year over year to 71.9 percent. It
> attributed the decline to increased generative AI costs associated with
> growing Duolingo Max adoption and to lower advertising margins, partly offset
> by a greater subscription share of revenue. Its first-quarter 2025 letter said
> Duolingo Max came "with variable costs that we are actively managing."

Change: restores the second cause Duolingo gave (lower advertising margins), so
the box no longer makes the whole decline look AI-driven. Checker's wording.

### 2-A. Chapter 2, section 2.4. Dated: June 2026

> In June 2026, Meta told employees in a memo that "individuals and teams have
> limited visibility into and control over how they use AI." The memo said the
> company was building an internal platform to track employee AI use and
> spending in real time, set budgets, and establish limits on employees' token
> spending. It expected to manage AI tokens "in a more structured way" in 2027,
> "with budgets, allocation decisions, and supporting tools." The Information
> reported that a copy of an internal leaderboard it reviewed in April showed
> employees had consumed 60.2 trillion tokens in a 30-day period. The
> publication reported that usage later reached 73.7 trillion tokens before the
> leaderboard was taken down.

Change: the token counts are now credited to the newspaper, which saw a copy
of the leaderboard; they were not in Meta's memo. Checker's wording.

### 2-B. Chapter 2, section 2.6. Dated: May 2026

> In May 2026, the Financial Times reported that Amazon had shut down an
> internal leaderboard that scored users of its Kiro developer platform on their
> AI activity, after workers tried to boost their scores with unnecessary
> activity that increased the company's computing costs. Amazon said "the beta
> dashboard was not a formal or approved tool, and has since been deprecated."
> According to people familiar with his remarks, senior vice president Dave
> Treadwell told staff: "Please don't use AI just for the sake of using AI."
> According to people familiar with the matter, Amazon had begun measuring the
> success of its AI tools and their adoption with "normalised deployments,"
> described as evidence of engineers regularly using AI to create useful code,
> rather than token consumption.

Change: workers "tried to" boost their scores (not that they did); Amazon's
own statement quoted in full; Treadwell's words and the new measure credited to
unnamed people, as the FT does. Checker's wording, with one copy edit: the
period and comma moved inside the closing quotation marks, the book's American
style.

### 2-C. Chapter 2, section 2.7. Dated: June 2026

> In June 2026, Bloomberg News reported that Uber had set usage caps on some AI
> tools after exhausting its AI budget earlier in the year. An Uber spokesperson
> confirmed that all employees were limited to $1,500 a month in token spending
> per AI coding tool. The limits applied only to agentic coding software, such
> as Cursor and Claude Code. Bloomberg also reported that every employee had a
> dashboard showing their own use across tools and could request permission to
> exceed the cap.

Change: only the cap is credited to Uber; the rest is Bloomberg's reporting.
Adds that the caps covered coding tools only. Checker's wording.

### 3-A. Chapter 3, section 3.2. Dated: August to September 2026

> In August 2026, a vice president of AT&T, Mark Austin, said the company's
> internal AI service, Ask AT&T, processed about 45 billion tokens a day and
> that open models powered 40 percent of employees' AI queries. He said AT&T
> planned to keep its employees' spending on Anthropic and OpenAI models flat in
> the coming years and that developers' spending was capped. He said that after
> AT&T began using LiteLLM to route employees' queries to cheaper models based
> on task complexity, the cost of some advanced AI tasks, including coding, fell
> by as much as 56 percent, while AI performance fell 2 percent. In September
> 2026, the Financial Times reported that AT&T was using open models tuned on
> its own data to perform specific tasks at lower cost, and the company's chief
> data and AI officer, Andy Markus, said AT&T aimed to run 70 percent of its AI
> workloads on open models within a year.

Change: no start date implied (AT&T had been moving work "over the past
year"); the token figure tied to Ask AT&T; the routing sentence names the tool
and keeps "as much as" for some tasks. Assembled from the checker's approved
sentences and put in date order.

### 3-B. Chapter 3, section 3.2. Dated: May 2026

> In May 2026, ServiceNow said it had already used up its full-year budget for
> Anthropic's AI tools. Its chief digital information officer, Kellie Romack,
> said the provider did not automatically show customers which of their users
> consumed which tools, or how much. ServiceNow tracked its employees' daily use
> of the tools through its own monitoring application and assigned a member of
> her team to watch the data. "I want more transparency," she said.

Change: "early in the year" dropped, because ServiceNow's own statement (May)
does not give the timing; only a later report does. Assembled; every remaining
fact was confirmed against S5.

## Gate 1 of 3: The box wording

**A. Accept all seven boxes as written above** *(recommended)*
Every fix makes a box narrower or credits a fact to the right speaker. Nothing
the boxes teach changes.

**B. Accept the five with checker's wording; send 3-A and 3-B back for one
re-read**
Those two were assembled by Claude. A short re-read costs one more round.

**C. Pull named boxes**
Reply with the IDs to drop or to look at again.

---

## Group 2. R-1: the narrowed sentence (Chapter 2 opening case)

Published:

> It does show that nothing in the public account identifies a control that
> changed the course of the spending, or a measure that connected the use to a
> return.

You approved adding "before the budget was gone". The checker confirms that
part. It also finds the second half too strong: on its May call Uber linked its
AI spending to slower hiring, which is a connection to a return, even though no
net figure was given.

## Gate 2 of 3: R-1

**A. Narrow both halves, keeping the chapter's sentence** *(recommended)*
"It does show that nothing in the public account identifies a control that
changed the course of the spending before the budget was gone, or quantifies
the net return on that spending."

**B. Use the checker's sentence as written**
"The sources reviewed do not identify a control that changed spending before
the original budget was exhausted or quantify the net return on Uber's AI
investment." Accurate, but it breaks the "does not establish ... does show"
pairing with the sentence before it.

**C. Narrow the first half only, as approved at Gate 1**
Leaves "a measure that connected the use to a return", which the checker calls
too broad.

---

## Group 3. The opening sentence of Chapter 2

Published:

> By April 2026, just four months into the year, Uber had already exhausted its
> annual AI budget.

The checker says "just four months" can read as four COMPLETED months, while
the source dates the exhaustion only to "just a few months into 2026" (reported
April 14). Uber's president placed it around mid-March.

## Gate 3 of 3: The first sentence

**A. Swap in the source's own phrase** *(recommended)*
"By April 2026, only a few months into the year, Uber had already exhausted its
annual AI budget." Small, true to the source, keeps the rhythm.

**B. Use the checker's sentence**
"By April 14, 2026, Uber had already exhausted its full-year AI budget,
according to its chief technology officer, Praveen Neppalli Naga." Most exact,
but it puts an attribution in the case's opening line.

**C. Leave it as published**
"By April" is true; the difference is small.

Noted, not proposed: the case title is "The budget that ran out in April". The
sources say the budget was gone BY April, perhaps in March. The checker did not
raise it. A title change can touch cross-references, so it is left alone unless
you want it looked at.

---

## Applying (after the three gates)

1. One `amend.py` run per chapter, batching that chapter's items. Each run
   renders the PDF, runs the fifteen print gates, the web build and voicecheck,
   and reports before committing.
2. New source register entries (S1 to S11 as used) and new lines in
   `AIOM_Claim_Ledger.md`, written from the chapter's sentences.
3. Claude rasterizes and reads every page that moved.
4. A push to `main` publishes the new locks.
