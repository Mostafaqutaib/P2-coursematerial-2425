import pytest
from tasks import Task, Tasklist
from datetime import date, timedelta


def test_task():
    today = date.today()
    task = Task("bake cake", today)

    assert task.description == "bake cake"
    assert task.due_date == today
    assert task.finished is False 

def test_task_can_be_marked_finished():
    today = date.today()
    task = Task("study testing", today)

    assert task.finished is False  # قبل

    task.finished = True

    assert task.finished is True   # بعد
    
@pytest.mark.parametrize("value, expected", [
    (True, True),
    (False, False),
    (1, True),
    (0, False),
    ("something", True),
    ("", False),
])
def test_task_finished_coerces_to_bool(value, expected):
    today = date.today()
    task = Task("anything", today)

    task.finished = value

    assert task.finished is expected
def test_task_description_is_readonly():
    task = Task("original", date.today())

    with pytest.raises(AttributeError):
        task.description = "new one"
def test_add_future_task_increases_length():
    tasks = Tasklist()
    tomorrow = date.today() + timedelta(days=1)
    task = Task("future task", tomorrow)

    tasks.add_task(task)

    assert len(tasks) == 1
    assert tasks.due_tasks == [task]
    assert tasks.finished_tasks == []
    assert tasks.overdue_tasks == []
def test_add_past_task_raises():
    tasks = Tasklist()
    yesterday = date.today() - timedelta(days=1)
    old_task = Task("old", yesterday)

    with pytest.raises(RuntimeError):
        tasks.add_task(old_task)