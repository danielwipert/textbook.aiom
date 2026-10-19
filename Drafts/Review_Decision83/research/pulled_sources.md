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
