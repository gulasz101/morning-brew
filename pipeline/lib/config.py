"""Config + environment loading. No secrets live in the repo or in the config file."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.toml"


class ConfigError(RuntimeError):
    pass


def expand(p: str) -> Path:
    return Path(os.path.expanduser(p))


def load_config(path: Path | None = None) -> dict:
    path = path or CONFIG_PATH
    with open(path, "rb") as fh:
        cfg = tomllib.load(fh)
    for key in ("vault_root", "blog_repo", "skill_md", "processor", "enrich"):
        cfg["paths"][key] = str(expand(cfg["paths"][key]))
    return cfg


def require_env(name: str, why: str) -> str:
    """Read a credential from the environment or stop with a clear message.

    There are deliberately no literal fallbacks here: this repo is public.
    """
    value = os.environ.get(name, "").strip()
    if not value:
        raise ConfigError(
            f"{name} is not set. {why} Export it and run again, for example:\n"
            f"  export {name}=...   # see pipeline/README.md"
        )
    return value
