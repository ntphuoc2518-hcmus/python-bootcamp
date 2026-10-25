import math
from collections import Counter
from typing import Any


def analyse(pairs: list[tuple[str, int]]) -> dict[str, Any]:
    """Analyze route latencies and return counts, p95, and the slowest route."""
    routes_data: dict[str, list[int]] = {}
    for route, latency in pairs:
        routes_data.setdefault(route, []).append(latency)

    counts = Counter({route: len(latencies) for route, latencies in routes_data.items()})
    p95_dict: dict[str, int] = {}

    for route, latencies in routes_data.items():
        sorted_lat = sorted(latencies)
        if not sorted_lat:
            p95_val = 0
        else:
            k = math.ceil(0.95 * len(sorted_lat)) - 1
            k = max(0, min(k, len(sorted_lat) - 1))
            p95_val = sorted_lat[k]
        p95_dict[route] = p95_val

    slowest = max(p95_dict, key=lambda k: p95_dict[k]) if p95_dict else None

    return {
        "counts": counts,
        "slowest": slowest,
        "p95": p95_dict,
    }