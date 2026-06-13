---
description: Capture a lesson from revised cold email copy and fold it into the knowledge base correctly. Use after the user revises generated copy, hand-writes a campaign that worked, or says "update the system" / "reflect this change" / "anneal this."
---

# Anneal: fold a revision back into the system

You are running the iteration protocol (`iteration-protocol.md`). Goal: take a
revision the user made and persist any reusable lesson to exactly the right place,
without breaking anything. Read `iteration-protocol.md` before starting if you
haven't this session.

The cardinal rule: **never silently edit the knowledge base.** Propose, get explicit
confirmation, then apply. The user is the arbiter of universal vs client-specific.

## Step 1: Get the before and after

You need both versions of the copy:

- **Before:** what the system generated (or the prior draft).
- **After:** what the user changed it to.

If you only have one, ask for the other. If the user hand-wrote a campaign from
scratch (no "before"), treat the validated examples as the baseline and diff against
the closest one.

## Step 2: Capture the deltas literally

List every change as raw diff before interpreting:

- **Kept:** lines that survived unchanged (signal: these are working).
- **Cut:** what was removed, quoted.
- **Reworded:** before -> after, quoted both sides.

Do not state "the lesson is X" yet. Name the literal changes first.

## Step 3: Classify each delta

For each meaningful delta, assign **scope** and **type**.

**Scope** (run the Three-Niche Test for anything you're tempted to call universal):

- A delta is **Universal** only if (a) you can state the rule without naming the
  client's product/channel/vertical, AND (b) it would improve emails in 3+ unrelated
  niches. If you can't strip the client out of the sentence, it is not universal.
- Otherwise it's **Niche-class** (applies to a category) or **Client-specific**
  (this campaign/sender only).

**Type:** style rule / heuristic / anti-pattern / new validated example.

Default to the **lower** scope when unsure. Premature promotion is the failure mode
this whole protocol exists to prevent. A lesson seen once is client-specific by
default; it earns universal status only after showing up across 2+ unrelated clients
(the promotion ladder).

State your classification for each delta and your reasoning, especially the
Three-Niche Test result.

## Step 4: Route

Map each lesson to its single home:

| Lesson | Home |
|---|---|
| Universal style rule | `CLAUDE.md` Style Rules |
| Universal heuristic | `best-practices.md` |
| Universal failure | `anti-patterns.md` |
| Niche-class rule | `anti-patterns.md`, tagged with scope |
| New proven copy | `examples/` new batch entry + `why-these-work.md` analysis |
| Client-specific | `clients/<client>/rationale.md` only |

Before proposing a new entry, **grep the keywords**: if the principle already has a
home, the correct action is to edit that entry, not add a second copy. Restating is
how the 2-3-vs-2-5-words drift happened.

## Step 5: Check for contradictions

For each proposed universal/niche rule, scan the validated examples. If any example
would now violate the rule, you must resolve it one of three ways, never leave both:

1. Change the rule (maybe it's wrong or too broad).
2. Fix or annotate the example.
3. Scope the rule so the example is exempt.

Flag any contradiction explicitly. This is the check that was missing when the
`{{companyName}}` and `{{icebreaker}}` rules were added against examples that used them.

## Step 6: Propose, confirm, apply

Present, for each lesson:

- the delta it came from,
- scope + type + the Three-Niche Test result,
- the exact file and location to edit, and the proposed text,
- whether it edits an existing entry or adds a new one,
- any contradiction found and how you'd resolve it.

Wait for explicit confirmation. The user decides universal vs client-specific.

On approval, apply the edits. If a new example was added or one removed, update every
reference: `Email N` citations, the README niche index, `why-these-work.md`, and
`/N` counts.

## Step 7: Verify

Run the linter and report the result:

```
python scripts/lint_kb.py
```

It must be green (0 errors) before the change is done. Fix any dangling reference or
stray `{{companyName}}` it reports. Mention the warning count; warnings (subject-length
phrasing, `/N` counts) are prompts to eyeball, not failures.

## Notes

- If every delta classifies as client-specific, the correct outcome is "nothing
  changes in the global KB, here's the note for `clients/<client>/rationale.md`."
  That is a valid and common result. Don't manufacture a universal rule to feel
  productive.
- Keep `CLAUDE.md` lean. A new universal style rule should usually *edit an existing*
  bullet, not add one. If you're adding a third near-identical bullet, you've found a
  consolidation, not a new rule.
