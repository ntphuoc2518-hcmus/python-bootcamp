def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return True if credits >= 120 and GPA >= 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons why the student does not qualify."""
    reasons = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append("need GPA of 2.0 or higher")

    return reasons