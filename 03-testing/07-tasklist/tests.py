import pytest
from tasks import Task, TaskList
from calendars import Calendar, CalendarStub
from datetime import date, timedelta


def test_task():
    #arrange
    today = date(2000, 1, 1)
    tomorrow =  date(2000, 1, 2)
    next_week =  date(2000, 1, 8)
    #act
    sut = Task("bake cake", today)

    #assert
    assert sut.description == "bake cake"
    assert sut.due_date == today
    assert sut.finished is False 

def test_task_can_be_marked_finished():
    #arrange
    today = date(2000, 1, 1)

    #act
    task = Task("study testing", today)

    #assert
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
    #arrange
    today = date(2000, 1, 1)
    #act
    task = Task("anything", today)
    task.finished = value
    #assert
    assert task.finished is expected

def test_add_future_task_increases_length():
    #arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    task = Task("future task", tomorrow)
    #act
    sut = TaskList(Calendar)
    sut.add_task(task)
    #assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.finished_tasks == []
    assert sut.overdue_tasks == []
def test_add_past_task_raises():
    yesterday = date(2000, 1, 1) - timedelta(days=1)
    
    old_task = Task("old", yesterday)
    sut = TaskList(Calendar)

    with pytest.raises(RuntimeError):
        sut.add_task(old_task)

def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks
