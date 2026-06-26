# Iteration Protocol

How the knowledge base learns without breaking itself.

This system is meant to compound: every time copy gets revised, the lesson should
feed back in so the next generation is better. That only works if changes are made
correctly. Past iteration didn't follow a process, and the result was predictable:
single-client rules promoted to universal law, the same principle restated in four
files until the copies drifted apart, new rules that contradicted the validated
examples, and examples removed without fixing the references that pointed at them.

This protocol exists to make each of those failures structurally hard to commit.
The `/anneal` skill runs it interactively; `scripts/lint_kb.py` verifies the
structural half automatically.

---

## When to run it

Run the protocol whenever a revision *might* contain a reusable lesson:

- You revised generated copy and the edits feel like more than this-campaign taste.
- You hand-wrote a campaign without using the system and it worked.
- You noticed the same correction twice across different clients.

Not every edit is a lesson. Most are one-off taste for a single campaign and belong
only in that client's folder. The protocol's job is to tell the difference and route
each lesson to exactly one place.

---

## The five stages

### 1. Capture

State the deltas literally before interpreting them. For each change: what was
**kept**, what was **cut**, what was **reworded**. Quote the before and after. Don't
jump to "the lesson is X" yet, name the raw diff first. (This is step 1 of the
Continuous Improvement loop in `CLAUDE.md`.)

### 2. Classify

Score every delta on two axes.

**Scope** decides where it can live:

- **Client-specific:** only this campaign, sender, product, or vertical.
- **Niche-class:** applies to a category (e.g. physical-product/retail, local
  service, creator outreach) but not all cold email.
- **Universal:** applies to all cold email.

**The Three-Niche Test** is the gate that prevents premature promotion. A delta is
**Universal only if both hold:**

1. You can state the rule without naming the client's product, channel, or vertical.
2. It would improve emails in **3+ unrelated niches.**

> "Compress proof lists to 2-3 names + and more" passes: no client in the sentence,
> helps any niche with a proof list.
>
> "Re-ordering goes on your existing Brakes delivery" fails: it only means anything
> for food-and-beverage distribution. That's a client-specific note, not a rule.

If you can't strip the client out of the sentence, it is **not** universal. Demote it.

**Type** decides which file:

- Style rule (a phrasing do/don't)
- Heuristic / principle (a why-it-works)
- Anti-pattern (a failure to catch)
- New validated example (proven copy worth referencing)

### 3. Route: one fact, one home

Each lesson goes to exactly **one** canonical location. Everywhere else links to it
rather than restating it. Restating is how drift starts.

| Lesson | Single home | Elsewhere |
|---|---|---|
| Universal style rule | `CLAUDE.md` → Style Rules | link, don't restate |
| Universal heuristic | `best-practices.md` | link |
| Universal failure | `anti-patterns.md` | link |
| Niche-class rule | `anti-patterns.md`, tagged with its scope | link |
| New proven copy | `examples/` (new batch entry) + analysis in `why-these-work.md` | reference by number |
| Client-specific | `clients/<client>/rationale.md` **only** | never touches the global KB |

### The promotion ladder

New lessons do **not** enter the global knowledge base on first sighting. They start
in `clients/<client>/rationale.md`. A lesson graduates to the global KB only after
the **same lesson appears across 2+ unrelated clients.** Until then it stays local.

This is the single rule that would have prevented most of the bloat: nearly every
over-promoted rule had only ever shown up once.

### 4. Check: before persisting

- **Contradiction.** Does the new rule break any validated example? If an example
  violates it, you must do one of three things, never leave both standing: change the
  rule, fix or annotate the example, or scope the rule so the example is exempt.
- **Duplication.** Grep the principle's keywords. If it already has a home, edit that
  home. Do not add a second copy.
- **Reference + count integrity.** Adding or removing an example means updating every
  `Email N` citation, the README niche index, the `why-these-work.md` analysis, and
  any `/N` trait count.

### 5. Verify

Run the linter:

```
python scripts/lint_kb.py
```

It fails on any `Email N` reference that doesn't resolve, any `{{companyName}}` in
live copy, and surfaces subject-length drift and `/N` counts for recheck. Green linter
is the bar for committing a knowledge-base change.

---

## Worked example

You generate a chiropractor email. You cut "I run a boutique chiro-marketing studio"
to "I run ads for chiropractors."

- **Capture:** reworded the identity line; cut "boutique," cut "studio."
- **Classify:** the lesson is "drop marketer adjectives the operator wouldn't use."
  Three-Niche Test: state it without the client (yes), helps gyms / cafes / agencies
  (yes) → **Universal, style rule.**
- **Route:** `CLAUDE.md` Style Rules (the "describe niches the way operators describe
  themselves" rule already exists → edit it, don't add a new bullet).
- **Check:** no validated example uses "boutique"; no contradiction. Already has a
  home → duplication check sends you to edit it.
- **Verify:** linter green. Done.

Counter-example: you cut "ships on your Brakes order" to "ships on your existing
delivery." Three-Niche Test fails (food distribution only) → **client-specific** →
goes in `clients/<client>/rationale.md`, nowhere else.
