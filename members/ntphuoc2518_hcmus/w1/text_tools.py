
import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words while ignoring punctuation."""
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words by frequency, then alphabetically."""
    if k <= 0:
        return []

    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
