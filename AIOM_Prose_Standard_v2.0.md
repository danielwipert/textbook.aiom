> **STATUS: ADOPTED 2026-08-19 as Decision 71, on Dan's ruling. This is THE prose
> standard, and it is ONE file.**
>
> It supersedes `AIOM_Prose_Style_Guide_v1.md` and `AIOM_Voice_and_Craft_v1.md`,
> both of which are retired to pointers at this document. It also supersedes the
> register rule in CLAUDE.md section 2 and in Consolidated Spec B.2.
>
> **The spine of this document is Dan's own guide, written after Chapter 1 and
> supplied on 2026-08-19.** His text is kept where it was already right, because
> the author's statement of his own voice is the authority and paraphrasing it
> would be the same error rule 4a forbids against the registry. What is added is
> the material absorbed from the two retired files, the reconciliation of four
> conflicts between them, and worked examples taken from this book rather than
> invented.

# AIOM Prose Standard v2.0

## The voice is Concrete Management Prose

---

## 0. Why this standard exists, and what it cost to learn

**The prose of Chapter 1's first draft was rejected, and the rejection was
correct.** It was abstract where it should have been concrete, it opened
paragraphs with categories rather than with business realities, and it introduced
conceptual labels before the actions they name. It read as philosophy rather than
as management writing.

**The cost is measurable and it is in this repository's own record.** The Stage 6
copy edit "rewrote the chapter rather than corrected it": round 1 alone changed 59
of 155 blocks, grew body prose 25 per cent, and took the chapter from 20 pages to
26. Under the scoped re-run matrix that forced the reopen of 2026-08-08, which
reset Stages 2, 3, 4, 5 and G2. That reopen is one of the five the 2026-08-19
process review identified as the most expensive class of event in the project.
**The deeper cause was not the step order. It was that the draft arriving at the
copy edit was in the wrong voice.**

**ADDING RULES IS NOT THE FIX, AND THIS IS THE POINT OF CONSOLIDATION.** The
retired style guide already required naming the thing, keeping the actor in the
sentence, one clause one job, varied sentence length, and rationed interrupters.
Those rules were on `main` and they did not bind. Three things were missing:

1. **A generative pattern.** The old files described qualities good prose has,
   which grades a draft. They never said what to write next. Sections 3 through 11
   here are that pattern.
2. **A ban on abstract openings.** The old files had none. It is section 3 here,
   and it is the single largest gap the rejection exposed.
3. **Ordinary business language as the default.** The old register was named
   "magisterial", stated first, above everything else. A drafter resolving a
   conflict between "magisterial" and "keep the actor visible" chose magisterial
   every time, because register sets the altitude. **That instruction is retired
   by Decision 71.**

**This standard binds from Stage 0, at drafting time. It is not a Stage 4 check.**
Stage 4 verifies it. A chapter drafted without it and repaired later costs a
reopen, which is the history above.

---

## 1. Purpose of the voice

This voice explains unfamiliar ideas about AI through familiar business realities.
It is written for managers, executives, MBA students, and operators who need to
understand what AI changes inside an organization without first mastering computer
science.

The writing should feel:

- Concrete rather than theoretical
- Direct rather than performative
- Serious without sounding academic
- Accessible without becoming simplistic
- Confident without overstating the evidence
- Structured without sounding mechanical

The reader should rarely need to reread a sentence. Each paragraph should make one
business idea easier to see, evaluate, or use.

---

## 2. The reader

Absorbed from the retired style guide, and unchanged in substance.

The reader is an intelligent, busy, sceptical MBA-level graduate student who has
read business books before and can tell when one is padded. They know how
organizations buy things, how budgets work, how a cost centre is charged, and what
a contract negotiation looks like. They do not know how a model is served, what a
token is, or why inference costs money.

Two failure modes, and the second is the one this book has actually committed:

- **Condescension.** Explaining what a budget is, or what procurement does.
- **Assumption.** Using a technical term, a coined term, or an abstraction as
  though the reader has already agreed to it. **This is the failure that produced
  the rejected draft.** It reads as sophistication to the writer and as fog to the
  reader.

**The expert-reader trap.** The drafter knows the argument already, so a sentence
that merely gestures at a mechanism feels complete. It is not complete. The test is
not whether the sentence is true. It is whether a reader who does not yet agree can
follow it on the first pass.

---

## 3. Core principle

**State the business reality first. Explain the abstraction second.**

