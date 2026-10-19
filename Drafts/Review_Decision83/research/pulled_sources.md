# Sources Dan pulled, read in full by Claude

Each entry: what was read, and the exact sentences that carry the facts. The
full article text is not committed (copyright); the upload stays with Dan.

## Pull list #1. Financial Times, read in full 2026-10-19

"Corporate America embraces cheaper 'open' AI models", Ryan McMorrow and George
Hammond, San Francisco, published September 27, 2026 (17:00 UTC).
https://www.ft.com/content/d9de4776-1fc9-4f2b-aaaf-9961c35d8acd (uploaded as an
archive.is capture).

- "Corporate America is turning to lower-cost "open" AI models, as spiralling IT expenses push executives to look for alternatives to Anthropic and OpenAI's frontier systems."
- "Executive mentions of "open weight" or "open source" models in earnings calls and investor conferences surged sixfold in August and September compared with the same two-month period last year, according to data from AlphaSense, the research platform."
- "a cross-industry swath, including PNC Financial Services, logistics group CH Robinson and industrial giant Siemens, have discussed using open-weight models in recent weeks."
- "For now, the two frontier AI labs capture the bulk of AI spending"
- "In August, open-weight models accounted for 56 per cent of all tokens processed through Vercel's AI Gateway, up from 7 per cent in December."
- Tinder CTO Vinay Kuruvila: "had begun routing some queries from non-technical users to open-weight models as the app worked to get control of rising AI costs." "In January we were spending at the rate of $1mn per year and by July it had climbed to $10mn . . . I don't want another 10X increase,"
- "AT&T now runs about 40 per cent of its AI workloads on open models and aims to reach 70 per cent within a year, according to Andy Markus, the telecom group's chief data and AI officer."
- Markus: "We're doing 45bn tokens a day," "At that scale, costs become super important. If we can move that traffic from a super expensive closed-source model to an open model that we can often serve at [a fraction] of the cost, and still maintain the accuracy, then we'll do that."
- Markus: AT&T "took open models and tuned them using the company's proprietary data so they performed as well as, or better than, closed alternatives for specific tasks."
- Digital Realty (Scott Wallace): "used a mix of open and proprietary systems depending on the sensitivity and complexity of the task." "Any customer data, never, never, never goes into a frontier."

Corrections to the pull-list summary: the quote is "costs become super
important", not "extremely important". The Tinder figures are an annualized
spending RATE ($1mn a year in January, $10mn by July). Digital Realty is new:
sourcing on sensitivity, not only cost.
Supports: Ch1 (cost grows with use at scale: Tinder tenfold, AT&T 45bn tokens a
day); Ch3 sourcing and allocation and routing (AT&T, Tinder, Digital Realty).
Caution: "the two frontier AI labs capture the bulk of AI spending", so the
shift shows in tokens more than dollars.

## Pull list #2. The Information, read in full 2026-10-19

"Tokenminimizing: Meta Moves to Curb Employee AI Usage as AI Costs Reach
Billions", Jyoti Mann, Exclusive, June 12, 2026, 11:57am PDT.
https://www.theinformation.com/articles/tokenminimizing-meta-moves-to-curb-employee-ai-usage-as-ai-costs-reach-billions
(Dashes inside quoted memo text are shown as [...].)

