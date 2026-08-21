Part I · The Argument


## The Flow


### [OPENING CASE]


## The budget that ran out in April

_Dated: December 2025 to May 2026. Figures and dates are drawn from press reporting of a paywalled primary account and are pending source verification. See the source register._

In April 2026, four months into the calendar year, press reporting indicates that Uber had spent the annual budget it had set for artificial intelligence. Nothing had broken. No contract had been renegotiated and no vendor had raised a price. The engineers were doing the work the company had asked them to do, with the tool the company had given them.

The tool was Claude Code, an assistant that writes and edits software, and the company had begun rolling it out to roughly five thousand engineers in December 2025. Adoption moved quickly. By February, about a third of the engineering organization was using it. By March, the reported figure was above eighty per cent.

By the measures an engineering organization normally applies, the rollout was going well. The tool was adopted and it was used heavily. Reporting indicates that by spring a large share of committed code had passed through it. Those measures establish adoption. They do not establish value, and the difference between the two is most of what this chapter is about.

A budget of that kind is normally built one way. A price per person is multiplied by a count of people and held roughly flat across the year. That is how software has been budgeted for thirty years, and for software it works. The public account does not describe the company’s method in detail, and the shape of the outcome is consistent with a forecast of this kind.

That method has a property worth naming, because it is the reason it survived so long. A seat forecast is falsifiable in advance. Multiply a known price by a headcount the human resources system already holds, and the result can be checked before the year begins. It is the kind of number a finance organization can defend in a planning meeting.

What the engineers were consuming did not hold flat. Reported monthly costs ran from several hundred to a few thousand dollars per engineer, varying with how much each one worked and how hard the work was. The rate was not the surprise. Spending rose as adoption spread and as per-engineer consumption varied, and the commercial terms turned that variable consumption into variable cost.

The shape of the surprise matters more than its size. This was not a budget missed by a margin and discovered at year end. The spending ran at a rate nobody was tracking against the plan, and the plan was only consulted when the money was gone. A rate that is never compared to a plan is not a forecast. It is a hope with a number attached.

Consider what a February review would have required. Observed consumption and the adoption trend would have had to sit in the same operating view, compared against the plan, by somebody whose job was to look. The public account does not establish whether such a view existed or what finance could see. It establishes only that the comparison did not change the outcome.

Two things about this episode are worth separating, because they are usually confused. The first is that the company could see what it was spending. The billing arrived and accumulated, and by April the total had reached the figure that had been set aside. The second is that the company could not say what it had received. The chief operating officer was publicly asking whether the spending had been worth it. That question suggests a documented return was unavailable, incomplete, or unpersuasive to senior leadership.

This is the position Chapter 1 predicted and did not describe. The company was buying a resource priced by use and planning for it with a figure held flat per person. Whether that was a category error, or a working understanding that never reached the forecast, the reporting does not settle. What the episode does show is a deployment that scaled without a mechanism able to govern its economics.

One question this chapter will not answer is how responsibility divides between the buyer and the provider. The commercial arrangement is not in the public account: what the contract priced, what consumption data the customer could see and when, and whether spending limits or alerts were available and declined. A reader should hold that question open. What follows does not depend on its answer, because an organization needs the ability to govern its own consumption whatever the provider supplies.


### [TEACHING BODY]


## 2.1 Work moves, and so does its record

Every organization already manages things that move. Orders move from a customer to a warehouse to a doorstep. Invoices move from a supplier to accounts payable to a bank. Managers do not think of these as static quantities. They think of them as streams that have a rate, a direction, and places where they can back up or leak.

Deployed AI moves the same way. Chapter 1 established the unit: a consumption event, a single use of an AI system that consumes metered computing resources. One event is a transaction. Thousands of events a day, arriving from many people and systems and varying with the work, are something else. They are a stream, and a stream is managed differently from a transaction.

The shift matters because the management instrument changes with it. A transaction is governed by approval: somebody with authority looks at it and says yes. That instrument has a hard limit, which is the attention of the person approving. It works for a purchase order and fails for five thousand engineers making decisions every few minutes about whether to ask for help on a problem.

Definition

Flow

A continuous stream of related activity within a deployment, described by its rate, its direction, and whether anything is being recorded about it. A flow is managed by governing the stream over time rather than by approving each event within it.

The distinction is practical rather than semantic. A transaction is approved once, by somebody with authority to approve it. A flow cannot be approved event by event, because nobody can sit between five thousand engineers and the work they are doing. It is managed by deciding in advance what may run, recording what does run, and comparing the total against a plan.


## 2.2 Three flows, not one

A deployment does not produce one stream. It produces three, and they are separable because different parts of the organization touch each of them.

The first is the work itself. Employees and systems send requests, models return results, and those results go into products, documents, decisions, and code. This is the activity the organization bought the tool for, and it is the only one of the three that anyone is trying to increase.

The second is the record of that work. Somewhere, something writes down what happened: which team made the request, against which system, at what volume. Chapter 1 established that the provider always holds a meter, because the provider must bill and must manage its own capacity. Whether the buyer holds an equivalent record is a separate question, and the answer is frequently no.

The third is the money and the value. Cost attaches to the work through the meter. Value attaches to the work through whatever the organization does with the output. These two belong together because a manager cannot use either one alone: a cost without a corresponding return is an expense report, and a return without its cost is a testimonial.

These are the usage flow, the record flow, and the cost-and-value flow. Naming them matters less than noticing that they are three separate things that can each be in a different condition. An organization can have a healthy usage flow and no record flow at all, which is the ordinary case in the first year of a deployment.

These three are separable because different people own them, and that is the practical reason the distinction earns its place. Engineering owns the usage flow, because engineering decides what is deployed and to whom. Whoever runs the platform owns the record flow, if anyone does. Finance owns the cost half of the third flow the moment an invoice arrives, and the value half belongs to whichever business unit was supposed to benefit. Four owners, three flows, and no single person whose job is the whole of it. Chapter 3 returns to this division and names what fills the gap.

A healthy usage flow looks like a rate that somebody can state. An organization with one can answer how many requests were made last month, by roughly whom, and whether the number is rising. It does not need to approve those requests. It needs to know they happened.

A healthy record flow has a grain, and the grain is what makes it useful. A record that says the organization spent a total last month is not a record flow, because no decision follows from it. A record that says which team, which product, and which system consumed what allows a manager to move something. The test is whether the record can answer a question the invoice cannot.

The record flow has a physical location, and naming it removes some of the mystery. It lives in one of three places. It can sit with the provider, in a usage console the buyer logs into. It can sit in a gateway or platform the organization runs between its users and the model. Or it can sit in the applications themselves, each logging its own calls.

Only the second and third belong to the buyer. That distinction decides what happens when the organization changes vendors, adds a second model, or is asked a question the console does not answer. A record the organization holds survives those events. A record it borrows does not.

A healthy cost-and-value flow is the rarest of the three, because it requires the two halves to be built to a comparable standard and by people who do not normally work together. Finance can produce a cost number without help. The value number requires somebody to have decided, before the deployment began, what it was supposed to improve.

The three flows also move at different speeds, which is why they cannot be reviewed on one schedule. Usage changes daily, because it follows the work. Cost resolves monthly, because that is when the invoice closes. Value, where it is measured at all, resolves over quarters, because that is how long it takes for a change in how work is done to show up in an outcome anyone tracks.

A manager who reviews all three at the same interval will always be looking at one of them too early and another too late. The practical arrangement is to watch usage continuously, reconcile cost monthly against a plan, and revisit value on the cycle the business already uses for the outcome in question.

Figure 2.1The three flows of a deployment. Usage runs continuously once a tool is adopted, and cost runs with it. The record flow is the one that must be constructed, and the value half of the third flow is constructed too. The solid lines run whether or not anyone attends to them; the dashed line and the tinted block exist only where an organization builds them.


## 2.3 Funded as a project, run as a flow

Most AI deployments are funded the way projects are funded. Somebody writes a business case, names a cost, names an expected benefit, and asks for approval once. The money is released, the tool is bought, and the project is marked delivered when people are using it.

Then the deployment runs as a flow. Consumption continues every working day, varying with the work, for as long as the tool is in use. The funding event was a single decision. The spending is a continuous process.

