# Email Examples

Add validated cold email copy here as `.md` files.

## How to Add Examples

1. Create a new `.md` file in this folder (e.g., `saas-outreach.md`, `agency-leads.md`, or just `batch-01.md`)
2. Paste the email copy in
3. Use the format below so Claude can parse them consistently

## Suggested Format

```markdown
# [Descriptive Name]

**Niche/Industry:** (if known)
**Goal:** (book a call, get a reply, etc.)

---

## Email 1

**Subject:** ...

**Body:**
...

---

## Email 2

(repeat as needed)
```

You don't have to follow this format exactly. The main thing is to separate each email clearly so they're easy to reference individually. Paste raw copy if that's easier.

## Niche Index

Quick reference for finding examples by industry, archetype, and length.

| Niche | Emails | Archetype | Length |
|-------|--------|-----------|--------|
| Creative agencies | 2 | A | Medium-long |
| Videographers / video agencies | 3, 4 | A | Medium-long |
| PPC agencies | 7, 8, 9 | B, B, B | Ultra-short, Medium-long, Short |
| Skool community owners | 10, 15 | A, A | Medium-long |
| Creators (YouTube/Skool) | 11, 16, 17, 19, 22 | A, A, B, A, B | Medium-long, Medium-long, Short, Medium-long, Ultra-short |
| Agencies (general) | 18 | A | Medium-long |
| Content/writing | 13 | B | Ultra-short |
| Beauty/skincare wholesale | 14 | B | Short |
| SaaS / sponsorship | 20 | B | Short |
| Marketing companies (B2B) | 21 | A | Medium-long |
| Podcasters | 23 | A | Medium-long |
| Agencies / B2B (lead-magnet offer) | 24, 25 | B, B | Ultra-short, Ultra-short |

**Archetype A** = Relationship-First (builds context before the offer, 150-250+ words)
**Archetype B** = Offer-First (leads with the offer, 60-200 words)

**Length key:** Ultra-short = under 80 words, Short = 80-120 words, Medium-long = 150-250+ words

Emails 15-23 (batch-02) include before/after pairs. The "Before" is shown as a short gist of its failures (full originals in git history); the "After" versions are the validated examples.

**Removed / non-existent example numbers:** 1, 5, 6, 12. Numbering is intentionally non-contiguous. Examples 5 and 6 were near-duplicates of Emails 3 and 2/4 (same template, different niche) and were removed to keep one canonical example per pattern; numbers 1 and 12 were never assigned. Don't go looking for them, and don't reference them in copy. `scripts/lint_kb.py` fails the build on any reference to a removed number.

Emails 24-25 (batch-03) are ultra-short, lead-magnet-first variants. They carry no case studies or proof on purpose: they work when the free asset offered (a built-for-you list of 30 decision makers + personalised first emails) is strong enough to sell itself. Rotate one of these into a campaign even when you have strong case studies, the strip-it-back direct ask pulls different responders than the proof-heavy variants.

## Source Provenance

Batch-02 (Emails 15-21) was extracted from a ~4.5 hour cold email masterclass by Nick (runs Leftclick, previously 1SecondCopy, runs Maker School). The transcript has been fully read and integrated across `best-practices.md` (principles 16-19), `anti-patterns.md` (subject-line and offer mistakes), `why-these-work.md` (Conversion Rate Formula, Four-Step Framework, Casualization Layer, platform optimization), and these examples. No need to re-read the raw transcript: all novel insights are already in the KB.

## How Examples Are Used

The skills `/review-email`, `/generate-email`, and `/strategy` all read from this folder before doing anything. Examples here are the gold standard for tone, structure, and persuasion. New copy is measured against them. See `why-these-work.md` in the project root for a breakdown of why each example works.
