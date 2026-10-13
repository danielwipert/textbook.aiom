# Fact-check package B findings: Chapter 3, "A Science and Its Discipline"

Method: chapter text only. Nothing was looked up and no source, register, or
registry was consulted. No finding says whether a fact is true. Each says where
the chapter claims more than it shows.

Notes on form:
- Findings are numbered in rank order, so B-1 is Rank 1.
- Quotations are normalized for the stated extraction artifacts (rejoined
  line breaks, letterspaced capitals set in sentence case, straight quotes).
- Where the same overreach appears in more than one sentence, the extra
  sentences are listed on an "Also:" line.
- Every proposed remedy follows the house rules: no em or en dashes, no
  hedging, no contractions.

---

## Findings

```
B-1. Rank 1  [Figure 3.2 caption, Section 3.4]
Sentence: "AI Business Economics states what is true about consuming AI."
Also: "Part II establishes what is true, Part III builds the five functions, and Part IV turns them into an institution." [3.6]; "That work requires both a body of knowledge about what is true and a practice that turns that knowledge into action." [Opening case]
Conflicts with: "It checks the structure and record of an argument, not its truth."   [3.1]
Also conflicts with: "Whether that smaller claim is true is a separate question the graph does not answer." [3.1]; "Here, science does not imply laboratory experiments or certainty." [3.1]
A reader would wrongly conclude: that a certified claim is a true claim, so a theorem can be relied on without examining what it rests on, which is the exact reading Section 3.1 rules out.
Proposed remedy: Caption: "AI Business Economics states conditional claims about consuming AI and records what each one rests on." Section 3.6: "Part II presents the certified claims the functions rest on, Part III builds the five functions, and Part IV turns them into an institution." Opening case: "That work requires both a body of knowledge whose claims state when they hold and a practice that turns that knowledge into action."
```

```
B-2. Rank 2  [Opening case, body and footnotes 2, 3, 5]
Sentence: "Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: 'No one can answer that question yet.'"
Also: footnote 5, "Practitioner quotation as reproduced in the report."; footnotes 2 and 3, which cite "State of FinOps 2026" directly, with an access date, for the survey size and the 98 and 31 percent figures.
Conflicts with: "Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself."   [Opening case banner]
A reader would wrongly conclude: that the authors read the quotation, the question that prompted it, and the figures in the report itself, and that the report selected the quotation, when the banner says only secondary coverage was compared.
Proposed remedy: Body: "Coverage of the report quotes one practitioner on whether AI was providing value: 'No one can answer that question yet.'" Footnote 5: "FinOps Foundation, 'State of FinOps 2026,' February 19, 2026. Practitioner quotation as given in secondary coverage of the report. It has not been checked against the report itself." Footnotes 2 and 3 take the same closing two sentences, with "Figures" in place of "Practitioner quotation".
```

```
B-3. Rank 3  [3.1; repeated in Chapter summary]
Sentence: "The registry supports each result the book teaches so that a reader who doubts a claim can trace its basis."
Also: "The registry supports each result so that readers who doubt a claim can trace its basis." [Chapter summary]
Conflicts with: "Nor does it establish Chapter 2's three flows, which belong to this book's framework."   [3.3]
Also conflicts with: "This book calls it the value boundary." [3.4]. The five functions and the five Founding Questions are stated with no registry identifier anywhere in the chapter.
A reader would wrongly conclude: that the three flows, the five functions, the Founding Questions, and the borders in Table 3.1 are certified registry results that can be traced like THM-004.
Proposed remedy: "The registry supports each formal claim the book presents in a panel or cites by identifier, so that a reader who doubts one can trace its basis. The book's own framework, including the three flows, the five functions, and the Founding Questions, is not a registry result." If the functions or questions do have registry identifiers, the remedy is to cite them where they are introduced.
```

