# AIOM Prose Style Guide

Version 1.6. Status: active. Scope, the section 2.4 vocabulary policy, and the
Part 6 slot-located voice model all ruled by Dan on 2026-08-05. Owner: Dan.
Drafter: Claude.

**ADOPTED ONTO `main` 2026-08-12, ON DAN'S RULING, AFTER A WEEK STRANDED.** This
guide was written on 2026-08-05 and pushed to `claude/chapter-1-prose-style-x0bzze`,
which was never merged. Nothing referenced it and no session read it. In that week
Chapter 1 went through a developmental edit, a fact check, a voice pass, a design
review, a production gate and two copy-edit rounds, none of which had access to
it. See the changelog entry for v1.6 for what that cost.

**THIS GUIDE AND `AIOM_Voice_and_Craft_v1.md` DIVIDE THE VOICE STANDARD. READ
THIS PARAGRAPH BEFORE ASSUMING EITHER GOVERNS ALONE.** Both were adopted
2026-08-05 by sessions that could not see each other, both name the same four
exemplars, and neither originally mentioned the other. The division ruled on
2026-08-12:

- **`AIOM_Voice_and_Craft_v1.md` governs the craft criteria C1 to C6**, the
  exemplars, and the guard. It is what Stage 4 grades against and what
  `status_check.py` enforces through the Stage 4 sub-checkboxes.
- **This guide governs everything else about prose**: the reader model, altitude
  and contextualization, the mechanical rules, sentence-level craft, the drafting
  protocol, and the house style sheet.
- **Part 6 of this guide is retired to a pointer**, because it duplicated the
  other file. Nothing in Part 6 is lost; it lives there now.
- **CLAUDE.md section 2 remains the authority for the standing prohibitions.**
  Part 3 and Part 4 below are their operative expansion and repeal none of them.

Where this guide and any older prose note disagree, this guide governs, with the
one exception above. Read it before drafting or editing any body prose. It is
long on purpose. The gap it closes is the gap that failed the Chapter 1 copy
edit, and that gap cannot be closed by a rule short enough to forget.

---

## 0. Why this guide exists

Chapter 1 passed the voice check, passed the structural gate, passed the
production gate, and then failed the copy edit. It failed for a reason the earlier
gates were not built to catch. The prose was written toward someone who already
holds the whole argument. It reads as elegant to a reader who already agrees and
as a locked door to the reader the book is actually for.

The cause is structural, not a lapse of care. The voice specification that
governed the draft is almost entirely correct and almost entirely negative. Its
instruction on the reader is four prohibitions: the book does not condescend, does
not repeat itself for reassurance, does not tell the reader what the chapter is
about to say, and does not pad. Every one of those is right. Together they tell
the drafter what to remove. None of them tells the drafter what to supply.

A drafter who satisfies four prohibitions and has no positive target produces
prose that is maximally compressed and maximally assuming, because compression and
assumption are what removing things gets you. Drafting toward Dan makes this worse,
because Dan holds every concept in the book already, so no term ever looks
unplaced from where he sits. The result satisfies every negative rule and still
fails, because the obligation to teach was never written down.

This guide writes it down. Its spine is one instruction, and every section below
is a consequence of it:

> Write to the reader in the chair, not to the author over your shoulder.

---

## 1. The reader

The book has one primary reader. Everything about altitude, contextualization, and
pacing follows from getting this person exactly right and then never drafting for
anyone else.

### 1.1 Who the reader is

An MBA-level graduate business student. Intelligent, busy, and sceptical. Has read
business books before and can tell when one is padded. Can read a case, a table,
and a simple figure without help. Understands how organizations buy software, how
budgets and margins work, and what an operations discipline is for. Is not
impressed by fluency and is offended by being talked down to.

The secondary reader is the practicing executive who must translate the discipline
into decisions. The book must be readable in that seat with material effect.

The reader is not an ML engineer, a prompt engineer, an AI strategist, or a
compliance specialist. The book stays out of those territories by design, and it
must not assume their knowledge either.

### 1.2 What the reader knows, and what the reader does not

This inventory is the working tool. Before a term carries argumentative weight,
find it in one of the two columns. If it is in the second column, it must be placed
before it is used as a premise.

The reader reliably **knows**:

- How enterprise software is bought, licensed, and managed: seats, per-seat
  pricing, procurement, renewals, license utilization.
- Managerial finance and accounting at the graduate level: fixed and marginal
  cost, margin, budget, variance, allocation, chargeback.
- Operations and supply-chain concepts in general form: a flow, a process, sourcing,
  planning, capacity, accountability.
- AI assistants at the level of a user: that ChatGPT exists, that coding assistants
  and support chatbots exist, that they take a prompt and return an answer.
- How to read a business case, a simple exhibit, and a two-panel figure.

The reader does **not** reliably know:

- What a token is, or that AI models are metered and billed per token.
- What "the API" is, or what an "API rate" or "usage-based billing" means in this
  setting.
- What "frontier model," "inference," "context window," "retrieval," or
  "long-horizon task" mean.
- The named models and vendors as anything but headlines. "Sonnet," "Opus,"
  "Cursor," "Copilot," "Anysphere" are not self-explanatory and carry no economics
  on their own.
- That deployed AI has a variable marginal cost at all. This is the book's central
  claim. It cannot be assumed anywhere, least of all in Chapter 1, whose job is to
  install it.
- Any of the book's coined vocabulary. That is what the definitional callouts are
  for, and they are the one place the book is allowed to define on introduction.

The second column is not a sign of a weak reader. It is the ordinary knowledge
boundary of an excellent generalist who has not spent the last three years inside
AI billing. Respecting that boundary is not condescension. It is the job.

### 1.3 The expert-reader trap

The author is the worst available proxy for the reader, because the author holds
everything the reader lacks. Prose that feels complete to the author is the prose
most likely to have skipped the reader's on-ramps, precisely because those on-ramps
are invisible to someone who does not need them.

The discipline, then, is to simulate the reader deliberately and against instinct.
When a sentence feels obvious, that is the signal to check whether it is obvious
only because you already hold the term it rests on. The drafter's fluency is not
evidence that the reader is being carried. It is often evidence that the reader has
been left behind at a term three sentences back.

### 1.4 Contextualize versus condescend: the line the old spec left implicit

The apparent conflict is between "the book does not condescend" and "the book must
place its terms." The conflict dissolves once the line is drawn precisely, and this
guide draws it:

- **Contextualizing** a term means placing it once, on first load-bearing use, in
  the sentence that needs it, in a form so light that the reader who already knows
  the term is not slowed by a single beat. It adds information the reader may lack.
- **Condescending** means re-explaining what you already placed, flattering the
  reader that the material is easy, telling the reader what they are about to
  learn, or defining a term the reader plainly owns already.

Placing "token" once, as the unit a model is billed in, is contextualizing.
Explaining twice, or prefacing it with "as everyone knows" or "simply put," is
condescending. The reader who owns the term glides over a good placement without
friction. The reader who does not is saved. A good placement costs the first reader
nothing and gives the second reader everything, which is exactly why it is not
condescension.

---

## 2. Altitude and contextualization

This is the craft layer the old specification lacked. It is the positive
counterpart to the prohibitions, and it is what the Chapter 1 redraft must satisfy.

### 2.1 Earned altitude

The magisterial register is the altitude the prose should *reach*, not the altitude
it should *start* at. Magisterial is a summit. A textbook carries the reader up to
the summit; it does not begin by speaking from it to a reader still standing at the
bottom.

Every teaching movement has the same shape. Land the reader on familiar ground.
Walk them up one step at a time, placing each new term as a stair. Only once they
stand at height do you speak from height. The finished paragraph can read as
magisterial. The reader arrived at that reading; they were not dropped into it.

The failure mode is starting at the summit. Section 1.1 of the current draft opens
"The buyer brought a model to the transaction" and argues upward from marginal
cost. That is summit prose delivered to a reader who has not yet climbed. The words
are correct and the reader is not with them.

### 2.2 Ground before build

A term that will carry argumentative weight must be given to the reader before it
is used as a premise. You may not build an inference on a word the reader does not
yet hold.

This is distinct from the definitional callouts, which handle the book's *coined*
terms. Ground-before-build governs the *inherited* vocabulary in the second column
of the 1.2 inventory: the words the book borrows from the AI world and immediately
makes load-bearing. Those words get no callout, so they must be placed in the prose
itself, lightly, the first time they carry weight.

### 2.3 Intuition before formalism

The concrete instance comes before the abstraction it licenses. The reader meets a
thing they can picture, and only then meets the category it belongs to. The
abstraction, arriving second, has something to attach to.

Chapter 1 already contains the model of this done right, in Section 1.4. The
manufacturer and its steel arrive first, fully concrete: a plant, a material,
tonnage, a plan, a place the material goes. Only after the reader can see the steel
does the prose lift to the general claim that these are the questions any
organization must answer about anything that flows through it and costs money. That
passage teaches. It is the target. Hold every other passage to it.

The inversion, formalism before intuition, is the summit failure again. It asserts
the category to a reader who has not yet been given the instance, and asks them to
trust a generalization they have no picture for.

### 2.4 The inherited-vocabulary policy

Ruled 2026-08-05: **in-line placement on first load-bearing use.** This is the
book's standing policy for the inherited technical vocabulary across all fifteen
chapters. It has one rule and one piece of bookkeeping that the rule requires.

**The rule.** Each inherited term from the 1.2 second column is placed the first
time it carries weight in the book, at the point of need, never as a glossary aside
and never as a callout. The placement states what the term is in words the reader
already owns. After the first placement, the term is used freely and never
re-explained, in that chapter or any later one.

**The form the placement takes, and a correction issued in v1.5.** This rule
originally directed the drafter to place the term "as an appositive or a short
clause" inside the sentence that needs it. Applied at scale that instruction
manufactured a defect: a chapter full of nonrestrictive appositives is a chapter of
center-branching sentences, and Chapter 1 came back from its copy edit reading as
fussy and over-punctuated for exactly that reason. Placement and interruption are
not the same requirement, and the guide had conflated them. The corrected order of
preference is:

1. **Its own short sentence,** when the host sentence is doing argumentative work.
   "Every request a model answers is counted in tokens. Tokens are the small units
   of text a model reads and writes on its way to an answer."
2. **A trailing clause** at the end of the host sentence, which branches right and
   suspends nothing.
3. **A brief appositive of three words or so,** and only when the host sentence is
   quiet. "Cloud financial management, known as FinOps, has turned."

A placement must never separate a subject from its verb by more than about three
words, and two placements never appear in one sentence. Section 5 states the
general form of that rule.

**The bookkeeping the rule requires.** Because a term is placed once in the book,
not once per chapter, the drafter has to know whether a given term was already
placed in an earlier chapter. That knowledge is kept in a running placed-vocabulary
ledger on the process side, outside the prose: which inherited terms have been
placed, and in which chapter. Chapter 6 does not re-place "token," because the
ledger shows Chapter 1 already did. The ledger is lightweight and grows as chapters
are drafted; it is the mechanism that keeps ground-before-build from colliding with
the no-repetition rule, not a second policy. It is started when Chapter 1 is
redrafted and the first terms are placed.

The ruling rejects the alternative of an assumed-read front-matter primer that
defines the vocabulary up front. A primer reintroduces the trap: it licenses the
drafter to assume knowledge the reader may have skipped, and a primer about tokens
and models is perishable in a book whose body prose is built to outlive its
examples. In-line placement puts the term where the reader needs it, at the moment
of need, and costs the knowing reader nothing.

The candidate inherited terms Chapter 1 must place include, at minimum: token,
model (as the metered thing, not the mental model), API rate, usage-based or
consumption billing, frontier or most-capable model, retrieval, and long-horizon or
agentic task. The named vendors and products (Cursor, Copilot, Anysphere, and the
model names) are placed by role on first mention, so the reader knows what kind of
thing each one is before the episode turns on it.

### 2.5 Cognitive load and pacing

One new idea per sentence, when the idea is new. A sentence may carry several ideas
the reader already holds, but it may introduce only one the reader does not.
Stacking unplaced terms is the most common altitude failure in the current draft.

The clearest instance: "the newest models consumed far more tokens per request on
long-horizon tasks than the flat price had been built to absorb." That single
clause introduces three concepts the reader may not hold, "tokens," "tokens per
request" as a cost measure, and "long-horizon tasks," and rests the whole payoff on
all three at once. The fix is not to shorten the sentence. It is to place "token"
earlier, as the unit of consumption, so that by the time this sentence arrives it is
carrying one new idea, the cost asymmetry, on top of ground already laid.

Pacing follows from the same principle. When the idea is hard, the sentences get
shorter and the steps get smaller. When the ground is familiar, the prose can move.
Uniform sentence length across easy and hard passages is a sign the drafter is not
feeling the reader's load.

### 2.6 Worked before and after

These pairs are illustrative of the altitude standard. They are not a fact-checked
redraft; the "after" text abstracts lightly to show the move, and the real Stage 6
redraft will be sourced and checked in the ordinary way. What each pair
demonstrates is the altitude fix, not the final wording.

**Pair A. Inherited vocabulary, from the opening case.**

Before:

> Cursor revised its Pro plan so that the previous monthly allotment of five hundred
> requests against external models, with Sonnet models counting as two, became a
> twenty-dollar monthly pool of frontier-model usage billed at the underlying API
> rates.

The reader who does not know what an API rate is, or why a Sonnet model counts as
two, loses the sentence, and this is the sentence the whole opening case turns on.

After, illustrating placement:

> Cursor changed the plan underneath them. The old plan had given each user a fixed
> monthly allowance of requests to the outside AI models it drew on, with the most
> capable models drawing that allowance down faster. The new plan replaced the
> allowance with a small fixed budget, and once a user spent it, further use was
> billed at what the models actually cost to run, the same per-use rate the company
> itself paid to call them.

Every load-bearing term is now placed in words the reader already owns, and the
sentence that carries the argument no longer rests on vocabulary the reader lacks.

**Pair B. Term-stacking, from the case's explanation.**

Before:

> the newest models consumed far more tokens per request on long-horizon tasks than
> the flat price had been built to absorb

After, once "token" has been placed earlier as the billed unit of consumption:

> the newest models consumed far more of that metered resource on the longest tasks
> than the flat price had been built to absorb

The cost asymmetry, which is the one idea this sentence exists to deliver, now
arrives on ground already laid instead of on three unplaced terms at once.

**Pair C. The positive exemplar already in the chapter.**

The Section 1.4 steel passage needs no rewrite. It lands the concrete instance
first, walks the reader up one practice at a time, and only then states the general
claim. It is what the rest of the chapter should sound like. Cited here so the
standard is a passage the book already contains, not an outside ideal.

---

## 3. Register and voice

Absorbed from Consolidated Spec B.2 and authoritative here.

### 3.1 Register

Magisterial, with combative energy transmuted into cold economic analysis. The book
is not neutral about its argument. Its neutrality about individual actors is
complete. It does not scold providers; it derives their behavior from the economics.
It does not sneer at buyers who bought AI as software; it explains why the mental
model was legible and where it breaks. The manifesto's taunting register is out. The
force of the argument comes from the argument, not from the voice.

Register is the altitude the prose reaches, per section 2.1, not the altitude it
starts at. A magisterial book that never carries the reader up is just a book that
assumes its reader. Both obligations bind at once: reach the summit, and bring the
reader to it.

### 3.2 Person

Third person throughout body prose. Second person is permitted sparingly in craft
sections ("the reader can now") and in discussion questions. First person appears
only inside voiced material: dialogue in cases, model answers, and the CIO-memo type
of constructed reply.

### 3.3 Not neutral about the argument

The prose argues. It does not hedge toward balance it does not believe. Provider
behavior is derived, not condemned; buyer error is explained, not mocked. The
combative energy is real and it is spent on the argument, never on a person or a
company.

### 3.4 No decorative apparatus, no prose signposting

Signposting is done through the fixed six-slot skeleton, not through prose. The
prose does not tell the reader what the chapter is about to say before saying it,
does not recap what it just said for reassurance, and carries no ornamental
transitions that announce structure. This rule and the ground-before-build rule do
not conflict: placing a term the reader needs is supplying information, not
signposting; announcing "in this section we will see" is signposting. The first is
required, the second is banned.

### 3.5 The fifty-year rule

Body prose is written to outlive its examples. Perishable specifics, prices, tier
names, usage limits, market shares, and company positions, are quarantined inside
dated cases and never appear in timeless body prose. A dated case carries its date
in a provenance line; the body prose it feeds states only what remains true when the
prices have changed.

---

## 4. The mechanical rules

Absorbed from B.2 and from `voicecheck.py`, which is the mechanical gate for the
first four. These are hard rules. The gate fails the build on the dash rules, and
the others are checked on every voice pass.

- **No em dashes. Anywhere.** Body prose, cases, craft sections, summaries, key
  terms, discussion questions, problems, back matter, and every file in this repo
  including commit messages and this guide. Rewrite with commas, colons, periods,
  parentheses, or restructure the sentence. In built chapters the gate is stricter
  still and also fails en dashes, so avoid both. This is the single most-violated
  rule under stress; it is violated exactly when the prose is working hardest, which
  is when the drafter must watch for it most.
- **No contractions in body prose.** Contractions are permitted only inside voiced
  material: dialogue in cases, model answers, and discussion questions where they
  serve the register.
- **No exclamation points.** Anywhere.
- **No rhetorical questions in body prose.** Questions are permitted in discussion
  questions, which is what they are for, and nowhere else in the running text.
- **No hedging.** No "perhaps," no "some argue," no "one might say," no "it could be
  argued." Hedging is a signal that a claim was not cited, not formalized as a
  conditional, and not cut, which are the only three things the evidence policy
  allows. If a sentence wants to hedge, one of those three was skipped; do that
  instead.
- **No comma splices, and no run-on (fused) sentences.** Two independent clauses,
  each able to stand as its own sentence, are joined by a period, a semicolon, or a
  comma followed by a coordinating conjunction (and, but, or, nor, for, so, yet).
  They are never joined by a comma alone (a comma splice) and never by nothing (a
  fused sentence). A series of three or more independent clauses takes semicolons or
  full stops, not commas. This is the grammatical error the accumulation sentence
  invites: a run of short independent clauses spliced with commas reads as momentum
  to the drafter and as an error to the reader. This rule is not yet fully
  machine-checkable, so it is enforced on the reader-simulation pass and the copy
  edit; treat it with the same weight as the gated rules above.

Voiced material, where the person and contraction rules relax, is marked in the
HTML by a block class (`model`, `dq`, `problem`) or by enclosing quotation marks.
`voicecheck.py` keys on those markers, so anything voiced must carry the marker or
the gate will flag it.

---

## 5. Sentence-level craft

These serve the altitude layer. They are the sentence mechanics that carry a reader
who does not already agree.

- **Vary sentence length with load.** Short sentences land ideas; long sentences
  develop them. A hard new idea gets a short sentence so it lands before the next
  one arrives. The current draft runs long and periodic throughout, which reads as
  confident and teaches slowly, because a new idea buried mid-clause in a long
  sentence does not land.
- **Name the thing.** Prefer the concrete noun to the abstraction, the instance to
  the category, on first exposure. "Five thousand agents drafting replies" before
  "the deployment's usage surface."
- **Keep the actor in the sentence.** Avoid nominalizations that hide who does what.
  "The provider re-indexes the price" teaches; "a re-indexing of the price occurs"
  hides the actor whose choice is the whole point.
- **Make transitions carry, not announce.** A transition earns its place by moving
  the argument one step, not by labeling the step. "The correction was the same"
  carries; "now let us turn to the correction" announces.
- **One clause, one job.** When a sentence is doing argumentative work, do not also
  make it introduce vocabulary. Place the term in an earlier, quieter sentence so
  the working sentence can work.
- **Place terms without stacking appositives.** The inline-placement policy (2.4)
  tempts the drafter to drop an appositive ("tokens, the units a model is billed by")
  into a sentence already carrying an argument, and a second appositive after it, and
  the commas pile up until the clause boundaries blur. When the host sentence is
  working, give the term its own short sentence, or set the gloss in parentheses,
  rather than threading a third and fourth comma through the line. Two clean
  sentences beat one that placement has overloaded.
- **Watch the comma count.** A sentence carrying more than about three commas is
  usually two sentences wearing one coat, or an appositive that wants parentheses or
  a full stop. Read it aloud. If the subject is lost by the time the verb arrives, or
  the breath runs out, split it. This is the same discipline as the no-splice rule in
  section 4, approached from the reader's ear rather than the grammar.
