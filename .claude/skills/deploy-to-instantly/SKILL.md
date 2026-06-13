---
description: Deploy generated cold email variations to Instantly.ai as a new campaign. Use after /generate-email when the user wants to push copy directly to Instantly.
---

# Deploy to Instantly

You are deploying generated cold email copy to Instantly.ai as a new campaign. Follow this process exactly.

## Instantly API Gotchas (READ FIRST)

These are hard-won lessons from production deployments. Do not skip.

1. **Body formatting: use Gmail-style `<div>` blocks, NEVER bare `<br>` tags or `<p>` tags.**
   Two stacked quirks:
   - Bodies with bare `<br>` tags get their text silently stripped by the API. Content must be inside block-level tags.
   - Bodies wrapped in `<p>...</p><p>...</p>` save fine, but on page refresh the Instantly editor (which normalizes to Gmail compose format, per their Clean HTML feature) collapses the paragraph margins so the email renders as one bunched-up block with no spacing.

   The fix is to emit Gmail-style HTML directly: `<div>paragraph1</div><div><br></div><div>paragraph2</div>`. The `CampaignBuilder.format_body_for_instantly()` handles this automatically for plain-text input. If you pass pre-formatted HTML, use this same shape — never `<p>` tags or bare `<br>`.

2. **Timezone: `Australia/Sydney` is rejected.** Use `Australia/Melbourne` instead (same timezone). The builder's `TIMEZONE_ALIASES` dict handles this automatically, but be aware if constructing payloads manually.

3. **Follow-up default is the two-variant, empty-subject pattern (A/B of one step).** Per the generate-email skill, the default follow-up is two variants (A = medium off-ramp, B = one-line spintax check-in), both with an **empty subject** so Instantly threads them as a reply on the step-1 send. Both variants live in the SAME follow-up step (step 2) as A/B variants, not as two sequential steps. `parse_generated_output` returns them already grouped: `followups: [{"variants": [varA, varB]}]`. Give a follow-up a real subject only if the user specifically wants a fresh-subject (new-thread) follow-up. A genuine multi-step drip (step 2, then step 3) is a separate, opt-in shape: pass a flat `followups` list where each entry is its own step.

4. **Updating campaigns: use PATCH, not DELETE + recreate.** The delete endpoint is finicky (`body must be null`). PATCH works reliably: `PATCH /api/v2/campaigns/{id}` with `{"sequences": ...}`.

5. **Verify after deploy.** Always fetch the campaign back via GET and confirm the body text survived. Don't assume success from a 200 status code alone.

## Step 1: Verify Prerequisites

Check two things before proceeding:

1. **Generated email copy exists.** Look for recent `/generate-email` output in the conversation (variations + follow-ups). If none exists, tell the user: "Run `/generate-email` first, or paste your email variations and follow-ups here."

2. **Python dependencies are installed.** Run:
   ```bash
   python -c "import requests; import dotenv; print('Dependencies OK')"
   ```
   If this fails, tell the user to run `pip install -r requirements.txt` from the project root.

## Step 2: Parse the Generated Emails

Extract the variations and follow-ups from the generate-email output using the parser:

```bash
python -c "
import json, sys
sys.path.insert(0, '.')
from instantly.builder import CampaignBuilder
builder = CampaignBuilder()
result = builder.parse_generated_output('''PASTE_GENERATED_OUTPUT_HERE''')
print(json.dumps(result, indent=2))
"
```

Replace `PASTE_GENERATED_OUTPUT_HERE` with the actual generated email markdown from the conversation. Escape any single quotes in the content.

Show the parsed result to the user:
- Number of variations extracted
- Subject line and first ~50 chars of body for each
- Number of follow-up variants extracted (read from `followups[0]["variants"]`, since the default groups them as A/B variants of one step)
- Subject line (usually empty, threaded on step 1) and first ~50 chars of each follow-up variant body

Ask: "Does this look right, or should I adjust anything?"

**If parsing fails or looks wrong:** Fall back to manual extraction. Ask the user to confirm each piece:
- "What's the subject line for Variation 1?"
- "What's the body for Variation 1?"
- Repeat for each variation and follow-up.

Build the variations and followups lists manually from their answers.

## Step 3: Gather Campaign Configuration

Ask the user for the following. Show the default value in brackets. Only require what's needed.

### Required (no defaults):

1. **Campaign name** — Suggest a name based on the niche/offer from the generate step. Example: "Agency Outreach - Creative Agencies Q2". **Never prefix the name with the client.** Each Instantly workspace is dedicated to one client, so a client prefix ("Client Name - G3 Student Housing") is redundant noise. Use just the campaign identifier and title ("G3 Student Housing").

### Hardcoded defaults (do NOT ask unless the user volunteers an override):

These were explicitly set as "always" defaults by the user. Do not re-prompt every deploy.

- **Sending accounts: skipped.** Deploy without `sending_accounts` set. The user attaches inboxes in the Instantly UI before activation. Only ask if the user proactively mentions sending accounts in the request.
- **Delay between steps (follow-up): 1 day.** Use 1-day delay for the follow-up step. Don't ask unless overriding.
- **Activation: never auto-activate.** Always leave the campaign as a draft after create. Do not ask "want me to activate it now?" at the end of Step 5. The user activates manually in the Instantly UI after attaching leads and sending accounts. Only activate if the user explicitly asks ("activate it," "turn it on," "go live").

### Optional (with defaults, ask only if relevant or if multiple variants exist):

2. **API key (per-client workspace)** — Each Instantly client workspace has its own API key. Convention:
   - `.env` stores keys as `INSTANTLY_API_KEY_<CLIENT_SLUG>` (e.g. `INSTANTLY_API_KEY_CLIENT_A`, `INSTANTLY_API_KEY_CLIENT_B`).
   - Instantiate as `InstantlyClient(client="<slug>")`, never the bare `InstantlyClient()`. The plain `INSTANTLY_API_KEY` is a legacy fallback; reusing it for another client will deploy into the wrong workspace.
   - When onboarding a new client, add `INSTANTLY_API_KEY_<CLIENT_SLUG>=` to `.env` and tell the user where to paste their key.
   - If no `.env` entry exists for the requested client, ask: "Provide your Instantly API key for `<client>`, and I'll add `INSTANTLY_API_KEY_<SLUG>=` to `.env`."

3. **Schedule** — Default: Mon-Fri, 9am-5pm Eastern. Don't ask unless the user mentions schedule or timezone.

4. **Daily send limit** — Default: 2000. Matthew leaves this high on purpose and rate-limits at the sending inbox level instead. Don't ask or lower unless he says to.

5. **Tracking** — Default: both off for deliverability. Don't ask unless the user mentions tracking.

6. **Start date** — Default: today. Don't ask unless the user mentions a future start.

## Step 4: Build and Confirm

Assemble the config dict and build the payload. The builder automatically handles HTML formatting and timezone aliases.

```python
config = {
    "name": "<campaign_name>",
    "variations": [
        {"subject": "<subject>", "body": "<body>"},
        # body can be plain text — builder auto-wraps in <p> tags
    ],
    # Default: two follow-up variants as A/B of ONE step (step 2), empty subjects,
    # threaded on the step-1 send. The step delay defaults to 1 day.
    "followups": [
        {"delay": 1, "variants": [
            {"subject": "", "body": "<variant A: medium off-ramp>"},
            {"subject": "", "body": "<variant B: one-line spintax check-in, system default — see generate-email skill>"},
        ]},
    ],
    # For a genuine multi-step drip instead, pass a flat list (one step per entry):
    #   "followups": [
    #       {"subject": "<subj>", "body": "<step 2 body>", "delay": 3},
    #       {"subject": "<subj>", "body": "<step 3 body>", "delay": 4},
    #   ],
    "sending_accounts": ["<email1>", "<email2>"],
    "schedule": {"timezone": "<tz>"},
    "daily_limit": 2000,
    "open_tracking": False,
    "link_tracking": False,
}
```

Display a human-readable summary for the user to review:

```
Campaign: "<name>"
Sending from: email1@domain.com, email2@domain.com
Schedule: Mon-Fri 9am-5pm ET, starting <date>

Step 1 (Initial Email):
  Variant A: Subject "<subject>" | "<first 60 chars of body>..."
  Variant B: Subject "<subject>" | "<first 60 chars of body>..."

Step 2 (Follow-up, +1 day, threaded on step 1):
  Variant A: Subject "(empty)" | "<first 60 chars of body>..."
  Variant B: Subject "(empty)" | "<first 60 chars of body>..."

Settings: 2000/day, 5min gap, stop on reply, tracking off
```

Ask: "Ready to create this campaign? Say 'send' to deploy, or tell me what to change."

## Step 5: Deploy

Run the deployment:

```bash
python -c "
import json, sys
sys.path.insert(0, '.')
from instantly.client import InstantlyClient
from instantly.builder import CampaignBuilder

client = InstantlyClient(client="<slug>")  # see Step 3 — must pass the client slug
builder = CampaignBuilder()

config = <CONFIG_DICT>
payload = builder.build(config)
result = client.create_campaign(payload)
print(json.dumps(result, indent=2))
"
```

### Post-deploy verification (REQUIRED):

After a successful create, always fetch the campaign back and verify the body text survived:

```bash
python -c "
import json, sys, requests
sys.path.insert(0, '.')
from instantly.client import InstantlyClient
client = InstantlyClient(client="<slug>")
headers = {'Authorization': f'Bearer {client.api_key}', 'Content-Type': 'application/json'}
resp = requests.get('https://api.instantly.ai/api/v2/campaigns/<CAMPAIGN_ID>', headers=headers)
steps = resp.json()['sequences'][0]['steps']
for i, step in enumerate(steps):
    for j, v in enumerate(step['variants']):
        has_text = len(v['body']) > 50
        print(f'Step {i+1} Variant {chr(65+j)}: subject=\"{v[\"subject\"]}\" body_len={len(v[\"body\"])} has_text={has_text}')
"
```

If any body is suspiciously short or missing text, the HTML formatting was stripped. Fix by ensuring all bodies use `<p>` tags (the builder does this automatically for plain text input).

### On success:
Display the campaign ID and status. Report: "Campaign created as a draft (ID: `<id>`). Attach leads and sending accounts in the Instantly UI, then activate when ready." Do NOT ask to auto-activate (see hardcoded defaults in Step 3).

If the user later asks to activate:
```bash
python -c "
import json, sys
sys.path.insert(0, '.')
from instantly.client import InstantlyClient
client = InstantlyClient(client="<slug>")
result = client.activate_campaign('<campaign_id>')
print(json.dumps(result, indent=2))
"
```

### On failure:
Surface a clear error with guidance:
- **400 timezone**: "Timezone not accepted. The builder handles common aliases (e.g., Australia/Sydney -> Australia/Melbourne), but if you see this error, try `Australia/Melbourne` or another nearby city."
- **401**: "Authentication failed. Double-check your API key."
- **422**: "Instantly rejected the payload: <details>. Want me to fix and retry?"
- **429**: "Rate limited. Wait a moment and I'll retry."
- **5xx**: "Instantly server error. Try again in a minute."

## Step 6: Summary

Print a final summary:

```
Deployed to Instantly:
  Campaign: "<name>" (ID: <id>)
  Status: Draft / Active
  Variations: N | Follow-ups: M
  Sending from: email1, email2
  Schedule: Mon-Fri 9am-5pm ET
  Starting: <date>
```

## Important Notes

- **Always confirm before sending.** The user must see and approve the payload before it hits the API. Cold email campaigns are high-stakes.
- **Tracking defaults to off.** Open/link tracking hurts deliverability. Only enable if the user explicitly asks.
- **Template variables** like `{{firstName}}`, `{{shortCompany}}`, `{{icebreaker}}` pass through as-is. Instantly uses the same double-curly-brace syntax.
- **Body formatting is automatic.** The builder's `_build_sequences` method auto-detects plain text bodies (no `<p>` or `<div>` tags) and wraps them in Gmail-style `<div>` blocks via `format_body_for_instantly` (see gotcha #1). Pre-formatted HTML passes through unchanged.
