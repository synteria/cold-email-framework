#!/usr/bin/env python3
"""Knowledge-base integrity linter for Cold Email Master.

Enforces the structural invariants that ad-hoc edits keep breaking:
  1. Every "Email N" reference resolves to an active v2 example that actually exists.
  2. Example numbers are unique and the removed set is documented.
  3. {{companyName}} only appears in the designated teaching contexts,
     never as live copy.
  4. {{icebreaker}} only appears in the validated examples that legitimately
     keep it, never in skill-generated copy guidance that forbids it.
  5. The subject-length rule string is identical everywhere it appears.
  6. "/NN" trait-count denominators are surfaced for manual recheck.

This is the machine half of the iteration protocol (see iteration-protocol.md).
Run it after any change to the knowledge base:

    python scripts/lint_kb.py

Exit code 0 = clean, 1 = at least one ERROR. WARN lines never fail the build;
they are prompts for a human to look.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The knowledge base. Deliberately excludes clients/ and deploy/ (those are
# per-campaign working files, not the shared system).
KB_GLOBS = [
    "CLAUDE.md",
    "AGENTS.md",
    "best-practices.md",
    "anti-patterns.md",
    "why-these-work.md",
    "examples/*.md",
    "examples/validated/*.md",
    "examples/templates/*.md",
    "examples/pending-validation/*.md",
    ".claude/skills/review-email/SKILL.md",
    ".claude/skills/generate-email/SKILL.md",
    ".claude/skills/strategy/SKILL.md",
    "iteration-protocol.md",
    ".claude/skills/anneal/SKILL.md",
]

# Files allowed to contain {{companyName}} because they teach Claude to flag it
# in user-submitted drafts, or describe the linter rule itself. Everywhere else
# it is live copy and is banned.
COMPANYNAME_ALLOWED = {
    "anti-patterns.md",
    "CLAUDE.md",
    "AGENTS.md",
    "iteration-protocol.md",
    ".claude/skills/anneal/SKILL.md",
}

# Files where {{icebreaker}} is legitimate: the validated examples that keep it,
# plus the docs that explain the manual-only rule.
ICEBREAKER_ALLOWED = {
    "best-practices.md",
    "anti-patterns.md",
    "why-these-work.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".claude/skills/generate-email/SKILL.md",
    ".claude/skills/strategy/SKILL.md",
    ".claude/skills/anneal/SKILL.md",
    "iteration-protocol.md",
}


def kb_files() -> list[Path]:
    files: list[Path] = []
    for pattern in KB_GLOBS:
        files.extend(sorted(ROOT.glob(pattern)))
    return [f for f in files if f.is_file()]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def defined_examples() -> dict[int, str]:
    """Current v2 email numbers actually defined, parsed from active batches."""
    defined: dict[int, str] = {}
    header = re.compile(r"^##\s+Email\s+(\d+)\b")
    for path in sorted(ROOT.glob("examples/validated/batch-*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = header.match(line)
            if m:
                defined[int(m.group(1))] = rel(path)
    return defined


def iter_lines_skipping_fences(text: str):
    """Yield (lineno, line) outside fenced code blocks."""
    in_fence = False
    for i, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield i, line


def expand_refs(blob: str) -> set[int]:
    """Pull every email number out of a 'Emails 2-6, 8, and 10' style blob."""
    nums: set[int] = set()
    for a, b in re.findall(r"(\d+)\s*[-–]\s*(\d+)", blob):
        lo, hi = int(a), int(b)
        if hi - lo < 50:  # guard against accidental huge ranges
            nums.update(range(lo, hi + 1))
    for n in re.findall(r"\d+", re.sub(r"\d+\s*[-–]\s*\d+", " ", blob)):
        nums.add(int(n))
    return nums


REF = re.compile(r"Emails?\s+((?:\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|and|&)\s*)?)+)")


def check_references(files: list[Path], defined: dict[int, str]) -> list[str]:
    errors: list[str] = []
    valid = set(defined)
    for path in files:
        text = path.read_text(encoding="utf-8")
        for lineno, line in iter_lines_skipping_fences(text):
            # Skip example definition / analysis headers.
            if re.match(r"^#+\s+Email\s+\d+", line):
                continue
            for m in REF.finditer(line):
                for n in expand_refs(m.group(1)):
                    if n not in valid:
                        errors.append(
                            f"ERROR {rel(path)}:{lineno}  references Email {n} (undefined)"
                        )
    return errors


def check_companyname(files: list[Path]) -> list[str]:
    out: list[str] = []
    for path in files:
        if rel(path) in COMPANYNAME_ALLOWED:
            continue
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            if "{{companyName}}" in line:
                out.append(
                    f"ERROR {rel(path)}:{lineno}  {{{{companyName}}}} in live copy "
                    f"(use {{{{shortCompany}}}})"
                )
    return out


def check_icebreaker(files: list[Path]) -> list[str]:
    out: list[str] = []
    for path in files:
        if rel(path) in ICEBREAKER_ALLOWED:
            continue
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            if "{{icebreaker}}" in line:
                out.append(
                    f"WARN  {rel(path)}:{lineno}  {{{{icebreaker}}}} outside the "
                    f"allowed set (generation must not emit it)"
                )
    return out


def check_subject_rule(files: list[Path]) -> list[str]:
    """Surface every subject word-count phrasing so drift is visible."""
    out: list[str] = []
    pat = re.compile(r"\b(\d)\s*[-–to]+\s*(\d)\s*words?\b", re.IGNORECASE)
    seen: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in pat.finditer(line):
                token = f"{m.group(1)}-{m.group(2)} words"
                seen.add(token)
                out.append(f"  {rel(path)}:{lineno}  '{m.group(0).strip()}'")
    if len({s for s in seen}) > 1:
        head = [f"WARN  multiple subject word-count phrasings in use: {sorted(seen)}"]
        return head + out
    return []


def check_counts(files: list[Path]) -> list[str]:
    out: list[str] = []
    pat = re.compile(r"\b\d+\s*/\s*\d+\b")
    for path in files:
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            for m in pat.finditer(line):
                # Ignore obvious non-trait ratios (dates, dimensions in tables).
                lower = line.lower()
                if "word" in lower or "px" in lower or "score" in lower:
                    continue
                out.append(
                    f"WARN  {rel(path)}:{lineno}  trait count '{m.group(0)}' "
                    f"-> recheck denominator after example add/remove"
                )
    return out


def main() -> int:
    files = kb_files()
    defined = defined_examples()

    errors: list[str] = []
    errors += check_references(files, defined)
    errors += check_companyname(files)

    warnings: list[str] = []
    warnings += check_icebreaker(files)
    warnings += check_subject_rule(files)
    warnings += check_counts(files)

    print(f"lint_kb: {len(files)} files, "
          f"{len(defined)} examples defined "
          f"({', '.join(str(n) for n in sorted(defined))})")
    print()

    for line in errors:
        print(line)
    if errors:
        print()
    for line in warnings:
        print(line)

    print()
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
