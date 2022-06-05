from enum import Enum


def add_time(start: str, duration: str, day: str = None):
    start = start.split()
    # start[0] = hours
    # start[1] = AM-PM
    start[1] = start[1].upper()

    start[0] = start[0].split(":")
    # start[0][0] = hours
    # start[0][1] = min

    start = [start[0][0], start[0][1], start[1]]
    # start[0] hours
    # start[1] min
    # start[2] AM-PM

    duration = duration.split(":")
    # duration[0] = hours
    # duration[1] = min


    return get_next_time(start, duration, day)



def get_next_time(start: list [str,str,str] , duration: list [str,str], day: str = None):

    start_hours = int(start[0])
    start_mins = int(start[1])
    start_am_pm: str = start[2].upper()

    duration_hours = int(duration[0])
    duration_mins = int(duration[1])


    if start_am_pm == "PM" :
        start_hours = start_hours + 12

    total_hours = start_hours + duration_hours
    total_mins = start_mins + duration_mins
    total_days = 0


    while total_mins >= 60:
        total_mins = total_mins - 60
        total_hours = total_hours + 1

    while total_hours >= 24:
        total_hours = total_hours - 24
        total_days = total_days +1


    return ensabling_the_result(total_hours, total_mins, total_days, day)

def ensabling_the_result(total_hours: int, total_mins: int, total_days: int, day: str):

    result_am_pm = calculate_am_or_pm(total_hours)

    if total_hours >= 13:
        total_hours = total_hours -12

    if total_hours == 0:
        total_hours = 12

    result_hours = total_hours

    if total_mins < 10:
        total_mins = f"0{total_mins}"

    result_day = returning_day_result(total_days, day)

    return f"{result_hours}:{total_mins} {result_am_pm}{result_day}"


class DaysOfTheWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

def get_next(day: DaysOfTheWeek):
    day_value_next = day.value + 1
    if day_value_next >= 7:
        return DaysOfTheWeek(0)
    return DaysOfTheWeek(day_value_next)


def calculate_am_or_pm(current_hours: int):
    if current_hours >= 12:
        return "PM"
    else:
        return "AM"

def get_current_day(days_passed: int, day: str):
    day = DaysOfTheWeek[day.capitalize()]
    for day_passed in range(days_passed):
        day = get_next(day)
    return day

def returning_day_result(days_passed: int, day: str):
    result_1 = ""
    result_2 = ""
    # handles the none value
    if day:
        result_1 = f", {get_current_day(days_passed, day).name}"
    if days_passed == 0:
        pass
    elif days_passed == 1:
        result_2 = " (next day)"
    else:
        result_2 = f" ({days_passed} days later)"

    return result_1 + result_2


