import re
from datetime import date


# Instantly's API only accepts a fixed allowlist of timezone strings. Map the
# common rejected names to the accepted-equivalent city.
TIMEZONE_ALIASES = {
    "Australia/Sydney": "Australia/Melbourne",
    "Australia/ACT": "Australia/Melbourne",
    "Australia/NSW": "Australia/Melbourne",
    "Australia/Canberra": "Australia/Melbourne",
    "America/New_York": "America/Detroit",
    # Europe/London is rejected by Instantly's allowlist. Europe/Isle_of_Man
    # is the accepted UK equivalent (same GMT/BST clock).
    "Europe/London": "Europe/Isle_of_Man",
    "GB": "Europe/Isle_of_Man",
    "Europe/Belfast": "Europe/Isle_of_Man",
    "Europe/Guernsey": "Europe/Isle_of_Man",
    "Europe/Jersey": "Europe/Isle_of_Man",
}


def format_body_for_instantly(text):
    """Convert plain text to Gmail-style HTML that Instantly preserves on refresh.

    Two Instantly quirks combine here:

    1. Bare <br> tags cause the API to silently strip ALL body text. Content
       must live inside block-level tags (<p>, <div>).
    2. <p>...</p><p>...</p> survives the write but the editor's normalizer
       (which targets Gmail-style HTML, per the Clean HTML help article)
       collapses the margins on refresh, so the email renders as one
       bunched-up wall of text.

    Gmail's compose editor itself uses <div> blocks with <div><br></div>
    spacers between paragraphs. Producing that exact shape sidesteps the
    normalizer and the spacing survives a page refresh.

    Output shape for "A\\n\\nB\\n\\nC":
        <div>A</div><div><br></div><div>B</div><div><br></div><div>C</div>
    """
    text = text.strip()
    paragraphs = text.split("\n\n")
    blocks = []
    for i, p in enumerate(paragraphs):
        if i > 0:
            blocks.append("<div><br></div>")
        inner = p.replace("\n", "<br>")
        blocks.append(f"<div>{inner}</div>")
    return "".join(blocks)


class CampaignBuilder:
    DEFAULT_SCHEDULE = {
        "schedules": [
            {
                "name": "Default Schedule",
                "timing": {"from": "08:15", "to": "17:00"},
                "days": {
                    "0": False,
                    "1": True,
                    "2": True,
                    "3": True,
                    "4": True,
                    "5": True,
                    "6": False,
                },
                "timezone": "America/Detroit",
            }
        ],
        "start_date": None,
        "end_date": None,
    }

    # Gap between initial email and first follow-up. Default 1 day for tight cadence.
    DEFAULT_DELAY = 1
    DEFAULT_DELAY_UNIT = "days"
    # Daily caps left high on purpose; rate limiting is configured at the
    # sending-inbox level inside Instantly, not at the campaign level.
    DEFAULT_DAILY_LIMIT = 2000
    DEFAULT_DAILY_MAX_LEADS = 2000
    DEFAULT_EMAIL_GAP = 5
    DEFAULT_RANDOM_WAIT_MAX = 10
    # Workspace-agnostic inbox tags. Every Instantly workspace tags its inboxes
    # with these so campaigns can pull groups without hardcoding addresses.
    DEFAULT_SENDING_ACCOUNT_TAGS = ["Cohort A", "Cohort B"]
    # Text-only on by default for deliverability — HTML tracking pixels and
    # styled emails get flagged harder than plain text.
    DEFAULT_TEXT_ONLY = True

    def build(self, config):
        sequences = self._build_sequences(
            config["variations"], config.get("followups", [])
        )
        schedule = self._build_schedule(config.get("schedule"))

        payload = {
            "name": config["name"],
            "campaign_schedule": schedule,
            "sequences": sequences,
            "stop_on_reply": config.get("stop_on_reply", True),
            "stop_on_auto_reply": config.get("stop_on_auto_reply", False),
            "stop_for_company": config.get("stop_for_company", True),
            "daily_limit": config.get("daily_limit", self.DEFAULT_DAILY_LIMIT),
            "daily_max_leads": config.get("daily_max_leads", self.DEFAULT_DAILY_MAX_LEADS),
            "email_gap": config.get("email_gap", self.DEFAULT_EMAIL_GAP),
            "random_wait_max": config.get("random_wait_max", self.DEFAULT_RANDOM_WAIT_MAX),
            "open_tracking": config.get("open_tracking", False),
            "link_tracking": config.get("link_tracking", False),
            "text_only": config.get("text_only", self.DEFAULT_TEXT_ONLY),
            "email_tag_list": config.get(
                "sending_account_tags", self.DEFAULT_SENDING_ACCOUNT_TAGS
            ),
        }

        if config.get("sending_accounts"):
            payload["email_list"] = config["sending_accounts"]

        return payload

    def _build_sequences(self, variations, followups):
        # Step 0: all variations become variants in the first step
        step_0_variants = []
        for v in variations:
            body = v["body"]
            # Auto-format plain text bodies to Gmail-style <div> HTML
            if "<p>" not in body and "<div>" not in body:
                body = format_body_for_instantly(body)
            step_0_variants.append({
                "subject": v["subject"],
                "body": body,
            })

        # Step delay is the gap until the NEXT step. With no follow-up,
        # there is no next step, so the delay is meaningless — but Instantly
        # persists the value and applies it if a step is added later in the UI.
        # Use 0 to avoid surprising the user with a 3-day default they never set.
        if followups:
            first_followup_delay = followups[0].get("delay", self.DEFAULT_DELAY)
            first_followup_delay_unit = followups[0].get("delay_unit", self.DEFAULT_DELAY_UNIT)
        else:
            first_followup_delay = 0
            first_followup_delay_unit = self.DEFAULT_DELAY_UNIT

        steps = [
            {
                "type": "email",
                "delay": first_followup_delay,
                "delay_unit": first_followup_delay_unit,
                "variants": step_0_variants,
            }
        ]

        # Steps 1+: each follow-up becomes its own step. A follow-up may carry a
        # single body (subject/body keys) or multiple A/B variants of that step
        # (a "variants" list); the latter is how Instantly rotates two follow-up
        # reads threaded on the same step-1 send.
        for i, fu in enumerate(followups):
            next_fu = followups[i + 1] if i + 1 < len(followups) else None
            next_delay = next_fu.get("delay", self.DEFAULT_DELAY) if next_fu else 0
            next_delay_unit = next_fu.get("delay_unit", self.DEFAULT_DELAY_UNIT) if next_fu else self.DEFAULT_DELAY_UNIT

            if fu.get("variants"):
                raw_variants = fu["variants"]
            else:
                raw_variants = [{"subject": fu.get("subject", ""), "body": fu["body"]}]

            step_variants = []
            for var in raw_variants:
                body = var["body"]
                # Auto-format plain text bodies to Gmail-style <div> HTML
                if "<p>" not in body and "<div>" not in body:
                    body = format_body_for_instantly(body)
                step_variants.append({
                    "subject": var.get("subject", ""),
                    "body": body,
                })

            steps.append({
                "type": "email",
                "delay": next_delay,
                "delay_unit": next_delay_unit,
                "variants": step_variants,
            })

        return [{"steps": steps}]

    def _build_schedule(self, overrides=None):
        schedule = {
            "schedules": [dict(s) for s in self.DEFAULT_SCHEDULE["schedules"]],
            "start_date": self.DEFAULT_SCHEDULE["start_date"],
            "end_date": self.DEFAULT_SCHEDULE["end_date"],
        }
        # Deep copy the nested dicts
        schedule["schedules"][0] = {
            "name": self.DEFAULT_SCHEDULE["schedules"][0]["name"],
            "timing": dict(self.DEFAULT_SCHEDULE["schedules"][0]["timing"]),
            "days": dict(self.DEFAULT_SCHEDULE["schedules"][0]["days"]),
            "timezone": self.DEFAULT_SCHEDULE["schedules"][0]["timezone"],
        }

        if overrides:
            if "timezone" in overrides:
                tz = overrides["timezone"]
                # Apply known aliases for timezones Instantly rejects
                tz = TIMEZONE_ALIASES.get(tz, tz)
                schedule["schedules"][0]["timezone"] = tz
            if "from" in overrides:
                schedule["schedules"][0]["timing"]["from"] = overrides["from"]
            if "to" in overrides:
                schedule["schedules"][0]["timing"]["to"] = overrides["to"]
            if "days" in overrides:
                schedule["schedules"][0]["days"] = overrides["days"]
            if "start_date" in overrides:
                schedule["start_date"] = overrides["start_date"]
            if "end_date" in overrides:
                schedule["end_date"] = overrides["end_date"]
            if "name" in overrides:
                schedule["schedules"][0]["name"] = overrides["name"]

        # Default start_date to today if not set
        if not schedule["start_date"]:
            schedule["start_date"] = date.today().isoformat()

        return schedule

    def parse_generated_output(self, raw_text):
        variations = []
        followup_variants = []

        # Split into sections by ### headers
        sections = re.split(r"(?=^###\s)", raw_text, flags=re.MULTILINE)

        for section in sections:
            section = section.strip()
            if not section:
                continue

            # Match variation sections
            if re.match(r"###\s*Variation", section, re.IGNORECASE):
                subject = self._extract_subject(section)
                body = self._extract_body(section)
                if subject is not None and body:
                    variations.append({"subject": subject, "body": body})

            # Match follow-up sections
            elif re.match(r"###\s*Follow[\s-]?[Uu]p", section, re.IGNORECASE):
                subject = self._extract_subject(section)
                body = self._extract_followup_body(section)
                if body:
                    # Follow-ups default to an empty subject so Instantly threads
                    # them on the step-1 send. A missing subject, or an italic
                    # annotation like "*(empty, replies on the step-1 thread)*",
                    # both normalize to "".
                    if subject is None or subject.startswith("*("):
                        subject = ""
                    followup_variants.append({"subject": subject, "body": body})

        # The generate-email default is the two-variant follow-up pattern: each
        # follow-up read is an A/B variant of a SINGLE follow-up step (step 2),
        # not a sequential drip, so they all thread on the step-1 send. Group
        # them into one step here. (Clients that genuinely want a multi-step
        # drip pass a flat followups list of their own.)
        followups = [{"variants": followup_variants}] if followup_variants else []

        return {"variations": variations, "followups": followups}

    def _extract_subject(self, section):
        # [ \t]* (not \s*) so a blank "**Subject:**" line doesn't let (.+) skip
        # the newline and capture the first body line as the subject.
        match = re.search(
            r"\*\*Subject(?:\s*[Ll]ine)?:\*\*[ \t]*(.+)", section
        )
        if match:
            subject = match.group(1).strip()
            # Remove surrounding backticks or quotes
            subject = re.sub(r"^[`\"']|[`\"']$", "", subject).strip()
            return subject
        return None

    def _extract_body(self, section):
        lines = section.split("\n")
        body_lines = []
        capturing = False

        for line in lines:
            # Skip the header line
            if re.match(r"###\s", line):
                continue
            # Skip subject line
            if re.match(r"\*\*Subject", line):
                capturing = True
                continue
            # Skip score line
            if re.match(r"\*\*Score", line):
                continue
            # Stop at explanation sections
            if re.match(r"\*\*(Inspired|Offer|Best|Archetype|Explanation)", line):
                break
            if re.match(r"---", line):
                break

            if capturing:
                body_lines.append(line)

        body = "\n".join(body_lines).strip()
        # Remove markdown code fences if the body is wrapped in them
        body = re.sub(r"^```[^\n]*\n?", "", body)
        body = re.sub(r"\n?```$", "", body)
        return body.strip()

    def _extract_followup_body(self, section):
        lines = section.split("\n")
        body_lines = []
        capturing = False

        for line in lines:
            if re.match(r"###\s", line):
                capturing = True
                continue
            # Skip pairing info like "(pairs with Variations 1 & 2)"
            if capturing and not body_lines and re.match(r"\s*\(", line):
                continue
            # Skip subject line if present
            if re.match(r"\*\*Subject", line):
                continue
            # Stop at explanation sections
            if re.match(r"\*\*(Inspired|Offer|Best|Archetype|Explanation)", line):
                break
            if re.match(r"---", line):
                break

            if capturing:
                body_lines.append(line)

        body = "\n".join(body_lines).strip()
        body = re.sub(r"^```[^\n]*\n?", "", body)
        body = re.sub(r"\n?```$", "", body)
        return body.strip()