- "Meta Platforms plans to clamp down on skyrocketing AI costs inside the company by imposing limits on employees' token usage, the company told staff in a memo on Tuesday, just weeks after it pushed them to adopt AI tools in their work."
- "The company is building an internal platform to track employee AI usage and spending in real time, set budgets and establish limits on employees' token spend, according to an internal memo reviewed by The Information, which Meta shared with about 6,000 staffers earlier this week."
- Memo: "We've seen an exponential increase in AI usage and [we] are tracking to spend billions on internal use alone in 2026," "At the same time, individuals and teams have limited visibility into and control over how they use AI. In 2027, we expect Meta will move toward managing AI tokens in a more structured way [...] with budgets, allocation decisions, and supporting tools."
- "a team of product developers and engineers has created a central dashboard called AI Gateway to monitor usage and spending in one place." "Meta will also roll out automated alerts for unusual spending spikes. The group is also keeping track of current costs to forecast future spending so it can plan computing capacity and negotiate with vendors."
- "In November, Meta told employees that demonstrating "AI-driven impact" would become a "core expectation" this year"
- "employees had burned through 60.2 trillion tokens in a 30-day period. Usage later climbed to 73.7 trillion tokens before the leaderboard was taken down"
- Bosworth (April memo): "Nobody should be using AI tools just for the sake of using them," "All motion is not progress and token usage alone is not a measure of impact of any kind. We will be using these tools because they'll genuinely allow us to do better work, faster."
- "Uber and ServiceNow used up their entire annual budgets for Anthropic's tools in just the first few months of 2026. ServiceNow is also monitoring employees' daily usage in a bid to track and reduce its costs."

Corrections: K5 confirmed; the "billions" is a 2026 projection for internal use
("tracking to spend"), not a realized figure; budgets and allocation are planned
for 2027, not in force. The ServiceNow budget fact (K6) is now confirmed in an
allowed source, in this article.
Supports: Ch1 (exponential usage, cost to billions); Ch2 THM-004 almost word for
word (scale, "limited visibility into and control over", then budgets,
allocation and tools: the governing apparatus); Ch2 value by design (Bosworth);
Ch3 metering (AI Gateway), planning (forecast to plan capacity), allocation.

## Pull list #3. Bloomberg, read in full 2026-10-19

"Uber Caps Usage of AI Tools Like Claude Code to Manage Costs", Natalie Lung,
June 2, 2026, 5:00 PM UTC (updated 8:09 PM UTC).
https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs

- "Uber Technologies Inc. has set usage caps on some artificial intelligence-powered tools used by its staff, a move meant to manage costs after the company blew through its AI budget earlier this year."
- "The rideshare giant is limiting all employees to $1,500 in monthly token spending per AI coding tool, an Uber spokesperson said in response to a Bloomberg News inquiry. That means spending on one tool doesn't have a bearing on the budget for another. The limits, which have been instituted in recent months, only apply to agentic coding software such as Cursor or Anthropic PBC's Claude Code."
- "Every employee has a dashboard where they can track their usage across various tools. The company has also implemented a process by which individuals can seek permission to exceed their normal cap."
- Spokesperson: "We think this is all a pretty straightforward way to responsibly encourage agentic AI adoption and experimentation at scale across the company,"
- "Chief Technology Officer Praveen Neppalli Naga told the Information in April that the company had already maxed out its full-year AI budget."
- "Walmart Inc. has capped staffers' use of an in-house AI agent that helps with workplace tasks, according to people familiar with the decision."
- "Uber said last month that it will moderate the overall pace of hiring relative to its plans entering the year, as a result of the benefits from using AI internally."
- Macdonald (Rapid Response podcast): "It's very hard to draw a line between one of those stats and 'OK, now we're actually producing like 25% more useful consumer features,'" "Over the coming quarters and years, maybe that will become clearer, but I think today it's hard even if some of the underlying metrics are trending in a really astronomical direction,"

