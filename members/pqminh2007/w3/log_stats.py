from collections import Counter
import math
from typing import Dict, List, Tuple, Any

def analyse(pairs: List[Tuple[str, int]]) -> Dict[str, Any]:
    """Analyze route latencies and return counts, p95, and the slowest route."""
    routes_data: Dict[str, List[int]] = {}
    for route, latency in pairs:
        routes_data.setdefault(route, []).append(latency)
        
    counts = Counter({route: len(latencies) for route, latencies in routes_data.items()})
    p95_dict: Dict[str, int] = {}
    
    for route, latencies in routes_data.items():
        sorted_lat = sorted(latencies)
        if not sorted_lat:
            p95_val = 0
        else:
            k = math.ceil(0.95 * len(sorted_lat)) - 1
            k = max(0, min(k, len(sorted_lat) - 1))
            p95_val = sorted_lat[k]
        p95_dict[route] = p95_val
        
    slowest = max(p95_dict, key=p95_dict.get) if p95_dict else None
    
    return {
        "counts": counts,
        "slowest": slowest,
        "p95": p95_dict
    }