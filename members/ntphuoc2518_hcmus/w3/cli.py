"""Command-line study planner for Week 3."""

import argparse
import re
import sys
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from ..w2.io_utils import load_tasks
from ..w2.models import Task


def _parse_iso_date(value: str) -> date:
    """Parse a date supplied as YYYY-MM-DD to argparse."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise argparse.ArgumentTypeError(
            "Date must use the YYYY-MM-DD format."
        )

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Invalid date: {value!r}"
        ) from exc


def prioritise_tasks(
    tasks: list[Task],
    today: date,
) -> list[Task]:
    """Sort tasks by descending importance per remaining day.

    Tasks with equal priority are ordered by deadline and title.
    """
    return sorted(
        tasks,
        key=lambda task: (
            -task.importance / max(task.days_left(today), 1),
            task.deadline,
            task.title.casefold(),
        ),
    )


def allocate_tasks(
    tasks: list[Task],
    hours: float,
) -> list[tuple[Task, float]]:
    """Allocate available hours to prioritized tasks greedily.

    A task can receive a partial allocation if the remaining
    time is insufficient for its full estimated effort.
    """
    remaining = hours
    blocks: list[tuple[Task, float]] = []

    for task in tasks:
        if remaining <= 1e-9:
            break

        if task.effort_h <= 0:
            continue

        allocated = min(task.effort_h, remaining)
        blocks.append((task, allocated))
        remaining -= allocated

    return blocks


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line study planner."""
    parser = argparse.ArgumentParser(
        description="Plan study tasks within an hour budget."
    )

    parser.add_argument(
        "csv_path",
        type=Path,
        help="Path to the tasks CSV file.",
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study time in hours.",
    )

    parser.add_argument(
        "--today",
        type=_parse_iso_date,
        default=None,
        help="Reference date in YYYY-MM-DD format.",
    )

    args = parser.parse_args(argv)

    if args.hours <= 0:
        parser.error("--hours must be greater than zero.")

    # Report a missing file clearly and return exit code 1.
    if not args.csv_path.is_file():
        print(
            f"Error: file '{args.csv_path}' not found.",
            file=sys.stderr,
        )
        return 1

    # Reuse the existing CSV loader from Week 2.
    try:
        tasks: list[Task] = load_tasks(args.csv_path)
    except (OSError, ValueError) as exc:
        print(f"Error: could not load tasks: {exc}", file=sys.stderr)
        return 1

    today: date = args.today if args.today is not None else date.today()

    ordered_tasks = prioritise_tasks(tasks, today)
    blocks = allocate_tasks(ordered_tasks, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")

    if not blocks:
        print("  No tasks to schedule.")
        return 0

    for index, (task, allocated_hours) in enumerate(blocks, start=1):
        label = f"{task.title} ".ljust(17, ".")
        print(
            f"  {index}. {label} {allocated_hours:.1f} h"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())