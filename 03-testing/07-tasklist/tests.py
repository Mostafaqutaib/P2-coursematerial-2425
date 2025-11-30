import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import Calendar, CalendarStub

@pytest.fixture
def today():
    return date(2000, 1,1) 
@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)
@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)
@pytest.fixture
def next_week(today):
    return today + timedelta(days=7)
@pytest.fixture
def calendar(today):
    return CalendarStub(today)
@pytest.fixture
def sut(calendar):
    return TaskList(calendar)

def test_task_stores_description_and_due_date(today):
    # Arrange
    

    # Act
    sut = Task("bake cake", today)

    # Assert
    assert sut.description == "bake cake"
    assert sut.due_date == today
    assert sut.finished is False


def test_task_can_be_marked_finished(today):
    # Arrange
    task = Task("study testing", today)

    # Act
    task.finished = True

    # Assert
    assert task.finished is True


@pytest.mark.parametrize("value, expected", [
    (True, True),
    (False, False),
    (1, True),
    (0, False),
    ("something", True),
    ("", False),
])
def test_task_finished_coerces_to_bool(value, expected, today):
    # Arrange
    task = Task("anything", today)

    # Act
    task.finished = value

    # Assert
    assert task.finished is expected
def test_add_future_task_increases_length(tomorrow,sut):
    # Arrange

    task = Task("future task", tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.finished_tasks == []
    assert sut.overdue_tasks == []
def test_add_past_task_raises(yesterday, sut):
    # Arrange
    old_task = Task("old", yesterday)

    # Act + Assert
    with pytest.raises(RuntimeError):
        sut.add_task(old_task)
def test_task_becomes_overdue(tomorrow, sut, calendar, next_week):
    # Arrange
    task = Task("description", tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert sut.overdue_tasks == [task]