This mismatch explains a pattern managers will recognize. The business case is never revisited, because projects are not revisited after delivery. The consumption keeps changing, because flows do. By the time anyone compares the two, the business case describes a deployment that no longer exists, and it is usually the only document stating what the deployment was supposed to achieve.

The practical consequence is a scheduling one. A flow needs a recurring review at an interval short enough to catch a change while it is still small. Monthly is usually enough. Annually is not, and annual is what a project-funded deployment gets by default.

There is a second consequence, and it is the one that reaches the value side. A project business case states a benefit at the moment of approval, when nobody can check it. If nothing revisits that statement, the claimed benefit becomes the organization’s permanent belief about what the deployment delivers. It was a forecast. It is now treated as a result, and no step in the process was responsible for the conversion.


## 2.4 An unmanaged flow does not stay still

A manager reading this far might reasonably conclude that an unmanaged flow is merely an unmeasured one, and that the remedy is to start measuring whenever it becomes convenient. That conclusion is wrong, and the reason is worth stating carefully.

An unmanaged usage flow grows toward whatever the tool makes easy. This is not a criticism of the people using it. An assistant that drafts code well is used more than one that drafts code badly, and the organization wanted it used. Growth in the usage flow shows that adoption is rising. Whether the deployment is succeeding depends on what that use produces.

An unmanaged record flow does not merely stay empty. It decays, because the raw material for a record is perishable. A request that was never attributed to a team when it was made usually cannot be attributed to that team six months later. The provider’s invoice will say what the organization spent in March; it will not say which product line spent it, because the provider never knew.

An unmanaged cost-and-value flow accrues on one side only, and this is the asymmetry the chapter turns on. Cost arrives without anyone doing anything, because the meter is already running and the invoice already has an owner. Value does not arrive on its own. Somebody has to define what the deployment was supposed to improve, measure it before and after, and attribute the change. Nothing in the tool does that, and no invoice contains it.

The decay is worth one concrete illustration, because managers routinely underestimate it. Consider an engineer who spends a morning on a difficult migration and asks an assistant for help forty times. On the day it happens, that activity could be attributed to the migration project, because the engineer knows what they were doing and the system knows which account made the calls. A month later the engineer has moved on and the calls have been aggregated into a monthly total. A quarter later the only surviving artifact is an invoice. Nothing was deleted. The context that made the record meaningful simply stopped being recoverable, and no amount of later diligence brings it back.


## 2.5 Why the record flow is the one that gets skipped

Of the three flows, the record flow is the one organizations almost always build last. The reason is structural rather than careless, and it is worth understanding before prescribing a remedy.

A record flow produces no benefit on the day it is built. The usage flow delivers work immediately. The cost flow arrives on its own. A record flow pays only later, and only if somebody asks a question it can answer. Its value is entirely in the future tense.

It is also nobody’s obvious job. Engineering has shipped the tool and moved on. Finance has an invoice that reconciles. The team that will eventually need the record is the one that has to justify the spend, and that team does not yet know it will need it. So the work sits in the space between three functions, each of which is doing its own job correctly.

The third reason is the most important. The absence of a record is invisible until it is needed. A broken usage flow announces itself, because people complain that the tool is down. A cost overrun announces itself, because the invoice arrives. A missing record announces nothing at all. It surfaces on the day a senior executive asks which product line drove the increase, and the honest answer is that nobody can say.

This is why the remedy is a decision rather than a habit. An organization does not drift into having a record flow. Somebody has to fund it before the question that needs it has been asked.

Definition

Cost-value asymmetry

The condition in which a deployment’s cost is recorded automatically, because metering produces the bill, while its value is recorded only where the organization has deliberately built a measurement. The two sides of the same activity are therefore known to different standards.


## 2.6 All of the cost, an unknown fraction of the value

The consequence of the asymmetry is the sentence a manager should carry out of this chapter. An organization running an unmanaged deployment holds all of the cost and an unknown fraction of the value.

The word doing the work in that sentence is unknown, not small. The claim is not that deployed AI fails to produce value, and this chapter asserts nothing about how much value any deployment produces. The claim is narrower and harder to escape: the cost figure is complete because billing made it complete, and the value figure is partial because nobody was required to make it complete.

This is why the two figures cannot be compared as if they were the same kind of number. A complete cost set against a partial return makes almost any deployment look worse than it is. An organization that responds by cutting the deployment has acted on an artifact of its own record keeping. The opposite error is equally available: a partial value figure assembled from the deployment’s best moments, set against the same complete cost, will make almost any deployment look better than it is.

A stipulated example makes the arithmetic visible. Suppose a deployment costs one million over a year, and that figure is complete because it came from invoices. Suppose the organization has measured the return on two of the five workflows the tool touches, and those two show a combined benefit of four hundred thousand. The ratio a manager would compute is four hundred thousand against one million, and the deployment looks like a serious loss.

Now notice what that ratio actually compares. The numerator covers two workflows and the denominator covers five. The comparison is not wrong because the numbers are wrong; both are accurate. It is wrong because the two figures have different scopes, and nothing on the page says so. The three unmeasured workflows might contribute nothing, or they might contribute more than the two that were measured. The organization has no basis for either belief, which is what “unknown” means.

There is a reason organizations reach for adoption figures at this point, and it is not laziness. An adoption figure is available. It is produced automatically by the same systems that produce the cost, it rises when things are going well, and it can be presented without anyone having to define what the deployment was supposed to improve. It has every property a reporting metric needs except relevance.

Adoption answers a question about the usage flow: are people using the tool. Value answers a question about the business: did the thing the tool was bought to improve get better. The two are related, and they are not substitutes. A tool can be used constantly and improve nothing measurable, and a tool used by a few people in the right place can pay for the whole deployment.

The substitution is easy to spot once named. Whenever a value claim is supported by a number describing how much the tool was used, the value question has been answered with usage data. That is rarely dishonest. It is what happens when the only complete measurement available is the wrong one.

The disciplined response is not to guess at the missing three. It is to state the ratio with its scope attached: four hundred thousand of return measured against the share of a one million cost attributable to the two workflows that were measured. That sentence is longer and less quotable, and it is the only version a manager can act on. Chapter 12 builds the boundary discipline that makes such a statement routine.

Uber’s position in April 2026 is the first error in progress. The company could total what it had spent. Its chief operating officer was asking, in public, what the company had received. Both statements were true at once, and they were true because of how the two numbers were produced rather than because of anything the engineers had done.

The pattern is not confined to one company. A 2025 study of enterprise deployments by MIT NANDA reported a striking gap. Ninety-five per cent of enterprise generative AI pilots delivered no measurable impact on profit and loss. A far higher share of organizations reported that they had piloted or deployed such tools. The figure attracted substantial methodological criticism after it circulated, and the study’s reported interview counts differ across accounts of it.

The criticism does not need to be settled for the finding to be useful, because the phrase carrying the weight is no measurable impact. A pilot that produced value nobody measured and a pilot that produced no value are indistinguishable in that statistic. That is the asymmetry appearing at market scale: the study could not observe what its subjects had not recorded.


## 2.7 Why this requires governance rather than attention

The registry states the consequence formally. Once a deployment scales, controlling its economics requires a governing apparatus rather than diligence from the people running it.

Theorem 2 · THM-004

Scaled AI Deployment Requires Cost Governance for Economic Control

Within a defined deployment and cost boundary, if:

  - (i)AI activity consumes resources and therefore accrues cost as it is used;

  - (ii)deployment has scaled beyond isolated or occasional use;

  - (iii)the resulting consumption varies with work rather than with headcount; and

  - (iv)no apparatus records, attributes, and constrains that consumption;

then the organization cannot exercise economic control over the deployment, whatever the diligence of the people operating it.

The final clause is the practical content. Economic control is not a property of how carefully individuals behave. Five thousand engineers can each act reasonably and still produce an aggregate none of them chose. Every one of those decisions is defensible on its own. None of them is visible to the others. Governance is what supplies the view none of the participants has.

The word apparatus is doing specific work, so it is worth unpacking into its parts. A governing apparatus for a deployment holds three things, and an organization missing any one of them does not have economic control.