- **Ration the parenthetical interrupter.** An interrupter is material inserted into
  the middle of a clause and fenced off by a pair of commas, most often a
  nonrestrictive appositive ("tokens, the units a model is billed by, are") or a
  nonrestrictive relative clause ("the API rate, which is the metered price of
  calling a model directly, applies"). The result is a center-branching sentence:
  the reader must hold the opening of the clause in memory while the aside runs, and
  then resume. One such sentence is graceful. A run of them is the texture that
  reads as fussy and over-punctuated even when every comma is correct.
  Three rules, in order of strictness:
  1. **Never separate a subject from its verb by more than about three words.**
     "Cloud financial management, known as FinOps, has turned" is fine.
     "An organization that runs its own vector store, the database holding the
     material available for retrieval, meters that step" is not: the verb arrives
     eleven words after its subject and the sentence has to be re-read.
  2. **Never stack two interrupters in one sentence.** "the chief executive of
     Anysphere, the company behind Cursor, Michael Truell, published" makes the
     reader traverse three appositives before reaching a verb. Split it into two
     sentences, each carrying one.
  3. **Prefer the right-branching alternative.** Move the aside to the end of the
     sentence, or give it a sentence of its own. "Every request is counted in
     tokens. Tokens are the small units a model reads and writes" carries the same
     information with no suspension at all.

---

## 6. Narrative and explanatory craft: RETIRED TO A POINTER

**This part is now `AIOM_Voice_and_Craft_v1.md`. Read it there.**

Part 6 originally carried the four touchstones (Michael Lewis, James Lardner, the
Financial Times, the New Yorker), the guard that keeps their registers out, and
the slot-located voice model: narrative craft in the cases, explanatory craft in
the teaching body, register discipline governing both. Dan ruled that model and
the case intensity on 2026-08-05.

On the same day, a concurrent session wrote `AIOM_Voice_and_Craft_v1.md` from the
same ruling and the same four exemplars. That file is the one that entered force:
CLAUDE.md cites it, Stage 4 grades against it, and `status_check.py` fails a
Stage 4 marked passed with one of its six criteria left open. It also carries
material this part never had, in particular the six criteria C1 to C6 and their
mechanical proxies.

Retiring this part to a pointer, rather than keeping both, was ruled on
2026-08-12. Two documents claiming authority over the same subject is the
condition that produced this duplication in the first place. **The slot-located
voice model and the case-intensity ruling are NOT repealed.** They are Dan's
rulings of 2026-08-05 and they stand; they are simply recorded in the other file.

---

## 7. The drafting and self-check protocol

### 7.1 Drafting

Draft with the 1.2 inventory open. Every time a term from the second column appears,
decide on the spot whether it has been placed yet in this book. If not, place it
here, lightly, and log it to the ledger. If it has, use it freely.

Draft each teaching movement ground-first: the instance before the category, the
familiar before the new, the stair before the height.

### 7.2 The reader-simulation pass

After drafting, read the passage once as the 1.2 reader, not as the author. Mark
every term from the second column that is used before it is placed. Mark every
sentence that introduces more than one new idea. Mark every paragraph that starts at
the summit. Each mark is a defect against this guide, and each has a named remedy
above.

This pass is the operational core of the guide. It is the deliberate simulation that
section 1.3 requires, run as a checklist rather than left to instinct, because
instinct is the author's instinct and the author is the wrong proxy.

### 7.3 Checklist

A passage satisfies this guide when:

1. No term from the 1.2 second column is used as a premise before it is placed.
2. Every teaching movement runs intuition before formalism.
3. No paragraph starts at the summit; each earns its altitude.
4. No sentence introduces more than one new idea.
5. Register, person, and the fifty-year rule hold (sections 3.1 to 3.5).
6. The mechanical rules hold (section 4): `voicecheck.py` is clean, and the prose
   carries no comma splices or run-on sentences (checked by eye until a linter
   exists).
7. Sentence length varies with load, actors stay in their sentences, and
   transitions carry rather than announce (section 5).
8. Voice is slot-correct (Part 6): the cases carry the narrative craft and the
   teaching body carries the explanatory three-layer move; no scene, character, or
   perishable specific has leaked into the timeless body; every narrative beat in a
   case also does analytical work; and no narrator personality, judgment, or
   hyperbole has entered anywhere.
9. The manuscript is publishable on its surface (Part 8): typographic quotes and
   apostrophes throughout, no rhetorical figure over its budget, no paragraph over
   roughly 150 words, reader-references confined to the craft section and summary,
   defined terms invariant across callout and key terms and body, and the apparatus
   ordered and cross-referenced consistently.

Items 5 and 6 are already gated. Items 1 through 4 and 7 through 9 are the new
standard, and they are what the Chapter 1 redraft must meet. Several are counting
problems rather than judgment problems (typography, figure budget, paragraph length,
reader-reference frequency, and an unplaced-term check against the ledger) and are
the first candidates for mechanization in `voicecheck.py`; until they are gated they
are checked by the reader-simulation pass and the copy edit.

### 7.4 Where this sits in the lifecycle

The altitude standard is a drafting and editing standard, so it binds at Stage 0
(draft), and it is verified at the voice check and again at the copy edit, the stage
where Chapter 1 failed. Reopening a chapter for altitude is a body-prose edit under
the scoped re-run matrix, so it re-runs the developmental edit, fact check, voice,
design, and the production gate, and leaves the structural gate intact unless a slot
moves. In practice, an altitude redraft that changes no empirical claim holds the
fact surface, exactly as the Chapter 1 developmental edit did.

---

## 8. Publishing readiness: the house style sheet

Parts 2 through 7 govern whether the prose teaches. This part governs whether the
manuscript is fit to set in type. The distinction matters because the two fail
independently: Chapter 1 reached a passing production build, a clean voice gate, and
a rebuilt altitude standard while still carrying defects that no university press
would set. Everything below was found by reading the redrafted Chapter 1 as an
acquiring editor would, and every rule states the count that produced it.

A founding text is judged on its surface before it is judged on its argument. These
rules are the surface.

### 8.1 Typography

The manuscript ships with typographic marks, not typewriter marks. This is the single
most visible signal of an unedited manuscript, and it is invisible on screen to the
person who wrote it.

- **Quotation marks and apostrophes are curly, always.** Use `’` for every
  apostrophe (`Cursor’s`, `the provider’s schedule`) and `“ ”` for quoted matter.
  Never the straight ASCII `'` or `"`. Chapter 1 as redrafted carried 26 straight
  apostrophes and 2 straight double quotes, and zero typographic marks of either
  kind. That is a production defect on every page.
- **Quoted matter takes American convention.** Double quotes outermost, single
  inside them, and terminal commas and periods sit inside the closing quote.
- **The apostrophe is never a prime.** A prime (`′`) is a unit mark, not a possessive.
- **Ellipses** use the ellipsis character with a space either side, not three periods.
- **No double spaces after a period,** anywhere, ever.
- **Numbers follow Chicago.** Spell out whole numbers one through one hundred and
  round numbers (five hundred requests, five thousand agents, twenty dollars). Use
  numerals for large or precise figures and for percentages (4.7 million, 75 percent).
  Percentages are written as "percent" in body prose, not with the sign.
- **Compounds are hyphenated before the noun and open after it,** and once a compound
  is set it never varies (per-seat price, priced per seat; long-horizon task).
- **Product and feature names take the owner's capitalization** on first use, then the
  book's generic phrasing thereafter. Do not silently lowercase a proper feature name.

Because em dashes are banned, their work is displaced onto other marks, and the
displacement is measurable: Chapter 1 carries 25 colons and 23 semicolons in a
19-page chapter. Both are correct punctuation and both become a tic in quantity.
When a colon is doing the job an em dash would have done, prefer a full stop and a
new sentence. The ban removes a mark; it does not license overworking the rest.

### 8.2 Rhetorical variation and the figure budget

A rhetorical figure used once is emphasis. Used a dozen times it is a mannerism, and
the reader begins to hear it coming, which drains the force from every instance
including the good ones.

The chapter's signature figure is the antithesis: a negation followed by the
correction, in the form "It is not X. It is Y." Chapter 1 as redrafted uses it
**twelve times**, including "was not an excuse. It was an account of arithmetic,"
"is not wrong about licensed software. It is wrong about," "did not fail. It was
applied to," and "What is absent is not attention. It is assembly." Each is well
made. Together they flatten every turn in the argument into one shape.

The rules:

1. **Budget.** No single rhetorical figure appears more than **three times in a
   chapter**. This applies to the antithesis above, to the tricolon, to anaphora
   (successive sentences opening on the same words), and to any other figure the
   drafter finds working.
2. **Reserved position.** The antithesis is spent at the chapter's genuine turning
   points, which are ordinarily the statement of the thesis, the answer to the
   objection, and the close. It is not spent to give a paragraph an ending.
3. **Vary the correction.** When a claim needs a contrast and the budget is gone,
   restructure: subordinate the negation ("Although the apparatus went on reporting
   faithfully, it reported a quantity that had stopped governing anything"), or state
   the positive alone and let the contrast be implied, or carry the contrast across
   two sentences without the parallel frame.

The figure is the book's best move. The budget exists to protect it.

### 8.3 Paragraph architecture

Chapter 1's teaching body runs 27 paragraphs at a mean of 92 words, with one
paragraph of 219 words carrying 13 sentences, and only nine paragraphs under 60
words. Uniform blocks read as relentless, and the outlier reads as a wall.

- **Ceiling.** No body paragraph exceeds roughly **150 words or eight sentences**.
  A paragraph past that is carrying more than one idea and should be split at its
  own hinge. The 219-word meter-relocation paragraph is the standing example: it
  states the mechanism, derives the instability, lists four instruments, and names
  the timing, which is three paragraphs wearing one coat.
- **Variation is required, not permitted.** A run of same-length paragraphs is a
  defect even when each is individually well made. Vary deliberately: a short
  paragraph after a long one lands the point the long one built.
- **Do not end every paragraph on a punch.** The short declarative close ("It is the
  central fact," "it is a blindfold," "It is assembly") is powerful and, used on
  every paragraph, becomes percussion the reader stops hearing. Let some paragraphs
  end quietly, on a qualifying clause or on the ordinary last step of the argument.
  Reserve the punch for the paragraphs that have earned one.
- **One idea per paragraph,** stated in the first or second sentence, developed, and
  closed. If the closing sentence introduces a new idea, that idea starts the next
  paragraph instead.

### 8.4 Referring to the reader

Third person for the reader is correct and sanctioned (section 3.2). Its frequency is
the problem. Chapter 1 says "the reader" **15 times**, and the construction has
migrated out of the craft section and the summary, where it belongs, into the
teaching body, where it turns stilted: "the reader can look for all three in any
organization, including the reader's own."

- **In the craft section and the chapter summary,** "the reader can now" is the house
  construction and is expected. That is what those slots are for.
- **In the teaching body, prefer the thing to the reader's relation to the thing.**
  Write "This book does not treat model internals" rather than "the reader will find
  no account here of model internals." Write "Three places show the failure" rather
  than "the reader can look for three places." The reader is not a character in the
  teaching body.
- **Never use "the reader's own"** or any construction that stacks the noun twice in
  one sentence.

### 8.5 Terminological invariance

A defined term is a fixed string. Once a term is defined in a callout and repeated in
the key terms list, its wording does not drift anywhere in the book.

Chapter 1 carries a live instance: the callout and the key term both state that a
flat rate does not **abolish** the meter, while the body prose now states that it
does not **remove** it. A reader checking the term against its definition finds two
verbs for one concept. The rule:

- **The callout text and the key-terms text for a term are identical strings.** Not
  paraphrases of each other.
- **Body prose uses the defining verb of the definition** when it restates the
  definition. Synonyms are permitted only in passages that are plainly not restating
  the term.
- **A copy edit that touches a defined term re-checks all three locations,** callout,
  key terms, and every body restatement.

### 8.6 Apparatus consistency

The back-of-chapter apparatus is read as a reference tool, not as prose, and it must
behave like one.

- **Key terms are ordered by a stated principle.** Chapter 1's seven terms are
  currently neither alphabetical nor in order of first appearance. Adopt **order of
  first appearance in the chapter**, which serves a reader reviewing the argument in
  sequence, and let the back-of-book glossary carry the alphabetical ordering.
- **No definition is circular.** "A metered resource is a resource whose consumption
  is measured per unit of use" defines the term with its own root. A definition
  states the genus and the differentia in words outside the term itself.
- **Cross-references resolve to exactly one destination per topic.** Chapter 1
  promises the neighbors of the subject to Chapter 14 in section 1.4 and to
  Chapter 3 in section 1.5. Both are true against the specification, and on the page
  they read as a contradiction. When two chapters treat one topic, the reference
  states the division ("Chapter 3 draws the borders; Chapter 14 designs the treaty
  with the nearest of them").
- **Procedures are set as numbered steps, not as run-in prose.** Chapter 1's
  four-step inventory procedure runs as a single dense paragraph with bold run-in
  heads. A procedure the reader is expected to execute against a real deployment must
  be scannable on the page and re-findable later. Expository prose runs in
  paragraphs; instructions run in lists.

### 8.7 The copy-edit pass

Stage 6 checks this part, in this order, because each check is cheaper than the one
after it:

1. Typography sweep (8.1), which is mechanical and should be gated.
2. Defined-term invariance (8.5), by comparing callouts, key terms, and restatements.
3. Figure budget and paragraph metrics (8.2, 8.3), by count.
4. Reader-reference frequency (8.4), by count.
5. Apparatus and cross-reference consistency (8.6), by inspection.
6. The line-level read for splices, run-ons, and comma density (sections 4 and 5).

Items 1, 3, and 4 are counting problems, not judgment problems, and they are gated by
machine rather than run by hand. The gating is split, and the split is not
arbitrary:

- **`voicecheck.py` carries the source-level checks** (guide v1.3): straight quotes
  and apostrophes in chapter prose, paragraphs over the word ceiling, the antithesis
  budget, "the reader" in the teaching body, and divergence between a definition
  callout and its key term. Run it on the chapter HTML. House-style findings fail the
  run; `--voice-only` suppresses them for work in progress.
- **`AIOM_build.py` carries the rendered-artifact check.** Typography must be gated
  against the PDF, beside the existing em dash gate, not against the HTML. The
  chapter's source block is JSON and legitimately carries straight quotes, so an
  HTML-only rule cannot distinguish syntax from prose. More importantly, footnotes
  are generated at build time from that block, so straight quotes can enter the
  printed page from the footnote apparatus even when every line of chapter prose is
  clean. The rendered page is the only place the whole defect is visible.
- **Not mechanizable, and checked by eye:** circular definitions, cross-reference
  collisions, key-terms ordering against first appearance, and comma splices. A
  splice detector without a parser produces more false positives than findings.

---

## 9. Relationship to the other specifications

Rewritten 2026-08-12 at adoption. The version written on 2026-08-05 described a
repository state that never came to exist, because this guide was never merged:
it claimed B.2 had been demoted and that `voicecheck.py` already carried the
Part 8 checks. Neither was true on `main`. What follows is the actual state.

- **`AIOM_Voice_and_Craft_v1.md` governs the craft criteria C1 to C6**, the four
  exemplars, and the guard. See the header and Part 6. Where the two files touch
  the same ground, that one governs.
- **CLAUDE.md section 2 holds the standing prohibitions** and is the authority on
  them. Parts 3 and 4 here are their operative expansion and repeal none of them.
  Part 4's no-splice and no-run-on rule is ADDITIONAL to section 2 rather than an
  expansion of it, and is not yet recorded there.
- **Consolidated Spec B.2 is NOT yet demoted.** The 2026-08-05 text asserted the
  demotion as done. It is not. B.2 still carries its own register, person and
  mechanical content, so two files state those rules. Booked as an open item
  rather than asserted away.
- **`voicecheck.py` is the mechanical gate for the dash, contraction, question
  and person rules in Part 4.** It does NOT yet carry the Part 8 source-level
  checks: straight quotes in prose, paragraph length, the figure budget, reader
  references, and callout-to-key-term divergence. Those were written on the
  originating branch against a 262-line version of the script; `main`'s is now
  470 lines and has grown craft metrics and the Decision 33 measure since, so
  they must be PORTED individually, not merged. Booked as the second half of this
  adoption.
- **Part 8's typography rule IS gated, in `AIOM_build.py` as gate 15**, added
  2026-08-12 and verified by negative test. It reads the rendered PDF and never
  the HTML, for the reasons section 8.7 gives.
- **The definitional callouts** remain the home for the book's coined terms. The
  inherited-vocabulary policy in section 2.4 governs borrowed terms that get no
  callout, and the two do not overlap.

---

## Changelog

- v1.0, 2026-08-05. Establishes the guide as the single authoritative home for
  prose rules, absorbs B.2, and adds the altitude and contextualization craft
  layer. Dan ruled the scope (comprehensive master guide) and the section 2.4
  inherited-vocabulary policy (in-line placement on first load-bearing use) on
  2026-08-05. No decisions remain open in the document.
- v1.1, 2026-08-05. Adds Part 6, the narrative and explanatory craft, with four
  touchstones (Michael Lewis, James Lardner, the Financial Times, the New Yorker)
  and the slot-located voice model: narrative craft in the cases, explanatory craft
  in the teaching body, register discipline governing both. Dan ruled the model
  (slot-located voice) and the case intensity (scene and character, actor-neutral)
  on 2026-08-05. Renumbers the former Parts 6 and 7 to 7 and 8, and adds checklist
  item 8 for slot-correct voice.
- v1.2, 2026-08-05. Adds a hard rule against comma splices and run-on sentences to
  Part 4, and two Part 5 craft rules on appositive restraint and comma density,
  after the Chapter 1 copy edit surfaced splices introduced by the redraft's
  accumulation style and stacked term-placement appositives. The no-splice rule is
  not yet machine-checkable and is enforced on the reader-simulation pass and the
  copy edit.
- v1.3, 2026-08-05. Adds Part 8, the house style sheet, after an editorial read of
  the redrafted Chapter 1 found defects that a passing production build and a clean
  voice gate did not catch: 26 straight apostrophes and 2 straight double quotes
  with no typographic marks anywhere, the "not X, it is Y" antithesis used 12 times,
  a 219-word paragraph against a 92-word mean, "the reader" 15 times, drift between
  "abolish" and "remove" on a defined term, key terms in no stated order, a circular
  definition of metered resource, a cross-reference collision between Chapter 3 and
  Chapter 14, and a four-step procedure set as run-in prose. Part 8 sets typographic
  standards, a three-per-chapter budget on any rhetorical figure, a 150-word
  paragraph ceiling with required variation, reader-reference discipline,
  terminological invariance, apparatus consistency, and the Stage 6 order of checks.
  Renumbers the former Part 8 to Part 9 and adds checklist item 9. Judgment calls
  made by Claude and open to Dan's revision: the figure budget of three, the 150-word
  ceiling, and key terms ordered by first appearance.
- v1.4, 2026-08-05. Mechanizes Part 8 where it can be mechanized, and corrects
  section 8.7, which had placed every mechanizable check in `voicecheck.py`. That was
  wrong for typography: the em dash gate reads characters out of the rendered PDF,
  the chapter's source block is JSON and legitimately carries straight quotes, and
  footnotes are generated at build time from that block, so straight quotes can reach
  the printed page from the apparatus even when chapter prose is clean. Typography is
  therefore gated in `AIOM_build.py` against the PDF. `voicecheck.py` gains the
  source-level checks: straight quotes in prose, paragraph length, the antithesis
  budget, "the reader" in the teaching body, and callout-to-key-term divergence, with
  `--voice-only` to suppress them for work in progress. 8.7 also now names what is
  not mechanizable and stays a human check.
- v1.5, 2026-08-05. Names and rations the parenthetical interrupter, after Dan read
  the rewritten Chapter 1 and flagged sentences broken up by long comma-fenced
  asides. Measured at 48 long interrupters across 202 body-prose sentences, 18 per
  cent. Root cause was this guide: section 2.4 told the drafter to place inherited
  vocabulary "as an appositive or a short clause", and an appositive is an
  interrupter, so the rule that fixed the vocabulary problem manufactured a prose
  one. 2.4 now states an order of preference (own sentence, then trailing clause,
  then brief appositive) and no longer treats placement and interruption as the same
  requirement. Part 5 gains the general rule: never separate subject from verb by
  more than about three words, never stack two interrupters in one sentence, and
  prefer the right-branching alternative.
- v1.6, 2026-08-12. **Adopted onto `main` after a week stranded**, on Dan's
  ruling. Part 6 retired to a pointer at `AIOM_Voice_and_Craft_v1.md`, resolving
  two documents that had claimed the same authority since both were adopted on
  2026-08-05 by sessions that could not see each other. Part 9 rewritten, because
  the original described a repository state that never existed: it asserted the
  B.2 demotion and the Part 8 `voicecheck.py` checks as done, and neither was on
  `main`.

  **WHAT THE WEEK COST, recorded because it is the argument for reading this file
  rather than filing it.** Two defects this guide already names were found again
  by hand and paid for twice. Part 8's callout-to-key-term rule is exactly the CE3
  defect found on 2026-08-12, where "Meter relocation" carried two different
  definitions; the check for it was already written here. Part 8's typography rule
  is gate 15, added the same day after Chapter 1 shipped straight quotes in six
  footnotes past fourteen green gates. And Part 5's rule 2, on stacked
  interrupters, cites one sentence as its example: the opening case's "Michael
  Truell, chief executive of Anysphere, the company behind Cursor, apologized".
  **That sentence is still in the chapter.** It was named as a defect on
  2026-08-05, the naming was stranded, and it has since survived a developmental
  edit, a voice pass, a design review, a production gate and two copy-edit rounds.

  Measured at adoption against the current chapter: 40 long comma-fenced asides
  across 433 body-prose sentences, 9 per cent, against the 18 per cent this guide
  measured on 2026-08-05. Halved, not solved. The two figures use different
  sentence-splitting methods and are indicative rather than strictly comparable.
