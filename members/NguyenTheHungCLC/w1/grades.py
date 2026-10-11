import statistics


def summary(scores: list[float]) -> tuple[float, float, float, float]:
    if not scores:
        raise ValueError("Score list cannot be empty")

    min_score = round(float(min(scores)), 2)
    max_score = round(float(max(scores)), 2)
    mean_score = round(float(statistics.mean(scores)), 2)
    median_score = round(float(statistics.median(scores)), 2)

    return min_score, max_score, mean_score, median_score
