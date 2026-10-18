from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self):
        return f"InfeasiblePlan: Needed {self.needed_h}h, but only {self.available_h}h available."

def check_feasible(tasks: list[Task], available_h: float):
    total_needed = sum(t.effort_h for t in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)
