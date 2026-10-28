#!/usr/bin/env python3
"""Read-only validator for references/curated-project-links.json.

Every link in the curated map gets probed over plain HTTPS (HTML HEAD/GET, browser
UA) and the final resolved URL is recorded. This catches:
  - renamed / transferred repos (GitHub 301s -> report the NEW owner/name)
  - deleted repos (404)
  - dead docs/homepage URLs
It does NOT use the GitHub API, so it is immune to the 60/hr unauthenticated
rate limit that kills a 21+-repo day mid-run.

Usage:
  python3 validate_project_links.py [--out /tmp/kk_run/link_check.json] [--quiet]

Exit code 0 = all links resolve, 1 = at least one problem (report written either way).
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CURATED = (os.environ.get("KK_CURATED")
           or os.path.join(os.path.dirname(HERE), "references", "curated-project-links.json"))
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/536.30.2 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")
# Chrome UA is used as an escalation, not the first attempt: sourceforge.net and
# gitlab.gnome.org answer 403/406 to a Chrome UA but 200 to a Safari UA
# (verified 2026-09-21), so a Chrome-first probe reports live projects as dead.
UA_CHROME = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# A 200 that lands on a login/consent page is a FAIL, not a verified repo:
# invent.kde.org/<repo> returns 200 -> /users/sign_in.
WALL_URL = re.compile(r"(/users/sign_in|/login|/signin|/auth/|consent\.|/captcha)", re.I)


def _curl_probe(url, ua):
    p = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-L", "-A", ua,
         "-w", "%{http_code} %{url_effective}", "--max-time", "25", url],
        capture_output=True, text=True, timeout=40)
    out = (p.stdout or "").strip().split(" ", 1)
    code = out[0] if out else "000"
    final = out[1] if len(out) > 1 else url
    return code, final


def probe(url):
    """Return (status_code, final_url, note). Uses curl -L so redirects resolve.
    Bot-wall aware: retries a 403/406 with a Chrome UA before declaring failure."""
    try:
        code, final = _curl_probe(url, UA)
        if code in ("403", "406", "000", "429"):
            code2, final2 = _curl_probe(url, UA_CHROME)
            if code2 == "200":
                code, final = code2, final2
    except Exception as e:
        return "000", url, f"probe failed: {e}"
    note = ""
    if code == "200" and WALL_URL.search(final or ""):
        return code, final, "LOGIN WALL (200 but not the repo)"
    if code == "404":
        note = "DEAD (404)"
    elif code in ("301", "302", "308") or final.rstrip("/") != url.rstrip("/"):
        # curl -L hides intermediate hops, so compare declared vs FINAL url.
        # Classification (stale org vs benign path change) happens in main().
        note = "REDIRECTS"
    elif code != "200":
        note = f"status {code}"
    return code, final, note


# A redirect that still lands on a live page is NORMAL, not a defect:
# plex.tv -> watch.plex.tv, vaultproject.io -> developer.hashicorp.com/vault,
# docs.rs/crate/x -> docs.rs/crate/x/latest, thunderbird.net -> /en-US/.
# Only a redirect that moves a *declared owner/repo* somewhere else is a
# problem (stale org), and that is handled separately below.
BENIGN_REDIRECT = "redirect (benign)"


def norm_final(final):
    """Pull owner/name out of a resolved github URL, lowercased."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/?#]+)", final)
    if m:
        return f"{m.group(1)}/{m.group(2)}".lower()
    return None


def main():
    out_path, quiet = "/tmp/kk_run/link_check.json", False
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    if "--quiet" in sys.argv:
        quiet = True

    curated = json.load(open(CURATED))
    entries = {k: v for k, v in curated.items() if not k.startswith("_")}

    report, problems, benign = [], [], []
    for key, meta in entries.items():
        if "repo" in meta:
            url = f"https://github.com/{meta['repo']}"
        else:
            url = meta.get("docs", "")
        code, final, note = probe(url)
        rec = {"key": key, "declared": meta.get("repo") or meta.get("docs"),
               "url": url, "status": code, "final": final, "note": note}
        if note == "REDIRECTS" and meta.get("repo"):
            resolved = norm_final(final)
            if resolved and resolved != meta["repo"].lower():
                # stale org: the declared owner/name moved. THIS is the real defect.
                rec["fix_repo"] = final.split("github.com/")[-1].rstrip("/")
                note = rec["note"] = "RENAMED -> " + rec["fix_repo"]
                problems.append(rec)
                report.append(rec)
                continue
        if note == "REDIRECTS":
            # live page, same project, normalized path — record, do not fail the gate
            rec["note"] = note = BENIGN_REDIRECT
            benign.append(rec)
        elif note:
            problems.append(rec)
        report.append(rec)

    json.dump({"checked": len(entries), "problems": problems,
               "benign_redirects": benign, "all": report},
              open(out_path, "w"), indent=2)

    if not quiet:
        print(f"checked {len(entries)} curated links -> {len(problems)} problems"
              f", {len(benign)} benign redirects")
        for r in problems:
            print(f"  [{r['status']}] {r['key']:22} {r['declared']}  {r['note']}")
        for r in benign:
            print(f"  ok  {r['key']:22} {r['url']} -> {r['final']}")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
