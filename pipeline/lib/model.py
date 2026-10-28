"""Writer model client: one item per call, JSON only out."""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request


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


class Writer:
    def __init__(self, model: str, base_url: str, api_key: str, timeout: int = 240):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

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
            raise ModelError(f"writer call failed: {exc}") from exc
        try:
            choice = body["choices"][0]
            content = choice["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ModelError(f"unexpected reply shape: {str(body)[:200]}") from exc
        # A reasoning model that spends the whole budget on thinking answers
        # finish_reason "length" with content null. That is a failed item, not a blank
        # reply: return nothing here and the item disappears from report.json.
        finish = choice.get("finish_reason")
        if content is None or not str(content).strip():
            raise ModelError(
                f"empty reply from the writer model (finish_reason={finish!r}); "
                "the model spent its max_tokens without answering"
            )
        if finish == "length":
            raise ModelError(
                f"reply truncated at max_tokens (finish_reason={finish!r}); "
                f"{len(str(content))} chars came back and it may be invalid JSON"
            )
        return content
