import re
from datetime import date, timedelta

WEEKDAYS = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}

def parse_due(text: str, today: date) -> date:
    text = text.strip().lower()

    if not text:
        raise ValueError("Date text cannot be empty")

    # Format: YYYY-MM-DD
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    # Format: tomorrow
    if text == "tomorrow":
        return today + timedelta(days=1)

    # Format: in N days
    match = re.fullmatch(r"in (\d+) days?", text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # Format: weekday name (next occurrence)
    if text in WEEKDAYS:
        target_weekday = WEEKDAYS[text]
        days_ahead = (target_weekday - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date text: {text}")
