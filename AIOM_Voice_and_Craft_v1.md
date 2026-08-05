# AIOM Voice and Craft Standard v1

The positive half of the voice standard. Adopted 2026-08-05.

The standing linguistic rules in CLAUDE.md and Consolidated Spec B.2 are
prohibitions: no em dashes, no contractions, no exclamation points, no
rhetorical questions in body prose, no hedging. Prohibitions are necessary and
they are not sufficient. Prose can break none of them and still be dead on the
page. This file is the half that says what good looks like, so that the voice
standard has something to be measured toward and not only away from.

Scope: body prose in all fifteen chapters, and the opening-case slot, where the
craft criteria bind hardest. Craft sections, discussion questions, and problems
inherit the criteria where they apply.

Owner of the standard: Dan. Claude drafts and checks against it.

---

## 1. The exemplars, and exactly what is borrowed

Four writers and houses are named because Dan named them. What follows extracts
the transferable technique from each and states its constraint inside this book.
The technique is borrowed. The register is not.

### 1.1 The concrete particular (Michael Lewis)

**The technique.** An abstraction that carries argumentative weight is anchored
to a named, specific instance. A number with a unit, a dated moment, a named
instrument, a physical detail. The particular does the work that a
generalization would otherwise do abstractly, and the reader remembers the
particular.

**In this book.** Chapter 1 does not say the team treated the tool as ordinary
software. It says the arrangement was "filed next to the ticketing system and
the design software and the password manager." The list of specific neighbors
carries the whole claim about the mental model, and it carries it without
asserting it.

**The constraint.** The fifty-year rule quarantines perishable specifics in
dated cases. So the Lewis move lives mostly in the opening-case slot, in worked
examples, and in the craft artifact. Body prose earns its particulars through
structure and worked numbers rather than through current events. A particular
that will read as dated in 2050 belongs in a case with a provenance line, not in
the teaching body.

### 1.2 Context and stakes (James Lardner)

**The technique.** Explaining a mechanism is only half the work. The other half
is the conditions that made the mechanism available at that moment, and what it
settled. Why then, and why it mattered. Lardner's account of the VCR is
memorable because it explains not only what the machine did but what had to be
true for it to arrive, and what its arrival decided.

**In this book.** Chapter 1 explains why organizations did not meter AI
consumption, and refuses the easy causal story. "It would be a mistake to read
those absences as negligence. They are inheritance. The organization did not
decide to stop metering. It never began, because the thing it had been buying
for three decades never required it." That is the mechanism plus the condition
that produced it, and it converts a reader's judgment into a reader's
understanding.

**Why this is the highest-value borrow.** It strengthens causal explanation
rather than decorating it. It is also the only one of the four that is fully
compatible with the magisterial register at no cost, because deriving a
behavior from its conditions is precisely what the register already demands
in place of scolding.

**The constraint.** Context is not background. A paragraph of history that does
not change what the reader concludes is padding, and the reader can tell.

### 1.3 Sentence economy (Financial Times)

**The technique.** The finding leads. The qualification subordinates. Nothing
clears its throat before speaking. An FT lede states the thing that happened in
its first clause and spends the rest of the sentence bounding it.

**In this book.** "Set the two episodes side by side and the shared feature is
not the apology, the timing, or the size of the vendor. The shared feature is
what broke." The instruction and the finding arrive together, and the negations
that would have opened a weaker paragraph are subordinated inside the sentence
that already made the point.

**The constraint.** Economy is not compression for its own sake. A sentence
stripped past the point of comprehension has failed the reader baseline, which
Stage 4 also checks.

### 1.4 Paragraph architecture (The New Yorker)

**The technique.** Sentence length varies deliberately, and the variation is
load-bearing: a short sentence after three long ones lands because of what
preceded it. Paragraphs end on the clause that carries the weight, not on a
trailing qualifier that lets the air out.

**In this book.** "Organizations that would never let a material flow through
the plant unrecorded let the AI flow through the work unrecorded, and the reason
is the packaging. The resource arrived labeled as software, and licensed
software does not flow." The paragraph ends on its shortest and hardest clause.
Reverse the two sentences and the paragraph dies.

**The constraint.** Rhythm is not decoration and it is never a reason to add a
sentence. If a short sentence is inserted only for cadence and asserts nothing,
it is padding under a different name.

---

## 2. The guard: what is not borrowed

This section matters as much as the four above, because the borrowed techniques
arrive attached to registers this book has already ruled out.

- **Lewis's populism.** Out. The register is magisterial. The book does not play
  to a gallery.
- **Lewis's heroes and villains.** Out, and this one is load-bearing. Lewis
  explains through character: someone saw what others missed. This book has a
  standing rule to derive provider behavior rather than scold it, and to explain
  why the buyer's mental model was legible rather than sneer at it. Where a
  structural explanation is available, the structural explanation is the one
  that runs. Character-driven causation is not permitted in body prose.
- **Second person and direct address.** Out except where already permitted:
  craft sections sparingly, discussion questions, and problems.
- **The manifesto's taunting energy.** Already out, and the Lewis borrow must
  not smuggle it back in through irony or a knowing aside.
- **New Yorker digression.** Out. The Financial Times economy rule wins any
  conflict with the New Yorker rhythm rule. When the two pull against each
  other, cut.

---

## 3. The six craft criteria

These are the checkable form of the above. They appear verbatim as sub-checkboxes
under Stage 4 in every chapter checklist, and `status_check.py` fails any Stage 4
marked passed with one of them left open and unexplained.

- **C1. Concrete particular.** Every abstraction carrying argumentative weight is
  anchored to at least one named, specific instance in the section that
  introduces it.
- **C2. Context and stakes.** Every mechanism explained states the conditions
  that made it available and what it settles, not only what it does.
- **C3. Front-loaded sentences.** Findings lead and qualifications subordinate.
  No throat-clearing openers.
- **C4. Deliberate rhythm.** Sentence length varies, and no long stretch runs at
  a uniform length.
- **C5. Paragraph close.** Paragraphs end on the load-bearing clause, not on a
  trailing qualifier.
- **C6. The guard holds.** No hero or villain framing, no populist register, no
  character-driven causation where a structural account is available.

C2 has no mechanical proxy and never will. It is assessed by reading, and it is
the criterion most worth the reading time.

---

## 4. Mechanical proxies and their limits

`voicecheck.py` prints a craft-metrics block on every run. The numbers are
advisory and permanently advisory. They are proxies, and a proxy optimized
against is a proxy that has stopped measuring.

| Metric | Proxies | Reads on |
|---|---|---|
| Sentence length distribution, variance, longest uniform run | rhythm | C4 |
| Throat-clearing openers | economy | C3 |
| Concrete-particular density (numerals, dates, proper nouns per 1,000 words) | the concrete particular | C1 |
| Copula rate and nominalization density | economy | C3 |
| Paragraphs closing on a trailing qualifier | paragraph close | C5 |

No metric reads on C2 or C6. Both are judgment, and the checklist is where they
are enforced.

Chapter 1 sets the baseline band. Later chapters are compared against it rather
than against an absolute threshold, because the right numbers for a craft-heavy
chapter and a proof-heavy chapter are not the same.

---

## 5. Worked exemplars

Drawn from the Chapter 1 Stage 4 render. Each pair shows a real passage and the
flat version it could have been. The flat versions are constructed for contrast
and are not drafts that existed.

**C1, the concrete particular.**

- To standard: "The arrangement was, on its face, a subscription like any other,
  filed next to the ticketing system and the design software and the password
  manager."
- Flat: "The arrangement was treated as an ordinary software subscription."

The flat version asserts the claim. The version to standard demonstrates it, and
costs eleven words to do so.

**C2, context and stakes.**

- To standard: "It would be a mistake to read those absences as negligence. They
  are inheritance. The organization did not decide to stop metering. It never
  began, because the thing it had been buying for three decades never required
  it."
- Flat: "Organizations did not meter AI consumption because they had not
  previously needed to meter software."

The flat version states the cause. The version to standard states the cause,
forecloses the wrong reading, and tells the reader what the finding settles.

**C4 and C5, rhythm and close.**

- To standard: "Organizations that would never let a material flow through the
  plant unrecorded let the AI flow through the work unrecorded, and the reason is
  the packaging. The resource arrived labeled as software, and licensed software
  does not flow."
- Flat: "The resource arrived labeled as software, which is why organizations
  that would never let a material flow through the plant unrecorded let the AI
  flow through the work unrecorded, although the packaging was not the only
  factor."

The flat version ends on a qualifier and runs one length throughout.

**C6, the guard.**

- To standard: "The buyers in these stories did not make an error of vendor
  selection. Cursor and Copilot were, and are, excellent tools. The buyers made
  an error of category."
- Off standard: any version in which a provider is characterized as having
  exploited the buyer, or a buyer as having been careless.

---

## 6. Revision history

- v1, 2026-08-05. Adopted following Dan's ruling on the voice enforcement
  decision. Process change: Stage 4 becomes the voice and craft check, and the
  six criteria enter the generated checklists.
