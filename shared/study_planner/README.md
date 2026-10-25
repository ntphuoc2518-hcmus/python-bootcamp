# Study Planner

A command-line tool (CLI) that helps plan study tasks using a CSV file.

## How to Use

Open a terminal in the `python-bootcamp` root folder and run:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

## Supported Arguments

- `file`: Path to the CSV file containing study tasks (required).
- `--hours`: Number of hours available for studying (required).
- `--today`: Date in `YYYY-MM-DD` format. If not provided, the program uses today's date.