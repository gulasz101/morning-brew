"""Assemble the two notes, publish through git, and check the live page."""

from __future__ import annotations

import difflib
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)


def frontmatter(day: str, tags: list[str]) -> str:
    slug = f"{day}-morning-brew"
    return (
        "---\n"
        f"date: {day}\n"
        f"slug: {slug}\n"
        f"tags: {', '.join(tags)}\n"
        "---\n"
    )


def _body(intro: str, body: str) -> str:
    return f"{intro.strip()}\n\n{body.rstrip()}\n"


def build_post(day: str, intro: str, body: str, tags: list[str]) -> str:
    return frontmatter(day, tags) + "\n" + _body(intro, body)


def build_vault_note(day: str, intro: str, body: str) -> str:
    """The vault note is the post body, byte for byte. The gate proves it."""
    return _body(intro, body)


def body_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a, b).ratio()


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :]
    return text


def numbering_problems(body: str) -> list[str]:
    nums = [int(n) for n in re.findall(r"^## (\d+)\. ", body, re.MULTILINE)]
    problems = []
    if nums != list(range(1, len(nums) + 1)):
        problems.append(f"section numbers are not 1..N in file order: {nums[:25]}")
    dupes = {n for n in nums if nums.count(n) > 1}
    if dupes:
        problems.append(f"duplicate section numbers: {sorted(dupes)}")
    return problems


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    tmp.replace(path)


def git_publish(repo: Path, rel: str, message: str, dry_run: bool) -> tuple[bool, str]:
    if dry_run:
        return True, "dry-run: nothing committed"
    cmds = [
        ["git", "-C", str(repo), "add", rel],
        ["git", "-C", str(repo), "commit", "-m", message],
        ["git", "-C", str(repo), "push", "origin", "HEAD"],
    ]
    for cmd in cmds:
        out = subprocess.run(cmd, capture_output=True, text=True)
        if out.returncode != 0:
            return False, f"{' '.join(cmd[:3])} failed: {(out.stderr or out.stdout).strip()[:400]}"
    return True, "committed and pushed"


def live_check(url: str, tries: int = 20, wait: float = 15.0) -> tuple[bool, str]:
    """Poll the published page until it answers 200, or give up."""
    last = ""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status == 200:
                    return True, f"live after {attempt * wait:.0f}s"
                last = f"HTTP {r.status}"
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
        except Exception as exc:  # network
            last = str(exc)[:120]
        time.sleep(wait)
    return False, f"not live after {tries * wait:.0f}s: {last}"
