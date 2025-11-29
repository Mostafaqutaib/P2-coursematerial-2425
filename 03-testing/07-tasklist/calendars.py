from datetime import date
class Calendar:
    @property
    def today(self):
        return date.today()

class CalendarsStub:
    def __init__(self, initial_date):
        self._initial_date = initial_date
    @property
    def initial_date(self):
        return self._initial_date
    @initial_date.setter
    def initial_date(self, value):
        self._initial_date = value
    