import re
from collections import Counter


def word_count(text: str) -> dict[str, int]:
    """Count word occurrences in lowercase text, ignoring punctuation .,!?;:."""
    cleaned = re.sub(r"[.,!?;:]", " ", text.lower())
    words = cleaned.split()
    return dict(Counter(words))


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words sorted by frequency descending, then alphabetically."""
    if k <= 0:
        return []
    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
