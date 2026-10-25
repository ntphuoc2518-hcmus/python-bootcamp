import argparse
import sys
from datetime import date
from pathlib import Path

from members.qmtu2520_fit_clc.w2.io_utils import load_tasks
from members.qmtu2520_fit_clc.w2.models import Task


def main() -> None:
    """Main CLI entry point for the Study Planner."""
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("file", type=str, help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available hours to study",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Current date (YYYY-MM-DD)",
    )

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    today_date: date = args.today
    print(f"Today is: {today_date}")

    try:
        tasks: list[Task] = load_tasks(file_path)
    except (OSError, ValueError) as error:
        print(f"Error: Cannot load tasks: {error}")
        sys.exit(1)

    # Prioritize tasks by deadline, then importance.
    tasks.sort(key=lambda task: (task.deadline, -task.importance))

    print(f"Tonight ({args.hours:.1f} h):")

    remaining = args.hours
    index = 1

    for task in tasks:
        if remaining <= 0:
            break

        allocated = min(task.effort_h, remaining)
        if allocated <= 0:
            continue

        print(f"{index:2}. {task.title} ...... {allocated:.1f} h")
        remaining -= allocated
        index += 1


if __name__ == "__main__":
    main()