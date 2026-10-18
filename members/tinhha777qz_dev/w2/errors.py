"""W2-3 Custom exception and feasibility checking."""

from collections.abc import Sequence

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when total effort required for tasks exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h} hours, "
            f"but only {available_h} hours are available.",
        )


def check_feasible(tasks: Sequence[Task], available_h: float) -> None:
    """Check if tasks can be completed within available hours.

    Raises:
        InfeasiblePlan: If total effort_h of tasks exceeds available_h.
    """
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
