# Template Library v2

This file is the default generation source for Cold Email Master.

It contains all 10 source templates from the follow-up handoff, plus the 4 filled-in source examples. The raw source is preserved for structure and provenance, but generated production copy must be normalized before output.

## Production Normalization

- Use `{{firstName}}`, `{{shortCompany}}`, and `{{sendingAccountFirstName}}` in production copy.
- Do not hardcode `Nick` or any other sender name.
- Prefer `Best,`, `Thanks,`, or a `Let me know` close. Reserve `Regards,` for formal ICPs.
- Do not generate `free` or `audit` by default, even where raw source placeholders or examples contain them.
- Do not write money with `$` in generated copy.
- Keep follow-ups short and human. Do not turn them into a second full pitch.
- If using the pain-point template, the pain must be specific and evidence-backed, not generic assumptive pain.

## Template-First Generation Protocol

Before writing copy:

1. Pick the closest template family from this file.
2. Fill the template with the campaign brief, proof, ICP, and offer.
3. Normalize the output against the repo rules before showing it to the user.

The template library is the generation source. Style rules, best practices, anti-patterns, and `why-these-work.md` are guardrails and diagnostics.

## Template Selection Map

| Use case | Default template |
| - | - |
| Two-step sequence with a short relevance-check opener | Template 1 plus Template 2 |
| Follow-up built around peer or competitor proof | Template 3 |
| Personalized first line plus direct result claim | Template 4 |
| Strong case study plus a lead magnet | Template 5 |
| No-brainer no-cost front-end offer | Template 6 |
| Strong direct offer with defensible risk reversal | Template 7 |
| Saturated market with a real, specific pain point | Template 8 |
| Good scraped or observed issue data | Template 9 |
| Harder ICPs, enterprise, or markets where insight is the wedge | Template 10 |

## All 10 Source Templates

These are source templates. Generated output must still be normalized.

### Template 1: Two Email Sequence, Email 1 of 2

**Subject:** quick question

**Body:**

```text
Hi {first name},

{Pain point specific first line},

Same case for {{Company}}?

Regards,
Nick

PS: {personalized line}
```

**Use note:** Use as the short opener or relevance check in a two-email sequence. Production version must normalize variables, signoff, money formatting, and avoid assumptive pain unless the pain line is grounded in real ICP evidence.

### Template 2: Two Email Sequence, Email 2 of 2 Follow-up

**Subject:** FOLLOW UP

**Body:**

```text
Hi {first name},

The reason I ask is we've been {{helping similar companies achieve result}}, and {{want to do the same for you, with risk reversal}}.

Can I send a 5 minute Loom explaining how?

Best,
Nick
```

**Use note:** Use as the second message in the two-email sequence. It explains the reason for the first email, adds proof, and asks for permission to send a Loom or short explanation.

### Template 3: Follow Up 1

**Subject:** Happy {day of the week}, {first name}

**Body:**

```text
Hi {first name},

We've been partnering with {ICP call out} like {competitor 1} and {competitor 2} to {generate result}.

{free value / CTA}

Regards,
Nick
```

**Use note:** Use when the campaign has competitor or peer proof and a simple give-first CTA. Production placeholder should be interpreted as `{no-cost value / CTA}`. Do not generate the word `free`.

### Template 4: Personalized First Line Plus Result Claim

**Subject:** Happy {day of the week}, {first name}

**Body:**

```text
Hi {first name},

{Personalized first line},

If I could {generate X result} {risk minimizer},
would you be interested in speaking?

Regards,
Nick
```

**Use note:** Use when the first line is genuinely personalized and the offer can be stated in one clean outcome plus risk-minimizer line.

### Template 5: Lead Magnet Plus Case Study

**Body:**

```text
{{first_name}}: created a {{lead magnet}} for {{company}} covering the {{strategy}} we used to help {{client}} generate {{result}} in {{timeframe}}, mind if I share it?
```

**Use note:** Best when there is a strong, recognizable case study and a concrete lead magnet. The asset and proof carry the email, so keep it extremely short.

### Template 6: The One Liner No-Cost Front-End Offer

**Body:**

```text
{{first_name}}: interested in {{free work / frontend offer}} for {{company}}?

P.S. {{social proof}}
```

**Use note:** Use for a no-brainer front-end offer. Production title and placeholder should be treated as One-Liner No-Cost Front-End Offer. Do not generate the word `free`.

### Template 7: Direct Offer Plus Guarantee

**Body:**

```text
{{first_name}}: interested in {{dream result}} for {{company}} in the next {{timeframe}}? Asking because our {{mechanism}} guarantees {{result}} or {{risk reversal}}, open to it?
```

**Use note:** Use only when product-market fit is real and the result or risk reversal can be defended on a call. Normalize guarantee language if the repo policy prefers softer risk-reversal wording.

### Template 8: Pain Point Plus Solution

**Body:**

```text
{{first_name}}: {{question around a real pain point}}? Our {{solution}} helps {{fix the problem}} so you {{end result}}. Worth a look?

P.S. {{social proof}}
```

**Use note:** Use in saturated markets only when the pain point is specific and credible. Do not turn this into generic assumptive pain like "struggling with leads."

### Template 9: Relevant Touchpoint Plus Observed Issue

**Body:**

```text
{{first_name}}: {{relevant touchpoint}}.

Noticed {{specific issue you scraped}}.

Interested in {{quick fix}}?
```

**Use note:** Use when there is a real observed issue from good data: missing flow, slow site, broken ads, competitor doing X, etc. Bad data makes this template fail.

### Template 10: Unique Market Insight

**Body:**

```text
{{first_name}}: {{question around a relevant touchpoint}}.

{{insight specific to their world}}.

{{CTA around implementing it}}
```

**Use note:** Use for tougher markets and enterprise-style ICPs where insight is more persuasive than a direct pitch.

## Four Filled-In Source Examples

These are raw examples from the source HTML. Keep them as teaching and reference examples, not as unfiltered production output.

### Filled Example 1: Two Email Sequence, Email 1 of 2

**Subject:** quick question

**Body:**

```text
Hi {first name},

I talked to a few other $10M/year CMOs, and many of them are struggling to crack TikTok Shop.

Same case for Sample DTC brand?

Regards,
Nick

PS: saw your LinkedIn post about hiring for CS, how's the search going?
```

### Filled Example 2: Two Email Sequence, Email 2 of 2 Follow-up

**Subject:** FOLLOW UP

**Body:**

```text
Hi {first name},

The reason I ask is we've been helping DTC brands like Case Study 1 add an additional $75 to $90K in monthly revenue with TikTok Shop, and want to do the same for you, completely on performance.

Can I send a 5 minute Loom explaining how?

Best,
Nick
```

### Filled Example 3: Follow Up 1

**Subject:** Happy Tuesday, Nick

**Body:**

```text
Hi Nick,

We've been partnering with agency owners like ABC Media and 123 Marketing to drive hands off Instagram growth with short form clips.

Can I send over an audit of your Instagram profile?

Regards,
Nick
```

### Filled Example 4: Personalized First Line Plus Result Claim

**Subject:** Happy Tuesday, Nick

**Body:**

```text
Hi Nick,

Saw your LinkedIn post about the 123 marketing summit, how was it?

If I could make you 60 short form video clips with 30 minutes of your time, would you be interested in speaking?

Regards,
Nick
```