```
B-4. Rank 4  [3.2, dated box]
Sentence: "It recorded 1,777 dependency links among these objects, and 397 of the 413 were certified."
Conflicts with: "This book renders and cites only certified claims, because presenting an uncertified claim as a theorem would assert more than the science establishes."   [3.1]
Also conflicts with: "A claim is certified when every claim it depends on is certified and its supporting argument meets the registry's fixed conditions." [3.1]
A reader would wrongly conclude: one of two things. First, that 397 claims had a supporting argument checked, when 175 of the 413 objects are definitions and axioms, which have no supporting argument, and 5 are evidence records, which are not claims. Second, a reader who adds the box's own counts finds that definitions, axioms, propositions, and lemmas sum to exactly 397 (140 + 35 + 201 + 21), and that theorems plus evidence records sum to exactly the 16 uncertified objects (11 + 5). The box does not say which 16 are uncertified, so the arithmetic permits the reading that no theorem was certified at the pinned version. The chapter never states that THM-004, THM-002, or LEM-021 is certified; it says so only of the four lemmas under THM-004.
Proposed remedy: none. The box needs the certified count broken out by object type, at least for theorems and lemmas, and this package does not contain those numbers.
```

```
B-5. Rank 5  [3.3]
Sentence: "The formal version does: the pilot fails the first condition, so the theorem is silent about it."
Also: "A pilot used by one team for a few weeks has not been scaled into daily operations, so it fails the first condition." [3.3]
Conflicts with: "It does not specify the scale at which governance becomes necessary or the size of the economic exposure."   [3.3]
A reader would wrongly conclude: that THM-004 supplies a test that separates a pilot from a scaled deployment, when the chapter states no threshold and classifies the pilot by assertion, which is the same gap it charges the common-sense version with for never defining "big".
Proposed remedy: "The formal version names what to check: whether production scaling has expanded the usage surface. It does not set the threshold, so the manager must still decide whether the one-team pilot has crossed it. If it has not, the theorem is silent about the pilot."
```

```
B-6. Rank 6  [3.2]
Sentence: "The second and third establish the only route to managing that exposure: measurement makes it visible, allowing management mechanisms to be applied."
Conflicts with: "LEM-020 establishes that visibility makes management mechanisms available."   [Problem P1, Step 5]
Also conflicts with: "LEM-002 says that measured and recorded activity becomes observable enough to support analysis, attribution, monitoring, or management." [Craft section, Step 4]
A reader would wrongly conclude: that two lemmas the chapter restates as enabling claims prove that no other route to control exists, which is the step from "makes possible" to "is required" that Section 3.3 warns against under the names sufficient and necessary.
Proposed remedy: "The second and third establish a route to managing that exposure: measurement makes it visible, and visibility allows management mechanisms to be applied. The step from that route to the conclusion that control requires it is made in the theorem's proof record, which this chapter does not reproduce."
```

```
B-7. Rank 7  [3.3, against the Craft section]
Sentence: "A deployment with no instruments installed can therefore meet all four conditions."
Conflicts with: "A team that can see its costs but lacks authority to cap them falls outside LEM-020's scope. The support for THM-004's third condition therefore does not extend to that team, and the theorem says nothing about it."   [Craft section, Step 4]
Also conflicts with: "LEM-020's scope requires reliable visibility and the authority to apply management mechanisms." [Craft section, Step 4]
A reader would wrongly conclude: that THM-004 covers an uninstrumented deployment. By the craft section's own reasoning, a deployment with no instruments has no reliable visibility, falls outside LEM-020's scope, and is a case the theorem says nothing about. The same reasoning places the stated falsifying case (control with no measurement and management apparatus) outside the theorem's coverage, which Section 3.3 says leaves a claim that "tells a manager nothing".
Proposed remedy: none. The two passages need one reading of whether a dependency's scope limits the theorem's coverage, and that choice depends on the registry record, which this package does not include.
```

```
B-8. Rank 8  [3.2]
Sentence: "Costs accrue with use and grow with scale, as the first and fourth conditions describe."
Also: "The first and fourth establish that economic exposure grows with the deployment and cannot be determined from the access price alone." [3.2]
Conflicts with: "LEM-016 says that moving from isolated use into repeated operations can increase the number of usage events and demand points."   [Craft section, Step 4]
Also conflicts with: "It does not specify the scale at which governance becomes necessary or the size of the economic exposure." [3.3]
A reader would wrongly conclude: that the registry establishes that cost rises with scale, when the two lemmas as the chapter restates them say that usage events can increase and that total cost exceeds the access price.
Proposed remedy: "Scaling can multiply the places where usage occurs, and total cost extends beyond the access price, as the first and fourth conditions describe." And: "The first and fourth establish that scaling can expand where usage occurs and that the buyer's total cost cannot be read from the access price alone."
```

