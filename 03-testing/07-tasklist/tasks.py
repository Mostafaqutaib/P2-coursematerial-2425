from datetime import date, timedelta
from calendars import Calendar, CalendarsStub
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

class Tasklist:
    def __init__(self):
        self._task_lijst = []
        self._calendar = Calendar.today
    @property
    def calendar(self):
        return self._calendar
    
    
    def add_task(self, task):
        if task.due_date < date.today():
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
            if not t.finished and t.due_date < date.today()
        ]

tasks = Tasklist()
calendar = CalendarsStub(date(2000,1,1))
tomorrow = Calendar.today + timedelta(days=1)
yesterday = Calendar.today - timedelta(days=1)
task_of_tomorrow = Task('over wat het gaat', tomorrow)
tasks.add_task(task_of_tomorrow)
print(len(tasks))