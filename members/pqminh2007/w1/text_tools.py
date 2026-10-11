import re
from collections import Counter

def word_count(text):
    if not text:
        return {}
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def top_k(text, k):
    counts = word_count(text)
    if not counts:
        return []
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]