import datetime
from calendar import monthrange
from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(year, month, nth=4, weekday=3):
    if nth > 0:
        # Get first day of the month
        first = datetime.date(year, month, 1)
        # If it is the correct weekday, then the Nth weekday will be in N weeks
        # otherwise, move to the correct weekday and jump N weeks later
        if first.weekday() == weekday:
            return first + datetime.timedelta(weeks=nth - 1)
        else:
            return first + datetime.timedelta(days=(weekday - first.weekday()) % 7, weeks=nth - 1)
    else:
        # Get last day of the month
        last = datetime.date(year, month, monthrange(year, month)[1])
        # If it is the correct weekday, then the Nth weekday will be in N weeks
        # otherwise, move to the correct weekday and jump N weeks backward
        if last.weekday() == weekday:
            return last - datetime.timedelta(weeks=abs(nth) - 1)
        else:
            return last - datetime.timedelta(days=(last.weekday() - weekday) % 7, weeks=abs(nth) - 1)

if __name__ == "__main__":
    print(meetup_date(2020, 1))
    print(meetup_date(2020, 1, nth=-1, weekday=Weekday.FRIDAY))