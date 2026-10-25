"""W3-3 Command-line study planner tool.

Prioritises tasks from a CSV file and allocates study time for tonight.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.tinhha777qz_dev.w2.io_utils import load_tasks
from members.tinhha777qz_dev.w2.models import Task


def calculate_priority(task: Task, today: date) -> float:
    """Calculate task urgency score: importance / max(1, days_left)."""
    days_left = (task.deadline - today).days
    effective_days = max(1, days_left)
    return task.importance / effective_days


def plan_study(
    tasks: list[Task], hours: float, today: date
) -> list[tuple[Task, float]]:
    """Prioritise tasks and greedily allocate study hours."""
    sorted_tasks = sorted(
        tasks,
        key=lambda t: calculate_priority(t, today),
        reverse=True,
    )

    allocated: list[tuple[Task, float]] = []
    remaining_hours = hours

    for task in sorted_tasks:
        if remaining_hours <= 0:
            break
        h = min(task.effort_h, remaining_hours)
        if h > 0:
            allocated.append((task, h))
            remaining_hours -= h

    return allocated


def render_plan(allocated: list[tuple[Task, float]], total_hours: float) -> str:
    """Format the study schedule into a readable summary."""
    lines = [f"Tonight ({total_hours:.1f} h):"]
    if not allocated:
        return "\n".join(lines)

    max_len = max(len(task.title) for task, _ in allocated)
    col_width = max(max_len + 6, 16)

    for idx, (task, h) in enumerate(allocated, start=1):
        dots_count = max(2, col_width - len(task.title))
        dots = "." * dots_count
        lines.append(f"  {idx}. {task.title} {dots} {h:.1f} h")

    return "\n".join(lines)


def main() -> None:
    """CLI entry point for the study planner."""
    parser = argparse.ArgumentParser(
        description="Plan tonight's study schedule from a tasks CSV file."
    )
    parser.add_argument("csv_path", type=str, help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Number of hours available tonight",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date YYYY-MM-DD (defaults to today)",
    )

    args = parser.parse_args()

    csv_file = Path(args.csv_path)
    if not csv_file.is_file():
        print(f"Error: file not found '{args.csv_path}'", file=sys.stderr)
        sys.exit(1)

    if args.today:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            print(
                f"Error: invalid date format '{args.today}', expected YYYY-MM-DD",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        today = date.today()

    try:
        tasks = load_tasks(csv_file)
    except (ValueError, OSError) as exc:
        print(f"Error reading tasks: {exc}", file=sys.stderr)
        sys.exit(1)

    allocated = plan_study(tasks, args.hours, today)
    print(render_plan(allocated, args.hours))


if __name__ == "__main__":
    main()
