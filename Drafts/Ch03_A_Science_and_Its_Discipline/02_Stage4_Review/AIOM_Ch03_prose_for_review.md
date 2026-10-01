Part I · The Argument

# A Science and Its Discipline

## [OPENING CASE]

## The discipline that changed its mission

*Dated: February 2026. Found by search. Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself. See the source register.*

In February 2026, the FinOps Foundation changed its mission statement. For years it had described its purpose as advancing the people who manage the value of cloud. The new statement replaced one word: the Foundation now advances the people who manage the value of technology.

The change was not a branding exercise. It followed the Foundation’s annual survey of its own practitioners, the people inside companies who manage cloud spending for a living. The 2026 survey reached 1,192 of them, responsible for more than $83 billion a year in cloud spending. Its central finding concerned work the discipline had not been founded to do. Ninety-eight percent of respondents now managed spending on AI. Two years earlier, the figure had been 31 percent.

FinOps was built for a specific problem. Cloud computing let engineers buy capacity with a few lines of code, and the bills arrived after the capacity had been used. The discipline grew up to make engineering, finance, and business teams jointly accountable for that spending. Nobody designed it to manage AI. Its practitioners took on AI spending anyway, and by 2026 nearly all of them were doing so.

The survey also recorded what that work had not yet produced. Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: “No one can answer that question yet.” The people closest to the AI bills could total what their organizations spent. They could not say what the spending returned.

That is the gap Chapters 1 and 2 described, now reported by the people asked to fill it. The organization pays for a metered resource, and the cost arrives by default. The value arrives only if someone builds the means to measure it. A cloud cost discipline is a capable neighbor, and it has moved toward this territory because the territory was empty. A territory occupied by default is not the same as a territory with its own body of knowledge and its own practice.

This chapter names both. The body of knowledge is a science, AI Business Economics, which states what is true about the economics of consuming AI. The practice is a discipline, AI Operations Management, which acts on what the science establishes. The FinOps case returns in Chapter 14, where the relationship between the two disciplines is worked out in full. Here it serves as evidence that the territory exists, that it is being claimed, and that the question at its center is still unanswered.

### 3.1 Why name a science

Managers act on claims about how their business works. A budget assumes that cost follows usage. A pricing negotiation assumes the provider has a reason to accept a lower price. A dashboard assumes that what it shows will change what someone does. When those claims are wrong, the management built on them fails, however carefully it is carried out.

Claims of this kind can live informally: in experience, in rules of thumb, and in the slides of whoever presented last. Informal knowledge is useful, and it has a cost. Two managers can hold opposite beliefs about the same deployment, and neither can show the other where the disagreement lies. The argument then turns on confidence rather than on evidence.

Chapters 1 and 2 each ended on a stated result rather than an opinion. Chapter 1 set out the conditions under which deployed AI is a resource the organization consumes. Chapter 2 set out the conditions under which a scaled deployment cannot be controlled without a governing apparatus. Each result appeared in a panel with an identifier, and each identifier points to a larger body of claims behind it.

That body is AI Business Economics. It is a science in a specific and limited sense: an ordered collection of conditional claims about the business economics of consuming AI, each stated precisely enough to be checked. The word does not mean laboratory experiments, and it does not mean certainty. It means that every claim says when it applies, what it concludes, and which other claims it rests on.

> **DEFINITION CALLOUT · AI Business Economics**
>
> The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

The claims are kept in a registry. The registry is a structured record of every definition, assumption, and result in the science, with each result linked to the claims that support it. A definition fixes what a term means. An axiom states an assumption the science accepts without proof. A proposition states a single claim, accepted because of the definitions, axioms, or earlier claims it names as its support. A lemma combines propositions, and sometimes other lemmas, into an intermediate result. A theorem combines lemmas into a result with direct consequences for management.

Those links are the registry’s most important feature. Every higher claim names the lower claims it depends on, and those claims name their own supports in turn. The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself. A reader can start at any theorem and follow its supports downward until they reach definitions and axioms.

The registry also records which claims are complete. A claim is certified when every claim it depends on is itself certified and its supporting argument has been checked. A claim with a gap below it carries a record of what is missing. This book renders and cites certified claims only. Presenting an uncertified claim as a theorem would claim more than the science claims.

