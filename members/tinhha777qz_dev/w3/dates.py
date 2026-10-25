"""W3-1 Dates module.

Provides natural language and ISO date parsing for study task deadlines.
"""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse a date string relative to a reference date.

    Supports:
    - ISO date: "YYYY-MM-DD", e.g. "2026-10-30"
    - "tomorrow": today + 1 day
    - "in X days" / "in X day": today + X days
    - Weekday names (e.g. "Fri", "Tue", "Wednesday"): strictly next occurrence (> today)

    Args:
        text: String describing the due date.
        today: Reference date.

    Returns:
        The resolved date object.

    Raises:
        ValueError: If text cannot be parsed as a supported date expression.
    """
    raw = text.strip()
    if not raw:
        raise ValueError("Due date cannot be empty")

    # 1. Check ISO format (YYYY-MM-DD)
    try:
        return date.fromisoformat(raw)
    except ValueError:
        pass

    lower = raw.lower()

    # 2. Check "tomorrow"
    if lower == "tomorrow":
        return today + timedelta(days=1)

    # 3. Check "in X days" or "in X day"
    match = re.fullmatch(r"in\s+(\d+)\s+days?", lower)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Check weekday name (strictly next occurrence, not today)
    if lower in _WEEKDAYS:
        target_day = _WEEKDAYS[lower]
        days_ahead = (target_day - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due date expression: {text!r}")
