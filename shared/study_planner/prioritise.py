"""Module 2: Prioritise tasks for study planner.

Part of team assignment T-W2.
Calculates priority using the formula: importance / max(days_left, 1)
"""

from datetime import date
from typing import Sequence

from shared.contract import Task


def calculate_priority(task: Task, today: date) -> float:
    """Calculate the priority score for a task.

    Formula: importance / days_left
    days_left < 1 is treated as 1 to avoid division by zero.
    Higher score indicates higher urgency.
    """
    days_left = (task.deadline - today).days
    effective_days = max(1, days_left)
    return task.importance / effective_days


def prioritise(tasks: Sequence[Task], today: date) -> list[Task]:
    """Sort tasks by urgency in descending order of priority score.

    Priority score = importance / max(1, days_left).
    Higher priority tasks appear earlier in the returned list.
    Preserves original order among tasks with equal priority scores.

    Args:
        tasks: Sequence of Task instances.
        today: The reference date for calculating days left.

    Returns:
        A new list of Task objects sorted by descending priority.
    """
    return sorted(tasks, key=lambda t: calculate_priority(t, today), reverse=True)