```
B-9. Rank 9  [3.5, Table 3.1, FinOps row]
Sentence: "A practitioner told its own survey that no one could yet say whether AI provides value"
Also: "The report also recorded what practitioners had yet to establish." [Opening case]; "The survey reveals the gap Chapters 1 and 2 described, as reported by the people asked to close it." [Opening case]
Conflicts with: "Asked whether AI was providing value, one practitioner gave an answer the report chose to quote: 'No one can answer that question yet.'"   [Opening case]
A reader would wrongly conclude: that one remark by one person, unverified per the banner, shows what the FinOps discipline lacks and what practitioners in general have not established. The table also says the remark was made to the survey, while the opening case says only that the report quoted it, and the table cell carries no footnote and no warning.
Proposed remedy: Table cell: "It was built around cloud billing. Coverage of its 2026 report quotes one practitioner saying that no one could yet answer whether AI was providing value" Opening case: "The report also carried one practitioner's statement of what remained unknown."
```

```
B-10. Rank 10  [Opening case]
Sentence: "Its practitioners later took on AI spending, and by 2026 nearly all of them were managing it."
Conflicts with: "Ninety-eight percent of respondents now managed AI spending, up from 31 percent two years earlier."   [Opening case]
A reader would wrongly conclude: that nearly all FinOps practitioners manage AI spending, when the figure covers 1,192 respondents to one survey. "Up from 31 percent" also reads as the same people measured twice, when the two figures come from two survey years with no stated overlap, and footnote 3 widens the population again with "Share of practitioners".
Proposed remedy: "Its practitioners later took on AI spending, and by 2026 nearly all of the survey's respondents were managing it." And: "Ninety-eight percent of the 2026 respondents managed AI spending. In the survey two years earlier, the share was 31 percent." Footnote 3: "Share of respondents managing AI spend, 2026 survey against 2024 survey."
```

```
B-11. Rank 11  [3.5, with Opening case and Table 3.1]
Sentence: "It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology."
Conflicts with: "The discipline developed to make engineering, finance, and business teams jointly accountable for that spending."   [Opening case, footnote 4: "The practice as the Foundation defines it."]
Also conflicts with: "Financial accountability for technology spending, through collaboration among engineering, finance, and business teams" [Table 3.1, footnote 15: "The Foundation's own definition of the practice."]; "Cloud cost management is a capable neighboring discipline" [Opening case]; "Cloud and wider technology spending" [Table 3.1]
A reader would wrongly conclude: nothing stable, because one source page is cited three times for three accounts: accountability for cloud spending, accountability for technology spending, and maximizing the business value of technology. The table's purpose cell leaves out the value purpose that Section 3.5 attributes to the same definition, which makes the "what it lacks" cell look stronger than the chapter's own text supports. The opening case also restates a mission about people who manage "cloud value" as people who "manage cloud spending for a living", and keeps the label "cloud cost management" after reporting that the mission moved to technology.
Proposed remedy: Table cell: "Maximizing the business value of technology through financial accountability and collaboration among engineering, finance, and business teams" Opening case: "FinOps is a capable neighboring discipline that has expanded into work no discipline in Table 3.1 was built to govern: the economics of an organization's AI consumption."
```

```
B-12. Rank 12  [3.5]
Sentence: "FinOps was built to make cloud spending accountable after capacity had been used."
Conflicts with: "FinOps was built to address a specific problem: cloud computing let engineers buy capacity with a few lines of code, but the bills arrived after they had used it."   [Opening case]
A reader would wrongly conclude: that FinOps by design acts only after money is spent. The opening case puts "after use" in the problem (when bills arrived), not in the discipline. The contrast in the next sentence, "a value boundary set before spending begins", depends on that shift.
Proposed remedy: "FinOps was built to make cloud spending accountable when bills arrived after capacity had been used."
```

```
B-13. Rank 13  [3.4; also 3.5 and Key terms]
Sentence: "The organization must set that boundary for each deployment and name the person responsible for knowing the answer."
Also: "AI Operations Management manages consumption metered by the request and judges it against a value boundary set before spending begins." [3.5]; "LEM-021 states that any evaluation of return on AI requires such a boundary." [Key terms, Value boundary]
Conflicts with: the quoted statement of LEM-021 in the same paragraph, which is conditional on an evaluation being made and names costs, value, time period, and outcomes.   [3.4]
A reader would wrongly conclude: that a certified lemma requires a boundary for each deployment, a named owner, and a boundary set before spending begins, and that it requires organizations to evaluate return at all. The quoted statement contains none of the first three and is conditional on the fourth. The lemma's own name says "Measurement Boundary", the same term THM-004 uses for its scope, and the chapter does not say whether the value boundary and the measurement boundary are one thing.
Proposed remedy: "LEM-021 requires a defined boundary whenever return is evaluated. This book adds two requirements of practice that the lemma does not state: the boundary is set for each deployment before spending begins, and one named person is responsible for knowing the answer. This book calls it the value boundary."
```

```
B-14. Rank 14  [3.1]
Sentence: "The registry's validator computes that status from the graph at each version; no one enters it manually."
Conflicts with: "The validator checks that every dependency is recorded and certified, that no chain of support loops back on itself, that every empirical claim has evidence attached, and that a reviewer has signed off on the claim's current wording."   [3.1]
A reader would wrongly conclude: that certification involves no human judgment. One of the four checks is a human sign-off, and neither it nor attached evidence is a property of the graph. The chapter also says evidence is "attached", and nowhere says anyone checks that the evidence supports the claim.
Proposed remedy: "The registry's validator computes that status at each version from the graph and from two recorded inputs: the evidence attached to each empirical claim and a reviewer's sign-off on its wording. No one enters the status itself by hand."
```

```
B-15. Rank 15  [3.3]
Sentence: "The registry records every claim's non-claims."
Conflicts with: "Nor does it establish Chapter 2's three flows, which belong to this book's framework."   [3.3]
A reader would wrongly conclude: that the registry's list of exclusions for a claim is complete, so a conclusion not listed as excluded is established. The chapter's own example adds a non-claim that comes from the book and not from the registry, and Step 5 of the craft section lists it with the recorded exclusions as if all had one source.
Proposed remedy: "The registry records exclusions for each claim. The list is not exhaustive: a conclusion absent from it is not thereby established."
```

```
B-16. Rank 16  [3.2]
Sentence: "This pairing explains Chapter 2's statement that THM-004 formalizes the economic consequence of the third flow's asymmetry."
Conflicts with: "Nor does it establish Chapter 2's three flows, which belong to this book's framework."   [3.3]
A reader would wrongly conclude: that a registry theorem is about the three flows and lends them certified support.
Proposed remedy: "This pairing is the basis for Chapter 2's reading of THM-004 through the third flow. The flows belong to this book's framework, and the theorem does not establish them."
```

```
B-17. Rank 17  [3.1]
Sentence: "A reader with the registry can start at any theorem and follow its supporting claims down to definitions and axioms."
Also: "Readers can therefore trace any claim to the lemma level using the book alone." [3.1]
Conflicts with: "A claim with a gap in its supporting claims carries a record of what is missing."   [3.1]
Also conflicts with: "Appendix A reproduces every certified theorem and lemma, while propositions are cited by identifier." [3.1]
A reader would wrongly conclude: that every theorem traces all the way down, and that a reader of the book can do the tracing. The chapter records gaps and 16 uncertified objects, never says readers can open the registry, and rests every scope condition, exclusion, and proof record in this chapter on registry footnotes (6 through 12, 17 through 20) that the book alone does not let a reader check.
Proposed remedy: "A reader with the registry can start at any certified theorem and follow its supporting claims down to definitions and axioms." And: "Readers can therefore trace any certified theorem to the lemma level using the book alone. Scope conditions, exclusions, and proof records are reported from the registry and are not reproduced in the book."
```

```
B-18. Rank 18  [3.1]
Sentence: "For a manager, the graph resolves one practical concern: no conclusion rests on circular reasoning."
Also: "The result is a dependency graph: a map in which no claim can rest, directly or indirectly, on itself." [3.1]
Conflicts with: "It checks the structure and record of an argument, not its truth."   [3.1]
A reader would wrongly conclude: that the reasoning is free of circularity, when the check covers recorded links only. Two claims that assume the same thing in different words pass it. The loop check is also listed as a condition of certification, which implies an uncertified claim can fail it, while "no claim can rest" says none can.
Proposed remedy: "For a manager, the graph resolves one practical concern: no certified claim names itself, directly or indirectly, among its recorded supports."
```

```
B-19. Rank 19  [3.3]
Sentence: "A flat-fee contract does not provide such a case."
Conflicts with: "If it does not, the organization would have to control the costs beyond the fee without measuring them."   [3.3]
A reader would wrongly conclude: that the flat-fee objection has been answered. The second branch restates the falsifying case and treats it as impossible, which assumes the theorem's conclusion. The first branch concedes that a scaled deployment under an all-inclusive fee is outside the theorem, a limit the plain summaries of THM-004 in Sections 3.2 and 3.3 do not carry.
Proposed remedy: "A flat-fee contract does not by itself provide such a case. If the fee covers every cost, the fourth condition fails and the theorem is silent. If it does not, the contract is a falsifying case only if the organization controls the costs beyond the fee without measuring them."
```

```
B-20. Rank 20  [Opening case]
Sentence: "Until both exist, the practitioner's question about whether AI is providing value remains unanswered."
Also: "Cloud cost management is a capable neighboring discipline that has expanded into work no discipline was designed to govern: the economics of an organization's AI consumption." [Opening case]; "A neighboring discipline cannot supply either on its behalf." [Opening case]
Conflicts with: "AI Business Economics is that body of knowledge."   [3.1]
Also conflicts with: "AI Operations Management is the practice of managing an organization's AI consumption from week to week." [3.4]
A reader would wrongly conclude: either that the science and the discipline do not yet exist, against the present-tense definitions that follow, or that no organization can know whether AI provides value until it adopts this book's two layers. The second is supported only by one quoted remark. "No discipline was designed" is a universal claim resting on a table of four neighbors. The practitioner also gave an answer, not a question.
Proposed remedy: "This book argues that an organization needs both to answer, from its own records, whether AI is providing value."
```

```
B-21. Rank 21  [Problem P2, Steps 3 and 6]
Sentence: "The buyer treats the access price as the total cost, yet the cost is not understated."
Also: "it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that the cost is understated holds without it." [P2, Step 3]
Conflicts with: "treating the access price as the whole cost risks understating it."   [P2, Step 2]
A reader would wrongly conclude: that THM-002 claims the cost is understated, when the statement quoted in the problem claims a risk. A case with no actual understatement does not defeat a claim about risk, so the worked Step 6 does not follow the procedure's own Step 6 ("meets every condition but lacks the conclusion"), in a problem students are told to complete by its model.
Proposed remedy: Step 6: "The buyer treats the access price as the total cost, yet doing so creates no risk of understating the cost within the evaluation boundary." Step 3: "it concerns what a buyer can do about an understated cost once that cost is visible, but the claim that treating access price as total cost creates underestimation risk holds without it."
```

```
B-22. Rank 22  [Craft section, Step 4]
Sentence: "The trace reveals a limit not stated in the theorem's own wording."
Conflicts with: "It adds a condition: the record must be detailed enough for the relevant person to observe the activity."   [Problem P1, Step 4, on LEM-002]
A reader would wrongly conclude: that the authority requirement is the only limit the trace of THM-004 uncovers. LEM-002 supports the theorem's second condition directly, and P1 reports a requirement of its own that the craft section's trace never mentions. P1 also calls it a "condition" while footnote 18 calls it a "scope condition", after the craft section insisted for LEM-020 that the requirement "belongs to the scope, rather than the third condition".
Proposed remedy: Add after that sentence: "LEM-002's scope adds a second limit: the record must be detailed enough for the relevant person to observe the activity." In P1, Step 4: "Its scope adds a requirement: the record must be detailed enough for the relevant person to observe the activity."
```

