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
    print(start[2])

    duration = duration.split(":")
    # duration[0] = hours
    # duration[1] = min

    new_time = ["", "", ""]
    # new_time[0] hours
    # new_time[1] min
    # new_time[2] day

    return get_next_time(start, duration, day)



def get_next_time(start: list, duration: list, day: str = None):

    if start[2] == "PM":
        hours_summed = int(duration[0]) + int(start[0]) + 12

    minutes_summed = int(duration[1]) + int(start[1])
    hours_summed = int(duration[0]) + int(start[0])

    total_days_summed = 0

    result = ["", "", "", ""]
    # result[0] = hours
    # result[1] = minutes
    # result[2] = AM-PM
    # result[3] = days

    while minutes_summed > 59:
        minutes_summed = minutes_summed - 60
        hours_summed = hours_summed + 1

    while hours_summed > 23:
        hours_summed = hours_summed - 24
        total_days_summed = total_days_summed + 1


    # -------- crating the result --------



    if minutes_summed <= 9:
        minutes_summed = f"0{minutes_summed}"

    result[1] = minutes_summed

    if hours_summed > 12:
        hours_summed = hours_summed - 12
        result[2] = change_am_or_pm(start[2])
    else:
        result[2] = start[2]

    result[0] = hours_summed

    result[3] = returning_day_result(total_days_summed, day)

    return f"{result[0]}:{result[1]} {result[2]}{result[3]}"




class DaysOfTheWeek(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

def get_next(day):
    if type(day) == int:
        next_day = day + 1
        if next_day >= 7:
            return DaysOfTheWeek.Monday.name
        else:
            return DaysOfTheWeek(day  + 1).name
    elif type(day) == str:
        get_next(DaysOfTheWeek[day.capitalize()].value)


def change_am_or_pm(am_or_pm: str):
    if am_or_pm.upper() == "AM":
        return "PM"
    else:
        return "AM"

def get_current_day(days_passed: int, day: str):
    for day_passed in range(days_passed):
        day = get_next(day)
    return day

def returning_day_result(days_passed: int, day: str):
    result_1 = ""
    result_2 = ""
    # handles the none value
    if day:
        result_1 = f", {get_current_day(days_passed, day)}"
    if days_passed == 0:
        pass
    elif days_passed == 1:
        result_2 = " (next day)"
    else:
        result_2 = f" ({days_passed} days later)"

    return result_1 + result_2

def day_of_duration(duration: list, caca: list):

    mins = int(duration[1]) + int(caca[1])
    hours = (int(duration[0])) + (int(caca[0]))
    days = 0

    while mins > 59 :
        mins = mins - 60
        hours = hours + 1
    while hours > 23 :
        hours = hours - 24
        days = days + 1


    return f"[added: {duration}, current: {caca},result = [{hours}:{mins}, days: {days}]]"
