def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return each day's courses in sorted order."""
    result = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day, course_list in result.items():
        course_list.sort()

    return result