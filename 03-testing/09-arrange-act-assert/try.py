def test_add_future_task_increases_length():
    #arrange
    tasks = Tasklist()
    tomorrow = date.today() + timedelta(days=1)
    task = Task("future task", tomorrow)
    #act
    tasks.add_task(task)
    #assert
    assert len(tasks) == 1
    assert tasks.due_tasks == [task]
    assert tasks.finished_tasks == []
    assert tasks.overdue_tasks == []