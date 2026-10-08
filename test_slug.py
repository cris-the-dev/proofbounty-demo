from slug import truncate


def test_truncate_keeps_short_text():
    assert truncate("abc", 5) == "abc"


def test_truncate_cuts_long_text():
    assert truncate("abcdef", 4) == "abc…"
