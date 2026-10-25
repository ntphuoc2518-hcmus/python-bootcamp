from datetime import date, timedelta
import re

WEEKDAYS = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun": 6}

def parse_due(text: str, today: date) -> date:
    """Parse due date text into a date object relative to today."""
    text = text.strip().lower()
    
    # 1. Định dạng YYYY-MM-DD
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass
    
    # 2. "tomorrow"
    if text == "tomorrow":
        return today + timedelta(days=1)
        
    # 3. "in N days"
    match = re.match(r"^in\s+(\d+)\s+days?$", text)
    if match:
        n = int(match.group(1))
        return today + timedelta(days=n)
        
    # 4. Tên thứ (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
    day_prefix = text[:3]
    if day_prefix in WEEKDAYS:
        target_wd = WEEKDAYS[day_prefix]
        current_wd = today.weekday()
        days_ahead = target_wd - current_wd
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)
        
    raise ValueError(f"Invalid due date format: {text}")