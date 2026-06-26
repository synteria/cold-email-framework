---
description: Generate 2-3 high-converting cold email variations with follow-ups. Use when the user wants new cold email copy for a campaign.
---

# Generate Cold Email

You are generating cold email copy. Follow this process exactly.

## Step 1: Gather Information

If the user hasn't provided all of the following, ask before writing:

- **Niche/industry:** Who are you targeting?
- **Offer:** What do you do for them?
- **Core benefit:** Which of the 4 B2B offers does this align to? (save time, save money, make more money, reduce risk)
- **Social proof:** What specific results can you reference? (numbers, outcomes, timeframes)
- **Goal:** Book a call, get a reply, get a referral, gauge interest?

Default context: The user runs an AI automation agency building systems for agencies and service-based companies. Use this unless told otherwise. When generating for this context, describe what the system does and the outcome it produces. Do not pitch "AI automation" as the service.

## Step 1.5: Classify Proof Strength

Before writing, classify the user's social proof into one of three tiers. This determines what you can credibly write.

| Strength | Definition | Examples |
|---|---|---|
| **Strong** | Multiple data points, verifiable names/descriptors, or massive aggregate numbers | ">10M driven," "collectively over 500k/month," "124 appointments in 30 days + 92k/month agency" |
| **Moderate** | Single proof point with specific numbers, or general experience with one concrete result | "92k/month at my own agency," "went from 5-6 calls to over 30 for one client" |
| **Weak/None** | No specific numbers, no named/described clients, no personal results | "I have a big network," "I'm good at what I do," or nothing provided |

**Constraints by proof tier:**

- **Strong:** Any archetype, any justified length. Full creative freedom.
- **Moderate:** Either archetype. If Archetype A, must include strong risk reversal and a give-first element. Confidence language must be calibrated; no "100% sure" or "extremely confident" without compensating proof. Humble/exploratory tone (Legacy Email 3) is a good fit here.
- **Weak/None:** Archetype B only, under 100 words. Default to flagging: *"The proof provided is thin. These emails will have a lower performance ceiling. Consider adding specific results (numbers, outcomes, timeframes) before sending."* Do not refuse to generate, but be explicit about the limitation.
  - **Exception, the v2 lead-magnet shape.** A no-proof email is not weak when a strong, ready-to-use asset does the persuading: a built-for-you deliverable the recipient can act on with one "yes." Here the brevity and the absence of proof are deliberate, and the email is a validated shape, not a thin one. Confirm the asset is genuinely deliverable on one reply. See `examples/templates/v2-frameworks.md` and `why-these-work.md`.

## Step 2: Read the Knowledge Base

Before writing anything, read these files:

1. `examples/README.md` (active example map and numbering rules)
2. `examples/template-library.md` (default v2 generation source, 10 source template families)
3. `examples/validated/batch-01.md` (v2 validated examples, starting at Email 1)
4. `examples/templates/v2-frameworks.md` (normalized v2 framework companion)
5. `best-practices.md` (foundational principles)
6. `anti-patterns.md` (every mistake to avoid)
7. `why-these-work.md` (understand the patterns beneath the surface)
8. `examples/archive/legacy/` only when you need legacy reference. Cite old examples as `Legacy Email N`.

Do not skip this step. Do not rely on memory or general knowledge.

## Step 2.5: Apply Generation Patterns

These are the v2 generation defaults. Apply them before reaching for archived legacy patterns.

- **V2 shape first.** Prefer 1 to 5 lines when the offer, observed issue, proof cue, or lead magnet is strong enough to carry the email. The default structure is one opener, one offer or proof cue, and one permission CTA.

- **Template family first.** Before drafting, choose the closest template family from `examples/template-library.md`. Fill that template with the brief, proof, ICP, and offer. Then normalize the output. Do not generate loose copy from memory when one of the 10 template families fits.

- **Rotate frameworks, not just wording.** Generate variants from different shapes: same-case question, lead magnet plus case study, one-liner front-end offer, direct offer plus risk reversal, observed issue, and market insight.

- **Ask permission for the next asset.** Use CTAs like "Can I send a 5-minute Loom explaining how?", "Mind if I send it?", "Worth a look?", or "Want me to send the 3 things I'd change?" Do not include the link in the first email.

- **Normalize wording.** Do not generate the literal words `free` or `audit` in live cold email copy. Use specific deliverable language, or use no-cost phrasing only when cost needs to be explicit.

- **Use v2 references first.** Reference `Email 1` through `Email 4` for current examples. Use `Legacy Email N` only when comparing against archived long-form patterns.

1. **CTA specificity.** If the goal is booking a call, include specific days and times. If the goal is gauging interest, a short yes/no or permission CTA is preferred.

2. **Proof placement.** Establish proof before or alongside the offer, never as an afterthought. In Archetype A, proof comes before the offer. In Archetype B, the offer can lead but proof must immediately follow. (`why-these-work.md` cross-email patterns: "social proof, authority, in-group signals placed before and around the offer.")

3. **Scarcity when genuine.** Legacy examples use lines like "You were one of the first people I found when looking into it" and "you and a Vancouver firm are one of the first people I'm reaching out to." Only include scarcity when it is real. Do not manufacture urgency.

4. **Length matches proof.** V2 default is 1 to 5 lines. Use longer copy only when every paragraph earns its place with specific proof, mechanism, or risk reversal. See the proof tier constraints in Step 1.5.

5. **Opener selection.** Four valid approaches. **Do not emit a `{{icebreaker}}` variable in any generated email.** The user adds icebreakers manually during review. Generate the email starting from the next line down (the "why you/why now" or first line of context). If the chosen archetype assumes a cold-read icebreaker would precede the body, write the email so it still reads naturally without one, then note in your explanation that the user can prepend an icebreaker line if they choose.
   - **Cold-read opener (icebreaker style):** Feels personal, applies to 80%+ of target audience. (Best Practice #10; Legacy Emails 2-4) When you choose this style, write the body that would follow such an opener, but do not insert the variable yourself.
   - **Fan/subscriber relationship:** Genuine fandom or gratitude. Only when the sender has a real connection to the prospect's work. (Legacy Emails 10-11, 16, 19)
   - **Specific, informed compliment:** Based on real observation, not generic flattery. Legacy examples use lines like "Huge work on the >290k/month solo man" and "Love your design btw."
   - **Simple intro + strong offer:** "I found you on LinkedIn and thought I'd reach out" works when followed immediately by a specific, compelling offer. (Legacy Emails 13, 14)
   - **Never:** Generic flattery ("you guys are doing amazing work"), assumptive pain ("Are you struggling with X?"), or vague compliments that could apply to anyone. See `anti-patterns.md` sections on Generic Personalization and Assumptive Pain-Point Framing.

6. **Risk reversal.** Use the outcome/time/guarantee formula when it fits. Or use co-defined metrics and performance-based language. Frame cost naturally without the flagged payment-status word.

7. **Approximate numbers with tildes.** Use "~20 appointments," "~2M/yr," or "~40mins" when the number is genuinely approximate and you want it to sound less rehearsed.

8. **Acknowledge the cold context only when it helps.** V2 emails often skip this and rely on the opener plus permission CTA. Use cold-context lines sparingly.

9. **Subject line plausible deniability.** If the prospect can tell what you are selling from the subject line alone, rewrite it. 2-5 words, lowercase or sentence case. Must pass the test: "If a friend saw this in their inbox, would they think it could be from someone they know?" (Best Practice #11; see Legacy Email 18 before/after for a clear failure and fix.)

10. **Confidence must match proof.** Strong proof (">10M driven") = softer language is fine, reads as genuine humility. Weak proof + soft language ("I'd aim to," "hopefully") = reads as uncertainty. Weak proof = be direct and pair with strong risk reversal. (See `anti-patterns.md` Hedging section and `why-these-work.md` Hormozi Value Equation analysis.)

11. **Keep the mechanism tight.** Default to one plain outcome sentence ("I help HVAC guys get more jobs by getting them the most traffic in their area"). Keep any "how it works" to a single clause, never a technical paragraph (attribution, iOS14, refund mechanics, funnel stats). Don't over-correct to outcome-only, a brief mechanism clause builds credibility when the reader values it (Legacy Email 3). After drafting, cut every clause that explains the plumbing. (`anti-patterns.md`: Over-Explaining the Mechanism.)

12. **Soft yes/no question as the CTA (give-first offers).** For no-cost-build or give-first offers, a one-word-answer question can be the CTA: "Want me to build a concept of your site at no cost?" (Best Practice #7; cf. Legacy Email 13). Book the call on the reply.

13. **Upfront framing on the value line.** A disarming honest lead-in ("To be upfront, I help..." / "I'll be upfront,") reads well on the identity/value sentence. Rotation option, not every variant.

14. **Bridge proof into the offer.** "[Proof]. Confident I could do something similar, [offer]." beats tacking "so I'm confident it would work for you" onto every proof line, which reads templated across variants. (`anti-patterns.md` Hedging section.)

15. **Set up each move before you make it (connective tissue).** Don't drop the pitch, the case study, or the offer cold. (a) Lead the pitch with a reason for writing ("To be upfront, I help...", "Reaching out because..."). (b) Attribute the case study to yourself so the reader knows the result was your work, "I did this for [client] recently, they..." or "Recently worked with [client] and...", never the bare "[Client] got [result]." (c) Introduce the offer as an offer, "My offer: if we don't hit [X] in [Y], then [Z]", not a bare fragment ("Two 1M+ deals in 12 months or we work at no cost"). The setup is a short connective, not a justification clause, the "trust the reader, cut clauses that show your work" rule still applies. This is one of the most common machine-generated failures; check for it on every variant. (`anti-patterns.md`: Dropping a Move With No Setup.)

Spoken/imperfect phrasing ("more jobs and work," "at no cost on your end at all") is a tool with its place, but don't overdo it; one or two touches per email, not every line.

## Step 3: Generate 2-3 Variations + Follow-Ups

Create 2-3 email variations that differ by **framework and offer angle**.

For example: one version leads with "make more money," another leads with "save time," another with "reduce risk."

For each variation:

- **Generate a subject line.** Follow gold standard patterns: "{{firstName}}?" / "{{firstName}}, question" / "Is {{shortCompany}} [relevance check]?" / "{{firstName}}, quick [topic] question". Keep to 2-5 words. Casual, not salesy.
- Match the tone and style of the v2 validated examples. The generated copy should feel short, specific, and one-to-one.
- Choose an archetype (respecting the proof tier constraints from Step 1.5):
- Choose a v2 pattern:
  - **Same-case question:** peer pattern, then "Same case for {{shortCompany}}?"
  - **Reason-I-ask follow-up:** proof or result, then permission to send a Loom or asset.
  - **One-liner offer:** concrete front-end offer with optional P.S. proof.
  - **Observed issue:** real touchpoint, real issue, permission to send the fix.
  - **Market insight:** question, specific insight, CTA around implementation.
- Use the proven v2 structure: subject line, relevant opener, compact offer or proof cue, one CTA, optional P.S.
- Include appropriate template variables: {{firstName}}, {{shortCompany}}, {{sendingAccountFirstName}}. **Do not emit `{{icebreaker}}` in generated copy.** The user adds icebreakers manually during review if they want one.

### Follow-Ups

**Default: generate two follow-up variants per campaign**, both with **empty subject lines** so Instantly threads them onto the step-1 send (recipient sees the original subject and the new body lands as a reply, not a new pitch).

The two variants:

1. **Variant A (medium + off-ramp).** Opens with a light check-in. **Default opener (use this): "was wondering if you saw this."** (acceptable rotations only if the campaign voice needs them: "this still on?", "did this land?"), then restates the offer in one sentence, then closes with the permission-to-leave off-ramp, **verbatim default: *"If it's not the right fit, no worries. I'll leave it here."*** Three short paragraphs. Reference the offer specifically (e.g. "sample box at no cost"), not abstractly.

2. **Variant B (one-line spintax check-in).** The best-performing short follow-up across campaigns and the **system default**. Single line, light check-in + off-ramp, with `{{RANDOM | ... }}` spintax on the greeting and sign-off so each send varies. Use it verbatim:

   ```
   {{RANDOM | Hey | Hi | hey | hi}} {{firstName}}, any thoughts on this? If this isn't the right fit no worries, just let me know.

   {{RANDOM | Thanks | Best}},
   {{sendingAccountFirstName}}
   ```

   Instantly supports `{{RANDOM | a | b}}` spintax natively and rotates it per send. Keep this as-is unless the campaign voice genuinely needs different phrasing.

Variant A ends with the signoff `Thanks,` + `{{sendingAccountFirstName}}`; Variant B uses the spintax sign-off shown above. Both keep the same tone as the step-1 email. Neither apologizes for following up. Neither says "I know you're busy." Neither uses banned vocabulary (ping, pinging, floating, floating up, floating this up, buried).

If the user explicitly requests a single follow-up (or one with a real subject line), override the default. The two-variant empty-subject pattern is the starting point, not a fixed rule.

### Internet Slang and Abbreviations

Internet slang ("Ngl," "lol," "rn," "Idk") is used in Legacy Email 10. It works when:
- The entire email's tone is ultra-casual
- The target audience communicates this way (creators, community owners, younger demographics)
- It feels natural to the sender's voice

Do not inject slang into a professional-casual email. When in doubt, leave it out. Most emails should not use it.

## Step 3.5: Self-Review

Before presenting, run each generated variation through these checks. Every item is binary pass/fail. These are the generation-specific hard-fails and scoring; the full pre-send list is the canonical "Quick Reference: Before You Send" checklist in `anti-patterns.md`, run that too.

### Hard Fails

Any failure here = revise before presenting. Do not present an email that fails any of these.

1. Does the email use "I" language throughout, never "We"?
2. Does it include at least one specific number in the social proof? (If proof tier is Weak/None, the email must still include whatever proof the user provided, and the limitation must be flagged.)
3. Does it avoid leading with "AI" or "automation"? (AI can appear mid-sentence as mechanism, never as the headline or opener.)
4. Is it free of AI vocabulary words? (Check against the banned list in `anti-patterns.md`: delve, crucial, pivotal, foster, garner, showcase, highlight, enhance, testament, underscore, meticulous, seamlessly, comprehensive, etc.)
5. Does it have exactly one CTA? (Two paths to the same outcome is fine.)
6. Is there an actual offer with a specific outcome, not just a capability description? (Compare Legacy Email 21 before vs. after.)
7. Is it free of em dashes, emojis, and the word "free" for no-cost offers?
8. Is it free of any `{{icebreaker}}` variable? (Other Instantly variables like `{{firstName}}`, `{{shortCompany}}`, `{{sendingAccountFirstName}}` are fine. The user adds icebreakers manually during review.)

### Quality Checks

Failure here = improve if possible before presenting.

9. Does proof appear before or alongside the offer, not as an afterthought?
10. If the goal is booking a call, does the CTA include specific days/times?
11. Is there a risk reversal element? (Outcome/time/guarantee, performance-based, co-defined metrics, or zero-cost upfront.)
12. Is the opener a cold-read, fan relationship, specific informed compliment, or simple intro followed by a strong offer? (Not generic flattery, not assumptive pain.)
13. Does the subject line create plausible deniability? (Could it be from a friend? Does it avoid revealing the pitch?)
14. Is the length justified by the proof density? (Can you cut a paragraph without losing anything concrete? If yes, cut it.)
15. Does it acknowledge the cold context when useful? ("I know this is a long shot," "Know this is out of left field," etc.) Not required in v2.

16. Does each move have a setup before it? Read the email as continuous speech: the pitch has a reason-for-writing lead-in, the case study is attributed to the sender (not a bare "[Client] got [result]"), and the offer is introduced as an offer (not a fragment). If any line lands as a disconnected claim, add a short connective. (`anti-patterns.md`: Dropping a Move With No Setup.)

### Reference Check

17. Identify the single closest validated example by archetype and offer angle. Does the generated email match its tone, density, and structure? If the generated email is significantly weaker on any dimension (proof, CTA strength, risk reversal, brevity), revise to close the gap.

### Score Each Variation

Rate each variation on the 7 Psychological Principles + 4 Hormozi Variables (each 0-2, total /22):

**Psychological Principles:** Give First, Micro Commitment, Social Proof, Authority, Rapport, Scarcity, Shared Identity
**Hormozi Variables:** Dream Outcome, Perceived Likelihood, Time Delay, Effort & Sacrifice

If any variation scores below 13/22, revise it before presenting. Present the score alongside each variation so the user can see the diagnostic.

## Step 4: Explain Your Choices

For each variation, briefly explain:

- Which example(s) inspired the structure and tone
- Which validated example is the closest match, and how the generated email compares to it
- Which offer angle it leads with
- Which best practices it demonstrates

## Style Rules

When writing email copy, apply all style rules from `CLAUDE.md`. The critical ones:

- Informal, one-to-one tone. Use "I" not "We." Never corporate. Never polished.
- Never lead with "AI" or "automation." Describe what the system does and the outcome.
- No marketing language. Use plain, slightly imperfect language.
- Never use the word "free" for no-cost offers. Use "no cost," "zero cost," "wouldn't cost you anything," "I'd pay for it all myself" instead.
- No emojis. No em dashes.
- No AI vocabulary words (delve, crucial, pivotal, foster, garner, showcase, highlight, enhance, testament, underscore, meticulous, seamlessly, comprehensive). Use "is" not "serves as." Don't pad lists to three. Don't cycle synonyms. No "not only X but also Y." No tacked-on "-ing" phrases. See `anti-patterns.md` for the full AI voice section.
- Exactly one CTA per email. (Two paths to the same outcome is fine.)
- Short and punchy by default. Longer only when every paragraph earns its place with specific value.
