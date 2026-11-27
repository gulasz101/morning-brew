"""Validator: every rule the writer's reply must satisfy."""

from __future__ import annotations

from lib.item import validate

ALLOWED = ["riffradar", "homelab-2nd", "ideogram4-local"]


def ok_item(**kw):
    base = {
        "in_short": "A short verdict about the thing.",
        "key_points": ["one", "two", "three"],
        "details": " ".join(["word"] * 120),
        "ideas": [],
        "project_links": [1],
    }
    base.update(kw)
    return base


def test_valid_item_passes(items):
    for entry in items:
        errs = validate(entry["reply"], 3, ALLOWED, entry.get("video", False),
                        entry.get("roundup", False))
        assert errs == [], (entry["title"], errs)


def test_key_point_count():
    assert any("key_points has 2" in e for e in validate(ok_item(key_points=["a", "b"]), 3, ALLOWED, False, False))
    assert any("key_points has 7" in e for e in validate(ok_item(key_points=["a"] * 7), 3, ALLOWED, False, False))


def test_details_word_floor_and_ceiling():
    assert any("at least 80" in e for e in validate(ok_item(details="too short"), 3, ALLOWED, False, False))
    long_video = " ".join(["word"] * 250)
    assert validate(ok_item(details=long_video), 3, ALLOWED, True, False) == []
    assert any("limit is 200" in e for e in validate(ok_item(details=long_video), 3, ALLOWED, False, False))


def test_video_gets_the_longer_details_limit():
    assert validate(ok_item(details=" ".join(["w"] * 290)), 3, ALLOWED, True, False) == []


def test_ideas_must_use_the_allowed_projects():
    bad = ok_item(ideas=[{"project": "star-office-ui", "idea": "x"}])
    assert any("not one of" in e for e in validate(bad, 3, ALLOWED, False, False))


def test_idea_needs_a_sentence():
    bad = ok_item(ideas=[{"project": "homelab-2nd", "idea": "  "}])
    assert any("idea must be a non-empty" in e for e in validate(bad, 3, ALLOWED, False, False))


def test_project_links_must_be_valid_indices():
    assert any("outside 1..3" in e for e in validate(ok_item(project_links=[4]), 3, ALLOWED, False, False))
    assert any("outside 1..3" in e for e in validate(ok_item(project_links=[0]), 3, ALLOWED, False, False))
    assert any("not a whole number" in e for e in validate(ok_item(project_links=["2"]), 3, ALLOWED, False, False))


def test_roundup_needs_names():
    errs = validate(ok_item(), 3, ALLOWED, False, True)
    assert any("projects must be a list" in e for e in errs)
    good = ok_item(projects=["Alacritty", "Kitty"])
    assert validate(good, 3, ALLOWED, False, True) == []


def test_idea_must_name_the_part_it_touches():
    components = {"homelab-2nd": ["pihole", "k3s"]}
    bad = ok_item(ideas=[{"project": "homelab-2nd", "idea": "Use it in my homelab for filtering."}])
    errs = validate(bad, 3, ALLOWED, False, False, components)
    assert any("names no part of homelab-2nd" in e for e in errs)
    good = ok_item(ideas=[{"project": "homelab-2nd",
                           "idea": "Run it as a second resolver next to pihole on k3s."}])
    assert validate(good, 3, ALLOWED, False, False, components) == []


def test_idea_needs_eight_words():
    bad = ok_item(ideas=[{"project": "homelab-2nd", "idea": "pihole"}])
    errs = validate(bad, 3, ALLOWED, False, False, None)
    assert any("at least 8" in e for e in errs)


def test_conditional_fit_needs_the_missing_condition():
    components = {"homelab-2nd": ["pihole", "k3s"]}
    bad = ok_item(ideas=[{"project": "homelab-2nd", "fit": "conditional",
                          "idea": "Put it next to pihole on k3s as a second resolver."}])
    errs = validate(bad, 3, ALLOWED, False, False, components)
    assert any("needs missing" in e for e in errs)
    good = ok_item(ideas=[{"project": "homelab-2nd", "fit": "conditional",
                           "missing": "it ships an arm64 image",
                           "idea": "Put it next to pihole on k3s as a second resolver."}])
    assert validate(good, 3, ALLOWED, False, False, components) == []


def test_fit_must_be_known():
    bad = ok_item(ideas=[{"project": "homelab-2nd", "fit": "maybe",
                          "idea": "Put it next to pihole on k3s as a second resolver."}])
    assert any("fit must be one of" in e for e in validate(bad, 3, ALLOWED, False, False, None))


def test_no_fit_reason_is_one_clause():
    long_reason = " ".join(["word"] * 45)
    bad = ok_item(no_fit_reason=long_reason)
    assert any("no_fit_reason is 45 words" in e
               for e in validate(bad, 3, ALLOWED, False, False, None))


def test_no_fit_reason_stays_one_clause():
    long_reason = " ".join(["word"] * 45)
    bad = ok_item(no_fit_reason=long_reason)
    assert any("no_fit_reason is 45 words" in e
               for e in validate(bad, 3, ALLOWED, False, False, None))
