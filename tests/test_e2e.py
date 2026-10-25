from datetime import date
from pathlib import Path
import pytest
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.allocate import allocate
from shared.study_planner.render import render

BOOTCAMP = Path(__file__).resolve().parents[1]

def test_study_planner_e2e() -> None:
    """End-to-end test for the study planner workflow using the existing sample CSV."""
    csv_path = BOOTCAMP / "samples" / "tasks.csv"
    assert csv_path.is_file(), f"Sample CSV file not found at {csv_path}"

    # 1. Parse input CSV
    tasks = parse_csv(csv_path)
    assert len(tasks) > 0, "Parsed tasks list should not be empty."

    # 2. Prioritize tasks
    prioritized_tasks = prioritise(tasks, today=date.today())
    assert len(prioritized_tasks) == len(tasks)

    # 3. Allocate study hours
    allocated_schedule = allocate(prioritized_tasks, hours=2)
    assert allocated_schedule is not None

    # 4. Render output results
    output_result = render(allocated_schedule)
    assert isinstance(output_result, str)
    assert "Assignment" in output_result