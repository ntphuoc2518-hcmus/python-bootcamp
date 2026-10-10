def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if student qualifies to register thesis (credits >= 120 and gpa >= 2.0)."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return list of human-readable reasons if student does not meet criteria."""
    reasons: list[str] = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append("need higher GPA (minimum 2.0)")

    return reasons