Do not begin by naming a framework, discipline, category, or conceptual
distinction. Begin with something the reader can picture happening inside an
organization.

Instead of:

> Resources that flow through an organization have long been governed by a mature
> management discipline.

Write:

> Businesses already know how to manage resources that are consumed in daily
> operations.

The first sentence asks the reader to interpret several abstractions at once. The
second gives the reader a familiar business situation immediately.

---

## 4. The basic explanatory pattern

Most passages should follow this sequence:

1. **State the idea plainly.** Tell the reader what is true in ordinary business
   language.
2. **Give the reader something concrete to picture.** Use a company, manager,
   product, contract, invoice, budget, or operating decision.
3. **Explain how the mechanism works.** Show who does what, using which
   information, and for what purpose.
4. **State the management consequence.** Explain what the organization can or
   cannot do as a result.
5. **Return to the larger argument.** Connect the example to AI management.

Example:

> Deployed AI is a resource the organization consumes. Every time an employee,
> workflow, or product uses AI, the organization incurs a cost. As the amount of
> work grows, that cost usually grows with it. Managing AI therefore requires more
> than buying access to a model. It requires the organization to track
> consumption, allocate it deliberately, and compare its cost with the value it
> creates.

---

## 5. Begin with the claim

The first sentence of a paragraph should usually contain its main point. Do not
make the reader work through several sentences before discovering why the paragraph
exists.

Weak opening:

> The same five practices, stated in timeless form, are not techniques belonging to
> manufacturing.

Stronger opening:

> These five practices are not unique to manufacturing.

Best when additional clarity is useful:

> The same five management practices apply to any resource that costs money as an
> organization uses it.

Use the shortest version that preserves the full meaning.

---

## 6. Use visible actors and actions

Business writing becomes clearer when the reader can see who acts.

Prefer:

- Procurement negotiates the contract.
- Engineering tracks system activity.
- Finance allocates the costs it can trace.
- Managers decide which teams receive access.
- The company compares actual consumption with its budget.

Avoid:

- The contract is subject to procurement activity.
- Instrumentation is performed on deployed systems.
- Allocation may occur where traceability exists.
- Governance should be applied to usage.

Use active voice unless the actor is genuinely unknown or irrelevant.

---

## 7. Translate abstractions into management questions

An abstraction becomes useful when it can be expressed as a question a manager must
answer.

Instead of writing about "resource governance," ask:

1. What are we buying?
2. What requirement must it meet?
3. How much do we expect to use?
4. Where is it being used?
5. Who decides how it is allocated?
6. What value are we receiving in return?

Questions make the operational meaning visible. They also allow the reader to test
whether an organization is actually managing the resource.

**These are management questions set as questions, not rhetorical questions in
running prose.** The mechanical ban in section 21 stands: a question mark in body
prose that the text then answers for effect is still forbidden. A numbered list of
questions a manager must answer is the permitted form, and `voicecheck.py` counts
question marks, so a list of this kind belongs in a list.

---

## 8. Define technical terms through business consequences

Use a technical term only when it gives the reader a useful distinction. Define it
through what changes for the business.

For example:

> A token is a unit used to measure model input and output. For a manager, its
> importance is practical: more tokens generally mean more computing consumption
> and a higher cost.

Do not define a term only through other technical terms. If the definition does not
change a decision, explain why the reader needs it or remove it.

**A coined term arrives AFTER the mechanism it names, never before it.** This is
the rule the rejected draft broke most often, and section 25 carries the worked
example. Show the reader what happens, then give the thing a name. A label
introduced first is a demand that the reader accept a category before they have
seen the behaviour it describes.

**Inherited vocabulary is placed once and never re-explained.** Absorbed from the
retired guide's section 2.4. A borrowed technical term is glossed in line at its
first load-bearing use in the book, then used freely everywhere after. Across
fifteen chapters this only works if something records what has already been placed,
which is the placed-vocabulary ledger. Coined terms are not tracked there: they
live in the definitional callouts and the key-term list, which are their home.

---

## 9. Use analogies to transfer structure

Analogies should clarify how a management problem works. They should not exist only
to make the prose more colorful.

The steel analogy works because both steel and deployed AI:

- Are acquired against requirements
- Are consumed through operating activity
- Cost money in proportion to use
- Can be tracked to products or teams
- May require allocation when constrained
- Must produce enough value to justify their cost

When using an analogy:

1. Identify the shared management structure.
2. Explain the familiar case in concrete terms.
3. Transfer only the relevant features to AI.
4. State where the analogy stops if the difference matters.

