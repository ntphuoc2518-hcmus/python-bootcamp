
def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Scores cannot be empty")

    sorted_scores = sorted(scores)

    mean = round(sum(scores) / len(scores), 2)

    n = len(sorted_scores)
    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": mean,
        "median": round(median, 2)
    }
