def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in courses:
        if day not in result:
            result[day] = []
        result[day].append(course)

    for courses_list in result.values():
        courses_list.sort()

    return result