> **DATED EVIDENCE BOX · Dated: August 2026**
>
> At the version this book was written against, the registry held 413 objects: 140 definitions, 35 axioms, 201 propositions, 21 lemmas, 11 theorems, and 5 records of evidence the science still needs. It recorded 1,777 dependency links among them, and 397 of the 413 objects were certified. The registry is revised as the science develops, so these figures describe one version and not the science itself.

One rule governs how this book uses the registry. The registry justifies the book. It does not organize it. The chapters follow the order in which a manager needs to learn, which is not the order in which the science derives its results. The registry’s role is to stand behind each result the book teaches, so that a reader who doubts a claim can follow it to its support. Reversing the rule would produce a book that proved everything and taught nothing.

### 3.2 Tracing a result the reader already accepts

The way to learn the registry is to follow one result down through it. The result chosen here is the one Chapter 2 ended on. A reader who accepted Chapter 2’s argument already believes it, so the only new thing to learn is how the support behind it is arranged. Once a deployment reaches scale, economic control requires a governing apparatus. Diligence from the people running the deployment is no longer enough.

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

Each condition has a plain meaning a manager can check against a deployment. The first says the deployment has grown from a pilot into daily operations, so the places where usage happens have multiplied. The second says that recording usage makes the activity that costs money visible. The third says that what is visible can be monitored, limited, and assigned. The fourth says the organization pays more in total than the price of access. When all four hold, an organization that wants control over the deployment’s economics needs cost governance.

THM-004 does not ask to be believed. It names four lemmas as its support, one for each condition, and all four are certified. LEM-016, “Production Scaling Expands Usage Surface,” supports the first. LEM-002, “Measurement Enables Visibility,” supports the second. LEM-020, “Visibility Enables Management Mechanisms,” supports the third. LEM-006, “Buyer Total Cost Extends Beyond Access Price,” supports the fourth.

The theorem’s own argument joins them in two pairs. The first and fourth lemmas give an exposure that grows with the deployment and cannot be read off the price. The second and third give the only route by which such an exposure becomes manageable: measurement makes it visible, and management mechanisms can be applied to what is visible. Control therefore requires the apparatus that does both, which the theorem calls cost governance.

One level further down, each lemma rests on propositions. LEM-020 is a useful one to follow, because it shows how the registry is built. Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.” It rests on seven propositions and on one other lemma.

The propositions are small claims, each close to obvious on its own. PROP-043 states: “If activity is metered, records describing measured activity are generated or maintained.” PROP-053 states: “If economic exposure exists, monitoring mechanisms may be used to observe the sources or magnitude of that exposure.” PROP-085 states: “If usage information becomes visible, decisions regarding management, allocation, optimization, or monitoring may reference that information.” No manager would dispute any of them. The work lies in how they combine.

The other lemma under LEM-020 is LEM-002, the same lemma that supports THM-004’s second condition directly. The registry is therefore not a tree, in which each claim has one parent. It is a graph, in which one claim can support several others. Figure 3.1 shows the branch through LEM-020, with the shared support visible.

[FIGURE 3.1. Drawn figure, not reproduced here.]

**Figure 3.1.** One branch of the trace. THM-004 rests on four lemmas, one for each condition. LEM-020 rests in turn on LEM-002, which also supports the theorem directly, and on seven propositions, three of which are shown.

The trace changes what a manager can do with the theorem. Before it, THM-004 is a conclusion to accept or reject as a whole. After it, the theorem is a set of smaller claims, each of which can be examined on its own. A manager who doubts the conclusion can now say which supporting claim they doubt. A disagreement about a whole conclusion has no obvious way to end. A disagreement about one proposition can be settled.

### 3.3 How to read a formal claim

A formal claim is read in four parts: its conditions, its scope, its non-claims, and the falsifying case that would defeat it. A manager who can state all four can use the claim without being misled by it.

The conditions say when the claim applies. In THM-004 they are the four numbered clauses. If a deployment fails any one of them, the theorem says nothing about it. A pilot used by one team for a few weeks has not been scaled into daily operations, so it fails the first condition. The theorem then neither requires governance for the pilot nor rules it out. Reading the conditions first prevents a basic misuse of a formal claim: applying it where it was never stated to hold.

