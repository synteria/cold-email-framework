---
name: spintax
description: Convert cold email copy into spintax format for cold outreach campaigns. Trigger when the user pastes cold email copy and asks to "add spintax", "spin this", "spin these emails", "make this deliverable", or asks for variations of an email. Also trigger when the user pastes 2 or more cold emails in a sequence and asks to spin them, or when they share Synteria cold email copy and want it ready to send. Default assumption is a Synteria cold email campaign unless told otherwise. Spins at the phrase level, 3 to 8 words, targets 2 to 3 variants per block, preserves the original phrasing as one option, and keeps numbers, names, time slots, and the guarantee structure locked.
---

# Spintax Playbook: Converting Cold Email Copy

## When to use this

Trigger when the user pastes cold email copy and asks to "add spintax", "spin this", "make this deliverable", or asks for variations of an email for cold outreach.

Default assumption: the email is going to a Synteria cold email campaign unless told otherwise.

## Core principles

1. **Sentiment stays constant.** Every variation carries the same emotional tone, claim strength, and intent as the original. If the original is consultative, all spins are consultative. No fear-based, aggressive, or hype variations sneaking in.
2. **Spin at the phrase level.** The sweet spot is 3 to 8 words swapped at a time. Whole-sentence rewrites lose the user's voice and read like spin-talk. Single-word swaps like `{Hi|Hello}` are too thin and do not move the needle on deliverability.
3. **Always include the original phrasing as one option.** The email should still read like the user wrote it. The other options are sibling phrasings, not replacements.
4. **Numbers, qualifiers, names, and time slots stay locked.** Only the angle and phrasing of soft tissue change. "3.5M condo," "234%," "2 deals of 1M+," "12 months," "2:30pm," and "Cindy Kelly in Seattle" do not get spun.
5. **Use `RANDOM` as the first option inside double-brace blocks.** This ensures the first variant is not skipped and distribution stays randomized: `{{RANDOM | option1 | option2 | option3}}`.
6. **Preserve custom variables.** Anything in `{{firstName}}`, `{{company}}`, `{{Title}}`, `{{sendingAccountFirstName}}`, etc. stays intact and usable inside spintax blocks.
7. **Target 3 variants per block.** 2 is fine if a third does not earn its spot. More than 3 dilutes quality. Do not pad to hit a number.
8. **Preserve the user's original line breaks and paragraph spacing exactly.** Do not squish paragraphs together. Do not collapse blank lines. Match the source formatting line for line.

## Syntax reference

| Element | Format |
|---|---|
| Basic spin block | `{{RANDOM | variant 1 | variant 2 | variant 3}}` |
| Variable outside spin | `{{firstName}}` |
| Variable inside spin | `{{RANDOM | Hi {{firstName}} | Hey {{firstName}}}}` |
| Nested spins | Avoid. Flatten into a single block. |

## What to spin

Aim for roughly 6 to 9 spin blocks per cold email, distributed across:

- **Greeting** (`{{RANDOM | Hey | Hi | hey | hi}}`). Lowercase variants of the same word count as separate options for inbox-display variety. Do not overthink this one.
- **Opener / observation phrase**: the part that compliments or references something about the prospect.
- **Closing flavor of the opener**: "keep it up," "nice work," "really impressive."
- **Setup phrase before the value prop**: "To be upfront," "Straight to the point."
- **The verb in the value prop**: "getting them ranked," "ranking them," "landing them."
- **Stat phrasing in the case study**: "she also has a 234% increase in traffic now," "her traffic is also up 234% now."
- **Confidence opener**: "Confident I could," "Pretty sure I could," "Think I can."
- **CTA opener**: "Worth a 15-min call?," "Open to a quick 15-min call?"
- **Call-time phrasing**: "Can ring you at 2:30pm tomorrow," "Happy to call you at 2:30pm tomorrow." The time itself stays locked.
- **Sign-off**: "Thanks," "Cheers," "Best."

## What not to spin

- Specific numbers, percentages, timeframes, prices.
- Proper nouns, including case study names, locations, and product names.
- Time slots in the CTA.
- The guarantee structure, for example "we work for free until you do."
- Anything carrying the core promise of the email.

## Process

### Step 1: Read the original and identify the soft tissue