The first is a record: some system that writes down what was consumed, at a grain finer than the invoice. The second is an attribution: a rule that assigns each unit of consumption to a team, a product, or a purpose. A record without an attribution tells an organization how much it spent and not who spent it. The third is a constraint: a limit, a budget, an alert, or an approval that can actually stop or slow consumption when it departs from plan.

Most organizations that believe they have cost governance have the first, sometimes the second, and rarely the third. A dashboard nobody acts on is a record flow with no constraint attached. It converts a surprise into a slower surprise, which is an improvement, and it is not control.

One question follows immediately and the chapter will not answer it here: who owns the apparatus. Chapter 1 named the problem as a category error and Chapter 3 names the discipline that resolves it. What can be said now is that the apparatus does not belong to whichever function noticed the problem first. Finance noticing an overrun does not make cost governance a finance system, any more than engineering noticing latency makes reliability an engineering-only concern.

This also explains why the remedy is never simply to spend less. An organization that cuts consumption without building the record flow has reduced its cost and learned nothing, which leaves it in the same position at a lower volume. Chapter 8 builds the record flow directly, and Chapter 10 turns it into a budget. What matters here is the order: the record comes before the budget, because a budget without a record is a number nobody can check.


## 2.8 What this chapter does not claim

Three limits belong on the record before the diagnostic that follows, because each is a conclusion a reader could reasonably draw and none of them follows.

The chapter does not claim that unmanaged deployments are wasteful. Waste is a statement about the ratio of value to cost, and the whole argument is that the value side of that ratio is unmeasured. Calling a deployment wasteful on a cost figure alone is one error. Calling it a success on an adoption figure alone is the same error, pointed the other way.

The chapter does not claim that measurement is free. Building a record flow costs engineering time, and building a value measurement costs more than that, because it requires deciding what to measure before the answer is known. Chapters 8 and 12 treat both as investments with their own returns rather than as hygiene.

The chapter does not claim that every deployment needs all three flows managed to the same standard. A pilot with twenty users and a fixed monthly cost does not need an attribution system. THM-004’s second antecedent is scale, and it is there precisely because the theorem does not bind below it. The judgment a manager has to make is when a deployment has crossed from the first case to the second, and the usual answer is that it crossed some time ago.


### [CRAFT SECTION]


## Mapping the three flows

This is the diagnostic the rest of the book uses. It takes one named deployment and establishes the condition of each flow, in order, with the evidence that settles it. It is deliberately short: it is meant to be run in an afternoon on a real deployment, not staffed as a project.

Two habits make the difference between a mapping that changes something and one that fills a slide. The first is naming the evidence for every diagnosis, because a diagnosis without evidence cannot be challenged and therefore cannot be corrected. The second is running it on a deployment that is already live rather than one being planned. A planned deployment has no flows yet, only intentions about them.

Step 1. Name the deployment and its boundary. State which tool, which population, and over what period. A boundary that is not stated will move while the diagnosis is being made.

Step 2. Trace the usage flow. Who or what sends requests, at what rate, and is the rate rising? The evidence is a count over time, not an impression. If no count exists, that is a finding about the record flow rather than the usage flow.

Step 3. Trace the record flow. State what is recorded, by whom, and at what grain. Ask one question to settle it: can the organization say which team consumed what, without asking the provider? An invoice total is not a record flow.

Step 4. Trace the cost-and-value flow, in two halves. On the cost side, state who owns the invoice and what it can be broken down by. On the value side, state what was supposed to improve, whether it was measured before the deployment, and whether it has been measured since.

Step 5. Diagnose each flow as managed, partly managed, or unmanaged, and say what evidence would change the diagnosis. A diagnosis nobody could overturn is an opinion.

Two failure modes recur when organizations run this mapping on themselves, and both are worth naming in advance. The first is answering step 3 with a number that came from the provider. A provider’s usage console is evidence about the provider’s record flow, not the buyer’s. An organization that can see its consumption only by logging into a vendor portal has confirmed the diagnosis rather than escaped it. The second is answering step 4’s value half with an adoption figure. The share of employees using a tool is a fact about the usage flow. It becomes a value claim only if somebody has established that use produces the outcome the deployment was funded to produce.

