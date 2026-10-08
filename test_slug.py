from slug import truncate


def test_truncate_keeps_short_text():
    assert truncate("abc", 5) == "abc"


def test_truncate_cuts_long_text():
    assert truncate("abcdef", 4) == "abc…"


from slug import slugify


def test_slugify_lowercases():
    assert slugify("Hello") == "hello"


def test_slugify_collapses_runs_of_other_characters():
    assert slugify("GenLayer -- Intelligent   Contracts!") == "genlayer-intelligent-contracts"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("  --Bradbury Testnet--  ") == "bradbury-testnet"


def test_slugify_empty_without_letters_or_digits():
    assert slugify("") == ""
    assert slugify("!!! ---") == ""


def test_slugify_keeps_digits():
    assert slugify("Version 2.0 Release") == "version-2-0-release"