Soft tissue means phrases that say the same thing in slightly different ways: greeting, hook flavor, value-prop verb, confidence opener, CTA opener, and sign-off.

Numbers and names are bone, not tissue.

### Step 2: Write 2 or 3 variants for each soft-tissue phrase

Each variant:

- Preserves sentiment, tone, and claim.
- Uses different sentence structure or angle, not just synonyms.
- Reads naturally when randomized into the surrounding sentence.
- Includes the original phrasing as one option.

### Step 3: Catch obvious typos, then flag them

If the original has a clear typo, correct it and flag it at the end so the user can revert if it was intentional.

Example: "get you least 2 deals" should become "get you at least 2 deals."

### Step 4: Mirror spin choices across emails in a sequence

If the user pastes 3 emails in a sequence with overlapping content, use the same variant pools for the shared lines across all 3. Do not reinvent the spin for each email.

This matters for shared case studies, guarantees, CTA structure, and repeated opener patterns.

### Step 5: Assemble

Insert spin blocks inline. Preserve paragraph breaks. Punctuation goes outside the spin block where possible because some platforms break when commas sit inside.

### Step 6: QA before delivering

- [ ] Every spin block starts with `RANDOM`.
- [ ] Every spin block has 2 or 3 options, with 3 preferred unless a third feels forced.
- [ ] Every option in every block carries identical sentiment.
- [ ] No option changes the claim, numbers, or core promise.
- [ ] Custom variables are intact.
- [ ] The original phrasing appears as one option in each block.
- [ ] Reading any combination top to bottom produces a coherent, natural email.
- [ ] No nested spintax blocks.
- [ ] Punctuation is outside spin blocks where possible.
- [ ] Paragraph spacing matches the source exactly.

## Output format

Return:

1. The fully spun email or emails in a code block, with original spacing preserved.
2. A short note at the end flagging any typos corrected, sections deliberately not spun, and anything else the user should sanity-check.
3. No sample-rendered variants unless the user asks.

If the user gives multiple emails, output each in its own code block under a clear header: `## Email 1`, `## Email 2`, `## Email 3`.

## When the user asks for more options for a specific phrase

If the user says "give me more options for the upfront line" or "more variants for the CTA," respond with a flat numbered or bulleted list of 10 to 15 candidates for that phrase only. Do not rebuild the whole spin block.

## Common failure modes to avoid

1. **Whole-sentence rewrites.** Spinning entire sentences makes the email feel AI-written and erases the user's voice. Phrase-level only.
2. **Tone drift.** "Quick idea for you" and "Final warning before your competitors crush you" are not interchangeable. Never mix consultative with aggressive.
3. **Claim drift.** "Lift revenue 20%" and "Lift revenue significantly" are not interchangeable. Numbers stay locked.
4. **Inventing a different value prop in a variant.** That is A/B testing, not spintax. Spintax varies how you say it, not what you say.
5. **Padding to hit a variant count.** A weak third option is worse than just having two. If the third feels forced, ship two.
6. **Squishing paragraphs.** Always preserve the source spacing.
7. **Punctuation inside the spin.** Some platforms break on commas or quotes inside spins. Keep terminal punctuation outside the block where possible.
8. **Reinventing spins for each email in a sequence.** If 3 emails share the same case-study line, the spin pool for that line should be identical across all 3.

## ICP segmentation rule

If the user has multiple ICPs, build a separate spintax pool per ICP. Do not try to make one universal email cover both. Vocabulary, examples, and metrics match the segment. Tone and claim strength stay constant across pools.

## A/B testing companion rule

If the user is also A/B testing, lock the test variable, subject, CTA, or value prop, as a fixed element in each arm and apply spintax only to the non-test sections. Causality stays clean while each arm still gets copy variety.

## Quick example of correct phrase-level spinning

Original:

> Confident I could do something similar for you and if we don't get you at least 2 deals of 1M+ in 12 months, we work for free until you do.

Spun correctly:

> {{RANDOM | Confident I could do something similar for you | Pretty confident we could do the same for you | Think we can pull off something similar for you}} and if we don't get you at least 2 deals of 1M+ in 12 months, we work for free until you do.

What stays locked: "at least 2 deals of 1M+ in 12 months, we work for free until you do." That is the guarantee. Do not touch it.

What got spun: just the confidence opener. 3 to 8 words. Original phrasing kept as option 1.
