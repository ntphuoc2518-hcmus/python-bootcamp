def summary(scores: list[float]) -> dict[str, float]:
    """Compute summary statistics for a list of scores.

    Returns a dictionary containing min, max, mean, and median.
    Mean and median are rounded to 2 decimal places.
    Raises ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores list cannot be empty")

    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    mean_val = round(sum(scores) / n, 2)

    if n % 2 == 1:
        median_val = sorted_scores[n // 2]
    else:
        median_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": mean_val,
        "median": round(median_val, 2),
    }