Do not imply that AI and a physical material are identical. The analogy concerns
how organizations manage consumption, cost, allocation, and return.

---

## 10. Keep one main idea per sentence

A sentence may contain a cause and its consequence, but it should not carry an
entire chain of reasoning.

Overloaded:

> In a deployed business context where AI activity requires compute, scaling
> expands the surface of AI usage, and the total cost runs past the access price,
> then the thing being operated is a resource-consuming activity rather than
> software access.

Clearer:

> In a deployed business context, AI activity consumes computing resources. As
> usage scales, its operational footprint grows, and total costs extend beyond the
> price of access. The business is therefore operating a resource-consuming
> activity, not merely accessing software.

When a sentence contains more than one "and," inspect it for possible division.

---

## 11. Build paragraphs in a straight line

Each sentence should answer the question created by the sentence before it.

A strong paragraph often moves through this sequence:

> **Claim:** Most organizations do not manage AI usage through a single discipline.
> **Reason:** Responsibility is divided across several existing functions.
> **Evidence:** Procurement owns the contract, engineering owns the system, and
> finance owns the costs it can trace.
> **Consequence:** Each function manages one part, but no function manages the
> resource from purchase through business return.

Avoid leaving a claim, inserting a side point, and returning to the claim several
sentences later.

---

## 12. Prefer ordinary business language

Use the language managers already use when it is precise enough.

| Prefer | Avoid unless necessary |
| --- | --- |
| Buy | Procure an entitlement |
| Use | Consume capacity through utilization |
| Cost | Economic burden |
| Track | Instrument for observability |
| Requirement | Requirement specification construct |
| Divide responsibility | Fragment organizational ownership |
| Compare with the plan | Evaluate variance against expectations |
| Value created | Value realization outcome |
| Who decides | Allocation authority mechanism |

Technical language is appropriate when it adds precision. It should not be used to
make an ordinary idea sound specialized.

---

## 13. Be precise about cause and effect

Do not present a sequence of events as proof of causation. Do not use "therefore"
unless the conclusion genuinely follows from what came before it.

Prefer:

> As more employees and workflows use the system, total consumption usually rises.
> If the provider charges for that consumption, total cost rises as well.

Avoid:

> Successful AI automatically creates uncontrollable costs.

Use qualifying words deliberately:

- **Usually** for a common pattern with exceptions
- **Can** for a real possibility
- **Often** for a recurring but non-universal condition
- **Requires** only when something is necessary
- **Causes** only when the causal relationship is established

**THIS IS NOT HEDGING, AND THE DISTINCTION IS RULED.** The standing rule against
hedging bans evasion about the book's own position: "perhaps", "some argue", "one
might say", "it could be argued". Those signal that a citation, a formalization or
a cut was skipped. Qualifying the SCOPE of an empirical claim accurately is the
opposite act: it is the claim being stated correctly. "Usage usually rises with
headcount" is precise. "Some argue that usage rises" is hedging. The first is
required by this section; the second remains forbidden.

---

## 14. Preserve force without rhetorical excess

The voice may reach firm conclusions, but those conclusions should be earned by the
explanation.

Effective:

> If an organization cannot answer these questions, it is not managing the
> resource. It is simply receiving invoices and paying them.

The ending works because the paragraph has already shown what management requires.
The final sentence compresses the argument instead of decorating it.

Use short concluding sentences for emphasis. Use them sparingly.

---

## 15. Sentence and rhythm guidelines

- Use mostly sentences of 12 to 24 words.
- Use a short sentence after a longer explanation to state the consequence.
- Keep the subject near the beginning of the sentence.
- Keep the verb close to the subject.
- Prefer periods over semicolons when the ideas can stand independently.
- Use colons to introduce questions, examples, or consequences.
- Use parentheses rarely. If information matters, it usually deserves a full
  sentence.
- Avoid strings of abstract nouns such as "the allocation of consumption
  accountability."
- Use parallel structure when presenting comparable actions.

Good rhythm:

> Procurement negotiates the contract. Engineering tracks the systems it operates.
> Finance allocates the costs it can trace. Each function manages one part of AI
> usage, but none manages it from purchase through business return.

**The interrupter rules, absorbed from the retired guide because they are the
sharpest statement of "keep the verb close to the subject" this project has.** An
interrupter is material inserted into the middle of a clause and fenced by a pair
of commas. One is graceful. A run of them is the texture that reads as fussy even
when every comma is correct.

