from datetime import date, timedelta
from calendars import Calendar, CalendarStub
class Task:
    def __init__(self, description, due_date):
        self._description = description
        self._due_date = due_date
        self._finished = False

    @property
    def description(self):
        return self._description
    
    @property
    def due_date(self):
        return self._due_date
    
    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, value):
        self._finished = bool(value)
    
    def __repr__(self):
        return f"Task('{self.description}', {self.due_date}, finished={self.finished})"

class TaskList:
    def __init__(self, calendar):
        self._task_lijst = []
        self._calendar = calendar

    @property
    def calendar(self):
        return self._calendar
    
    
    def add_task(self, task):
        if task.due_date < self._calendar.today:
            raise RuntimeError("cannot add task in the past")
        self._task_lijst.append(task)
    
    def __len__(self):
        return len(self._task_lijst)
    @property
    def finished_tasks(self):
        return [t for t in self._task_lijst if t.finished]
    
    @property
    def due_tasks(self):
        return [t for t in self._task_lijst if not t.finished]
    @property
    def overdue_tasks(self):
        return [
            t 
            for t in self._task_lijst
            if not t.finished and t.due_date < self._calendar.today
        ]

