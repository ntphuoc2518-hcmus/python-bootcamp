from datetime import date


class Task:

    def __init__(
        self, title: str, priority: int, work_hours: float, deadline: date
    ):
        if not (1 <= priority <= 5):
            raise ValueError("Priority must be between 1 and 5")

        self.title = title
        self.priority = priority
        self.work_hours = work_hours
        self.deadline = deadline

    def days_left(self, today: date) -> int:
        delta = (self.deadline - today).days
        return max(0, delta)