The scope says what the claim covers. THM-004 opens with its scope, before the word “if”: one defined deployment and its measurement boundary. The registry adds that the theorem applies where an organization seeks economic control over the resulting cost. The claim concerns one deployment inside one boundary, not an organization’s AI activity in general. A manager who applies it across a whole company must first show that each deployment meets the conditions.

The non-claims say what the claim deliberately does not establish. The registry records them for every claim, so a reader does not have to guess. THM-004 asserts that governance is necessary for control, not that governance delivers control. It does not claim that governance is costless. It does not say at what scale the requirement begins to bind, and it asserts nothing about how large the exposure is. The theorem also does not establish the three flows. As Chapter 2 noted, the three flows are this book’s organizing framework. THM-004 formalizes the economic consequence of the third flow’s asymmetry, and it does not establish the taxonomy itself.

> **DEFINITION CALLOUT · Non-claim**
>
> A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating the non-claims prevents a claim from being cited for more than it says.

The distinction between necessary and sufficient matters most in practice. A manager who reads THM-004 as “governance produces control” will buy a dashboard and expect the costs to settle. The theorem promises nothing of the kind. It says only that without governance there is no route to control. LEM-020 makes the same limit explicit one level down: it does not claim that management mechanisms are automatically effective.

The falsifying case says what would show the claim to be wrong. For a conditional claim, the test is precise: a case that meets every condition and still lacks the conclusion. For THM-004, that would be a scaled deployment meeting all four conditions whose organization holds economic control over its cost with no measurement and management apparatus at all. A claim that names no such case cannot be wrong, and a claim that cannot be wrong tells a manager nothing.

These four parts answer an objection the formal style invites. A skeptical reader may call the registry a set of word games: obvious points dressed in numbered clauses. The objection mistakes the purpose of the form. Formal statement is not decoration. It fixes in advance what would count as the claim being wrong. A claim about AI that never says when it applies or what would defeat it cannot be wrong in that sense. A claim that states its conditions can be tested, and a claim that can be tested can be improved.

### 3.4 The discipline that acts on the science

A science says what is true. It does not, by itself, change what an organization does. Medicine needs physiology, but a patient is treated by clinicians who apply it. Engineering needs physics, but a bridge is built by engineers working to codes and procedures. In each case a practice stands between the knowledge and the result, and that practice has its own methods, roles, and standards.

AI Operations Management is that practice for AI consumption. It is the work an organization does week to week to manage what it consumes. It buys AI capacity, plans its use, and records and assigns that use. It decides what runs when capacity is short, and it holds the spending to account for what it returns. Chapter 1 described the problem as a category error. AI Operations Management is the discipline that resolves it.

> **DEFINITION CALLOUT · AI Operations Management**
>
> The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

The discipline is organized as five functions. Each is a capability an organization either has or lacks, and each is taught in its own chapter in Part III.

The first function is sourcing. The organization must be able to buy AI capacity that matches what its work requires, neither paying for capability the work does not use nor starving work that needs more. Sourcing decides which models and providers serve which work, and on what terms.

The second function is planning and budgeting. The organization must be able to state how much AI it expects to consume in the coming period and to notice when actual consumption departs from that expectation. A budget in this sense is a commitment made in advance, so that a deviation is visible when it happens rather than when the money is gone.

The third function is metering and attribution. The organization must be able to record what was consumed and to assign each unit of consumption to the team, product, or purpose it served. Chapter 2 called this the record flow. Without it, the other functions have nothing to work from.

The fourth function is allocation and routing. When capacity is limited, the organization must decide what runs first and send each piece of work to the capacity that suits it. Those decisions happen whether or not anyone makes them deliberately, so the function exists to make them by rule rather than by accident.

The fifth function holds value to account at a boundary. The organization must be able to say where a deployment pays for itself, measured over a defined scope and period, and who is responsible for knowing. This is the hardest of the five, and it is the function the FinOps practitioners in the opening case could not yet perform.

Figure 3.2 sets the two layers together. The science lies beneath. The discipline stands on it, and the five functions are what carry its weight.

[FIGURE 3.2. Drawn figure, not reproduced here.]

