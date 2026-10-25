
"""Utilities for analysing request counts and response latency."""

from collections import Counter, defaultdict
from math import ceil
from typing import TypedDict


class AnalysisResult(TypedDict):
    """Describe the structure of the request analysis result."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: list[tuple[str, float]]) -> AnalysisResult:
    """Count requests and calculate p95 latency for each route."""
    counts = Counter()
    latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95 = {}

    for route, values in latencies.items():
        sorted_values = sorted(values)
        index = ceil(0.95 * len(sorted_values)) - 1
        p95[route] = sorted_values[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }
