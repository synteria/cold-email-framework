# Cold Email Master

An AI system for writing cold email copy that actually performs.

One skill isn't enough. This is the whole thing: a knowledge base of validated
examples, the rules behind why they work, the mistakes that kill reply rates, and
the Claude Code skills that generate, review, and ship copy against all of it.

## The knowledge base

Four foundations. The skills read these in full before touching any copy.

- `examples/` validated cold email copy from proven sources. The gold standard for tone, structure, and persuasion.
- `best-practices.md` the foundational principles that underpin effective cold email.
- `anti-patterns.md` the common mistakes to catch and avoid.
- `why-these-work.md` a meta-analysis of why each validated example lands.

## The skills

Drop these into Claude Code and run them as slash commands.

- `/generate-email` write 2-3 variations that rotate the offer angle, matched to the examples.
- `/review-email` run a draft through the full checklist, with specific feedback and rewrites.
- `/strategy` subject lines, CTAs, follow-ups, personalization, deliverability, campaign structure.
- `/deploy-to-instantly` push the copy to Instantly.ai as a campaign (payload formatting, A/B variants, follow-up sequencing).
- `/anneal` fold a revision back into the knowledge base without breaking it (see `iteration-protocol.md`).

Plus copywriting reference skills: `conversion-copywriting` (Schwartz awareness levels + AIDA) and `dan-kennedy-copywriter` (direct-response).

## How it stays sharp

Every revision is a learning signal, not a one-off edit. `iteration-protocol.md`
is the process for routing each lesson to exactly one home, and `scripts/lint_kb.py`
checks the knowledge base stays consistent. The point is a system that compounds:
the next email is better than the last because the last one taught it something.

## Setup

```
pip install -r requirements.txt
cp .env.example .env   # add your Instantly API key(s) for deploy
```

Open the repo in Claude Code and the skills are ready to use.

## Note

This is the framework, with no client data. Per-client briefs, drafts, and live
copy live elsewhere. Bring your own brief (see the "Client Data Source" section in
`CLAUDE.md`) and the system writes against it.