1. **Never separate a subject from its verb by more than about three words.**
   "Cloud financial management, known as FinOps, has turned" is fine. "An
   organization that runs its own vector store, the database holding the material
   available for retrieval, meters that step" is not: the verb arrives eleven words
   after its subject.
2. **Never stack two interrupters in one sentence.** Split it into two sentences,
   each carrying one.
3. **Prefer the right-branching alternative.** Move the aside to the end, or give
   it its own sentence. "Every request is counted in tokens. Tokens are the small
   units a model reads and writes" carries the same information with no suspension.

**A sentence carrying more than about three commas is usually two sentences wearing
one coat.** Read it aloud. If the subject is lost by the time the verb arrives,
split it.

---

## 16. Paragraph length and structure

Aim for paragraphs of three to six sentences. A paragraph may be shorter when
delivering an important conclusion or transition.

Break a paragraph when:

- The subject changes
- The writing moves from example to conclusion
- The writing moves from a familiar business practice to its AI equivalent
- A list of questions or practices needs to be scanned
- The reader has received enough information to pause and absorb the point

Do not keep related material in one large paragraph merely because it belongs to the
same section.

---

## 17. Lists and tables

Use a numbered list when the number and order of management questions matter. Use
bullets when the items are related but unordered. Use a table when the reader must
compare exact roles, practices, or concepts.

Introduce every list with a sentence explaining why the list matters.

Good:

> To manage AI consumption, leaders must be able to answer five questions:

Then present the five questions.

Avoid lists that merely repeat the surrounding prose.

---

## 18. Transitions

Transitions should show the logical relationship between ideas.

Useful transitions include:

- **To see why, consider...** for an example
- **The same logic applies to AI.** for transferring an analogy
- **The problem is not... It is...** for correcting a likely misunderstanding
- **As a result...** for a direct consequence
- **In practice...** for moving from principle to operation
- **This distinction matters because...** for explaining relevance

Avoid ceremonial transitions such as "It is worth stating precisely" unless
precision itself is the subject.

**THE BAN ON PROSE SIGNPOSTING DOES NOT BAN THESE, AND THE OLD WORDING LET A
DRAFTER THINK IT DID.** Signposting is telling the reader what the chapter is about
to say before saying it: "in this section we will see", "having established X, we
now turn to Y". That remains forbidden, because the six-slot skeleton does the
structural work. A transition that carries the argument one step is not signposting,
it is the connective tissue without which paragraphs read as a list of assertions.
The test: does the transition move the argument, or does it announce a move?

---

## 19. What to avoid

### Abstract openings

Avoid beginning with "the nature of," "the shape of," "the category of," or "the
discipline of" when a direct business statement is available.

### Fragmented questions posed as prose

Avoid:

> What is being bought, and against what requirement. Where the resource actually
> went. Who decides when there is not enough.

Write complete questions or complete declarative sentences.

### Hidden actors

Avoid saying "decisions are made" when the important issue is who has authority to
make them.

### Unexplained conceptual labels

Do not introduce terms such as "consumption event," "allocation logic," or
"economic observability" without immediately connecting them to a recognizable
action.

### Excessive compression

Do not remove the steps that allow the reader to understand why a conclusion
follows. Clarity is more important than brevity.

### False sophistication

Avoid replacing an ordinary word with a more abstract one unless the abstract term
adds a real distinction.

### LinkedIn-style rhetoric

Avoid staccato fragments, manufactured suspense, inflated declarations, and lines
designed mainly to sound quotable.

### The aphorism that replaces an explanation

Added from the rejected draft, where it was the signature move. "A horizontal line
does not become an accumulating one" and "that assumption is a bet" are compressed,
quotable, and they do the reader's thinking somewhere the reader cannot see. An
aphorism is earned only after the mechanism is on the page, and section 14 is where
it belongs.

---

## 20. Person, and what the book is not neutral about

**Third person throughout body prose.** Second person is permitted sparingly in
craft sections and in discussion questions. First person appears only inside voiced
material: dialogue in cases, model answers, and the constructed-reply type of
artifact. `voicecheck.py` enforces this mechanically.

**The book is not neutral about its argument, and it is completely neutral about
individual actors.** This is what survives of the retired register rule, and it
survives because it is about the argument rather than about the altitude of the
sentences. Provider behaviour is derived from the economics, never scolded. A buyer
who bought AI as software is not sneered at; the prose explains why the mental model
was legible and where it breaks. **The force comes from the explanation being right,
not from the prose sounding weighty.**

---

## 21. The mechanical rules

Non-negotiable, and most are enforced by `voicecheck.py` or by a build gate.

- **No em dashes anywhere**, including every file in this repository and every
  commit message. Rewrite with commas, colons, periods, parentheses, or restructure.
  Print gate 2 fails the build on any em dash or en dash; a number range therefore
  sets with a hyphen.
- **No contractions** in body prose. Permitted in dialogue inside cases and in
  discussion questions where they serve the register.
- **No exclamation points.**
- **No rhetorical questions** in body prose. Genuine management questions set in a
  list are permitted, per section 7.
- **No hedging**, as distinguished from accurate qualification in section 13.
- **No comma splices and no run-on sentences.**
- **Typographic quotation marks and apostrophes**, never straight ones. Print gate
  15 fails the build otherwise.
- **`lang="en-US"`**, never `lang="en"`, and `.nb` on proper nouns. Decisions 59
  and 58.

---

## 22. The fifty-year rule

Body prose is written to outlive its examples. Perishable specifics, prices, tier
names, usage limits, market shares, and company positions are quarantined inside
dated cases and never appear in timeless body prose. A dated case carries its date
in a provenance line. The body prose it feeds states only what remains true when the
prices have changed.

This constrains section 4's demand for something concrete to picture: the concrete
particular lives in cases, worked examples and craft artifacts, and body prose
carries the mechanism that survives them.

---

## 23. Revision method

Revise each passage in five passes.

**Pass 1: Find the actual claim.** Write the paragraph's main point in one plain
sentence. Place that sentence first or very near the beginning.

**Pass 2: Identify the actors.** Name the department, manager, employee, provider,
product, or workflow performing each important action.

**Pass 3: Make the mechanism visible.** Explain what happens in operational order:
purchase, use, measurement, allocation, and return.

**Pass 4: Remove unnecessary abstraction.** Replace conceptual phrases with ordinary
business language. Retain technical terms only when they provide needed precision.

**Pass 5: Test the logic.** Ask whether each conclusion follows from the sentences
before it. Add a missing step when necessary. Remove a transition that claims more
certainty than the evidence supports.

---

## 24. Before and after, from Dan's guide

### Before

> Yet no assembled discipline governs it, and the reason is worth stating
> precisely, because it is not indifference. Each of the five questions falls
> inside the scope of some practice the organization already has.

### After

> Most organizations do not manage AI usage through a single, coordinated
> discipline. This is not because no one is paying attention. It is because
> responsibility is divided across several existing functions.

### Why the revision works

- It states the conclusion first.
- It replaces "assembled discipline" with a familiar phrase.
- It separates the claim, correction, and explanation.
- It prepares the reader for the departments named next.

---

## 25. Before and after, from this book

**Both passages are real.** The BEFORE is Chapter 1's Stage 0 draft as it stood on
2026-08-07, before the copy edit. The AFTER is the same passage in the locked
chapter today. Nothing here is invented, and the pair is the clearest statement of
what this standard is for.

### 25.1 The coined term arriving before its mechanism

**Before:**

> The objection is not confused, and the answer is not that the buyer is billed by
> the token after all. The answer is meter relocation: a flat rate moves the meter,
> it does not abolish it. When a provider offers a flat price for a metered
> resource, the provider does not stop metering.

**After:**

> The objection is valid. A buyer who pays a flat monthly price is not secretly
> being billed by the token. But this does not mean that the underlying resource is
> unmetered. Flat pricing relocates the meter from the buyer to the provider. It
> does not abolish it. This is meter relocation.

**What changed.** The before opens with a double negative about the reader's
objection and hands over the coined term as "the answer", four words in, before the
reader has seen anything happen. The after concedes plainly, states the mechanism in
ordinary words, and names the term LAST, once there is something for the name to
attach to. That is section 8 and section 19's unexplained-conceptual-labels rule
working together. Sentence length falls from a mean near 24 words to near 12.

### 25.2 The aphorism standing in for the explanation

**Before:**

> The seat model and the event model are not two views of the same economics. They
> are two different economics, and Figure 1.2 draws the difference the invoice
> hides. A horizontal line does not become an accumulating one.

**After:**

> The seat model and the event model do not describe the same cost in different
> ways. They describe two different cost structures. The seat model is the software
> access model defined in 1.1. The event model is the resource consumption model,
> in which each use is a metered consumption event.

