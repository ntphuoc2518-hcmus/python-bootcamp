"""W3-2 Chat log analysis module.

Computes request counts, p95 latencies, and identifies the slowest route.
"""

from collections import Counter, defaultdict
from collections.abc import Sequence
import math
from typing import Any


def analyse(pairs: Sequence[tuple[str, int | float]]) -> dict[str, Any]:
    """Analyse route latencies from log pairs.

    Args:
        pairs: A sequence of (route, latency_ms) tuples.

    Returns:
        A dict containing:
        - "counts": Counter of request counts per route.
        - "p95": Dict of 95th percentile latency per route.
        - "slowest": Name of the route with the highest p95 latency (None if empty).
    """
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    grouped: dict[str, list[int | float]] = defaultdict(list)
    counts: Counter[str] = Counter()

    for route, latency in pairs:
        grouped[route].append(latency)
        counts[route] += 1

    p95: dict[str, int | float] = {}
    for route, latencies in grouped.items():
        sorted_lats = sorted(latencies)
        idx = max(0, min(math.ceil(0.95 * len(sorted_lats)) - 1, len(sorted_lats) - 1))
        p95[route] = sorted_lats[idx]

    slowest = max(p95, key=lambda r: p95[r])

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