```
B-23. Rank 23  [Problem P1, Steps 2 and 6]
Sentence: "The falsifying case is an organization that can see a deployment's usage and has authority to manage it, but still cannot apply any monitoring, limit, or attribution to it."
Conflicts with: "When the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it."   [P1, Step 2]
A reader would wrongly conclude: that P1 is a complete model trace. The procedure's Step 2 says "State its scope", P1's Step 2 states none, and Step 6 then relies on "has authority", which appears in no condition P1 restated. A student using P1 as the model for P2 would omit scope.
Proposed remedy: Step 2: "Scope: the relevant actor has reliable visibility and the authority to apply management mechanisms. Within that scope, when the people responsible for a deployment can see its usage or cost, they can apply monitoring, limits, attribution, or other management mechanisms to it."
```

```
B-24. Rank 24  [Figure 3.1; 3.2; Problem P2]  (unsure: the names are probably verbatim from the registry)
Sentence: "PROP-053 Economic Exposure Creates Incentives For Monitoring"   [Figure 3.1 label]
Also: "LEM-016, 'Production Scaling Expands Usage Surface,' supports the first." [3.2]; "THM-002, 'AI Adoption Cost Is Underestimated When Access Price Is Treated as Total Cost,' states a result taught in Part II." [P2]
Conflicts with: "PROP-053 establishes that monitoring can be used to observe economic exposure."   [3.2]
Also conflicts with: the craft section's restatement that LEM-016 "can increase" usage events, and THM-002's quoted statement, which claims "underestimation risk".
A reader would wrongly conclude: that a claim's name states what it establishes. Three names in this chapter say more than the statements or restatements the chapter gives for them (incentives, expansion as fact, underestimation as fact), and Step 1 of the procedure tells the reader to record the name exactly.
Proposed remedy: Add to Step 1 of the procedure: "A claim's name is a label. Only its statement says what the claim establishes."
```

```
B-25. Rank 25  [3.2]
Sentence: "A disagreement over a specific proposition can be settled."
Conflicts with: "Whether that smaller claim is true is a separate question the graph does not answer."   [3.1]
A reader would wrongly conclude: that the registry settles disputes at the proposition level, when propositions rest on axioms the science "accepts without proof" and certification does not test truth.
Proposed remedy: "A disagreement over a specific proposition concerns one stated claim, so the two sides can name the fact that would decide it."
```

```
B-26. Rank 26  [3.6; also 3.5]
Sentence: "AI Operations Management exists to answer five questions that an organization cannot answer without the discipline."
Also: "It can always produce an answer by asking the provider, estimating, or repeating the business case, but none of those methods produces knowledge the organization holds and can check." [3.6]; "Only the discipline can determine whether the organization's requests, taken together, are worth what they cost." [3.5]
Conflicts with: "It already manages spending, has expanded into AI, and defines its purpose in terms of maximizing the business value of technology."   [3.5, on FinOps]
A reader would wrongly conclude: that no organization today can say, for example, who consumed what last month without adopting this discipline. The chapter tests no organization. Its evidence about organizations is one quoted remark and one company announcement.
Proposed remedy: 3.6: "AI Operations Management exists to answer five questions from an organization's own records. Each question needs the function that corresponds to it." 3.5: "That judgment needs the combined record of consumption, cost, and value that the discipline's functions build."
```

```
B-27. Rank 27  [3.1; 3.4]
Sentence: "When those claims are wrong, management based on them fails, however carefully managers carry it out."
Also: "The discipline depends on the science because a practice built on incorrect claims fails however well it is run." [3.4]
Conflicts with: "It checks the structure and record of an argument, not its truth."   [3.1]
A reader would wrongly conclude: that any wrong claim always produces failure, and, read with B-1, that building on the certified science protects a practice from that failure.
Proposed remedy: 3.1: "When those claims are wrong, careful execution does not repair the decisions built on them." 3.4: "The discipline depends on the science because careful practice cannot repair a decision built on an incorrect claim."
```

```
B-28. Rank 28  [Part I cumulative case]
Sentence: "Customers resolved their questions in under two minutes, compared with eleven minutes previously."
Conflicts with: "The company's own announcement, using its own figures. Only that announcement is used here."   [Cumulative case banner]
A reader would wrongly conclude: that the resolution times are established facts. Every other figure in the paragraph is marked "reported" or "estimated"; this one is stated flat and with no period attached.
Proposed remedy: "The company reported that, in that first month, customers resolved their questions in under two minutes, compared with eleven minutes previously."
```

```
B-29. Rank 29  [Part I cumulative case, tasks]
Sentence: "For each question, state whether the public record provides an answer from the organization's own records and what record would be needed to answer it."
Also: "Identify the consumption events described in the announcement and where each is metered."
Conflicts with: "Work from this announcement alone."   [Cumulative case]
A reader would wrongly conclude: that other public information is in scope, and that the announcement says where consumption is metered. The chapter's account of the announcement contains no metering facts, so the first task rests on facts the chapter neither established nor labelled.
Proposed remedy: "For each question, state whether the announcement provides an answer from the organization's own records and what record would be needed to answer it." And: "Identify the consumption events described in the announcement and state whether the announcement says where each is metered."
```

```
B-30. Rank 30  [Opening case]
Sentence: "The new statement replaced one word: the Foundation now advances the people who manage technology value."
Conflicts with: "Figures and the quotation agree across secondary coverage and have not yet been checked against the report itself."   [Opening case banner]
A reader would wrongly conclude: that the authors compared the two mission statements word for word. Both statements are paraphrased, not quoted, and the banner's check covers "figures and the quotation" and is silent on the mission statement, so its verification status is not stated anywhere.
Proposed remedy: none. The one-word claim needs both statements quoted in full, and this package does not contain them.
```

```
B-31. Rank 31  [3.4]
Sentence: "The organization buys AI capacity, plans its use, records consumption, and assigns it to the work it serves."
Also: "It decides what runs when capacity is limited and holds spending accountable for the value it returns." [3.4]
Conflicts with: "Each function is a capability an organization either has or lacks."   [3.4]
A reader would wrongly conclude: that organizations in general already do these things, when the sentences describe the practice and not observed behavior.
Proposed remedy: "An organization that practices it buys AI capacity, plans its use, records consumption, and assigns it to the work it serves. It decides what runs when capacity is limited and holds spending accountable for the value it returns."
```

```
B-32. Rank 32  [3.4]
Sentence: "AI Operations Management resolves it by managing AI as a resource the organization consumes rather than as software it has bought."
Conflicts with: "Chapter 1 stated the conditions under which deployed AI is a resource the organization consumes."   [3.1]
A reader would wrongly conclude: that deployed AI is always a consumed resource, with no conditions, and that the discipline has been shown to resolve the error.
Proposed remedy: "AI Operations Management addresses it by managing AI as a resource the organization consumes wherever Chapter 1's conditions hold."
```

```
B-33. Rank 33  [3.4]
Sentence: "If two workflows share a provider account with a fixed rate limit, one waits whenever the other is busy."
Conflicts with: none. The example is neither established nor labelled as constructed, unlike the help-desk example two paragraphs later.
A reader would wrongly conclude: that a shared rate limit always blocks one workflow while the other runs, when waiting follows only if combined demand exceeds the limit.
Proposed remedy: "Consider a constructed example: two workflows share a provider account with a fixed rate limit. When their combined demand exceeds the limit, one of them waits, and no one has decided which."
```

```
B-34. Rank 34  [3.5; Chapter summary]
Sentence: "AI Operations Management begins with that call, when each use consumes resources and costs money."
Conflicts with: "AI Operations Management begins with buying capacity for the chosen use and manages its consumption from then on."   [3.5]
Also conflicts with: "It begins when a model becomes a service an organization consumes." [Chapter summary]
A reader would wrongly conclude: that sourcing, the first function, lies outside the discipline, because it happens before any call is made.
Proposed remedy: "AI Operations Management begins where a model is a service an organization can buy and call."
```

```
B-35. Rank 35  [3.3]
Sentence: "The most costly misreading confuses necessary with sufficient."
Conflicts with: none.
A reader would wrongly conclude: that the chapter has compared the cost of misreadings, or knows how often managers make this one. Its only illustration is a hypothetical manager who "might buy a dashboard".
Proposed remedy: "One misreading with a direct cost confuses necessary with sufficient."
```

```
B-36. Rank 36  [3.5, footnote 13]
Sentence: "The originating definition of AIOps."
Conflicts with: none. The table cell it supports gives a description and makes no claim about origin.
A reader would wrongly conclude: that the cited glossary originated the term, a claim made only in a footnote note and supported nowhere in the chapter.
Proposed remedy: "The glossary's definition of AIOps."
```

---

## Coverage notes

### Item 3: one organization, described consistently

- FinOps: inconsistencies are in B-9, B-10, B-11, B-12. Discussion question 2
  ("which is hardest to defend") is consistent with Section 3.5 ("the hardest
  to define"). The two Chapter 14 cross-references agree.
- Klarna: the figures are internally consistent across the case and footnote
  21. The two defects are B-28 (unattributed figure) and B-29 (task scope).

### Item 4: remaining sentences about what organizations, managers, or practitioners generally do

Sentences already raised: B-10, B-20, B-26, B-27, B-31, B-35. The rest are
listed here so the inventory is complete. None is ranked, because each is
definitional, modal ("can"), or a stipulated conditional.

- "Managers act on claims about how their business works." [3.1]
- "A budget assumes that costs follow usage." and the two sentences after it
  on a pricing negotiation and a dashboard. [3.1]
- "Claims like these can remain informal, held in experience, rules of thumb,
  or the slides of the last person to present." [3.1]
- "That knowledge is useful, but it has a cost: two managers can hold opposing
  beliefs about the same deployment without being able to identify where they
  disagree." [3.1]
- "Without stating their claims, neither can identify the fact that would
  settle the disagreement, so the argument turns on confidence rather than
  evidence." [3.1]
- "Organizing the chapters by proof would leave a manager reading definitions
  for many pages before reaching a recognizable decision." [3.1]
- "When an organization pays for a metered resource, costs accrue with use,
  but someone must build the means to measure the value it receives."
  [Opening case]
- "FinOps was built to address a specific problem: cloud computing let
  engineers buy capacity with a few lines of code, but the bills arrived after
  they had used it." [Opening case]
- "A manager who can state all four can use the claim without being misled by
  it." [3.3] This one is a guarantee; it is the closest of the list to a
  finding.
- "Knowledge alone does not change what an organization does." and the
  medicine and engineering sentences after it. [3.4]
- "A budget is a commitment made in advance that makes deviations visible as
  they happen, before the money is gone." [3.4] A budget alone shows nothing
  without the record the third function builds; also close to a finding.
- "These choices occur even when no one makes them deliberately." [3.4]
- "Without that assignment, managers can see a cost but cannot trace it to the
  work that caused it." [3.4]
- "A result about governance changes nothing until an organization builds the
  apparatus it describes" [3.4]
- "the time is worth spending once for each claim on which a decision
  depends." [Craft section]

### Item 5: what each example and problem rests on

Established in this chapter or cited to the registry:
- The THM-004 trace in Section 3.2 and the craft section (footnotes 6 to 12,
  17).
- Problem P1 (footnotes 18, 19). Four propositions (PROP-032, 039, 041, 042)
  are paraphrased without their statements being quoted. See also B-22, B-23.
- Problem P2 (footnote 20). See B-21.

Labelled as constructed, stipulated, or company-reported:
- The help-desk assistant in Section 3.4 ("a constructed example").
- The Klarna cumulative case (banner). See B-28, B-29.
- The dashboard buyer in Section 3.3 (signalled by "might").

Resting on another chapter, not checkable from this package:
- "Chapter 1's Cursor licenses" [3.1].
- "whose absence proved costly in Chapter 2's opening case" [3.4]. This is a
  causal attribution; whoever holds Chapter 2 should confirm that chapter
  shows the cost followed from the missing function.
- Discussion question 4 and the cumulative case's first two tasks (Chapter 1
  inventory, Chapter 2 flows).

Neither established nor labelled (the third kind):
- The one-team pilot [3.3]. See B-5.
- The flat-fee contract [3.3]. See B-19.
- The company that sends every request to its most capable model [3.4]. The
  premise is stipulated inside the sentence, so no wrong conclusion follows.
- The two workflows sharing a rate limit [3.4]. See B-33.
- The team that can see its costs but lacks authority [Craft section]. See
  B-7.
- The senior colleague in Problem P3. Plainly a scenario; no wrong conclusion
  follows.
- The medicine and engineering analogies [3.4]. General knowledge, unlabelled;
  no wrong conclusion follows.

---

FIX FIRST: B-1, because a caption telling students the science "states what is true" cancels the chapter's own warning that certification checks structure and not truth, and that warning governs how every formal claim in the book is read.
