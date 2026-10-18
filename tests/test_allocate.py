from shared.contract import Task
from shared.study_planner.allocate import allocate


def test_allocate_zero_or_negative_hours():
    t1 = Task(name="Task 1", effort_h=3)
    assert allocate([t1], 0) == []
    assert allocate([t1], -5) == []


def test_allocate_empty_tasks():
    assert allocate([], 10) == []


def test_allocate_sufficient_hours():
    t1 = Task(name="Task 1", effort_h=2)
    t2 = Task(name="Task 2", effort_h=3)
    blocks = allocate([t1, t2], 10)

    assert len(blocks) == 2
    assert blocks[0].task == t1
    assert blocks[0].hours == 2
    assert blocks[1].task == t2
    assert blocks[1].hours == 3


def test_allocate_partial_hours():
    t1 = Task(name="Task 1", effort_h=4)
    t2 = Task(name="Task 2", effort_h=4)
    blocks = allocate([t1, t2], 6)

    assert len(blocks) == 2
    assert blocks[0].hours == 4
    assert blocks[1].hours == 2