Run against Uber as reported, the mapping produces a result worth reading carefully, because it is less flattering than it first appears. The usage flow is partly managed. The direction of adoption was visible month by month, and adoption is a count of people rather than a count of requests. Section 2.2 asks a usage flow to state how many requests were made and whether the number is rising, and the public account does not establish that anyone could.

The record flow is partly managed. A per-engineer cost range was reported, so consumption was visible at some grain, and the reporting does not establish that it was attributed to teams or compared against the plan. The cost-and-value flow has a complete cost half and an unbuilt value half, which is what the chief operating officer’s question suggests.

Notice that the mapping refuses to award the deployment a clean flow anywhere, on evidence that a casual reading would treat as success. That is the diagnostic working. An adoption percentage is the most available number in any deployment, and it answers a question about people rather than about consumption.

A second mapping shows what a different answer looks like. The deployment below is constructed for this exercise and is not drawn from a source.

A retailer deploys an AI assistant to two hundred customer-service agents. Volumes are recorded per agent per shift, because the contact-center platform already recorded everything else per agent per shift. Cost is billed monthly to the service organization and broken out by queue. Before the deployment, the retailer measured average handling time and first-contact resolution for six months. It still measures both.

The usage flow here is managed, and for an unremarkable reason: the record was a by-product of a system the retailer already ran. The record flow is managed at a useful grain, because consumption can be attributed to a queue. The cost-and-value flow is managed on both halves, because somebody measured the outcome before the deployment began and kept measuring after.

Notice what made the difference. The retailer did not have better intentions than the engineering organization in the opening case. It had a prior measurement system that happened to fit, and a deployment small enough that fitting it was cheap. Most of the work of managing flows is done before a deployment scales, which is the awkward part: the moment when it is easiest to build the apparatus is the moment when it is hardest to justify.

The mapping is deliberately blunt about partial answers. An organization that can attribute half its consumption has a partly managed record flow, not a managed one, and recording it as partial is what makes the next conversation possible. The purpose is to produce a short list of the specific things that are not known, so that somebody can decide which of them is worth the cost of knowing. Awarding a grade would settle nothing.

The common result of this exercise in a first-year deployment is a healthy usage flow, an absent record flow, and a cost-and-value flow with only its cost half built. Organizations are usually surprised by the second finding rather than the third, because the absence of a record is invisible until somebody asks a question that needs one.


### [CHAPTER SUMMARY]

A deployment produces three flows: the work itself, the record of that work, and the money and value attached to it. Each can be in a different condition, and they are managed by different parts of the organization.

An unmanaged flow does not stay still. Usage grows toward whatever the tool makes easy, records decay because their raw material is perishable, and cost accrues without anyone acting.

Cost is recorded automatically because billing requires it. Value is recorded only where an organization builds the measurement. The consequence is that an organization running an unmanaged deployment holds all of the cost and an unknown fraction of the value, and the load-bearing word is unknown.

Deployments are funded as projects and run as flows. A funding decision happens once; the consumption it authorizes continues daily and changes as the work changes. Without a recurring comparison, the business case quietly becomes the organization’s belief about what the deployment delivers, and a forecast is treated as a result.

The record flow is skipped most often, and for structural reasons rather than careless ones. It pays only in the future, it belongs to no single function, and its absence is invisible until somebody asks a question that needs it. Building it is a decision an organization has to make before that question arrives.

Because consumption varies with work rather than with headcount, economic control at scale requires an apparatus rather than diligence. That is THM-004, and it is why the chapters that follow build the record before they build the budget.


### [KEY TERMS]

A continuous stream of related activity within a deployment, described by its rate, its direction, and whether anything is being recorded about it. A flow is managed by governing the stream over time rather than by approving each event within it.

The stream of consumption events a deployment generates: requests made, work performed, and outputs returned. It is the only one of the three flows an organization is normally trying to increase.

The stream of information an organization keeps about its own usage, including which team or product consumed what, at what volume, and when. The provider always holds a record because it must bill; the buyer holds one only if it builds one.

The stream of money spent on a deployment together with the return attributed to it. The two halves are treated as one flow because neither is usable alone for a management decision.

The condition in which a deployment’s cost is recorded automatically, because metering produces the bill, while its value is recorded only where the organization has deliberately built a measurement. The two sides of the same activity are therefore known to different standards.

