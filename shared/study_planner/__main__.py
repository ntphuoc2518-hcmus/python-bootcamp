"""Study Planner CLI.

Executes the pipeline: parse_csv -> prioritise -> allocate -> render.
Usage:
    python -m shared.study_planner samples/tasks.csv --hours 2 [--today 2026-10-26]
"""

import argparse
from datetime import date
from pathlib import Path
import sys

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the study planner."""
    parser = argparse.ArgumentParser(
        description="Plan study hours for tasks loaded from a CSV file."
    )
    parser.add_argument(
        "file",
        type=str,
        help="Path to the CSV file containing study tasks.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Number of hours available for studying tonight.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format (defaults to today).",
    )
    return parser.parse_args(argv)


def run_pipeline(
    file_path: str | Path,
    hours: float,
    reference_date: date | None = None,
) -> str:
    """Execute the study planner pipeline and return rendered schedule."""
    csv_path = Path(file_path)
    if not csv_path.exists():
        msg = f"File not found: '{file_path}'"
        raise FileNotFoundError(msg)

    if not csv_path.is_file():
        msg = f"Path is not a regular file: '{file_path}'"
        raise ValueError(msg)

    if csv_path.stat().st_size == 0:
        msg = f"CSV file is empty: '{file_path}'"
        raise ValueError(msg)

    if hours <= 0:
        msg = f"Study hours must be positive, got {hours}"
        raise ValueError(msg)

    today = reference_date if reference_date is not None else date.today()

    tasks = parse_csv(csv_path)
    prioritized_tasks = prioritise(tasks, today=today)
    allocated_blocks = allocate(prioritized_tasks, hours=hours)
    return render(allocated_blocks)


def main(argv: list[str] | None = None) -> None:
    """Main CLI entry point for the study planner."""
    args = parse_args(argv)

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
        output = run_pipeline(args.file, args.hours, reference_date=today)
        print(output)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
