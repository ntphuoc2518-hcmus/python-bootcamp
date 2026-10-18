class InfeasiblePlan(Exception):

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h} hours, but only {available_h} hours available."
        )


def check_feasible(tasks: list, available_h: float) -> None:
    needed_h = sum(task.work_hours for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)