#!/usr/bin/env python3
"""Extract the real GitHub repo behind opensourceprojects.dev / linuxlinks.com
bookmarks and fetch structured metadata from the GitHub REST API.

Usage:
  python3 extract_github_repos.py <union.json> [--out /tmp/kk_run/<date>/repo_meta.json]

<union.json> is the domain-union bookmark dump (a dict with a "bookmarks" key,
see the truncation pitfall in SKILL.md). For each bookmark whose URL is on
opensourceprojects.dev or linuxlinks.com, this script:
  1. recovers the repo path (opensourceprojects.dev: from content.imageUrl's
     opengraph.githubassets.com/1/<owner>/<repo>; linuxlinks: by curling the
     article body and grepping github.com/<owner>/<repo>),
  2. fetches GitHub API metadata (description, stars, language, license, html_url).

Stdlib only (json, re, urllib). Prints a per-repo table and writes JSON.
"""
import json, re, sys, time, urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
GH_UA = "hermes"

NOISE = {"issues","pulls","releases","actions","blob","tree","wiki","discussions",
         "sponsors","security","settings","notifications","features","marketplace",
         "topics","collections","events","about","contact","login","join","new",
         "orgs","site","apps","pricing","explore","trending","stars","search",
         "codespaces","copilot","enterprise","readme","git-guides","open-source",
         "team","press","terms","privacy","site-policy","security-policy",
         "community","support","resources","skills","certifications","education",
         "students","teachers","partners","sponsorships","features","mobile",
         "desktop","cli","docs","blog","changelog","roadmap","status","pricing",
         "solutions","customers","careers","shop","marketplace","sponsors",
         "packages","deployments","environments","dependabot","code-scanning",
         "secret-scanning","insights","branches","tags","commits","contributors",
         "graphs","network","forks","stargazers","watchers","compare","milestones",
         "labels","assignees","projects","security","dependabot","code-scanning",
         "secret-scanning","actions","packages","releases","deployments",
         "environments","codespaces","copilot","security","insights","settings",
         "notifications"}


def curl(url, ua=UA):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "ignore")


def gh_meta(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url, headers={"User-Agent": GH_UA,
        "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    return {
        "full_name": d.get("full_name"),
        "description": d.get("description"),
        "stars": d.get("stargazers_count"),
        "language": d.get("language"),
        "license": (d.get("license") or {}).get("spdx_id"),
        "html_url": d.get("html_url"),
        "topics": d.get("topics", [])[:8],
        "archived": d.get("archived"),
        "pushed_at": d.get("pushed_at"),
    }


def osp_repo(b):
    """opensourceprojects.dev: repo path from content.imageUrl (NOT manifest og_image,
    which is often the generic logo)."""
    c = b.get("content", {})
    img = c.get("imageUrl", "") or ""
    m = re.search(r"opengraph\.githubassets\.com/1/([^/]+)/([^/]+)", img)
    return (m.group(1), m.group(2)) if m else None


def ll_repos(b):
    """linuxlinks.com: grep the article body for github.com/<owner>/<repo>."""
    url = b.get("content", {}).get("url", "")
    html = curl(url)
    found = re.findall(r"github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)", html)
    seen, out = set(), []
    for o, r in found:
        if r.lower() in NOISE:
            continue
        key = (o.lower(), r.lower())
        if key not in seen:
            seen.add(key)
            out.append((o, r))
    return out


def main():
    src = sys.argv[1]
    out_path = "/tmp/kk_run/repo_meta.json"
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    with open(src) as f:
        data = json.load(f)
    bookmarks = data.get("bookmarks", data) if isinstance(data, dict) else data

    results = {}
    for b in bookmarks:
        url = b.get("content", {}).get("url", "")
        bid = b["id"]
        if "opensourceprojects.dev" in url:
            repo = osp_repo(b)
            if repo:
                try:
                    results[bid] = gh_meta(*repo)
                except Exception as e:
                    results[bid] = {"error": str(e), "full_name": f"{repo[0]}/{repo[1]}"}
            else:
                results[bid] = None  # generic logo -> stub
        elif "linuxlinks.com" in url:
            repos = ll_repos(b)
            if repos:
                try:
                    results[bid] = gh_meta(*repos[0])
                except Exception as e:
                    results[bid] = {"error": str(e), "full_name": f"{repos[0][0]}/{repos[0][1]}"}
            else:
                results[bid] = None  # roundup, no single repo
        time.sleep(0.3)

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    for bid, r in results.items():
        if r and "error" not in r:
            print(f"{r['full_name']:35} | ★{r['stars']:>6} | {r['language']:12} | "
                  f"{r['license']} | {(r['description'] or '')[:55]}")
        elif r:
            print(f"{r['full_name']:35} | ERROR {r['error']}")
        else:
            print(f"{bid} | (stub/roundup, no single repo)")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
