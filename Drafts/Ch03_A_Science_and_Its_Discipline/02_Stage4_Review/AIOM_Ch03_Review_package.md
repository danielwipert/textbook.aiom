# Review package: Chapter 3, "A Science and Its Discipline"

This is ONE self-contained file. Everything you need is inside it: your
instructions, the required output format, and all the material to review. Do not
ask for other files. Read the whole file before you begin.

---

## PART 1. Your task

You are reviewing one chapter of an academic textbook for business graduate
students, titled *AI Operations Management*. Chapter 3 is under review.

This file contains three documents, each between clear BEGIN and END markers in
Part 3 below:

- **Document 1: Chapter 3, the text under review.**
- **Document 2: the reference extract.** What the chapter is meant to do (its
  structure entry, its competency, its outline, the author's rulings on its
  plan) and the book's seven craft criteria, C1 to C7.
- **Document 3: Chapter 1 of the same book**, locked and published. It is the
  exemplar the craft standard was measured from. Calibrate against Chapter 1,
  not against how closely Chapter 3 resembles itself.

### Three warnings

1. **Sourcing is out of bounds.** Whether any figure or fact is true is checked
   separately, later, against the sources. You may still flag a sentence that
   makes an empirical claim with no visible support.
2. **Formal statements are not prose.** Quoted statements of theorems, lemmas
   and propositions are verbatim from a formal registry. Do not judge their
   wording. Judge the prose around them.
3. **"No findings" is not an answer.** A review that says the chapter meets the
   criteria with no findings will be discarded as confirmatory.

### How to review

Review in three separate sections. In every section, do not report whether
something is met. Quote the WEAKEST evidence, say precisely what is wrong, and
say whether it is a defect, a deliberate choice serving something else, or noise.

**Section A, structure.** Does every slot serve the chapter's stated purpose?
Is competency C4 DELIVERED, meaning a reader could actually perform it after this
chapter, unaided, on a theorem they have not seen? Is the trace load-bearing or
decorative? Does the chapter front-run anything a later chapter is meant to
reveal? Does anything in the outline go missing, and does anything appear that
the outline does not call for?

**Section B, teaching.** Where would a sceptical, busy MBA-level reader stall,
lose the thread, or stop believing the argument? Judge clarity, pacing,
cognitive load, example fitness, and transitions. Name the single paragraph you
would cut first and the single place most in need of a concrete example.

**Section C, voice and craft.** One finding per criterion, C1 to C7, quoting the
weakest passage by section and the strongest, so your calibration is visible.

---

## PART 2. Required output format

Reply in Markdown, using exactly this structure and nothing else. No preamble.

```
# Second-model review: Chapter 3

## Section A: Structure
## Section B: Teaching
## Section C: Voice and craft

## Findings

| ID | Sec | Where (section heading) | Quote (exact, under 30 words) | What is wrong | Type | Severity | Suggested fix |
|---|---|---|---|---|---|---|---|
| S-1 | A | ... | "..." | ... | defect | high | ... |

## Fix first
1. S-n: one line on why
2. S-n: ...
3. S-n: ...
```

Rules for the table:

- **ID**: S-1, S-2, and so on, numbered across all three sections.
- **Sec**: A, B or C. For Section C, start the "What is wrong" cell with the
  criterion (C1 to C7). Give every criterion at least one row.
- **Quote**: copied exactly from Document 1, so the author can find it.
- **Type**: one of `defect`, `deliberate`, `noise`.
- **Severity**: one of `high`, `medium`, `low`.
- Under each Section heading, write at most five sentences of overall judgment.
  The findings themselves go only in the table.
- Do not use em dashes or en dashes anywhere in your reply.

---

## PART 3. The material

<<<<< BEGIN DOCUMENT 1: CHAPTER 3, UNDER REVIEW >>>>>

Part I · The Argument

# A Science and Its Discipline

## [OPENING CASE]

## The discipline that changed its mission

*Dated: February 2026. Found by search. Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself. See the source register.*

In February 2026, the FinOps Foundation changed its mission statement. For years it had described its purpose as advancing the people who manage the value of cloud. The new statement replaced one word: the Foundation now advances the people who manage the value of technology.

The change came with the Foundation’s annual survey of its own practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 of them, responsible for more than $83 billion a year in cloud spending. Its central finding concerned work the discipline had not been founded to do. Ninety-eight percent of respondents now managed spending on AI. Two years earlier, the figure had been 31 percent.

FinOps was built for a specific problem. Cloud computing let engineers buy capacity with a few lines of code, and the bills arrived after the capacity had been used. The discipline grew up to make engineering, finance, and business teams jointly accountable for that spending. Nobody designed it to manage AI. Its practitioners took on AI spending anyway, and by 2026 nearly all of them were doing so.

The report also recorded what that work had not yet produced. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.” The practitioner was speaking from inside the discipline asked to manage AI spending.

That is the gap Chapters 1 and 2 described, now reported by the people asked to fill it. The organization pays for a metered resource, and the cost arrives by default. The value arrives only if someone builds the means to measure it. A cloud cost discipline is a capable neighbor, and it has moved toward work that no discipline was built to hold: managing the economics of what an organization consumes when it uses AI.

That work needs two things a neighbor cannot lend it: a body of knowledge about what is true, and a practice that acts on it. The relationship between the two disciplines is worked out in full in Chapter 14. The question at the center of the work is still unanswered.

### 3.1 Why name a science

Managers act on claims about how their business works. A budget assumes that cost follows usage. A pricing negotiation assumes the provider has a reason to accept a lower price. A dashboard assumes that what it shows will change what someone does. When those claims are wrong, the management built on them fails, however carefully it is carried out.

Claims of this kind can live informally: in experience, in rules of thumb, and in the slides of whoever presented last. Informal knowledge is useful, and it has a cost. Two managers can hold opposite beliefs about the same deployment, and neither can show the other where the disagreement lies. The argument then turns on confidence rather than on evidence.

Chapters 1 and 2 each ended on a stated result rather than an opinion. Chapter 1 set out the conditions under which deployed AI is a resource the organization consumes. Chapter 2 set out the conditions under which a scaled deployment cannot be controlled without a governing apparatus. Each result appeared in a panel with an identifier, and each identifier points to a larger body of claims behind it.

That body is AI Business Economics. It is a science in a specific and limited sense: an ordered collection of conditional claims about the business economics of consuming AI, each stated precisely enough to be checked. The word does not mean laboratory experiments, and it does not mean certainty. It means that every claim says when it applies, what it concludes, and which other claims it rests on.

> **DEFINITION CALLOUT · AI Business Economics**
>
> The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

The claims are kept in a registry. The registry is a structured record of every definition, assumption, and result in the science, with each result linked to the claims that support it. A definition fixes what a term means. An axiom states an assumption the science accepts without proof. A proposition states a single claim, accepted because of the definitions, axioms, or earlier claims it names as its support. A lemma combines propositions, and sometimes other lemmas, into an intermediate result. A theorem combines lemmas into a result with direct consequences for management.

Those links are the registry’s most important feature. Every higher claim names the lower claims it depends on, and those claims name their own supports in turn. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. Anyone holding the registry can start at any theorem and follow its supports downward until they reach definitions and axioms. In this book, Appendix A reproduces every certified theorem and lemma, and propositions are cited by identifier, so a reader can trace any claim to lemma level unaided and below it wherever a chapter or an exercise supplies the propositions. For a manager, that settles something practical: no conclusion is propped up by circular reasoning, so any doubt can be pushed down to a smaller claim that can be checked.

The registry also records which claims are complete. A claim is certified when every claim it depends on is itself certified and its supporting argument meets the registry’s fixed conditions. No one types that status in. The registry’s own validator computes it from the graph, version by version. A claim with a gap below it carries a record of what is missing. This book renders and cites certified claims only. Presenting an uncertified claim as a theorem would claim more than the science claims.

> **DATED EVIDENCE BOX · Dated: August 2026**
>
> At the version this book was written against, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records of evidence the science still needs. It recorded 1,777 dependency links among them, and 397 of the 413 objects were certified. The registry is revised as the science develops, so these figures describe one version and not the science itself.

One rule governs how this book uses the registry. The registry justifies the book. It does not organize it. The chapters follow the order in which a manager needs to learn, which is not the order in which the science derives its results. The registry’s role is to stand behind each result the book teaches, so that a reader who doubts a claim can follow it to its support. Reversing the rule would order the chapters by proof rather than by need, and a manager would meet definitions for many pages before reaching a decision they recognize.

### 3.2 Tracing a result the reader already accepts

Chapter 2 ended on a result, and following it down through the registry is the way to learn how the registry works. A reader who accepted Chapter 2’s argument already believes the result, so the only new thing to learn is how the support behind it is arranged. Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough.

The registry states that result as THM-004:

> **THEOREM PANEL · Theorem 2 · THM-004**
>
> *Scaled AI Deployment Requires Cost Governance for Economic Control*
>
> Within the defined deployment and measurement boundary, if:
>
>   (i) production scaling expands the usage surface of AI deployment;
>
>   (ii) measurement enables visibility into measurable cost-bearing activity;
>
>   (iii) visibility enables management mechanisms; and
>
>   (iv) buyer total cost extends beyond access price;
>
> then scaled AI deployment requires cost governance for economic control.

