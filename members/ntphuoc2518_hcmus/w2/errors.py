
class InfeasiblePlan(Exception):
    """Raised when the total task effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h

        super().__init__(
            f"Infeasible plan: needed {needed_h} hours, "
            f"but only {available_h} hours are available."
        )


def check_feasible(tasks, available_h: float) -> None:
    """Raise InfeasiblePlan if tasks require too many hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
