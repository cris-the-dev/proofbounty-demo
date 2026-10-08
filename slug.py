"""Tiny text utilities used by the ProofBounty demo."""


def truncate(text: str, limit: int) -> str:
    """Return text cut to at most `limit` characters, ending with '…' when cut."""
    if limit <= 0:
        return ""
    return text if len(text) <= limit else text[: limit - 1] + "…"