Each condition has a plain meaning a manager can check against a deployment. The first says the deployment has moved from a pilot into daily operations, which multiplies the places where usage can occur. The second says that measuring usage makes the activity that costs money visible. The third says that what is visible can have monitoring, limits, attribution, or other management mechanisms applied to it. The fourth says the organization pays more in total than the price of access. When all four hold, an organization that wants control over the deployment’s economics needs cost governance.

THM-004 names four lemmas as its support, one for each condition, and all four are certified. LEM-016, “Production Scaling Expands Usage Surface,” supports the first. LEM-002, “Measurement Enables Visibility,” supports the second. LEM-020, “Visibility Enables Management Mechanisms,” supports the third. LEM-006, “Buyer Total Cost Extends Beyond Access Price,” supports the fourth.

The registry also records the theorem’s proof, which joins them in two pairs. The first and fourth lemmas give an exposure that grows with the deployment and cannot be read off the price. The second and third give the only route by which such an exposure becomes manageable: measurement makes it visible, and management mechanisms can be applied to what is visible. Control therefore requires the apparatus that does both, which the theorem calls cost governance.

One level further down, each lemma rests on propositions. LEM-020 is a useful one to follow, because it shows how the registry is built. Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.” It rests on seven propositions and on one other lemma.

The propositions are small claims, each close to obvious on its own. PROP-043 states: “If activity is metered, records describing measured activity are generated or maintained.” PROP-053 states: “If economic exposure exists, monitoring mechanisms may be used to observe the sources or magnitude of that exposure.” PROP-085 states: “If usage information becomes visible, decisions regarding management, allocation, optimization, or monitoring may reference that information.” No manager would dispute any of them. The work lies in how they combine.

The other lemma under LEM-020 is LEM-002, the same lemma that supports THM-004’s second condition directly. Figure 3.1 shows the branch through LEM-020, with the shared support visible. The registry is therefore not a tree, in which each claim has one parent. It is a graph, in which one claim can support several others.

[FIGURE 3.1. Drawn figure, not reproduced here.]

**Figure 3.1.** One branch of the trace. THM-004 rests on four lemmas, one for each condition. LEM-020 rests in turn on LEM-002, which also supports the theorem directly, and on seven propositions, three of which are shown.

The trace changes what a manager can do with the theorem. Before it, THM-004 is a conclusion to accept or reject as a whole. After it, the theorem is a set of smaller claims, each of which can be examined on its own. A manager who doubts the conclusion can now say which supporting claim they doubt. A disagreement about a whole conclusion has no obvious way to end. A disagreement about one proposition can be settled.

### 3.3 How to read a formal claim

A formal claim is read in four parts: its conditions, its scope, its non-claims, and the falsifying case that would defeat it. A manager who can state all four can use the claim without being misled by it.

The conditions are the “if” clauses. Each is true or false of a given case, and in THM-004 they are the four numbered clauses. If a deployment fails any one of them, the theorem says nothing about it. A pilot used by one team for a few weeks has not been scaled into daily operations, so it fails the first condition. The theorem then neither requires governance for the pilot nor rules it out. Reading the conditions first prevents a basic misuse of a formal claim: applying it where it was never stated to hold.

The scope fixes which cases the claim talks about at all. As this book sets it, THM-004 opens with its scope, before the word “if”: one defined deployment and its measurement boundary. The registry adds that the theorem applies where an organization seeks economic control over the resulting cost. The claim concerns one deployment inside one boundary, not an organization’s AI activity in general. A manager who applies it across a whole company must first show that each deployment meets the conditions.

The non-claims say what the claim deliberately does not establish. The registry records them for every claim, so a reader does not have to guess. THM-004 asserts that governance is necessary for control, not that governance delivers control. It does not claim that governance is costless. It does not say at what scale the requirement begins to bind, and it asserts nothing about how large the exposure is. One further limit is this book’s, not the registry’s. As Chapter 2 noted, the three flows are this book’s organizing framework. THM-004 formalizes the economic consequence of the third flow’s asymmetry, and it does not establish the taxonomy itself. The link is direct: cost arrives by default and grows with scale, which is what the first and fourth conditions say, so control over it can arrive only by design, through the measurement and management the second and third describe.

> **DEFINITION CALLOUT · Non-claim**
>
> A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating the non-claims prevents a claim from being cited for more than it says.

The distinction between necessary and sufficient matters most in practice. A manager who read THM-004 as “governance produces control” could buy a dashboard and expect the costs to settle. The theorem promises nothing of the kind. It says only that without governance there is no route to control. LEM-020 makes the same limit explicit one level down: it does not claim that management mechanisms are automatically effective.

The falsifying case says what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition and still lacks the conclusion. The conditions describe what measurement and management would do, not that they are in place, so a deployment with no instruments installed can still meet all four. For THM-004, the falsifying case would be a scaled deployment meeting all four conditions whose organization holds economic control over its cost with no measurement and management apparatus at all. A claim that names no such case cannot be wrong, and a claim that cannot be wrong tells a manager nothing.

These four parts answer an objection the formal style invites. A skeptical reader may call the registry a set of word games: obvious points dressed in numbered clauses. The objection mistakes the purpose of the form. Formal statement is not decoration. It fixes in advance what would count as the claim being wrong. A claim about AI that never says when it applies or what would defeat it cannot be wrong in that sense. A claim that states its conditions can be tested, and a claim that can be tested can be improved.

### 3.4 The discipline that acts on the science

Knowing what is true does not, by itself, change what an organization does. Medicine needs physiology, but a patient is treated by clinicians who apply it. Engineering needs physics, but a bridge is built by engineers working to codes and procedures. In each case a practice stands between the knowledge and the result, and that practice has its own methods, roles, and standards.

AI Operations Management is that practice for AI consumption. It is the work an organization does week to week to manage what it consumes. It buys AI capacity, plans its use, and records and assigns that use. It decides what runs when capacity is short, and it holds the spending to account for what it returns. Chapter 1 described the problem as a category error. AI Operations Management is the discipline that resolves it, by managing AI as the consumed resource it is rather than as software the organization has bought.

> **DEFINITION CALLOUT · AI Operations Management**
>
> The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

The discipline is organized as five functions. Each is a capability an organization either has or lacks, and Part III teaches each one, with metering and attribution taking two chapters.

The first function is sourcing. The organization must be able to buy AI capacity that matches what its work requires, neither paying for capability the work does not use nor starving work that needs more. Sourcing decides which models and providers serve which work, and on what terms. A company that sends every request to its most capable model, including requests a smaller one would answer as well, is paying for capability its work does not use.

The second function is planning and budgeting. The organization must be able to state how much AI it expects to consume in the coming period and to notice when actual consumption departs from that expectation. A budget in this sense is a commitment made in advance, so that a deviation is visible when it happens rather than when the money is gone. Chapter 2’s opening case showed what its absence costs.

The third function is metering and attribution. The organization must be able to record what was consumed and to assign each unit of consumption to the team, product, or purpose it served. Chapter 2 called this the record flow.

The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to the capacity that suits it. Those decisions happen whether or not anyone makes them deliberately. When two workflows draw on one provider account with a fixed rate limit, one of them waits whenever the other is busy. The function exists to make that choice by rule rather than by accident.

The fifth function holds value to account at a boundary. The organization must be able to say where a deployment pays for itself, measured over a defined scope and period, and who is responsible for knowing. This is the hardest of the five, and it is the function the FinOps practitioners in the opening case could not yet perform.

Figure 3.2 sets the two layers together, with the science beneath and the discipline standing on it through its five functions.

[FIGURE 3.2. Drawn figure, not reproduced here.]

**Figure 3.2.** The two layers. AI Business Economics states what is true about consuming AI. AI Operations Management acts on it through five functions, all taught in Part III.

The two layers depend on each other in different ways. A result about governance changes nothing until an organization builds the apparatus the result describes, so the science needs the discipline to have any effect. The discipline needs the science for a different reason: a practice built on wrong claims fails however well it is run.

### 3.5 Where the discipline ends

Several kinds of work with AI happen before or beside the work this book governs. Chapter 1 set aside three subjects that sit close to AI but outside this book. Each has its own purpose and literature, and each ends before AI Operations Management begins.

The first is how models work: their architectures, training, and internal behavior. That subject belongs to computer science and machine learning engineering. It ends where a model becomes a service an organization can call. AI Operations Management begins at that call, where each use consumes resources and costs money.

The second is prompt engineering, the craft of writing inputs that produce better outputs. It improves individual uses of AI. AI Operations Management governs the total of those uses: how many there are, what they cost, and what they return. A better prompt can lower the cost of one request. Only the discipline can say whether the organization’s requests, taken together, are worth what they cost.

The third is finding uses for AI: deciding which business problems AI might solve. That work belongs to strategy and innovation, and it ends when a use is chosen. AI Operations Management begins there, with how the capacity for that use is bought, and manages the use from then on.

