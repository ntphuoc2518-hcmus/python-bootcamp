"""Unit and integration tests for shared/study_planner/__main__.py."""

import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from shared.study_planner.__main__ import run_pipeline

BOOTCAMP = Path(__file__).resolve().parents[1]
SAMPLE_CSV = BOOTCAMP / "samples" / "tasks.csv"


def test_run_pipeline_success():
    output = run_pipeline(SAMPLE_CSV, hours=2.0, reference_date=date(2026, 10, 26))
    assert "Assignment" in output
    assert "DS exam" in output
    assert "Total" in output
    assert "2.0" in output


def test_run_pipeline_missing_file():
    with pytest.raises(FileNotFoundError):
        run_pipeline("non_existent_file.csv", hours=2.0)


def test_run_pipeline_empty_file(tmp_path):
    empty = tmp_path / "empty.csv"
    empty.write_text("")
    with pytest.raises(ValueError, match="empty"):
        run_pipeline(empty, hours=2.0)


def test_run_pipeline_invalid_hours():
    with pytest.raises(ValueError, match="positive"):
        run_pipeline(SAMPLE_CSV, hours=-1.0)


def test_cli_execution_success():
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            str(SAMPLE_CSV),
            "--hours",
            "2",
            "--today",
            "2026-10-26",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert proc.returncode == 0
    assert "Assignment" in proc.stdout
    assert "DS exam" in proc.stdout


def test_cli_execution_missing_file():
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            "missing.csv",
            "--hours",
            "2",
        ],
        capture_output=True,
        text=True,
        cwd=BOOTCAMP,
        check=False,
    )
    assert proc.returncode == 1
    assert "Error:" in proc.stderr
