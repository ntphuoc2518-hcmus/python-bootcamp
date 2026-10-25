import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> int:
    """Run the study planner command-line interface."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a CSV file."
    )
    parser.add_argument("csv_file", type=Path, help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study time in hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Reference date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    if args.hours <= 0:
        print("Error: --hours must be greater than 0.", file=sys.stderr)
        return 1

    if not args.csv_file.is_file():
        print(f"Error: file not found: {args.csv_file}", file=sys.stderr)
        return 1

    try:
        tasks = parse_csv(args.csv_file)
        ordered_tasks = prioritise(tasks, args.today)
        blocks = allocate(ordered_tasks, args.hours)
        print(render(blocks))
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_file}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