Four established disciplines sit closer still. Each manages something adjacent to AI consumption, and each lacks something this territory needs. Table 3.1 sets them side by side.

| Neighbor | What it is for | What it manages | What it lacks for this territory |
|---|---|---|---|
| AIOps | Applying machine learning to run IT operations: correlating events, detecting anomalies, finding causes | The health and performance of IT systems | It uses AI to watch systems. It does not govern what consuming AI costs or returns |
| MLOps | Building, deploying, and monitoring machine learning models in production | The lifecycle of models an organization builds | It ships models. It does not govern the consumption of capacity an organization buys |
| FinOps | Financial accountability for technology spending, through collaboration among engineering, finance, and business teams | Cloud and wider technology spending | It was built around cloud billing. A practitioner told its own survey that no one could yet say whether AI provides value |
| Regulatory AI governance | Ensuring that uses of AI are lawful, safe, and accountable to regulators | Risk and compliance | It asks whether a use is permitted, not whether it is economically managed |

Table 3.1. The four neighboring disciplines. Each manages something adjacent to AI consumption, and none was built to govern its economics.

FinOps is the nearest neighbor and the hardest border to draw. It already manages spending, it has moved toward AI, and its own definition speaks of maximizing the business value of technology. How the two divide the work is a question for Chapter 14. The border does not lie in intent. It lies in the evidence of the opening case, where a practitioner of the discipline that reads the AI bills told its own survey that no one could yet say whether AI was providing value.

Regulatory governance decides whether an organization may use AI in a given way, and this book takes that answer as given and asks how the permitted use is managed.

### 3.6 Five questions the discipline exists to answer

AI Operations Management exists to answer five questions an organization cannot answer without it. Each belongs to one of the five functions, and each is answered in the chapter that teaches that function. Part III takes them in a different order, for reasons given there.

An organization that manages its AI consumption can answer these five questions from its own records:

Question 1. “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7.

Question 2. “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10.

Question 3. “Who consumed what last month, in service of which work?” This is the metering and attribution question, answered across Chapters 8 and 9.

Question 4. “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11.

Question 5. “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12.

These are the Founding Questions. The phrase that matters is the one that introduces them: “from its own records.” An organization can always produce an answer by asking the provider, estimating, or repeating the business case. Each of those produces a number, and none produces knowledge the organization holds and can check.

A reader who has finished Part I has no method yet for answering any of them from records. The opening case suggests the gap is not peculiar to newcomers: a practitioner in the discipline closest to AI spending said no one could yet tell whether AI was providing value. That is the fifth question, put by someone well placed to answer it. Parts II through IV exist to change that. Part II establishes what is true. Part III builds the five functions. Part IV turns them into an institution.

## [CRAFT SECTION]

## The trace procedure

The **trace procedure** is how a manager reads a formal claim before relying on it. It turns a theorem from a conclusion to be accepted or rejected whole into a set of smaller claims, each of which can be checked. The procedure has six steps.

Step 1. Locate the claim in the registry by its identifier, and record its name exactly as the registry gives it.

Step 2. Restate its conditions in one sentence of ordinary business language, keeping every antecedent and adding none.

Step 3. List the claims it depends on, by identifier and name.

Step 4. Walk one level down. Restate each dependency in one sentence, and note any condition it adds that the claim above did not state.

Step 5. State what the claim establishes and, separately, what it does not.

Step 6. Name the falsifying case: a case that meets every condition and still lacks the conclusion.

Steps 2 and 6 do most of the work. A restatement that drops an antecedent produces a claim the registry does not make, and step 2 is where that error enters. Step 6 is the test of whether the reader has understood the claim at all. A reader who cannot describe the case that would defeat a claim cannot say what the claim rules out.

Applied to THM-004, the procedure runs as follows.

Step 1 records THM-004, “Scaled AI Deployment Requires Cost Governance for Economic Control.”

Step 2 restates its conditions. Within one deployment and its measurement boundary, the theorem applies when four things hold. Scaling the deployment expands where usage can occur. Measurement makes the costly activity visible. What is visible can have management mechanisms applied to it. Total cost runs beyond the price of access.

Step 3 lists its four dependencies: LEM-016, LEM-002, LEM-020, and LEM-006, one for each condition. The registry marks all four as required. Some claims also carry contextual dependencies, which bear on the claim without being conditions of it, and step 3 records which kind each is.

Step 4 restates each one. LEM-016 says that moving from isolated use into repeated operations can increase the number of usage events and demand points. LEM-002 says that measured and recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. LEM-020 says that visible usage or exposure can have monitoring, limits, attribution, or other management mechanisms applied to it. LEM-006 says that a buyer who incurs several kinds of cost pays more in total than the access price.

Step 4 also asks what each dependency adds, and LEM-020 adds something. Its scope requires that the organization have reliable visibility and the authority to apply management mechanisms. The third condition of THM-004, that visibility enables management mechanisms, therefore carries more than its words show. It holds only for someone with the authority to act. A team that can see its costs but cannot cap them does not meet it. The trace found what the condition requires in practice.

Step 5 separates the claim from its readings. THM-004 establishes that cost governance is necessary for economic control of a scaled deployment. It does not establish that governance is sufficient or costless, at what scale the requirement binds, how large the exposure is, or that a deployment has three flows.

Step 6 names the falsifying case: a scaled deployment meeting all four conditions whose organization controls its cost with no measurement and management apparatus. Finding one would show the theorem false.

The procedure is deliberately slow. A trace of one theorem takes longer than reading the theorem and agreeing with it. The time is worth spending once for each claim a decision rests on, because it is how a manager learns what the decision is resting on.

### Chapter summary

AI Business Economics is the science of consuming AI. It is an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on. The claims are kept in a registry, linked by dependency, and this book renders and cites certified claims only.

The registry justifies this book. It does not organize it. The chapters follow the order in which a manager needs to learn, and the registry stands behind each result so that a reader who doubts a claim can follow it to its support.

A trace follows a claim down through the registry, from a theorem to the lemmas and propositions it rests on. It turns a conclusion into a set of smaller claims that can each be examined.

A formal claim is read in four parts: its conditions, its scope, its non-claims, and the evidence that would defeat it. Formal statement is not decoration. It fixes in advance what would count as being wrong.

AI Operations Management is the discipline that acts on the science, through five functions: sourcing, planning and budgeting, metering and attribution, allocation and routing, and holding value to account at a boundary. It begins where a model becomes a service an organization consumes, and it borders AIOps, MLOps, FinOps, and regulatory governance without being any of them.

The Founding Questions are the five questions the discipline exists to answer from an organization’s own records. At the end of Part I, the reader has no method yet for answering any of them.

### Key terms

**AI Business Economics.** The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

**AI Operations Management.** The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

**Registry.** The structured record of every definition, assumption, and result in AI Business Economics, with each result linked to the claims that support it.

**Theorem.** A registry result that combines lemmas into a conclusion with direct consequences for management. The book sets each theorem it relies on in a numbered panel.

**Lemma.** An intermediate registry result that combines propositions, and sometimes other lemmas, and supports one or more theorems.

**Certified claim.** A registry claim whose supporting argument has been checked and whose every dependency is itself certified. The book renders and cites certified claims only.

**Trace.** Following a registry claim down through the claims it depends on, from a theorem to its lemmas and from a lemma to its propositions.

**Condition.** A requirement a deployment must meet for a formal claim to apply to it. A claim says nothing about a case that fails any of its conditions.

**Scope.** The part of a formal claim that fixes which cases it talks about at all, such as one deployment inside one boundary. A case outside the scope is outside the claim, whatever its conditions.

**Non-claim.** A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating the non-claims prevents a claim from being cited for more than it says.

**Falsifying case.** A case that meets every condition of a formal claim and still lacks its conclusion. Finding one would show the claim to be wrong.

**Founding Questions.** The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions.

**Trace procedure.** The six-step method for reading a formal claim before relying on it: locate it, restate its conditions, list its dependencies, walk one level down, separate what it establishes from what it does not, and name the case that would defeat it.

### Discussion questions and problems

## [DISCUSSION QUESTIONS]

**1.** The book insists that the registry justifies it but does not organize it. Describe what a reader would lose if the chapters followed the registry’s order of derivation instead.

**2.** Of the four borders in Table 3.1, which is hardest to defend, and why? State what evidence would move that border.

**3.** Restate one Founding Question in the language your chief financial officer would use, without losing any of its content. Then say which part of the question the restatement was most tempted to drop.

**4.** Chapter 2 diagnosed a deployment through its three flows. Match each flow to the functions in Section 3.4 that manage it, and say which functions share a flow and which manage none.

## [PROBLEMS]

**P1 · Worked.** A trace of LEM-020

The craft section traced a theorem. Trace one of its lemmas, LEM-020, with the same six steps, as a model for problem P2.

Step 1. LEM-020, “Visibility Enables Management Mechanisms.” Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.”

Step 2. When the people responsible for a deployment can see its usage or its cost, they can apply monitoring, limits, attribution, or other management mechanisms to it.

