"""Validator, voice lint and template render for one Morning Brew item."""

from __future__ import annotations

import re
from pathlib import Path

BANNED_PATH = Path(__file__).resolve().parent.parent / "prompts" / "banned.txt"

# Characters the lint refuses as dashes. Em dash and en dash only.
BAD_DASHES = ("\u2014", "\u2013")

# "not X, but Y" and its cousins.
CONTRAST_RE = re.compile(
    r"\bnot\s+(?:just\s+|only\s+)?[\w\s\-,]{1,40}?\bbut\b"
    r"|\bisn't\s+[\w\s\-,]{1,40}?\bit'?s\b"
    r"|\bthe question isn'?t\b",
    re.IGNORECASE,
)

MIN_KEY_POINTS, MAX_KEY_POINTS = 3, 6
MIN_DETAILS_WORDS, MAX_DETAILS_WORDS = 80, 200
MAX_DETAILS_WORDS_VIDEO = 300
MAX_IDEAS = 2


def load_banned(path: Path | None = None) -> list[str]:
    path = path or BANNED_PATH
    out = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line.lower())
    return out


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9'’\-]+", text or ""))


def validate(item: dict, n_candidates: int, allowed_projects: list[str], is_video: bool,
             is_roundup: bool) -> list[str]:
    """Everything the writer's reply must satisfy. Returns a list of readable errors."""
    errors: list[str] = []
    if not isinstance(item, dict):
        return ["the reply is not a JSON object"]

    short = item.get("in_short")
    if not isinstance(short, str) or not short.strip():
        errors.append("in_short must be a non-empty string")
    elif word_count(short) > 70:
        errors.append(f"in_short is {word_count(short)} words, keep it to 1-2 sentences (max 70)")

    points = item.get("key_points")
    if not isinstance(points, list):
        errors.append("key_points must be a list of strings")
    else:
        if not MIN_KEY_POINTS <= len(points) <= MAX_KEY_POINTS:
            errors.append(f"key_points has {len(points)} entries, need {MIN_KEY_POINTS}-{MAX_KEY_POINTS}")
        for i, p in enumerate(points, 1):
            if not isinstance(p, str) or not p.strip():
                errors.append(f"key_points[{i}] must be a non-empty string")
            elif len(p.split()) > 40:
                errors.append(f"key_points[{i}] is {len(p.split())} words, keep a bullet under 40")

    details = item.get("details")
    hi = MAX_DETAILS_WORDS_VIDEO if is_video else MAX_DETAILS_WORDS
    if not isinstance(details, str) or not details.strip():
        errors.append("details must be a non-empty string")
    else:
        n = word_count(details)
        if n < MIN_DETAILS_WORDS:
            errors.append(f"details is {n} words, need at least {MIN_DETAILS_WORDS}")
        if n > hi:
            errors.append(f"details is {n} words, the limit is {hi}{' for a video' if is_video else ''}")

    ideas = item.get("ideas", [])
    if not isinstance(ideas, list):
        errors.append("ideas must be a list (possibly empty)")
    else:
        if len(ideas) > MAX_IDEAS:
            errors.append(f"ideas has {len(ideas)} entries, at most {MAX_IDEAS}")
        for i, idea in enumerate(ideas, 1):
            if not isinstance(idea, dict):
                errors.append(f"ideas[{i}] must be an object with project and idea")
                continue
            proj = idea.get("project")
            if proj not in allowed_projects:
                errors.append(
                    f"ideas[{i}].project '{proj}' is not one of {', '.join(allowed_projects)}"
                )
            if not isinstance(idea.get("idea"), str) or not idea["idea"].strip():
                errors.append(f"ideas[{i}].idea must be a non-empty concrete sentence")

    plinks = item.get("project_links", [])
    if not isinstance(plinks, list):
        errors.append("project_links must be a list of candidate numbers")
    else:
        for i, n in enumerate(plinks, 1):
            if not isinstance(n, int) or isinstance(n, bool):
                errors.append(f"project_links[{i}] is not a whole number")
            elif n < 1 or n > n_candidates:
                errors.append(f"project_links[{i}] = {n} is outside 1..{n_candidates}")

    if is_roundup:
        names = item.get("projects")
        if not isinstance(names, list):
            errors.append("this is a roundup: projects must be a list of project names")
        elif isinstance(names, list):
            if not 2 <= len(names) <= 14:
                errors.append(f"projects has {len(names)} names, need 2-14")
            for i, n in enumerate(names, 1):
                if not isinstance(n, str) or not n.strip():
                    errors.append(f"projects[{i}] must be a project name")
    return errors


def lint(text: str, banned: list[str] | None = None) -> list[str]:
    """Voice lint on rendered text. Em/en dashes, banned words, contrasts, third person."""
    banned = banned if banned is not None else load_banned()
    problems: list[str] = []
    low = text.lower()
    for dash in BAD_DASHES:
        if dash in text:
            problems.append(f"dash: '{dash}' (use a comma or a full stop)")
    for phrase in banned:
        if re.search(r"(?<![a-z0-9])" + re.escape(phrase) + r"(?![a-z0-9])", low):
            problems.append(f"banned word/phrase: '{phrase}'")
    m = CONTRAST_RE.search(text)
    if m:
        problems.append(f"'not X, but Y' contrast: '{m.group(0).strip()}'")
    if "wojtek cares" in low:
        problems.append("'Wojtek cares because' filler")
    if re.search(r"\bwojtek\b", low):
        problems.append("third person: 'Wojtek' (write in first person)")
    if re.search(r"\bi (tried|ran|installed|tested|benchmarked|use[d]?)\b", low):
        problems.append("claims a hands-on trial: I only read about it")
    return problems


def render(index: int, item: dict, meta: dict, links: list[dict],
           resolved_projects: list[dict] | None = None) -> str:
    """The fixed item template. No dashes, no invented URLs."""
    title = meta["title"].strip()
    source = meta["source"].strip()
    lines = [f"## {index}. {title}, by {source}"]
    if meta.get("image"):
        lines.append(f"![]({meta['image']})")
    picks = [links[n - 1] for n in item.get("project_links", []) if 1 <= n <= len(links)]
    if picks:
        first = picks[0]
        line = f"**Project:** [{_name_of(first)}]({first['url']})"
        if len(picks) > 1:
            extra = ", ".join(f"[{_name_of(p)}]({p['url']})" for p in picks[1:])
            lines.append(f"{line}, also {extra}")
        else:
            lines.append(line)
    lines.append(f"**Source:** {meta['url']} · **Karakeep:** `{meta['id']}`")
    lines.append("")
    lines.append(f"**In short:** {item['in_short'].strip()}")
    lines.append("")
    lines.append("**Key points:**")
    lines.extend(f"- {p.strip()}" for p in item["key_points"])
    lines.append("")
    lines.append(f"**Details:** {item['details'].strip()}")
    lines.append("")
    ideas = item.get("ideas") or []
    if ideas:
        lines.append("**For my projects:**")
        for idea in ideas:
            lines.append(f"- {idea['project']}: {idea['idea'].strip()}")
    else:
        lines.append("**For my projects:** Nothing for my projects.")
    if resolved_projects:
        lines.append("")
        lines.append("**Projects:**")
        for row in resolved_projects:
            blurb = row.get("what") or ""
            bits = f"- [{row['name']}]({row['url']})"
            lines.append(f"{bits}: {blurb}" if blurb else bits)
    return "\n".join(lines).rstrip() + "\n"


def render_probe(data: dict, allowed: list[str]) -> str:
    """A complete block with placeholder header fields, so the lint sees every word
    the writer produced plus the fixed template text around it."""
    probe = dict(data)
    probe.setdefault("in_short", "")
    probe.setdefault("key_points", [])
    probe.setdefault("details", "")
    meta = {"title": "Title", "source": "source", "url": "https://example.invalid",
            "id": "id", "image": ""}
    links = [{"label": "project", "url": "https://example.invalid", "code": True,
              "where": "test"}]
    probe.setdefault("project_links", [])
    return render(1, probe, meta, links)


def _name_of(row: dict) -> str:
    label = (row.get("label") or "").strip()
    if "/" in label and row.get("code"):
        return label.split("/")[-1]
    return label or "project"
