# Python Bootcamp — Team Homework

This repository is used to organize, implement, and test our team's Python homework for Weeks 1, 2, and 3.

Each member works in their own directory. We use GitHub Issues to track tasks, Pull Requests (PRs) to review code, and GitHub Actions to run automated tests.

## 1. Team Members

| GitHub Username     | Personal Directory           |
| ------------------- | ---------------------------- |
| `ntphuoc2518-hcmus` | `members/ntphuoc2518_hcmus/` |
| `trquan287`         | `members/trquan287/`         |
| `tinhha777qz-dev`   | `members/tinhha777qz_dev/`   |
| `qmtu2520-fit-clc`  | `members/qmtu2520_fit_clc/`  |
| `pqminh2007`        | `members/pqminh2007/`        |
| `NguyenTheHungCLC`  | `members/NguyenTheHungCLC/`  |

Each member should work primarily in their own directory unless the team assigns them to modify shared files.

## 2. Repository Structure

```text
python-bootcamp/
├── .github/
│   └── workflows/
│       └── ci.yml
├── members/
│   ├── ntphuoc2518_hcmus/
│   │   ├── w1/
│   │   ├── w2/
│   │   └── w3/
│   ├── trquan287/
│   ├── tinhha777qz_dev/
│   ├── qmtu2520_fit_clc/
│   ├── pqminh2007/
│   └── NguyenTheHungCLC/
├── shared/
│   ├── contract.py
│   └── study_planner/
├── tests/
│   ├── conftest.py
│   ├── test_w1.py
│   ├── test_w2.py
│   └── test_w3.py
├── PROGRESS.md
└── README.md
```

* `members/`: Contains each member's homework, organized by week.
* `shared/`: Contains code or components shared by multiple members.
* `tests/`: Contains automated tests for checking homework solutions.
* `.github/workflows/ci.yml`: Configures automated testing with GitHub Actions.
* `PROGRESS.md`: Tracks the team's overall progress.

The `.gitkeep` files keep otherwise empty directories in Git until actual files are added.

## 3. Environment Setup

Install Python and Git before starting. Use the Python version required by the course.

Open a terminal in the repository directory and check your installations:

```bash
python --version
git --version
```

Install `pytest` if it is not already available in your Python environment:

```bash
python -m pip install pytest
```

If the course or repository provides additional dependency installation instructions, follow those instructions as well.

## 4. Running Tests

Run the entire test suite:

```bash
python -m pytest -q
```

Run the tests for a specific week, such as Week 1:

```bash
python -m pytest -q tests/test_w1.py
```

Run Week 1 tests for a specific member and variant:

```bash
python -m pytest -q tests/test_w1.py --member ntphuoc2518_hcmus --variant 1
```

Run only tests whose names contain `summary`:

```bash
python -m pytest -q tests/test_w1.py --member ntphuoc2518_hcmus --variant 1 -k summary
```

Replace the member name with the corresponding Python package directory name. For example, the GitHub username `ntphuoc2518-hcmus` maps to the Python package name `ntphuoc2518_hcmus`.

If a test fails, read the error message, fix the code, and run the relevant tests again before creating or updating a Pull Request.

## 5. Weekly Homework Workflow

### Step 1 — Create or Update an Issue

Each member creates **one Issue per week** to track their individual homework.

Example Issue title:

```text
Python homework — W1 — ntphuoc2518-hcmus
```

Each Issue should include:

* The homework week.
* The responsible member.
* The assigned reviewer according to the team's rotation schedule.
* A checklist of individual exercises.
* Estimated and actual working hours.

Example Issue template:

```markdown
Week: w1
Member: @ntphuoc2518-hcmus
Reviewer (rotation): @reviewer-username

- [ ] W1-1
- [ ] W1-2
- [ ] W1-3
- [ ] W1-4
- [ ] W1-5

Estimated hours: 5
Actual hours:
```

Replace the reviewer placeholder with the member assigned to review your work. Update the checklist and actual working hours as your progress changes.

### Step 2 — Set the Milestone and Labels

Create the following milestones:

* `PY-W1`: Week 1 homework.
* `PY-W2`: Week 2 homework.
* `PY-W3`: Week 3 homework.

Set each milestone's due date according to the official course deadline.

Create these labels:

| Label       | Purpose               |
| ----------- | --------------------- |
| `python-hw` | Python homework tasks |
| `w1`        | Week 1 tasks          |
| `w2`        | Week 2 tasks          |
| `w3`        | Week 3 tasks          |
| `team-hw`   | Team homework tasks   |

For each Issue, select the appropriate milestone and labels. Assign the Issue to yourself using the **Assignees** section.

### Step 3 — Update the `main` Branch

Before starting new work, synchronize your local repository with the latest version:

```bash
git switch main
git pull origin main
```

### Step 4 — Create a Personal Branch

Each member must work on their own branch instead of committing directly to `main`.

Example:

```bash
git switch -c py/w1-ntphuoc2518-hcmus
```

Use the following branch naming convention:

```text
py/w<week>-<github-username>
```

For example:

```text
py/w2-trquan287
```

Continue using the same branch for additional changes to the same week's homework. You do not need to create a new branch for every commit.

### Step 5 — Implement and Test Your Code

Place your code in your personal directory and the correct week's folder.

For example:

```text
members/ntphuoc2518_hcmus/w1/
```

Run the relevant tests after completing each part of the homework. Mark an exercise as complete only after you have checked your implementation and confirmed that it works as expected.

### Step 6 — Commit and Push Your Changes

Check which files have changed:

```bash
git status
git diff
```

Stage the files you want to commit:

```bash
git add members/ntphuoc2518_hcmus/w1/
```

Create a commit:

```bash
git commit -m "feat(py-w1): implement grade summary"
```

Push your branch to GitHub:

```bash
git push -u origin py/w1-ntphuoc2518-hcmus
```

For later updates on the same branch, use:

```bash
git add <file-to-update>
git commit -m "fix(py-w1): handle edge cases"
git push
```

Replace the example paths and commit messages with ones that accurately describe your changes.

### Step 7 — Open a Pull Request

On GitHub, go to **Pull requests → New pull request**.

Choose the following branches:

* **Base:** `main`.
* **Compare:** your working branch.

Use this PR title format:

```text
py-w1: ntphuoc2518-hcmus
```

The team's recommended naming convention is:

```text
py-w<week>: <github-username>
```

In the PR description, summarize your changes and report the test results.

If the PR completes all the work tracked by an Issue, add:

```text
Closes #<issue-number>
```

Replace `<issue-number>` with the actual Issue number. Use `Closes` only when the PR completes the entire Issue. If other exercises in that Issue are still unfinished, do not use `Closes` yet; you may link the Issue without automatically closing it.

### Step 8 — Review and Merge

* Request the reviewer assigned according to the team's rotation schedule.
* Reviewers should check code correctness, naming, edge cases, and test results.
* If changes are requested, update your code and push the changes to the same branch.
* Merge only after the team's review and testing requirements have been satisfied.
* After merging, update your progress and close the Issue when the work is complete.

## 6. Team Collaboration Rules

1. Do not commit directly to `main`.
2. Work in your personal directory unless assigned to modify shared code.
3. Do not change tests merely to make them pass unless you have been assigned to maintain the tests.
4. Do not commit generated cache files such as `__pycache__/` or `.pyc` files.
5. Keep commits small and use descriptive commit messages.
6. Synchronize with `main` before starting new work.
7. Run the relevant tests before creating or updating a PR.
8. Have another team member review your code if required by the team's rules.
9. Update your Issue and `PROGRESS.md` when your progress changes.
10. If you encounter a blocker, inform the team early and explain the problem.

## 7. Automated Testing with GitHub Actions

This repository uses GitHub Actions to run automated checks based on `.github/workflows/ci.yml`.

After pushing code or opening a Pull Request, check the workflow status on GitHub.

* **Success:** All checks in the workflow completed successfully.
* **Failure:** Open the workflow details, inspect the error, and fix the issue before requesting a merge.
* **Warning:** Read the warning to determine whether action is needed. A warning does not necessarily mean that the tests failed.

A green CI status is a good sign, but it does not replace code review or verification that the solution meets the homework requirements.

## 8. Progress Tracking

The team uses the following tools:

* **Issues:** Track each member's homework tasks.
* **Milestones:** Track weekly progress and deadlines.
* **Labels:** Categorize tasks.
* **Pull Requests:** Review and propose code changes for integration.
* **GitHub Actions:** Run automated tests.
* **`PROGRESS.md`:** Summarize the team's overall progress.

Our goal is to make sure every member knows what to do, who will review their work, and how much of the homework has been completed.