**What changed.** "Two different economics" is a phrase a reader must decode;
"two different cost structures" is one they already own. The geometric aphorism is
cut and replaced with the two definitions the sentence was gesturing at. The after
is longer, and that is correct: section 19 ranks clarity above brevity.

---

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

## 27. Mechanical proxies, and the band

`voicecheck.py` prints advisory craft metrics beside the mechanical bans. They are
proxies, permanently advisory, and never a pass-or-fail threshold. C2 and C7 have no
proxy and are enforced by reading alone.

**The band comes from the locked Chapter 1, which is the book's own exemplar of this
voice.** As measured on 2026-08-19: mean sentence length 14.3 words, median 14,
standard deviation 6.1, 36 per cent of sentences under 12 words, none over 35, and
the longest uniform run 5 sentences within 4 words of each other. That sits inside
the 12 to 24 band section 15 prescribes and confirms it against real prose rather
than against a preference.

**One proxy is defective and its numbers must not be quoted.** The Part 5 rule 1
proxy counts fronted adverbial phrases as subject-verb separations, and a fronted
adverbial is right-branching and permitted. The sound measure beside it, long
comma-fenced asides, does work.

---

## 28. Reusable prompt for drafting or revision

> Write in Concrete Management Prose for an MBA-level textbook on AI management.
> Make the argument direct, concrete, and easy to follow. Begin each paragraph with
> its main business claim. Use visible actors and active verbs. Explain unfamiliar
> AI concepts through familiar operating practices, decisions, costs, and
> consequences. Keep one main idea per sentence and build the reasoning in a
> straight line. Translate abstractions into questions a manager could answer.
> Preserve intellectual seriousness, but avoid academic phrasing, unexplained
> jargon, rhetorical flourishes, and LinkedIn-style fragments. End important
> passages with a concise conclusion that follows directly from the explanation.

---

## 29. Final editing checklist

Before approving a passage, ask:

- Is the main claim visible in the first one or two sentences?
- Can the reader identify who is acting?
- Are the actions concrete enough to picture inside a real organization?
- Does each sentence contain one main idea?
- Does each sentence follow logically from the previous one?
- Are technical terms defined through business meaning?
- Does every coined term arrive after the mechanism it names?
- Could an abstract statement become a management question?
- Does the analogy transfer a real structure rather than merely add color?
- Are qualifications such as "usually," "can," and "requires" used accurately?
- Has unnecessary jargon been replaced with ordinary business language?
- Is the conclusion earned by the explanation?
- Could an MBA reader understand the passage on the first read?

---

## 30. The voice in one sentence

**Explain AI management by showing what an organization buys, who uses it, how it is
measured, who decides, what it costs, and what value it returns.**

---

## 31. The four conflicts this standard resolves

Recorded because this repository's recurring failure is two documents that disagree
silently, and because each of these was a live contradiction on `main` before today.

1. **Register.** "Magisterial" is retired as the named register. What survives is
   section 20: not neutral about the argument, completely neutral about actors.
2. **Transitions.** The ban on prose signposting stands and is narrowed in section
   18 so it no longer reads as a ban on connective tissue.
3. **Hedging.** Section 13 distinguishes accurate qualification, which is required,
   from evasion about the book's position, which stays forbidden.
4. **Exemplars.** The four journalism exemplars are retired as models for the
   voice. They taught texture, and this book needs managerial clarity. What they
   contributed survives inside C1 through C6. **The exemplar of this voice is the
   locked Chapter 1.**

---

## 32. Relationship to the other documents

- `AIOM_Prose_Style_Guide_v1.md` and `AIOM_Voice_and_Craft_v1.md` are RETIRED to
  pointers at this file.
- CLAUDE.md section 2 states the rules that bite and points here. This file is
  authoritative on prose.
- `AIOM_Consolidated_Spec_v1.md` B.2 still duplicates the register rules and is a
  known, booked duplication.
- The Structure document, the exit competencies and the maturity model are
  unaffected: this standard governs how sentences are written, never what the book
  argues.

---

## Changelog

- **v2.0, 2026-08-19.** Adopted as Decision 71. Consolidates Dan's Concrete
  Management Prose guide with the surviving material from the two retired v1 files.
  Retires the magisterial register, adds C7, restates C3 and C6, resolves the four
  conflicts in section 31, and replaces the invented worked examples with real
  before-and-after pairs from Chapter 1.