Step 3. Eight dependencies, all required: the lemma LEM-002 and seven propositions, PROP-032, PROP-039, PROP-041, PROP-042, PROP-043, PROP-053, and PROP-085.

Step 4. LEM-002 says recorded activity becomes observable enough to support analysis, attribution, monitoring, or management. It adds a condition: the recording must be detailed enough for the relevant person to observe it. PROP-032 says compute use can be measured. PROP-039 says measured compute use can be used as an input to methods for assigning cost. PROP-041 says that metering a resource or activity records one or more measurements of it. PROP-042 says measured activity can be told apart by quantity. PROP-043 says metering produces records of what was metered. PROP-053 says that where economic exposure exists, monitoring can be used to observe it, which adds the condition that there is exposure to observe. PROP-085 says that once usage is visible, management decisions can draw on it. Together they explain why visibility opens the door to management.

Step 5. LEM-020 establishes that visibility makes management mechanisms available. It does not claim the mechanisms work automatically, and it does not claim that visibility alone settles the right policy or price.

Step 6. The defeating case is an organization that can see a deployment’s usage, holds the authority to manage it, and still cannot apply any monitoring, limit, or attribution to it.

**P2 · Completion.** A trace with two steps left open

THM-002, “AI Adoption Cost Is Underestimated When Access Price Is Treated as Total Cost,” states a result Part II is about to teach. Its statement reads: “If buyer AI adoption cost includes cost categories beyond access price, and ROI evaluation requires a defined measurement boundary for cost and value, then treating access price as total adoption cost creates underestimation risk within the evaluation boundary.” Steps 1, 2, 3, and 6 are worked below. Complete steps 4 and 5.

Step 1. THM-002, as named above.

Step 2. When a buyer’s cost of adopting AI includes more than the access price, and judging the return requires a boundary that takes in both cost and value, treating the access price as the whole cost risks understating it.

Step 3. Four dependencies. LEM-006 and LEM-021 are required. LEM-002 and LEM-020 are contextual.

Step 4. Restate each dependency in one sentence, and note any condition it adds.

Step 5. State what THM-002 establishes and what it does not. Then explain what LEM-002 and LEM-020 contribute, given that the theorem is not conditioned on them.

Step 6. The defeating case is a buyer whose adoption cost includes categories beyond the access price, who evaluates the return inside a boundary covering cost and value, who treats the access price as the total, and whose cost is not understated.

**P3 · Independent.** A reply to the word-games objection

A senior colleague reads THM-004 and says: “This is common sense in numbered clauses. Anyone who has run a large deployment knows you need controls. Formalizing it adds nothing.” Write a one-page reply. Use the four parts of a formal claim from Section 3.3, and name at least one thing the formal statement lets the colleague do that the common-sense version does not. Do not argue that the colleague is wrong about the conclusion.

*Interleaving: question 4 requires Chapter 2’s three flows, and the cumulative case below requires both earlier chapters.*

## [PART I CUMULATIVE CASE]

**Cumulative case · Part I.** One announcement, three readings

Dated: February 2024. The company’s own announcement, using its own figures. Only that announcement is used here.

In February 2024, the payments company Klarna announced the results of the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had held 2.3 million conversations, two-thirds of its customer-service chats. By its own estimate, the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, against eleven before. The company estimated that the assistant would improve its profit by $40 million in 2024.

Work from this announcement alone.

First, apply Chapter 1’s consumption-event inventory. Identify the consumption events the announcement describes and where each is metered.

Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and cost-and-value flows, and name the evidence behind each diagnosis.

Third, pose each of the five Founding Questions against the announcement. For each, state whether the public record answers it from the organization’s own records, and what record would be needed to answer it.

Keep your answers. The case returns in Chapter 6.

<<<<< END DOCUMENT 1 >>>>>

<<<<< BEGIN DOCUMENT 2: REFERENCE EXTRACT >>>>>

# Chapter 3 review: reference extract

Everything the reviewer grades against, in one file. Extracted verbatim from the
book's own planning documents on 2026-10-01.

## 1. Part I and Chapter 3, from the structure document

### Part I: The Argument
Purpose: the reader learns why the discipline must exist. Founding Questions posed at part's end, deliberately unanswerable yet.

1. The Category Error
   - Big idea: deployed AI use is resource consumption, not software access.
   - Competency: C1. Anchor theorem: THM-009.
   - Craft section: the consumption-event inventory (reading a deployment as events).
2. The Flow
   - Big idea: AI runs as three flows (usage, records, cost-and-value); unmanaged flows degrade; cost accrues by default, value only by design.
   - Competencies: C2, C3. Anchor theorem: THM-004.
   - Craft section: the three-flow mapping (recurring diagnostic used across the book).
3. A Science and Its Discipline
   - Big idea: AI Business Economics is the science; AI Operations Management is the practice that acts on it.
   - Competency: C4. No single anchor; contains the trace set piece (walk one theorem down through lemmas to propositions).
   - Also: five functions previewed; Founding Questions posed; borders drawn (not AIOps, not FinOps, not MLOps, not regulatory governance).
   - Craft section: the trace procedure (how to read a formal claim).


## 2. Competency C4 and assessment 4, from the exit competencies

Competency C4: Read a formal claim: parse conditions, trace dependencies, state what it does and does not establish.

Assessment 4: Registry literacy on THM-008: restate conditions; state non-claims; trace one lemma to propositions; answer the "word games" objection. Requires the trace set piece earlier in the book.

## 3. The Chapter 3 outline, from the specification

### CHAPTER 3: A Science and Its Discipline

**Big idea:** AI Business Economics is the science; AI Operations Management is the discipline that acts on it.
**Competency:** C4. No single anchor theorem; contains the trace set piece.
**Prepares assessment:** 4 (registry literacy, tested later on THM-008 unseen). Poses the Founding Questions; draws the borders; closes Part I with the cumulative case.

#### Slot 1: Opening case
Case 14.1 excerpted for this chapter's purpose: in February 2026 the FinOps Foundation, a discipline built for cloud cost, formally rewrote its mission from managing the value of cloud to managing the value of technology, with 98% of its practitioners now managing AI spend (up from 31% two years earlier) and its practitioners telling the survey that no one can yet answer whether the AI is providing value. The case dramatizes the vacancy: adjacent disciplines are being pulled toward territory none was built for, and the pull is measurable. The territory needs its own science and its own discipline, named. (The full FinOps treatment, including the boundary treaty, remains Ch14's; this opener uses only the mission rewrite and the arc.)

#### Slot 2: Teaching body
3.1 Why name a science. What "science" claims here: an ordered body of conditional, testable propositions about the business economics of AI consumption, not a metaphor. The registry introduced: 200 propositions, 20 lemmas, 8 theorems, arranged as a dependency graph in which every higher claim rests on stated lower ones. The governing relationship stated plainly: the registry justifies this book; it does not organize it. Pedagogy ordered the chapters; the registry proves the claims.

3.2 The trace set piece. Subject: THM-004, the theorem the reader accepted one chapter ago. Walk it down: theorem to its supporting lemmas to representative propositions [REGISTRY PULL for the exact chain; the maturity model's grounding section indicates THM-004 rests on territory including LEM-020]. The reasoning for this choice: the trace is performed on a claim the reader already believes, so the only new cognitive load is the machinery itself; assessment 4 then tests the machinery cold on THM-008, which the reader will not have seen traced. FIGURE 3.1: the dependency trace as a tree, theorem at top, propositions at the leaves.

3.3 How to read a formal claim. Conditions (when the claim applies); scope (what it quantifies over); non-claims (what it deliberately does not establish); falsification (what evidence would defeat it). The "word games" objection answered: formalization is not decoration; it is the commitment that fixes what would count as being wrong, which is precisely what executive discourse about AI currently lacks.

3.4 The discipline. AI Operations Management defined: the practice that acts on the science. The five functions previewed, each in one paragraph, as what an organization must be able to DO: source the capacity, plan and budget its consumption, meter and attribute the usage, allocate under constraint, and hold value accountable at a boundary. (Function ordering pedagogy is deliberately absent here; the Part III introduction owns that one-paragraph teaching point.) FIGURE 3.2: the two-layer architecture, science below, discipline above, five functions as the load-bearing columns.

3.5 The borders. Four neighbors, each treated with the same two sentences: what it is for, and what it lacks for this territory. AIOps (IT operations telemetry: watches systems, not economics). MLOps (model lifecycle engineering: ships models, does not govern their consumption). FinOps (cloud cost management: the nearest neighbor, mid-expansion per the opener; owns spend plumbing, lacks the value side; the full treaty is Chapter 14's). Regulatory AI governance (one fence sentence, per the standing one-sentence policy). Presented as a table rather than a figure, per Mayer coherence: the content is categorical, not spatial.

3.6 The Founding Questions posed. The five questions stated verbatim [REGISTRY PULL / manifesto pull], each paired with the function that will earn its answer and the chapter where that happens. Then the part's closing move, stated without drama: the reader cannot currently answer any of them with records, and neither can most organizations on earth; Parts II through IV exist to change that. Part I ends.

#### Slot 3: Craft section
The trace procedure. Numbered steps: (1) locate the claim in the registry; (2) restate its conditions in one sentence; (3) list its stated dependencies; (4) walk one level down and restate each dependency; (5) state what the claim establishes and, separately, what it does not; (6) state what evidence would falsify it. Fully worked on the THM-004 chain from 3.2.

#### Slot 4: Chapter summary
The two-layer architecture; the registry and its role; the trace machinery; the five functions previewed; the borders drawn; the Founding Questions on the table, unanswered.

#### Slot 5: Key terms
AI Business Economics; AI Operations Management; registry; theorem, lemma, proposition; dependency; condition; non-claim; falsification; the Founding Questions; the five functions (each named).

#### Slot 6: Discussion questions and problems, plus the Part I cumulative case
Discussion: why does the book insist the registry justifies but does not organize it, and what would go wrong under the reverse; which border is hardest to defend and why; restate one Founding Question in your CFO's language without losing its content.
Problems: (P1, worked) full trace on THM-004 per the craft section; (P2, completion) trace on a second theorem with steps 4 and 5 blank [theorem choice at drafting; candidate THM-002, which Part II is about to teach, making the completion problem double as a preview]; (P3) the "word games" objection assigned as a one-page reply.

**PART I CUMULATIVE CASE.** Subject: Klarna, February 2024 public record only (the announcement, before the correction). The reader performs, in sequence, the consumption-event inventory (Ch1), the three-flow mapping with per-flow diagnosis (Ch2), and then poses all five Founding Questions against the public record, documenting that not one is answerable from it (Ch3). Payoff engineered for Chapter 6: when the correction arc is revealed there, the reader has already discovered its predictability from the flows alone. The cumulative case thereby teaches Part I's whole argument on one page of evidence and sets the Klarna reprise without narrative apparatus. CONSEQUENCE FOR CH6: Chapter 6's opener presents the Klarna arc as the completion of the reader's own Part I analysis (the reveal framing), not as a fresh case.

---

## 4. Dan's rulings on the plan, 2026-10-01

1. No registry counts in body prose; dated counts in one dated box.
2. The spec's line "neither can most organizations on earth" is replaced by the opening case's sourced practitioner quotation.
3. The Part I cumulative case sits inside the chapter's last slot.
4. THM-002 is the theorem for problem P2.

## 5. The seven craft criteria, from the prose standard

## 26. The craft criteria, and how Stage 4 grades this standard

Stage 4 has two halves. The mechanical half is `voicecheck.py`. The judgment half
reads the chapter against the criteria below and records a finding per criterion.
They appear as sub-checkboxes in every generated checklist, and `status_check.py`
fails a Stage 4 marked passed with one left open and unexplained.

**There are SEVEN, and C7 is new.** C1 through C6 carry their numbers from the
retired craft file so that Chapter 1's record stays readable, with C3 and C6
restated to match this standard. C7 grades the core principle, which nothing graded
before and which is the failure the rejected draft committed most often.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to a named, specific instance. Bounded by the fifty-year rule, so it
  lives mostly in cases, worked examples and craft artifacts.
- **C2. Context and stakes.** Every mechanism states the conditions that made it
  available and what it settles, not only what it does. No mechanical proxy exists.
- **C3. Claim first.** The main point of a paragraph is visible in its first
  sentence or two. Findings lead, qualifications subordinate, no throat clearing.
  Restated from "front-loaded sentences" to match section 5.
- **C4. Deliberate rhythm.** Sentence length varies, mostly 12 to 24 words, with a
  short sentence after a long explanation. No long stretch at a uniform length.
- **C5. Paragraph close.** Paragraphs end on the load-bearing clause, not a
  trailing qualifier and not a cross-reference.
- **C6. The guard holds, in both directions.** No hero or villain framing, no
  populist register, no character-driven causation where a structural account is
  available. **And no false sophistication:** no abstraction where an ordinary word
  is available, no aphorism standing in for an explanation. Restated, because the
  old guard watched only one direction and the book failed in the other.
- **C7. Business reality first.** No paragraph opens on a framework, category or
  conceptual distinction where a business statement is available. Every coined term
  arrives after the mechanism it names.

**Read adversarially and by section.** For each criterion, quote the WEAKEST passage
in the chapter and rule it, rather than asking whether the criterion is met. Read
the per-section table, never the chapter average alone.

---

<<<<< END DOCUMENT 2 >>>>>

<<<<< BEGIN DOCUMENT 3: CHAPTER 1, THE EXEMPLAR >>>>>

Part I · The Argument

# The Category Error

## [OPENING CASE]

## Two subscriptions, one correction

*Dated: June 2025 to June 2026. Vendor actions, dates, and figures are sourced. The buying organization is a composite.*

Twenty dollars per developer, per month. In the spring of 2025, that was the price of Cursor, an AI coding assistant. A software team bought one Cursor license for each developer who would use it, just as it did with every other software tool. The expense went into the budget beside the company’s ticketing system, design software, and password manager.

Cursor was useful, and it was cheap. Once the agreement was signed, nobody in finance had a reason to examine the line item again. Nothing about a twenty-dollar software seat demanded attention. But beneath every seat, a meter was running.

On June 16, 2025, the twenty dollars stopped being a price and became a balance. Cursor replaced the Pro plan’s monthly allowance of five hundred requests to external models with a twenty-dollar credit for frontier-model usage. Each request now drew down that credit at the model provider’s API rate. The subscription still cost twenty dollars a month, but what that price bought had changed completely.

Light users barely noticed the change because their activity remained within the included credit. Heavy users had a different experience. A handful of prompts could exhaust the credit, after which additional usage was billed at the underlying API rates. The change therefore affected the customers who relied on the product most and often received the most value from it. Many faced charges they had not anticipated or budgeted for.

On July 4, less than three weeks after the change, Michael Truell apologized and promised refunds for charges incurred during the transition. Truell is chief executive of Anysphere, the company behind Cursor. His explanation reduced the dispute to arithmetic. The newest models consumed far more tokens on long-horizon tasks than a flat monthly price could cover.

On June 18, 2025, two days after Cursor changed its plan, GitHub began enforcing monthly premium-request allowances for Copilot and letting customers pay for usage beyond them. It then spent the next year preparing a larger change.

On June 1, 2026, GitHub stopped measuring standard usage in requests and began measuring it in credits. Those credits reflected the tokens each customer consumed and the published rate of the model that customer selected. Customers received advance notice and could preview their charges before the bill arrived. Every plan included an allowance, and annual subscribers kept premium-request pricing until their subscriptions expired. The subscription price did not change by a dollar. What changed was what that dollar bought.

Microsoft’s scale changed how the pricing correction arrived, but not whether the underlying economics required it. On January 28, 2026, four months before that change, the company told investors on its earnings call that Copilot had passed 4.7 million paid subscribers and was growing 75 percent year over year. If a provider can fund the gap between a flat price and the cost of the resource that price buys, then it controls the timing and the form of the correction. That control is what buys advance notice, a published schedule, and tooling that shows customers the effect before it lands. If a provider cannot fund the gap, the gap sets the timing instead. Scale made the correction orderly. It did not make the variable cost disappear.

From the buyer’s side, the two pricing corrections looked very different. Cursor changed its plan without warning, then apologized and issued refunds after customers objected. GitHub announced its change in advance, published a schedule, and gave customers tools to preview the effect on their bills. The execution differed. The economic correction was the same.

Both products had been sold and purchased like conventional software: one seat, one flat price, and a cost fixed when the contract was signed. Beneath that subscription, however, the provider carried a variable cost. Every request consumed computing resources, and heavier use increased that cost while the revenue from each seat remained fixed. Once the cost of serving heavy users exceeded what the subscription could support, the provider changed the terms.

The provider determined when and how that correction occurred. Customers did not have to approve the change, or even know how many tokens they were consuming, for it to affect them. In both cases, the movement was in one direction: away from unlimited use at a flat price and toward plans that tied allowances, credits, and additional charges to consumption.

The buyers had not chosen the wrong vendors, and the tools had not failed. They made an **error of category**. They bought access to a metered resource but managed it as conventional licensed software, assuming that the subscription price fixed the cost. What had looked like fixed-price software became a consumption-based resource all at once.

### 1.1 The purchase that is not one

> **DEFINITION CALLOUT · Access price**
>
> The stated amount an organization pays for the right to use an AI capability, usually per seat or subscription. It does not include additional costs based on how much AI the organization actually uses.

> **DEFINITION CALLOUT · Software access model**
>
> A purchasing model in which an organization pays a fixed price for access to software, usually per seat or subscription. Because additional use creates little or no additional cost, the organization manages who has access rather than how much of the software each user consumes.

The buyer understood the transaction through the conventional software model. Under that model, an organization buys licenses that give a defined number of employees access to a program. Once the organization pays for a seat, additional use creates almost no additional cost. An employee who opens the program a thousand times a day costs the same as one who opens it once a week.

The organization therefore fixes its cost when it signs the contract. Procurement negotiates the number of seats and the price of each seat. That per-seat amount is the **access price**. After the purchase, the organization manages access rather than consumption: who has a login, how many seats are active, and when the contract renews.

**The software access model** is not flawed. It accurately describes licensed software, and organizations have refined it through decades of enterprise purchasing. The problem begins when buyers apply that model to AI.

An AI assistant may be sold as a program licensed by the seat, but each task calls a model and consumes computing resources. The amount consumed depends on factors such as the model selected and the size of the request and response. Each additional use therefore creates an additional underlying cost, whether the provider charges the buyer immediately or absorbs that cost for a time. AI access may be packaged like licensed software, but AI use behaves like a metered resource.

The result is a mismatch between what the organization manages and what its AI systems consume. Access management asks who can use the tool and how many seats are active. Resource management asks how much AI the work consumes, what that consumption costs, and what value the work returns.

An organization that manages only access to a metered resource is measuring the wrong quantity. It counts seats even though usage and cost are determined by tokens, requests, and credits. The organization is managing the right tool through the wrong economic model.

### 1.2 The consumption event

> **DEFINITION CALLOUT · Consumption event**
>
> A single use of an AI system that consumes metered computing resources and creates an underlying cost greater than zero, whether or not the buyer is charged for it separately. A consumption event may be measured in tokens, requests, credits, compute time, or another equivalent unit. It is the basic unit of consumption tracked in AI Operations Management.

The discipline developed in this book begins with a single unit of measurement: **the consumption event**. Each time an employee, workflow, or product calls an AI model, the system consumes computing resources and creates one of these events. The meter records them, and the invoice sums their cost.

The anatomy of a consumption event is simple, and Figure 1.1 shows its parts. Something enters the model: a prompt, a document, or a conversation history. The model performs a computation. Something returns: a completion, a suggestion, an answer, or a tool call.

As this work occurs, a meter records the resources consumed. Providers typically measure this consumption in input and output tokens, the units into which the model divides the material it reads and generates. The provider records those units in a usage ledger, even when the buyer never sees the individual event.

This creates an important difference in visibility. The provider sees a stream of metered consumption. The buyer may see only a flat subscription charge at the end of the month. Token counts can rise into the millions while remaining hidden behind that fixed price. The buyer often has no reason to examine the underlying consumption until usage exceeds an allowance or additional charges begin to appear.

[FIGURE 1.1. Drawn figure, not reproduced here.]

**Figure 1.1.** Anatomy of a consumption event. The system assembles an input, the model performs the computation, and the system returns an output. A meter records the resources consumed by the event. In most cases, the provider retains this event-level record, while the buyer receives only an aggregate usage total or charge.

AI Operations Management must measure cost in the same unit used to record consumption. Three units appear possible: the seat, the task, and the consumption event.

A seat measures access, not use. Two employees with identical seats can consume vastly different amounts of AI. A task is the right unit for measuring business value, because it connects AI use to completed work. It cannot, however, measure cost reliably, because one task may require a single model call while another requires hundreds.

The consumption event provides the necessary unit for cost. It is the smallest recorded use of AI that consumes computing resources and creates an underlying cost. It is also the unit captured by the provider’s usage meter. The organization can attribute costs to users, tasks, workloads, and workflows only by connecting those categories to the events that produced the costs. Later chapters group individual events into these larger operating units. Because each total begins with recorded events, the organization can trace it back to actual consumption and reconcile it with the provider’s invoice.

A seat measures access. A task measures value. A consumption event measures use and cost.

[FIGURE 1.2. Drawn figure, not reproduced here.]

**Figure 1.2.** Two purchase models. Under the seat model, the buyer pays a fixed price for access, so cost remains flat as usage rises. Under the event model, each consumption event adds to the total, so cost rises with usage.

The seat model and the event model do not describe the same cost in different ways. They describe two different cost structures. The seat model is the software access model defined in 1.1. The event model is the **resource consumption model**, in which each use is a metered consumption event. Figure 1.2 makes visible the difference that a flat subscription price can hide. Under the software access model, the buyer pays a fixed price for access, regardless of how much the software is used. Under the resource consumption model, every use adds to the total cost.

A contract may package AI as fixed-price software, but that packaging does not make the underlying cost fixed. If the buyer manages seats while consumption governs the economics, the mismatch remains invisible until the provider changes the terms or additional charges appear. The correction then arrives on the provider’s schedule, not the buyer’s.

### 1.3 The flat-rate objection, answered

One objection stands against everything said so far: “We pay twenty dollars per seat each month. Our price is fixed, and the provider never bills us by the token. From our perspective, this is simply software.”

The objection is valid. A buyer who pays a flat monthly price is not secretly being billed by the token. But this does not mean that the underlying resource is unmetered. Flat pricing relocates the meter from the buyer to the provider. It does not abolish it. This is **meter relocation**.

The provider continues to measure what each customer consumes. It sets the flat price based on an estimate of how much the average customer will use and what that usage will cost. The price is therefore built on an assumption. It remains viable while subscription revenue covers the total cost of serving the customer base.

The arrangement becomes unstable when actual usage departs from that assumption. If a small group of heavy users consumes a disproportionate share of the resource, the flat price collected across all customers may no longer cover the provider’s cost. The provider must then bring the price or the product limits back into line with consumption.

It can raise the subscription price, charge for usage above an allowance, redefine the allowance in tokens or credits, or cap consumption outright. Chapter 4 examines these instruments in detail. The method may vary, but the direction does not: what the customer receives becomes more closely tied to what the customer consumes.

The buyer does not choose when this correction occurs. The provider holds the meter, bears the variable cost, and decides when the existing terms have become unsustainable. A flat price can hide the meter from the buyer. It cannot prevent the provider from acting when the numbers no longer work.

This result does not depend on a vendor being careless or badly managed. It follows from the economics of deployed AI, and the AI Business Economics registry states it as a theorem.

> **THEOREM PANEL · Theorem 1 · THM-009**
>
> *AI Use Is Resource Consumption, Not Merely Software Access*
>
> Within a defined deployment and cost boundary, if:
>
>   (i) an AI activity requires compute, and executing it consumes resources;
>
>   (ii) production scaling expands the surface over which that activity is used;
>
>   (iii) the buyer’s total cost extends beyond the access price; and
>
>   (iv) measurement makes resource use, or the cost-bearing activity, visible;
>
> then that AI use is a resource-consuming operating activity, not merely software access.

A theorem in this book is a statement established within a defined system from earlier propositions and lemmas. It is not a generalization drawn from the Cursor and Copilot episodes. Those cases illustrate the result; they do not prove it. Like every theorem in this book, Theorem 1 applies only when its stated conditions hold.

Its claim is deliberately narrow. The theorem does not say that flat-rate AI subscriptions are impossible, nor does it predict that every provider will reprice them. It says that when an AI activity requires computation, each execution consumes resources. As employees, workflows, and products use that activity at greater scale, its resource consumption grows. When the stated cost boundary includes the cost of those resources, the economics of the activity cannot be described by the access price alone.

The fourth condition asks only that the resource use be measured somewhere, not that the buyer can see it. A provider’s meter satisfies that condition even when the invoice shows a single flat charge. The business is operating a resource-consuming activity, not merely accessing software.

> **DEFINITION CALLOUT · Meter relocation**
>
> The placement of consumption metering on the provider’s side of a flat-rate subscription. The buyer pays a fixed price for access, while the provider continues to measure actual use. The provider sets the flat rate based on expected consumption and may change the price, allowance, or usage limits when actual consumption exceeds that expectation.

A flat monthly subscription to ChatGPT does not contradict this conclusion. The subscription price states what the buyer pays for access under a particular plan. It does not show how much computing capacity the buyer consumes, what that consumption costs, or whether the provider absorbs the cost within the subscription. Buyers may classify the charge as another SaaS expense because that is how it appears on the invoice. But the invoice describes the commercial arrangement, not the operating economics beneath it. The subscription buys access. Each use still consumes a resource.

The public record already shows this pattern running its course in several forms. Some providers have moved directly to usage-based pricing. Others have retained a flat subscription while adding allowances, credits, or hard limits on consumption. The commercial instrument differs, but the correction is the same: what the buyer receives is brought back into line with what the buyer consumes.

> **DATED EVIDENCE BOX · Dated: January 2025**
>
> OpenAI provided an early example. Chief executive Sam Altman said publicly that the company was losing money on its two-hundred-dollar Pro subscriptions because subscribers used them more than the price had assumed. He also acknowledged that he had personally set the price. The problem was not the price of access. Actual consumption had exceeded the assumption built into it.

> **DATED EVIDENCE BOX · Dated: July 2025**
>
> Claude Code customers encountered the same economic correction through tighter limits rather than a higher subscription price. Subscribers reported that they were reaching their plans’ usage limits sooner, although Anthropic had given no notice of a change. Many had not realized that their subscriptions were subject to such limits at all. Anthropic acknowledged the reports but did not confirm that it had altered the plans. Those reports were published on July 17, 2025.
>
> Eleven days later, the company announced two new weekly usage caps in addition to its existing five-hour limits. The caps would take effect the following month for all Pro and Max subscribers. Max subscribers could continue using Claude Code beyond those limits by purchasing additional usage at standard API rates. The subscription price remained intact, but the amount of consumption included within it now had a clearer boundary.

The Cursor and GitHub Copilot episodes that opened this chapter show the same pattern. Within twelve months, two widely used AI coding products revised their subscriptions so that what customers received more closely reflected what they consumed. Cursor made the correction abruptly and responded to complaints with an apology and refunds. GitHub announced its change in advance and introduced it with billing tools and a transition period. The method differed. The economic correction did not.

In both cases, the provider continued to measure usage beneath the flat subscription price. The provider determined when the existing terms no longer worked and changed the arrangement on its own schedule. The flat rate had not removed the meter. It had placed the meter, and control over the correction, on the provider’s side of the transaction.

### 1.4 What follows if this is true

Once an organization recognizes deployed AI as a resource it consumes, the management requirements become familiar. Businesses already know how to manage resources used in daily operations. Consider a manufacturer that relies on steel. Counting how many employees are authorized to order steel would measure access to the resource, but it would not manage the resource itself. The company must determine how much steel its operations require, what specifications it must meet, what it costs, where it is used, and what value it helps create. The same management logic applies to AI.

Before purchasing steel, the company forecasts demand, sets a budget, and evaluates suppliers against its requirements. During production, it compares actual consumption with the plan and tracks how much steel each product line uses. If supply becomes limited, it allocates the available steel according to business priorities. It then includes the cost of that steel when calculating the profitability of each finished product. If a product consumes more steel than its margins can support, management can see the problem and respond.

These practices are not unique to manufacturing. They apply to any resource that costs money as it moves through an organization. To manage such a resource, leaders must be able to answer five questions:

What is the organization buying, and what requirement must it meet?

How much does it expect to consume, and how will it know when actual use departs from the plan?

Where is the resource being used?

Who decides how it is allocated when there is not enough?

What value does the organization receive in return?

If an organization cannot answer these questions, it is not managing the resource, regardless of what its organizational chart or policies suggest. It is simply receiving invoices and paying them.

Deployed AI is one of these resources. Every time an employee, workflow, or product uses AI, the organization consumes computing resources and incurs a cost. Total consumption rises with the volume of work, and as a deployment succeeds, that volume usually grows.

Most organizations, however, do not manage AI usage through a single, coordinated discipline. Responsibility is divided across several existing functions. Procurement negotiates the contract. Cloud cost management monitors infrastructure spending. Engineering tracks the systems it operates. Finance allocates the costs it can trace. Each function manages one part of the resource, but none manages it from purchase through consumption to business return.

These functions were designed before deployed AI created a resource that crossed all of their boundaries. As a result, AI usage touches several owners but belongs fully to none. Chapter 14 distinguishes the subject of this book from these neighboring disciplines. What is missing is not attention. It is a management system that brings the separate responsibilities together.

Organizations that would never allow material to move through a plant without a record often allow AI consumption to pass through daily work unrecorded. The five questions therefore go unanswered, and the reason is visible in three places.

First, the organization tracks the wrong quantities. A company accustomed to seat-based software tracks headcount, license utilization, and renewal dates. None of these measures shows how much AI the organization consumes or what produces the bill.

Second, the organization lacks a record of use. Under a seat-based contract, each additional use costs nothing at the margin, so the buyer has little reason to record it. Under an event-based model, every use consumes resources and can add to the bill. Yet a company that has not built a meter cannot show which work produced that consumption. The invoice does not provide this record. It reports the total cost, not the uses that created it.

Third, the organization has no basis for accountability. Finance cannot assign a cost to the team, workflow, or product that incurred it unless the company can trace the cost back to the work. A cost assigned to no one is defended by no one.

It would be a mistake to treat these gaps as negligence. The organization inherited them from the seat-based software model, just as it inherited the absence of a clear owner. It did not decide to stop metering software use. It never began, because the software it had purchased for three decades did not require it. Enterprise software procurement built a management system around the economics of the license: count the seats, track utilization, and manage renewals. That system worked.

AI often entered the organization in familiar packaging. It came through the same vendors and procurement channels, initially at a price low enough to approve without much debate. The organization therefore managed it as another software license. The existing system did not fail. It did exactly what it was built to do, continuing to report seats, utilization, and renewal dates even after those measures had stopped explaining consumption and cost.

Scale makes this inherited arrangement untenable. While AI remains a pilot, the organization can afford to manage it as a software license. One team uses a few seats, and the bill is too small to matter against the larger software budget.

This all changes when the pilot enters production. AI usage then grows with the volume of work the system performs. A contact center does not merely add licensed users. It applies AI across the conversations and workflows those users handle, generating a new consumption event each time the system performs work.

The contact-center deployment examined later in this chapter illustrates the difference. It operates with roughly five thousand seats but generates tens of millions of consumption events each month. The craft section calculates this ratio in full. At pilot scale, seat count is a harmless simplification. At production scale, it is a blindfold.

The problem established in this chapter defines the work of the rest of the book. Once AI consumption moves through daily operations and produces variable cost, the organization needs a system for measuring, assigning, and governing it. No existing management practice provides that system in assembled form. The remaining chapters build it.

### 1.5 What this book is not

This book addresses what happens after an organization decides to deploy AI. It does not explain how models work internally, so it carries no account of architectures, training, or weights. It does not teach prompt engineering or offer techniques for improving a model’s output. It also does not help leaders identify problems that AI might solve. Each of these subjects has its own purpose and literature, and Chapter 3 explains where each ends and AI Operations Management begins.

The subject of this book is the deployed resource itself. It examines what AI consumes as employees, workflows, and products use it; what that consumption costs; and how the organization measures, assigns, and governs both. The decision to deploy establishes the need. This book explains how to manage what follows.

## [CRAFT SECTION]

## The consumption-event inventory

*The contact-center setting and approximate agent population are drawn from the cited study. The event architecture and all volume assumptions are stipulated for this exercise.*

A seat count shows how many people can use an AI system. It does not show how much AI activity their work generates. **The consumption-event inventory** replaces that administrative count with an operating view of the deployment. It identifies each kind of consumption event, what resources the event consumes, where that consumption is measured, and what the seat count leaves hidden.

This is the first artifact the reader produces in this book. Later artifacts use it to trace consumption, assign costs, and compare those costs with the value created. The inventory therefore needs to be specific enough to run against an actual deployment.

The procedure has four steps.

**Step 1: Enumerate the event types.** List every distinct kind of consumption event generated by the deployment. Begin with the work the system performs, not with the number of employees who have access. A single deployment may classify a request, retrieve information, generate several responses, call a tool, and summarize the completed interaction. Each is a separate event type when it triggers its own measurable use of resources.

**Step 2: Identify the resource drivers.** For each event type, state what causes its resource consumption to rise. Common drivers include input tokens, output tokens, model calls, retrieval operations, tool invocations, and the amount of context processed. Do not assume that two events consume the same resources merely because they occur inside the same workflow.

**Step 3: Locate the meter.** State which system records the consumption and which party controls that record. The meter may sit with the model provider, the application vendor, the organization’s cloud environment, or an internal platform. A flat-rate contract does not remove this step. It means only that the provider may hold the operational meter while the customer sees a fixed price.

**Step 4: State what the seat count conceals.** Estimate the volume of each event type over a defined period. Show the operating assumptions used in the calculation, then compare the resulting activity with the number of seats. The purpose is not merely to produce a larger number. It is to reveal the work, consumption, and cost drivers that cannot be seen from the seat count alone.

Consider a customer-support organization that has deployed a generative AI assistant across its contact center. For each incoming customer message, the assistant drafts a suggested reply that the agent may edit and send; the assistant draws on a knowledge base and on the conversation so far. The deployment covers a large agent population, on the order of five thousand agents, and the organization currently accounts for it as a per-seat tool.

Model inventory

**Step 1. Event types.** The deployment generates at least three: (a) a suggested-reply generation, triggered each time an agent asks the assistant to draft a response to a customer message; (b) a knowledge retrieval, triggered when the assistant pulls reference material to ground a suggestion; and (c) a conversation-close operation, in which the deployment summarizes or tags the resolved conversation.

**Step 2. Resource drivers.** For suggested-reply generation, the drivers are input tokens (the system instructions, the retrieved knowledge, and the conversation history assembled into the prompt) and output tokens (the drafted reply). The volume driver is the number of customer messages that receive a drafted reply, which scales with contacts multiplied by the number of turns per contact. For knowledge retrieval, the drivers are the number of retrieval calls and the tokens those calls embed and return. For the conversation-close operation, the drivers are input tokens (the full conversation) and output tokens (the summary or tags); their volume scales with the number of resolved conversations.

**Step 3. The meter.** The generation and close operations are metered on the provider’s side, by token. Retrieval is metered wherever the retrieval service runs. In the architecture stipulated here, the retrieval service is the provider’s managed index, metered by call and by token; an organization that operates its own vector store meters that step itself. Meter location is a property of the architecture rather than of the event type, which is why Step 3 directs the reader to locate the meter instead of assuming it. Under its per-seat plan, the organization receives a monthly invoice that shows only a seat count.

**Step 4. What the seat count conceals.** The seat count treats the agent population as a set of equal units: five thousand seats at one price. Put the volume drivers from Step 2 against it and the two quantities separate immediately. Stipulate, for this exercise, five thousand agents, each handling forty contacts on a working day, with six drafted replies per contact, one retrieval per drafted reply, and twenty-one working days in the month. Suggested-reply generations then run at 5,000 × 40 × 6 × 21, or 25.2 million events a month. Retrievals match them one for one at 25.2 million. Conversation-close operations run once per contact, at 4.2 million. The deployment generates roughly 54.6 million consumption events a month, which is about 10,900 events behind every seat.

Change any stipulated figure and the total moves; change none of them and the seat count still does not move, because the seat count is not a function of any of these quantities. Two agents on identical seats can consume amounts of the resource that differ by an order of magnitude: a high-volume agent handling long, reference-heavy conversations generates many times the consumption of a low-volume agent, at the same seat cost. The quantity that drives the bill is tokens per resolved contact. It does not appear on the seat line, and until the inventory names it, the organization is managing a number that does not govern its cost.

The inventory has done its work when the organization can see, for the first time, the shape of what it is buying. Not five thousand seats. A flow of tens of millions of consumption events whose volume and intensity, not headcount, determine the bill.

### Chapter summary

The category error is now clear. Under the software access model, the organization fixes its cost when it signs the contract and manages the number of seats. Under the resource consumption model, each metered event adds to total cost, and the organization must manage the resulting flow of consumption. These are different operating models, even when the provider packages both as software subscriptions.

The consumption event is the atomic unit of the second model. It is the smallest use of AI that consumes resources and creates an underlying cost. It is also the smallest unit whose consumption the provider’s meter records. Seats measure access. Consumption events measure use and cost.

A flat price does not erase this distinction. It relocates the meter to the provider, which continues to measure consumption and decides when the commercial terms must change. This conclusion does not require a prediction about any particular vendor. It follows from Theorem 1: deployed AI is a resource-consuming operating activity, not merely software access.

The reader can now apply the consumption-event inventory to a deployment description. The inventory identifies the types of events the deployment produces, the resources each event consumes, where that consumption is metered, and which cost drivers the seat count conceals. It makes the flow visible. It does not yet explain how to manage that flow. Seeing it whole comes first.

### Key terms

**Category error.** The error of managing a metered resource as if it were licensed software. It rests on a false assumption: that the access price fixes the total cost. The tool is the right one and the vendor is not at fault. The economic model applied to the tool is wrong.

**Consumption event.** A single use of an AI system that consumes metered computing resources and creates an underlying cost greater than zero, whether or not the buyer is charged for it separately. A consumption event may be measured in tokens, requests, credits, compute time, or another equivalent unit. It is the basic unit of consumption tracked in AI Operations Management.

**Resource consumption model.** The economic model in which deployed AI is consumed as a metered resource. Each use creates a consumption event, and cost accrues with each event. It contrasts with the software access model.

**Software access model.** A purchasing model in which an organization pays a fixed price for access to software, usually per seat or subscription. Because additional use creates little or no additional cost, the organization manages who has access rather than how much of the software each user consumes.

**Access price.** The stated amount an organization pays for the right to use an AI capability, usually per seat or subscription. It does not include additional costs based on how much AI the organization actually uses.

**Metered resource.** A resource whose consumption is measured per unit of use, here in tokens or their equivalents.

**Flat-rate objection.** The claim that a flat per-seat price makes AI equivalent to licensed software; answered by meter relocation.

**Meter relocation.** The placement of consumption metering on the provider’s side of a flat-rate subscription. The buyer pays a fixed price for access, while the provider continues to measure actual use. The provider sets the flat rate based on expected consumption and may change the price, allowance, or usage limits when actual consumption exceeds that expectation.

### Discussion questions and problems

## [DISCUSSION QUESTIONS]

**1.** A colleague argues that your organization pays a flat per-seat price and never receives a token bill, so AI is a seat-priced good and the consumption model does not apply. Explain why the contract does not change the underlying economic model. Your answer should not depend on predicting how any specific vendor will price its product in the future.

**2.** The Cursor and GitHub Copilot episodes can be read as two companies changing their prices. Taken together, what do they reveal about where consumption was being measured all along? Why does the evidence become stronger when the two cases are considered together?

**3.** Section 1.2 treats the consumption event, rather than the user or the task, as the discipline’s atomic unit. Make the strongest case for using the task instead. What could a task-based discipline explain or manage more effectively? What would it lose by moving away from the event?

**4.** Construct the strongest flat-rate objection a capable skeptic could make after reading this chapter. Then answer it. Your response should explain why flat-rate pricing does not eliminate the underlying consumption problem without assuming that any particular subscription will eventually be repriced.

## [PROBLEMS]

**P1 · Worked.** Five hundred seats, one meter

A company purchases an AI coding assistant for five hundred employees at a fixed annual price per seat. The contract contains no token charges, and the finance team records the entire purchase as software expense. Over the next year, some employees use the assistant occasionally while others use it throughout the workday.

Using the resource consumption model, explain why the absence of a usage-based charge on the company’s invoice does not make seat count the underlying unit of AI consumption. Identify where the meter is likely to reside, what it measures, and what the per-seat price conceals.

Model answer

The company pays for the AI coding assistant by the seat, but the seat is the commercial pricing unit, not the underlying unit of consumption. The five hundred employees do not consume the same amount of AI simply because the company purchases five hundred licenses. An employee who uses the assistant several times a month generates far less activity than one who relies on it throughout the workday.

The underlying meter therefore sits behind the seat price. Each time an employee uses the assistant, the system processes a request and consumes computing resources. The provider can measure those consumption events even when it does not expose them as separate charges on the customer’s invoice. The flat annual price is built around assumptions about how much consumption the average seat will generate.

Seat count therefore conceals the actual cost driver. Two companies may each purchase five hundred seats while generating very different levels of AI consumption. The same difference can exist inside one company: a small group of heavy users may account for a disproportionate share of total consumption even though every employee carries the same accounting cost per seat.

Under the resource consumption model, the meter has not disappeared. It has moved to the provider’s side of the transaction. The company sees a fixed software price, while the provider sees the flow of consumption events that the price must cover.

Annotated reasoning

The response begins by separating the commercial pricing unit from the underlying consumption unit. The company buys five hundred seats, but equal seat count does not imply equal AI use. It then makes the hidden mechanism visible: each request consumes computing resources, and the provider can measure those events even when the customer never sees a usage-based charge. From there, the response explains what the seat price conceals. Users, teams, and companies with the same number of seats can generate very different levels of consumption. The conclusion follows directly: flat pricing changes where the meter is visible, not whether consumption exists.

**P2 · Worked.** Inventory a coding-assistant deployment

A software company has deployed an AI coding assistant to three hundred developers. The assistant provides inline code completions, answers questions in the editor, and can perform multi-step agentic tasks. Produce the consumption-event inventory for the deployment.

Model inventory

**Event types:**

(a) Inline completion: triggered as a developer types and the assistant generates a code suggestion.

(b) Editor chat query: triggered when a developer asks the assistant a question.

(c) Agentic task run: triggered when a developer delegates a multi-step task to the assistant.

**Resource drivers:**

Inline completions consume input tokens from the surrounding code context and output tokens from the generated suggestion. Each event may be small, but the total volume can be high because completions occur repeatedly throughout the workday.

Editor chat queries consume input tokens from the developer’s question and any code or file context supplied with it. They also consume output tokens from the assistant’s response.

Agentic task runs consume resources across multiple model calls rather than a single request. They may also invoke tools, inspect files, generate code, and repeat steps before the task is complete. For that reason, one agentic run can consume substantially more resources than a single completion or chat query.

**Meter:** The meter sits primarily on the provider’s side. The provider can measure token consumption and, for agentic tasks, additional activity such as tool calls or repeated model requests. Under a seat-priced plan, the buyer may see only the number of seats and the resulting subscription charge.

**What the seat count conceals:** Seat count does not show how much AI the developers actually consume. Two developers with identical seats may generate very different levels of usage. A developer who runs long agentic tasks throughout the day may consume far more resources than several developers who use only occasional inline completions.

The important cost drivers are therefore the number, type, and intensity of consumption events. In this deployment, agentic task volume and length are likely to be especially important. The seat count reveals none of that variation.

**P3 · Completion.** Inventory a document-review deployment

A legal operations team has deployed an AI assistant that extracts key clauses from each contract submitted, compares them against a policy playbook, and drafts a redline memo. Complete the inventory below by filling the blank column.

*Interleaving: none. This is the first chapter; problem sets begin reaching back to earlier chapters in Chapter 2.*

<<<<< END DOCUMENT 3 >>>>>

---

END OF PACKAGE. Now produce your review in the format given in Part 2.
