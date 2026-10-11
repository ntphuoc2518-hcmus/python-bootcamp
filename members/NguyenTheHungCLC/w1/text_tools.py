def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for punctuation in ".,!?:;":
        text = text.replace(punctuation, " ")

    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts
