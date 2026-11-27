#!/usr/bin/env python3
"""How many items carry a project fit, per Morning Brew post.

The writer used to answer "Nothing for my projects" for 93% of items. This prints the count
per post and the average over the last N, so a change to the prompt or the project inventory
can be judged by a number instead of a feeling.

Usage: uv run pipeline/fit_report.py [--last N] [--dir content]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gate import fit_counts  # noqa: E402
from lib.config import expand, load_config  # noqa: E402
from lib.publish import strip_frontmatter  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--last", type=int, default=10)
    ap.add_argument("--dir", default=None, help="content directory (default: the blog repo)")
    args = ap.parse_args(argv)

    cfg = load_config()
    content = Path(args.dir) if args.dir else expand(cfg["paths"]["blog_repo"]) / "content"
    posts = sorted(content.glob("*-morning-brew.md"))[-args.last:]
    if not posts:
        print(f"no posts in {content}", file=sys.stderr)
        return 1

    total = fitted = sparks = 0
    print(f"{'post':<12} {'items':>5} {'direct':>6} {'cond':>5} {'none':>5} {'reasoned':>8} "
          f"{'spark':>6} {'fit%':>5}")
    for path in posts:
        body = strip_frontmatter(path.read_text())
        c = fit_counts(body)
        items = c["direct"] + c["conditional"] + c["none"]
        fit = c["direct"] + c["conditional"]
        total += items
        fitted += fit
        sparks += c["spark"]
        pct = f"{100 * fit / items:.0f}%" if items else "-"
        print(f"{path.name[:12]:<12} {items:>5} {c['direct']:>6} {c['conditional']:>5} "
              f"{c['none']:>5} {c['reasoned_none']:>8} {c['spark']:>6} {pct:>5}")

    pct = f"{100 * fitted / total:.0f}%" if total else "-"
    print(f"{'TOTAL':<12} {total:>5} {'':>6} {'':>5} {'':>5} {'':>8} {sparks:>6} {pct:>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