Confirms in full what the Bloomberg Law copy cut off: the usage dashboard and the
exceptions process. Supports Ch2 (the governing apparatus after an overrun: a cap
per person per tool, a record for each employee, an exception path) and Ch2's
value-by-design point (Macdonald, a second quotation beside "That link is not
there yet"). Ch3 metering (per-employee dashboard) and allocation (caps).
Note: Bloomberg titles Macdonald "Chief Operating Officer"; Ch2 says "president
and chief operating officer" (Fortune). Both are true.

## Pull list #4. Wall Street Journal, read in full 2026-10-19

"Why AT&T Is Betting Big on Open-Weight AI", Belle Lin, CIO Journal, published
August 12, 2026 (11:00 UTC). Standfirst: "The telecom company is staking its
future on open models, both to control token cost and protect its proprietary
data". https://www.wsj.com/cio-journal/why-at-t-is-betting-big-on-open-weight-ai-a0ea03b1
(Dashes inside quoted text are shown as [...].)

- "Corporate America's AI playbook is changing as more businesses substitute proprietary AI models in favor of open alternatives to save on costs."
- "Such open models currently power about 25% of the telecommunications company's overall AI usage, including helping manage its network, said AT&T Chief Data and AI Officer Andy Markus, "and we believe we can get way higher than that." Over time, he expects open models to power 70% to 80% of the company's total AI usage."
- Open models "help prevent AT&T from becoming "beholden to any one solution," he said."
- "The company's focus on using open models comes at a time when U.S. companies are starting to put tighter controls around their AI spending."
- "Because AT&T uses an average of 45 billion AI tokens each day, directing user prompts toward cheaper models makes an impact, Markus said. The company built what it calls a "smart router" to automatically pick the most cost-effective model for a specific task."
- "Switching from closed, proprietary AI models to open models has already resulted in savings of 80% to 90% for AT&T in certain applications, he said."
- Markus: "You hear the stories of the 'token apocalypse,' and we're not scared of the token future," "It's something that we feel like we can manage."
- "AT&T has over a thousand internal uses for AI"
- "Summarizing and analyzing customer service call transcripts [...] is supported entirely by open models, he said."
- Open models "can be run on AT&T's own data centers rather than rented infrastructure from a cloud-computing provider [...] a setup that trims AI costs even further."
- Markus: "We have to keep our information safe and protected, and we have to control the inputs and the outputs of the models," "The enterprise data is the gold mine, and the tools are just a way to mine the gold."
- Reported Gartner view (Chirag Dekate): enterprises "soon reach an inflection point where the costs of such models become unsustainable". Gartner is not an allowed source on its own; this is the WSJ reporting it.

AT&T's open-model share by date and source (never merge): about 25% (WSJ, Aug
12, 2026); 20% "by May", since risen to 40%, may reach 60% (NYT, Sept 4, 2026);
about 40%, aiming for 70% within a year (FT, Sept 27, 2026). Savings: 80% to 90%
"in certain applications" (WSJ); "up to 80%" (NYT); "as much as 80%" (AMD);
"as much as 90%" (AT&T blog). Tokens: 45 billion a day (all sources).
Supports: Ch3 sourcing (provider choice on cost, capability and data protection,
avoiding being "beholden to any one solution") and allocation and routing (the
"smart router", a stated rule); Ch1 consumption at scale (45 billion tokens a
day); Ch3 planning ("we feel like we can manage").

## Pull list #5. The Information, read in full 2026-10-19

"Uber CTO Shows How Claude Code Can Blow Up AI Budgets", Laura Bratton, Applied
AI newsletter, April 14, 2026, 10:33am PDT.
https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets
(Dashes inside quoted text are shown as [...].)

- "Uber's surging use of AI coding tools, particularly Anthropic's Claude Code, has maxed out its full year AI budget just a few months into 2026, according to chief technology officer Praveen Neppalli Naga."
- Neppalli Naga: "I'm back to the drawing board because the budget I thought I would need is blown away already,"
- "Uber is one of a number of companies that say they have encouraged employees to use AI as much as possible, creating internal "leader boards" ranking software engineers who use the most AI."
- "since the end of last year, Uber's Claude Code usage has soared, while usage of Cursor has "kind of plateaued," though still high."
- "He wouldn't disclose exact figures of the company's software budget or what it spends on AI coding tools."
- "about 11% of real, live updates to the code in its backend systems are being written by AI agents built primarily with Claude Code, up from just a fraction of a percent three months ago."

