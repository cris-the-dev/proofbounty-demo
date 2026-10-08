"""Tiny text utilities used by the ProofBounty demo."""


def truncate(text: str, limit: int) -> str:
    """Return text cut to at most `limit` characters, ending with '…' when cut."""
    if limit <= 0:
        return ""
    return text if len(text) <= limit else text[: limit - 1] + "…"


def slugify(text: str) -> str:
    """Lowercase `text` and join its runs of letters and digits with single hyphens."""
    out, gap = [], False
    for ch in text.lower():
        if "a" <= ch <= "z" or "0" <= ch <= "9":
            if gap and out:
                out.append("-")
            out.append(ch)
            gap = False
        else:
            gap = True
    return "".join(out)
