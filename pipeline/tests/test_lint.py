"""Voice lint: dashes, banned words, contrasts, third person, fake hands-on claims."""

from __future__ import annotations

from lib.item import lint, load_banned

BANNED = load_banned()


def test_clean_text_passes():
    assert lint("The tool is quick and the setup is dull. I would say it works.", BANNED) == []


def test_em_dash_and_en_dash_are_both_caught():
    assert any("dash" in p for p in lint("It works \u2014 mostly.", BANNED))
    assert any("dash" in p for p in lint("It works \u2013 mostly.", BANNED))


def test_banned_words():
    assert any("leverage" in p for p in lint("They leverage the runtime.", BANNED))
    assert any("robust" in p for p in lint("A robust pipeline.", BANNED))
    assert any("it's worth noting" in p for p in lint("It's worth noting that it runs.", BANNED))


def test_banned_list_comes_from_the_skill():
    assert "delve" in BANNED and "game changer" in BANNED
    assert len(BANNED) > 30


def test_contrast_pattern():
    assert any("not X, but Y" in p for p in lint("This is not a database, but a cache.", BANNED))
    assert any("not X, but Y" in p for p in lint("The point isn't speed, it's the licence.", BANNED))


def test_third_person_and_filler():
    assert any("Wojtek" in p for p in lint("Wojtek cares because he runs this at home.", BANNED))
    assert any("first person" in p for p in lint("Wojtek would like this.", BANNED))


def test_fake_hands_on_claims():
    assert any("hands-on" in p for p in lint("I installed it on the arr-box.", BANNED))
    assert any("hands-on" in p for p in lint("I tried it for a week.", BANNED))


def test_fenced_code_and_urls_do_not_break_the_lint():
    assert lint("Link: https://github.com/morluto/rea and `npx rea-agents setup`.", BANNED) == []
