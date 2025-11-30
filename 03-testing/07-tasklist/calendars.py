from datetime import date
class Calendar:
    @property
    def today(self):
        return date.today()

from datetime import date

class CalendarStub:
    def __init__(self, today):
        self._today = today

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self, new_today):
        self._today = new_today
