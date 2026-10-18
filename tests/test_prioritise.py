"""Unit tests for Module 2: prioritise (T-W2)."""

from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import calculate_priority, prioritise


def test_prioritise_empty():
    """Empty task list should return an empty list."""
    assert prioritise([], date(2026, 10, 26)) == []


def test_prioritise_single_task():
    """Single task should be returned in a list unchanged."""
    today = date(2026, 10, 26)
    task = Task(title="Single Task", importance=3, effort_h=2.0, deadline=date(2026, 10, 30))
    result = prioritise([task], today)
    assert result == [task]


def test_calculate_priority_score():
    """Verify priority calculation formula: importance / max(1, days_left)."""
    today = date(2026, 10, 26)

    # 4 days left: 4 / 4 = 1.0
    t1 = Task(title="Task 1", importance=4, effort_h=2.0, deadline=date(2026, 10, 30))
    assert calculate_priority(t1, today) == 1.0

    # 1 day left: 3 / 1 = 3.0
    t2 = Task(title="Task 2", importance=3, effort_h=1.0, deadline=date(2026, 10, 27))
    assert calculate_priority(t2, today) == 3.0

    # Due today (0 days left -> treated as 1): 5 / 1 = 5.0
    t3 = Task(title="Task 3", importance=5, effort_h=1.0, deadline=date(2026, 10, 26))
    assert calculate_priority(t3, today) == 5.0

    # Overdue (-2 days left -> treated as 1): 2 / 1 = 2.0
    t4 = Task(title="Task 4", importance=2, effort_h=1.0, deadline=date(2026, 10, 24))
    assert calculate_priority(t4, today) == 2.0


def test_prioritise_sorting_order():
    """Tasks should be sorted in descending order of priority score."""
    today = date(2026, 10, 26)

    t_exam = Task(title="DS exam", importance=5, effort_h=6.0, deadline=date(2026, 10, 30))  # 5 / 4 = 1.25
    t_assign = Task(title="Assignment", importance=4, effort_h=1.5, deadline=date(2026, 10, 27))  # 4 / 1 = 4.0
    t_quiz = Task(title="Pop quiz", importance=2, effort_h=0.5, deadline=date(2026, 10, 28))  # 2 / 2 = 1.0

    ordered = prioritise([t_exam, t_quiz, t_assign], today)

    # Expected order: Assignment (4.0) > DS exam (1.25) > Pop quiz (1.0)
    assert ordered == [t_assign, t_exam, t_quiz]


def test_prioritise_urgency_beats_higher_importance():
    """A task with lower importance but very close deadline can outrank a higher importance task."""
    today = date(2026, 10, 26)

    t_high_far = Task(title="Big Project", importance=5, effort_h=10.0, deadline=date(2026, 11, 5))  # 5 / 10 = 0.5
    t_low_soon = Task(title="Small Homework", importance=2, effort_h=1.0, deadline=date(2026, 10, 27))  # 2 / 1 = 2.0

    ordered = prioritise([t_high_far, t_low_soon], today)
    assert ordered == [t_low_soon, t_high_far]


def test_prioritise_preserves_equal_priority_order():
    """Tasks with identical priority scores preserve their original relative order (stable sort)."""
    today = date(2026, 10, 26)

    t1 = Task(title="Task A", importance=2, effort_h=1.0, deadline=date(2026, 10, 28))  # 2 / 2 = 1.0
    t2 = Task(title="Task B", importance=3, effort_h=1.0, deadline=date(2026, 10, 29))  # 3 / 3 = 1.0

    ordered = prioritise([t1, t2], today)
    assert ordered == [t1, t2]

    # Reversed input order should keep t2 first
    ordered_rev = prioritise([t2, t1], today)
    assert ordered_rev == [t2, t1]