This is the primary behind Chapter 2's opening case (which cites Forbes and
Fortune). Timing: the budget was gone by April 14, 2026, "just a few months
into 2026"; the chapter's "by April 2026" holds. Macdonald's "middle of March"
(podcast) is consistent with it. Uber did not disclose the budget's size, which
the chapter already avoids stating.
Supports: Ch2 opening case and its planning point ("the budget I thought I
would need"); Ch1 (use soared, the budget set in advance did not hold); Ch2's
leaderboards point beside Meta's (usage rewarded without a value test).
Possible upgrade: cite this primary beside Forbes in Ch2's opening case.

## Pull list #6. The Information, read in full 2026-10-19

"Why Anthropic Costs Are Unpredictable", Laura Bratton, Applied AI newsletter,
May 14, 2026, 12:08pm PDT.
https://www.theinformation.com/newsletters/applied-ai/anthropic-costs-unpredictable
(Dashes inside quoted text are shown as [...]. The opening line on Anthropic's
price increases belongs to Chapter 4 and is NOT used.)

- "Anthropic customers like PagerDuty and ServiceNow [...] which says it already blew through its full-year budget for Anthropic AI tools [...] can't predict what they'll pay this year."
- "One reason Anthropic costs are tough to predict, ServiceNow chief digital information officer Kellie Romack told me, is that Anthropic doesn't automatically show customers the kind of granular data that allows them to see which of its users consume which tools; how much they use the tools, and how they're using them."
- "Having that data from Anthropic would make it easier to cut off employees who are "tokenmaxxing" or using the tools inefficiently."
- "Customers can monitor staffers' usage of Anthropic's tools to some extent by connecting their Claude accounts to an external analysis tool through standard application programming interfaces. But this requires customers to have access to such a tool to make sense of all that data."
- "ServiceNow uses this method to track employees' daily use of Claude tools through AI Control Tower, an application ServiceNow also sells to its own customers to monitor AI usage across their workforces, she said. Romack has assigned a member of her team to monitor the data through that app."
- National Life Group CIO Nimesh Mehta: the lack of granular usage data makes Anthropic "great for consumer usage but not great for companies" that want to monitor individuals' usage.
- Romack: "I want more transparency."
- Reporter's analysis (not a source fact): "customers can theoretically turn off such spending at the drop of a hat if they absolutely need to"

Corrections: Romack's title is chief digital information officer (CDIO). The
AI Control Tower internal use is now CONFIRMED (Ch3 research P4 had it as
unconfirmed).
Supports: Ch3 metering and attribution almost exactly ("Only the organization
can attribute consumption, because only it knows which team, product, or
customer a request served": here the buyer had to build its own record because
the provider's invoice gave no per-user breakdown, and assigned a person to
watch it); Ch3 planning (cannot predict the bill); Ch2 record flow (the record
the buyer lacked). K6 confirmed in full.

## Pull list #7. The Information, read in full 2026-10-19

"AT&T is Using Open Source Models to Curb Anthropic Bills", Aaron Holmes,
Applied AI newsletter, August 20, 2026, 11:55am PDT.
https://www.theinformation.com/newsletters/applied-ai/t-using-open-source-models-curb-anthropic-bills
(Dashes inside quoted text are shown as [...].)

- "The telecommunications firm plans to keep its employees' spending on Anthropic and OpenAI models flat in the coming years by using more open-source models such as Nvidia's Nemotron, according to Mark Austin, an AT&T vice president."
- "Austin oversees AI used by the company's 100,000 employees for everything from coding and financial analysis to tools for HR and customer support staff."
- "Over the past year, he said, AT&T boosted its use of open-source models to the point where such models now power 40% of employees' AI queries. AT&T plans to raise that figure to between 60% and 70% in the coming years, he said."
- "AT&T's software developers still rely on cutting-edge models for complex tasks like generating code, but can use cheaper open source models for less intense tasks like generating summaries of previously submitted code, he said."
- "AT&T also has gotten savings from using so-called model routers that automatically route employees' queries to cheaper models based on the complexity of the task. After the company began using router provider LiteLLM, the costs of some advanced AI tasks such as coding fell by as much as 56% while the quality of the AI's performance fell just 2%, Austin said."
- "AT&T started developing its primary internal AI system, Ask AT&T, in 2023 which initially relied entirely on OpenAI models the company purchased through Microsoft's cloud, Austin said."
- "Software developers using Ask AT&T can choose a specific model or AI agent such as GitHub Copilot, Devin, Claude Code or Codex, but their spending is capped, Austin said."
- "The Ask AT&T service now processes 45 billion tokens [...] per day, Austin said."
- "AT&T also is analyzing Chinese open source models from DeepSeek and Moonshot but isn't currently using them for work. The company is still evaluating potential risks from using them, he said."
- "open source models have typically been around six to 10 months behind frontier models in terms of capabilities, but the gap seems to be narrowing."

Notes: the speaker here is Mark Austin (VP), not Markus; the 40% here is "of
employees' AI queries" (scope differs from the FT's "AI workloads"). The 45
billion tokens a day is the Ask AT&T service. The reporter's "at least hundreds
of millions annually" is an estimate from list prices, not an AT&T figure: do
not use it.
Supports ALL FIVE Ch3 functions in one organization: sourcing (single provider
in 2023, now several, with a risk test before adopting a model); planning and
budgeting (provider spending held flat for years ahead); metering (tokens per
day through one internal service); allocation and routing (a router by task
complexity: cost down as much as 56%, quality down 2%; complex coding kept on
frontier models; developer spending capped). Strongest single candidate for a
Chapter 3 dated box, or for a problem set.
Related, NOT read (possible counterpoint): The Information, "Anthropic Models Can
Be Cheaper to Use Than Chinese Ones, Study Finds", Laura Bratton, about August
13, 2026.

## Pull list #8. The Information, read in full 2026-10-19

"Meta's AI Incubator Is Developing an OpenRouter Rival to Cut Coding Costs",
Jyoti Mann, July 21, 2026, 3:36pm PDT.
https://www.theinformation.com/articles/metas-ai-incubator-developing-openrouter-rival-cut-coding-costs

- "Meta Platforms internal incubator for AI-powered products and tools is developing a version of the OpenRouter service that would help cut costs by sending some AI tasks to lower-cost models."
- "The AI model router, dubbed Switchboard, is among those projects. It would determine which models should handle each request from a human user or AI agent by scoring tasks by difficulty. It would send simpler requests to smaller, cheaper models"
- "Switchboard is an early-stage effort and may never be launched as a product, according to a person familiar with the matter."
- Internal Meta document: "We pay top-model prices for every coding request, including the easy ones." "Today everything goes to one model, so we overpay on easy work or underperform on hard work," "Cost is what limits how widely we can run agents,"
- "Most coding-agent tasks can be handled by smaller models, while only a minority require the capabilities of more expensive frontier models, according to the project proposal rationale outlined in the document."
- "Meta also has been looking for ways to rein in the billions of dollars it is spending on AI tools for its coders and other employees." (the reporter's characterization, citing the June memo)
- "Meta declined to comment."

Notes: the words are from an internal proposal reviewed by the reporter, not a
Meta statement; Switchboard is early-stage and may never launch. Use as "an
internal Meta document described the problem as", never as Meta's policy.
Supports: Ch3 sourcing almost word for word ("A company that sends every
request to its most capable model, including requests a smaller model would
answer just as well, is paying for capability that work does not need": Meta's
own engineers wrote "we overpay on easy work or underperform on hard work");
Ch3 allocation and routing (a router scoring difficulty: a stated rule, at the
proposal stage); Ch1 (cost limits how widely the work can run).
