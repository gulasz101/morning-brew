"""Writer model client: one item per call, JSON only out."""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

# Cloudflare sits in front of llm.voitech.dev and answers HTTP 524 at ~100 s of origin
# time. A client timeout above that never fires: you wait for the edge and get an
# unhelpful error page instead of a retryable failure. See pipeline/README.md.
EDGE_TIMEOUT_SEC = 100
EDGE_MARGIN_SEC = 5


class ModelError(RuntimeError):
    pass


def _strip_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return text.strip()


def extract_json(text: str) -> dict:
    """Pull the first JSON object out of a model reply. Raises ModelError."""
    if not isinstance(text, str) or not text.strip():
        raise ModelError(f"empty reply: expected JSON, got {type(text).__name__}")
    body = _strip_fence(text)
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        pass
    start = body.find("{")
    if start < 0:
        raise ModelError("no JSON object in the reply")
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(body)):
        ch = body[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(body[start : i + 1])
                except json.JSONDecodeError as exc:
                    raise ModelError(f"bad JSON: {exc}") from exc
    raise ModelError("unterminated JSON object in the reply")


def _budget_note(body: dict) -> str:
    """Token accounting for an error message. Never a credential."""
    usage = body.get("usage") or {}
    bits = [f"{key}={usage[key]}" for key in
            ("prompt_tokens", "completion_tokens", "total_tokens")
            if usage.get(key) is not None]
    details = usage.get("completion_tokens_details") or {}
    if details.get("reasoning_tokens") is not None:
        bits.append(f"reasoning_tokens={details['reasoning_tokens']}")
    return ", ".join(bits) or "no usage in the reply"


class Writer:
    def __init__(self, model: str, base_url: str, api_key: str,
                 timeout: int | None = None):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        # Never wait past the edge: a 524 is a hang with a nicer error page.
        self.timeout = int(timeout or (EDGE_TIMEOUT_SEC - EDGE_MARGIN_SEC))

    def call(self, system: str, user: str, max_tokens: int = 2000) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.7,
            "max_tokens": max_tokens,
            "response_format": {"type": "json_object"},
        }
        req = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode(),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                # Cloudflare in front of llm.voitech.dev rejects the default urllib UA (403/1010).
                "User-Agent": "morning-brew-pipeline/0.1 (+https://gulasz101.github.io/morning-brew)",
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                body = json.load(r)
        except urllib.error.HTTPError as exc:
            detail = exc.read()[:300].decode("utf-8", "replace")
            raise ModelError(f"HTTP {exc.code} from the writer model: {detail}") from exc
        except Exception as exc:  # network, timeout
            raise ModelError(
                f"writer call failed inside the {self.timeout}s budget "
                f"(the edge cuts at {EDGE_TIMEOUT_SEC}s): {exc}"
            ) from exc
        try:
            choice = body["choices"][0]
            finish = choice.get("finish_reason")
            content = (choice.get("message") or {}).get("content")
        except (KeyError, IndexError, TypeError) as exc:
            raise ModelError(f"unexpected reply shape: {str(body)[:200]}") from exc

        # A reasoning model that spends the whole budget thinking answers
        # finish_reason="length" with content=null. That must become a visible, retried
        # drop with a reason, never an item that quietly disappears from report.json.
        if finish == "length":
            raise ModelError(
                "reply hit the token limit before writing the answer "
                f"(finish_reason=length, {_budget_note(body)})"
            )
        if finish in ("content_filter", "content_filtered"):
            raise ModelError(f"reply blocked by the provider (finish_reason={finish})")
        if not isinstance(content, str) or not content.strip():
            raise ModelError(
                f"empty reply: content is {type(content).__name__}, "
                f"finish_reason={finish!r} ({_budget_note(body)})"
            )
        return content
