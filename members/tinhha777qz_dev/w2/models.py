"""W2-1 Task model."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a study task with importance, effort in hours, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task fields."""
        if not 1 <= self.importance <= 5:
            raise ValueError(f"Importance must be 1-5, got {self.importance}")
        if self.effort_h < 0:
            raise ValueError(f"Effort cannot be negative, got {self.effort_h}")

    def days_left(self, today: date) -> int:
        """Return the number of days left until the deadline, never below 0."""
        return max(0, (self.deadline - today).days)
