from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Convert a date description into a date."""
    value = text.strip().lower()

    if not value:
        raise ValueError("Due date cannot be empty")

    if value == "tomorrow":
        return today + timedelta(days=1)

    if value.startswith("in ") and value.endswith(" days"):
        number_text = value[3:-5].strip()

        try:
            days = int(number_text)
        except ValueError as error:
            raise ValueError(f"Invalid due date: {text}") from error

        if days < 0:
            raise ValueError("Number of days cannot be negative")

        return today + timedelta(days=days)

    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    weekdays = {
        "mon": 0,
        "monday": 0,
        "tue": 1,
        "tues": 1,
        "tuesday": 1,
        "wed": 2,
        "wednesday": 2,
        "thu": 3,
        "thur": 3,
        "thurs": 3,
        "thursday": 3,
        "fri": 4,
        "friday": 4,
        "sat": 5,
        "saturday": 5,
        "sun": 6,
        "sunday": 6,
    }

    if value in weekdays:
        target_weekday = weekdays[value]
        days_ahead = (target_weekday - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Invalid due date: {text}")
