import argparse
import sys
from datetime import date
from pathlib import Path


def main() -> None:
    """CLI tool for processing assignment tasks."""
    parser = argparse.ArgumentParser(description="Task CLI assignment processor")
    parser.add_argument("csv_file", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=int, default=2, help="Hours allocation")
    parser.add_argument("--today", type=str, default=str(date.today()), help="Today's date YYYY-MM-DD")

    args = parser.parse_args()

    if not args.csv_file.is_file():
        print(f"Error: File '{args.csv_file}' not found.", file=sys.stderr)
        sys.exit(1)

    print("Assignment processing results:")
    try:
        args.csv_file.read_text(encoding="utf-8")
        print("Assignment details loaded successfully.")
    except OSError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()