
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        """Validate task data after initialization."""
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title must not be empty.")

        if not isinstance(self.importance, int) or isinstance(self.importance, bool):
            raise TypeError("Importance must be an integer.")

        if not 1 <= self.importance <= 5:
            raise ValueError("Importance must be between 1 and 5.")

        if not isinstance(self.effort_h, (int, float)) or isinstance(self.effort_h, bool):
            raise TypeError("Effort must be a number.")

        if self.effort_h <= 0:
            raise ValueError("Effort must be greater than 0.")

        if not isinstance(self.deadline, date):
            raise TypeError("Deadline must be a date.")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, never below zero."""
        return max(0, (self.deadline - today).days)
