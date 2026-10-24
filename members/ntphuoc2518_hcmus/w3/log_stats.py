"""Utilities for analyzing request latency logs."""

import math
from collections import Counter, defaultdict
from collections.abc import Iterable


def analyse(
    pairs: Iterable[tuple[str, int | float]],
) -> dict[str, object]:
    """Calculate request counts and P95 latency for each route.

    P95 uses the nearest-rank method:
    sort the latency values and select the value at rank
    ceil(0.95 * number_of_observations).

    If the input is empty, return empty counts and P95,
    with None for the slowest route.
    """
    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[float]] = (
        defaultdict(list)
    )

    # Group latency observations by route.
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies_by_route[route].append(float(latency_ms))

    # Calculate P95 for every route.
    p95: dict[str, float] = {}

    for route, latencies in latencies_by_route.items():
        ordered = sorted(latencies)
        rank = math.ceil(0.95 * len(ordered))
        p95[route] = ordered[rank - 1]

    # Find the route with the highest P95.
    slowest = max(p95, key=p95.__getitem__) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }