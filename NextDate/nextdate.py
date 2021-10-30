import datetime

class Weekday(object):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate(object):
    def __init__(self, day : Weekday) -> None:
        super().__init__()
        self.next_day = day
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({Weekday.__name__}.{dict({v : k for k, v in Weekday.__dict__.items()})[self.next_day]})"

    def days_until(self):
        d = datetime.date.today()
        days_ahead = self.next_day - d.weekday()
        if days_ahead < 0:
            days_ahead += 7
        return days_ahead

    def date(self):
        d = datetime.date.today()
        return d + datetime.timedelta(self.days_until())

if __name__ == '__main__':
    next_thursday = NextDate(Weekday.MONDAY)
    print(next_thursday.days_until())
    print(next_thursday.date())
    print(next_thursday)
    