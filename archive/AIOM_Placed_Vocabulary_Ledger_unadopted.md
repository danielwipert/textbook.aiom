> **STATUS: PRESERVED, NOT ADOPTED. UNRULED AS OF 2026-08-12.**
>
> Recovered from `claude/chapter-1-prose-style-x0bzze` (tip `84d6d04`) before that
> branch was deleted, so that deleting the branch would not destroy the file. It
> is filed here rather than at the repo root because Dan has not ruled it in, and
> a file at the root reads as adopted.
>
> **IT IS PROBABLY A LIVE REQUIREMENT RATHER THAN A DEAD ARTIFACT, WHICH IS WHY IT
> WAS NOT SIMPLY BINNED.** `AIOM_Prose_Style_Guide_v1.md` was adopted on
> 2026-08-12 and its section 2.4 places inherited vocabulary once, on first
> load-bearing use, and never re-explains it. That policy only works across
> fifteen chapters if something records what has already been placed. This is that
> something. Chapter 2 is the first chapter that would need it.
>
> Two things to check before ruling it in: whether `AIOM_Continuity_Ledger.md`
> already covers this ground, since it tracks terms owned per chapter, and whether
> the two should merge rather than sit side by side. Nobody has checked.

# AIOM Placed-Vocabulary Ledger

Process-side record required by the prose style guide, section 2.4 (in-line
placement on first load-bearing use). Inherited technical vocabulary is placed once
in the book, on its first load-bearing use, and then used freely and never
re-explained. This ledger is how a drafter knows whether a term has already been
placed in an earlier chapter. It is bookkeeping, not book content, and it never
ships.

Rule of use: before placing a term, check this ledger. If the term is already
listed, use it freely and do not re-place it. If it is not listed, place it in-line
where it first carries weight, then add a row here.

Coined terms (consumption event, access price, software access model, meter
relocation, and the rest) are not tracked here. They live in the definitional
callouts, which are their own home; this ledger is only for the borrowed vocabulary
that gets no callout.

## Placed terms

| Term | Chapter | First-use placement (the gloss the reader meets) |
|---|---|---|
| Cursor | 1 | "Cursor, an assistant that suggests and writes code alongside the programmer" |
| Anysphere | 1 | "the chief executive of Anysphere, the company behind Cursor" |
| GitHub, GitHub Copilot | 1 | "GitHub Copilot, the coding assistant integrated into GitHub, the platform where software teams host and review their code" |
| Sonnet models | 1 | placed by role: "the more capable Sonnet models among them counting as two" |
| frontier models | 1 | "the frontier models, the most capable and most expensive tier" |
| API rate | 1 | "the models' API rates, the metered price of calling a model directly" |
| token (input and output tokens) | 1 | "the tokens a model reads and writes on its way to an answer" |
| premium requests | 1 | "premium requests, its name for uses of the more capable models" |
| credits (usage billing unit) | 1 | "credits counted in tokens, priced at each model's published rate" |
| request (to a model) | 1 | "Each use sends a request to a model, the model performs computation to answer it" |
| retrieval, retrieved material | 1 | "retrieved material, documents pulled in and handed to the model so it can ground its answer" |
| tool call | 1 | used in the consumption-event anatomy: "an answer, a call to another tool" |
| vector store | 1 | "its own vector store, the database that holds the material available for retrieval" |

Notes:

- "long-horizon or agentic task" was rendered in Chapter 1 as "the longest and most
  open-ended tasks" rather than as a placed term. If a later chapter needs the term
  "agentic" or "long-horizon" as load-bearing vocabulary, it is not yet placed, and
  the chapter that first needs it should place it and add a row.
- "marginal cost" is reader-owned MBA vocabulary, not inherited AI vocabulary, so it
  is used without placement and is not tracked here.
- Perishable product names dropped in favor of a role gloss (Cursor's Tab model
  became "Cursor's own built-in model"; models in Auto became "an automatic mode
  that picked a model for the user") are not ledger terms, because the book does not
  carry them forward as vocabulary.