**Figure 3.2.** The two layers. AI Business Economics states what is true about consuming AI. AI Operations Management acts on it through five functions, each taught in its own chapter of Part III.

The two layers depend on each other in different ways. The discipline needs the science, because a practice built on wrong claims fails however well it is run. The science does not need the discipline in order to be true. It needs the discipline in order to matter. A result about governance changes nothing until an organization builds the apparatus the result describes.

### 3.5 Where the discipline ends

A new discipline is defined as much by what it leaves alone as by what it claims. Chapter 1 set aside three subjects that sit close to AI but outside this book. Each has its own purpose and literature, and each ends before AI Operations Management begins.

The first is how models work: their architectures, training, and internal behavior. That subject belongs to computer science and machine learning engineering. It ends where a model becomes a service an organization can call. AI Operations Management begins at that call, where each use consumes resources and costs money.

The second is prompt engineering, the craft of writing inputs that produce better outputs. It improves individual uses of AI. AI Operations Management governs the total of those uses: how many there are, what they cost, and what they return. A better prompt can lower the cost of one request. Only the discipline can say whether the organization’s requests, taken together, are worth what they cost.

The third is finding uses for AI: deciding which business problems AI might solve. That work belongs to strategy and innovation, and it ends when a use is chosen and deployed. AI Operations Management begins with the deployment and manages it from then on.

Four established disciplines sit closer still. Each manages something adjacent to AI consumption, and each lacks something this territory needs. Table 3.1 sets them side by side.

Table 3.1. The four neighboring disciplines. Each manages something adjacent to AI consumption, and none was built to govern its economics.

FinOps is the nearest neighbor and the hardest border to draw. It already manages spending, it has moved toward AI, and its own definition speaks of maximizing the business value of technology. The border does not lie in intent. It lies in the evidence of the opening case: the practice that reads the AI bills reports that it cannot yet say what the spending returns. The two disciplines share the cost side and part of the record. How they divide the rest is a question for Chapter 14.

Regulatory governance needs only one sentence. It decides whether an organization may use AI in a given way, and this book takes that answer as given and asks how the permitted use is managed.

### 3.6 Five questions the discipline exists to answer

A discipline proves itself by answering questions its organization could not answer before. AI Operations Management exists to answer five. Each belongs to one of the five functions, and each is answered in the chapter that teaches that function.

An organization that manages its AI consumption can answer these five questions from its own records:

Question 1. “Are you paying for capability you do not need, or starving work that needs more?” This is the sourcing question, answered in Chapter 7.

Question 2. “What do you expect the AI flow to consume next period, and how will you know when it deviates?” This is the planning and budgeting question, answered in Chapter 10.

Question 3. “Who consumed what last month, in service of which work?” This is the metering and attribution question, answered across Chapters 8 and 9.

Question 4. “When capacity is constrained, who decides what runs first, and by what rule?” This is the allocation question, answered in Chapter 11.

Question 5. “Where, exactly, does this AI flow pay for itself, and who is on the hook for knowing?” This is the value boundary question, answered in Chapter 12.

These are the Founding Questions. The phrase that matters in each is “from its own records.” An organization can always produce an answer by asking the provider, estimating, or repeating the business case. Each of those produces a number, and none produces knowledge the organization holds and can check.

After Part I, none of the five can yet be answered for a real deployment, and the opening case suggests this is not a gap peculiar to newcomers. The practitioners closest to AI spending reported that no one could yet say whether the AI was providing value. That is the fifth question, unanswered by the people best placed to answer it. Parts II through IV exist to change that. Part II establishes what is true. Part III builds the five functions. Part IV turns them into an institution.

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

Step 2 restates its conditions. Within one deployment and its measurement boundary, the theorem applies when four things hold. Scaling has multiplied where usage happens. Recording makes the costly activity visible. What is visible can be managed. Total cost runs beyond the price of access.

Step 3 lists its four dependencies: LEM-016, LEM-002, LEM-020, and LEM-006, one for each condition.

Step 4 restates each one. LEM-016 says that moving from isolated use into repeated operations can increase the number of usage events and demand points. LEM-002 says that measured and recorded activity becomes observable enough to analyze, assign, and manage. LEM-020 says that visible usage or exposure can have monitoring, limits, and attribution applied to it. LEM-006 says that a buyer who incurs several kinds of cost pays more in total than the access price.

