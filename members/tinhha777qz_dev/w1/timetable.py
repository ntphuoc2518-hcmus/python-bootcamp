def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return a dictionary mapping each day to a sorted list of course codes."""
    timetable: dict[str, list[str]] = {}

    for course, day in courses:
        timetable.setdefault(day, []).append(course)

    for day_courses in timetable.values():
        day_courses.sort()

    return timetable
