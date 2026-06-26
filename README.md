# Cold Email Master

An AI system for writing cold email copy that actually performs.

This framework is a knowledge base of validated examples, reusable templates, the rules behind why they work, the mistakes that kill reply rates, and Claude Code skills that generate, review, and ship copy against all of it.

The copy standard has been remastered around v2 examples: shorter, sharper emails that create one clean reply instead of explaining the whole business in the first touch.

## Current Standard

Use the restarted v2 set first:

- `examples/validated/`: validated v2 examples, starting at `Email 1`.
- `examples/templates/`: reusable frameworks derived from validated structures.
- `examples/pending-validation/`: future examples that are not approved yet.
- `examples/archive/legacy/`: old validated batches, kept as legacy reference only.

Old examples are never plain `Email N` in current guidance. Refer to them as `Legacy Email N` when needed.

## Core Files

- `CLAUDE.md`: canonical operating instructions for the repo.
- `best-practices.md`: foundational principles.
- `anti-patterns.md`: mistakes and pre-send checks.
- `why-these-work.md`: v2 pattern analysis.
- `iteration-protocol.md`: how the knowledge base learns without drifting.
- `scripts/lint_kb.py`: structural verifier for example references and live-copy variables.

## V2 Copy Priority

Default to 1 to 5 lines when the offer, insight, or lead magnet is strong enough to carry the email.

Use longer copy only when proof, mechanism, or risk reversal genuinely needs the space.

The usual v2 shape is:

- one relevant opener, peer cue, proof cue, or observed issue
- one compact offer or reason for writing
- one yes/no or permission CTA

Live generated copy should not emit the literal words `free` or `audit`. Use specific deliverable language instead.

## Skills

Drop these into Claude Code and run them as slash commands.

- `/generate-email`: write 2-3 variations that rotate the offer angle, matched to the examples.
- `/review-email`: run a draft through the full checklist, with specific feedback and rewrites.
- `/strategy`: subject lines, CTAs, follow-ups, personalization, deliverability, and campaign structure.
- `/spintax`: convert approved variants into phrase-level spintax for delivery.
- `/deploy-to-instantly`: push the copy to Instantly.ai as a campaign.
- `/anneal`: fold a revision back into the knowledge base without breaking it.

## Setup

```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
```

Add your Instantly API key to `.env`, open the repo in Claude Code, and the skills are ready to use.

## Note

This is the framework, with no client data. Per-client briefs, drafts, and live copy live elsewhere. Bring your own brief and the system writes against it.
