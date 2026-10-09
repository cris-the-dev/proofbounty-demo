"""Tiny text utilities used by the ProofBounty demo."""

import unicodedata


def truncate(text: str, limit: int) -> str:
    """Return text cut to at most `limit` characters, ending with '…' when cut."""
    if limit <= 0:
        return ""
    return text if len(text) <= limit else text[: limit - 1] + "…"


def slugify(text: str) -> str:
    """Lowercase `text` and join its runs of letters and digits with single hyphens.

    Accented letters are reduced to their base letter first ("Café" -> "cafe"),
    so non-ASCII input is handled instead of being dropped.
    """
    base = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    out, gap = [], False
    for ch in base.lower():
        if "a" <= ch <= "z" or "0" <= ch <= "9":
            if gap and out:
                out.append("-")
            out.append(ch)
            gap = False
        else:
            gap = True
    return "".join(out)
