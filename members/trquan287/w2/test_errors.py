from datetime import date

from .errors import InfeasiblePlan, check_feasible
from .models import Task

tasks = [
    Task("DS exam", 5, 6, date(2026, 10, 30)),
    Task("Assignment", 4, 1.5, date(2026, 10, 27)),
]

try:
    check_feasible(tasks, 4)
except InfeasiblePlan as error:
    print(error)
    print("Needed:", error.needed_h)
    print("Available:", error.available_h)
