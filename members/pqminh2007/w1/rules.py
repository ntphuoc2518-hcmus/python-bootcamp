def can_register_thesis(credits, gpa):
    return credits >= 120 and gpa >= 2.0

def missing(credits, gpa):
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("GPA too low")
    return reasons