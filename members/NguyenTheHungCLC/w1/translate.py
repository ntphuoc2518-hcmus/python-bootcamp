def translate(text: str, dictionary: dict[str, str]) -> str:
    words = text.split()
    translated = [dictionary.get(word, word) for word in words]
    return " ".join(translated)