Step 4 also asks what each dependency adds, and LEM-020 adds something. Its scope requires that the organization have reliable visibility and the authority to apply management mechanisms. The third condition of THM-004, that visibility enables management mechanisms, therefore carries more than its words show. It holds only for someone with the authority to act. A team that can see its costs but cannot cap them does not meet it. The trace found what the condition requires in practice.

Step 5 separates the claim from its readings. THM-004 establishes that cost governance is necessary for economic control of a scaled deployment. It does not establish that governance is sufficient or costless, at what scale the requirement binds, how large the exposure is, or that a deployment has three flows.

Step 6 names the falsifying case: a scaled deployment meeting all four conditions whose organization controls its cost with no measurement and management apparatus. Finding one would show the theorem false.

The procedure is deliberately slow. A trace of one theorem takes longer than reading the theorem and agreeing with it. The time is worth spending once for each claim a decision rests on, because it is the only way to know what the decision is resting on.

### Chapter summary

AI Business Economics is the science of consuming AI. It is an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on. The claims are kept in a registry, linked by dependency, and this book renders and cites certified claims only.

The registry justifies this book. It does not organize it. The chapters follow the order in which a manager needs to learn, and the registry stands behind each result so that a reader who doubts a claim can follow it to its support.

A trace follows a claim down through the registry, from a theorem to the lemmas and propositions it rests on. It turns a conclusion into a set of smaller claims that can each be examined.

A formal claim is read in four parts: its conditions, its scope, its non-claims, and the evidence that would defeat it. Formal statement is not decoration. It fixes in advance what would count as being wrong.

AI Operations Management is the discipline that acts on the science, through five functions: sourcing, planning and budgeting, metering and attribution, allocation and routing, and holding value to account at a boundary. It begins where a model becomes a service an organization consumes, and it borders AIOps, MLOps, FinOps, and regulatory governance without being any of them.

The Founding Questions are the five questions the discipline exists to answer from an organization’s own records. At the end of Part I, none of them can yet be answered for a real deployment.

### Key terms

**AI Business Economics.** The science of the business economics of consuming AI: an ordered body of conditional claims, each stating when it applies, what it concludes, and which other claims it depends on.

**AI Operations Management.** The management discipline that acts on AI Business Economics: the practice by which an organization buys, plans, records, assigns, allocates, and holds accountable its consumption of AI.

**Registry.** The structured record of every definition, assumption, and result in AI Business Economics, with each result linked to the claims that support it.

**Theorem.** A registry result built from lemmas and propositions, with direct consequences for management. The book sets each theorem it relies on in a numbered panel.

**Lemma.** An intermediate registry result that combines propositions and supports one or more theorems.

**Certified claim.** A registry claim whose supporting argument has been checked and whose every dependency is itself certified. The book renders and cites certified claims only.

**Trace.** Following a registry claim down through the claims it depends on, from a theorem to its lemmas and from a lemma to its propositions.

**Condition.** A requirement a deployment must meet for a formal claim to apply to it. A claim says nothing about a case that fails any of its conditions.

**Non-claim.** A conclusion a formal claim deliberately does not establish, though a reader might be tempted to draw it. Stating the non-claims prevents a claim from being cited for more than it says.

**Falsifying case.** A case that meets every condition of a formal claim and still lacks its conclusion. Finding one would show the claim to be wrong.

**Founding Questions.** The five questions AI Operations Management exists to answer from an organization’s own records, one for each of its five functions.

**Trace procedure.** The six-step method for reading a formal claim before relying on it: locate it, restate its conditions, list its dependencies, walk one level down, separate what it establishes from what it does not, and name the case that would defeat it.

### Discussion questions and problems

## [DISCUSSION QUESTIONS]

**1.** The book insists that the registry justifies it but does not organize it. Describe what a reader would lose if the chapters followed the registry’s order of derivation instead.

**2.** Of the four borders in Table 3.1, which is hardest to defend, and why? State what evidence would move that border.

**3.** Restate one Founding Question in the language your chief financial officer would use, without losing any of its content. Then say which part of the question the restatement was most tempted to drop.