The diagnostic that establishes the condition of the usage, record, and cost-and-value flows in a named deployment, and states what evidence would change each diagnosis.


### [DISCUSSION QUESTIONS]

An executive says the organization’s AI deployment is well managed because the monthly invoice is reviewed and approved every month. Using the three flows, explain what that review does and does not establish.

The chapter claims that an unmanaged record flow decays rather than merely staying empty. Give a concrete example of information about AI usage that is available on the day the work happens and unavailable six months later, and explain what makes it perishable.

Why does the chapter insist that the load-bearing word is "unknown" rather than "small"? What would a manager do differently under each reading?

Chapter 1 argued that a flat price relocates the meter to the provider rather than abolishing it. Using that result, explain why a flat-rate contract does not remove an organization’s need for a record flow.

The chapter argues that a record flow is skipped because its value is entirely in the future tense and it belongs to no single function. Which function in your organization would you make responsible for it, and what would that function need in order to accept the responsibility?


### [PROBLEMS]

P1 · Worked

Mapping a deployment from public reporting

Using only the facts given in the opening case, map the three flows for the deployment described, diagnosing each as managed, partly managed, or unmanaged, and stating the evidence that would change your diagnosis.

Work through the flows in order, and resist the first answer. The usage flow looks managed, because adoption was tracked month by month and the share of engineers using the tool could be stated. But section 2.2 sets the test as request volume, not headcount. On the facts given, the organization could state how many people had the tool and not how much they were consuming, so the correct diagnosis is partly managed.

The record flow is also partly managed. A per-engineer monthly cost range was reported, so consumption was visible at some grain. What the given facts do not establish is whether that record was attributed to teams or compared against the plan. The evidence that would change the diagnosis is a monthly consumption figure attributed to a team and set beside a forecast.

The cost-and-value flow is unmanaged on its value half. The cost half is complete, because the invoices arrived and the annual total was known by April. The value half is absent, and the evidence for that absence is that a senior executive was publicly asking whether the spending had been worth it. That question is not asked about a deployment whose return has been measured.

The diagnosis is therefore two partial flows and one half-built, on a deployment that most observers would have called a success four months in. That is the point of the mapping. It converts an impression of success into a short list of things nobody can state, and the list is what a manager can act on.

P2 · Guided

The seat forecast that did not hold

A company budgets an AI assistant at a fixed monthly amount per employee, multiplied by the number of employees expected to have access, held flat for twelve months. Twelve months later the total spend is three times the budget, while the number of employees with access is exactly what was forecast.

State which of the three antecedents of THM-004 this situation satisfies, and identify the specific assumption in the forecasting method that failed. Then state what the company would need to record, at what grain, to produce a forecast that could have held.

Work in that order rather than starting from the remedy. The antecedents establish whether the theorem applies at all; a deployment that has not scaled is outside its scope and needs no apparatus. Only once the theorem applies is the forecasting question worth asking, and only then does the grain of the missing record become determinate rather than a matter of taste.

P3 · Independent

Two organizations, one number

Two organizations report the same annual AI spend. The first has built a record flow that attributes consumption to teams and a value measurement for two of its five deployments. The second has neither, and knows only its invoice total.

Explain why the two organizations are not in comparable positions despite the identical number, and state what the second organization can and cannot conclude from its own spend figure. Your answer should distinguish what is unknown from what is known to be small.

Then answer a second question. The first organization has measured value on two of five deployments and the second has measured none. State which of the two is more likely to cut a deployment that was in fact producing a return, and explain the mechanism by which its better record keeping could produce that outcome.

P4 · Independent

The business case that became a belief

An organization approved an AI deployment two years ago on a business case projecting a twenty per cent reduction in the time taken to complete a routine task. The deployment is still running. The projection has never been revisited, and it is quoted in the current year’s planning documents as the deployment’s contribution.

Identify what has happened to the status of the twenty per cent figure between the business case and the planning document, and name the step in the organization’s process that should have prevented it. Then state the smallest change to the review schedule that would stop it recurring, and explain why a change to the business-case template would not.

Interleaving: question 4 and problem P2 require Chapter 1's results. P2 uses the resource consumption model and question 4 uses meter relocation.