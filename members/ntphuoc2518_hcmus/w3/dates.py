"""Utilities for parsing due-date descriptions."""

import calendar
import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
    alias: index
    for index, name in enumerate(calendar.day_name)
    for alias in (name.casefold(), name[:3].casefold())
}


def parse_due(text: str, today: date) -> date:
    """Parse a date description relative to the supplied date.

    Supported formats:
    - YYYY-MM-DD
    - tomorrow
    - in N days
    - Weekday names, such as Fri or Friday

    A weekday matching today refers to its next occurrence,
    seven days later. Invalid input raises ValueError.
    """
    normalized = text.strip().casefold()

    if not normalized:
        raise ValueError("Due date cannot be empty.")

    # Case 1: An explicit date in YYYY-MM-DD format.
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", normalized):
        try:
            return date.fromisoformat(normalized)
        except ValueError as exc:
            raise ValueError(
                f"Invalid calendar date: {text!r}"
            ) from exc

    # Case 2: Tomorrow.
    if normalized == "tomorrow":
        return today + timedelta(days=1)

    # Case 3: A relative number of days.
    match = re.fullmatch(r"in\s+(\d+)\s+days?", normalized)

    if match is not None:
        number_of_days = int(match.group(1))
        return today + timedelta(days=number_of_days)

    # Case 4: The next occurrence of a weekday.
    weekday = _WEEKDAYS.get(normalized)

    if weekday is not None:
        days_ahead = (weekday - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown due-date description: {text!r}")