**4.** Chapter 2 diagnosed a deployment through its three flows. Match each flow to the function in Section 3.4 that manages it, and name the function that has no flow of its own.

## [PROBLEMS]

**P1 · Worked.** A trace of LEM-020

The craft section traced a theorem. Trace one of its lemmas, LEM-020, with the same six steps, as a model for problem P2.

Step 1. LEM-020, “Visibility Enables Management Mechanisms.” Its statement reads: “If economic exposure or usage activity is visible to the relevant actor, then monitoring, limits, attribution, or management mechanisms can be applied within the relevant scope.”

Step 2. When the people responsible for a deployment can see its usage or its cost, they can apply monitoring, limits, and attribution to it.

Step 3. Eight dependencies: the lemma LEM-002 and seven propositions, among them PROP-043, PROP-053, and PROP-085.

Step 4. LEM-002 says recorded activity becomes observable enough to manage. PROP-043 says metering produces records of what was metered. PROP-053 says that where exposure exists, monitoring can be used to observe it. PROP-085 says that once usage is visible, management decisions can draw on it. Each restates a small part of the lemma. Together they explain why visibility opens the door to management.

Step 5. LEM-020 establishes that visibility makes management mechanisms available. It does not claim the mechanisms work automatically, and it does not claim that visibility alone settles the right policy or price.

Step 6. The defeating case is an organization that can see a deployment’s usage, holds the authority to manage it, and still cannot apply any monitoring, limit, or attribution to it.

**P2 · Completion.** A trace with two steps left open

THM-002, “AI Adoption Cost Is Underestimated When Access Price Is Treated as Total Cost,” states a result Part II is about to teach. Its statement reads: “If buyer AI adoption cost includes cost categories beyond access price, and ROI evaluation requires a defined measurement boundary for cost and value, then treating access price as total adoption cost creates underestimation risk within the evaluation boundary.” Steps 1, 2, 3, and 6 are worked below. Complete steps 4 and 5.

Step 1. THM-002, as named above.

Step 2. When a buyer’s cost of adopting AI includes more than the access price, and judging the return requires a boundary that takes in both cost and value, treating the access price as the whole cost risks understating it.

Step 3. Four dependencies: LEM-006, LEM-021, LEM-002, and LEM-020.

Step 4. Restate each dependency in one sentence, and note any condition it adds.

Step 5. State what THM-002 establishes and what it does not. Then explain why LEM-002 and LEM-020 support the theorem even though neither appears among its conditions.

Step 6. The defeating case is a buyer whose adoption cost includes categories beyond the access price, who evaluates the return inside a boundary covering cost and value, who treats the access price as the total, and whose cost is not understated.

**P3 · Independent.** A reply to the word-games objection

A senior colleague reads THM-004 and says: “This is common sense in numbered clauses. Anyone who has run a large deployment knows you need controls. Formalizing it adds nothing.” Write a one-page reply. Use the four parts of a formal claim from Section 3.3, and name at least one thing the formal statement lets the colleague do that the common-sense version does not. Do not argue that the colleague is wrong about the conclusion.

*Interleaving: question 4 requires Chapter 2’s three flows, and the cumulative case below requires both earlier chapters.*

## [PART I CUMULATIVE CASE]

**Cumulative case · Part I.** One announcement, three readings

Dated: February 2024. The company’s own announcement, using its own figures. Only that announcement is used here.

In February 2024, the payments company Klarna announced the results of the first month of an AI assistant built on OpenAI’s models. The company reported that the assistant had held 2.3 million conversations, two-thirds of its customer-service chats. By its own estimate, the assistant was doing the work of 700 full-time agents. Customers resolved their questions in under two minutes, against eleven before. The company estimated that the assistant would improve its profit by $40 million in 2024.

Work from the announcement alone, and do not use anything published afterward.

First, apply Chapter 1’s consumption-event inventory. Identify the consumption events the announcement describes and where each is metered.

Second, apply Chapter 2’s three-flow mapping. Diagnose the usage, record, and cost-and-value flows, and name the evidence behind each diagnosis.

Third, pose each of the five Founding Questions against the announcement. For each, state whether the public record answers it from the organization’s own records, and what record would be needed to answer it.

Keep your answers. The case returns in Chapter 6.
