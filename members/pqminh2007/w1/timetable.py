from collections import defaultdict

def by_day(schedule):
    if not schedule:
        return {}
    
    result = defaultdict(list)
    for course, day in schedule:
        result[day].append(course)
        
    return {day: sorted(courses) for day, courses in result.items()}