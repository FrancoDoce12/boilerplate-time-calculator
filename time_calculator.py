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

    new_time = ["", "", ""]
    # new_time[0] hours
    # new_time[1] min
    # new_time[2] day

    return get_next_time(start, duration, day)


def return_day_am_or_pm(am_or_pm: str, twelve_hours_passed: int):
    result = ["", ""]
    total_days = 0
    if twelve_hours_passed % 2 == 1:
        if am_or_pm == "AM":
            result[0] = "PM"
        else:
            total_days = total_days + 1
            result[0] = "AM"
    else:
        result[0] = am_or_pm

    while twelve_hours_passed >1:
        twelve_hours_passed = twelve_hours_passed - 2
        total_days = total_days + 1

    result[1] = total_days

    return result


def get_day(days_to_change: int, day: str = None):

    result = ["", ""]

    extra_space = ""

    if days_to_change == 1:
        result[0] = " (next day)"
    elif days_to_change == 0:
        extra_space = ""
        result[0] = ""
    else:
        result[0] = f" ({days_to_change} days later)"

    if day:
        days_to_change = DaysOfTheWeek[day.capitalize()].value + days_to_change
        while days_to_change >= 7:
            days_to_change = days_to_change - 7
        if days_to_change == 0:
            result[1] = f", {day.capitalize()}{extra_space}"
        else:
            result[1] = f", {DaysOfTheWeek(days_to_change).name}{extra_space}"



    return f"{result[1]}{result[0]}"


def get_next_time(start: list, duration: list, day: str = None):
    minutes_summed = int(duration[1]) + int(start[1])
    hours_summed = int(duration[0]) + int(start[0])
    twelve_hours_summed = 0
    total_days_summed = 0

    result = ["", "", "", ""]
    # result[0] = hours
    # result[1] = minutes
    # result[2] = AM-PM
    # result[3] = days

    while minutes_summed > 59:
        minutes_summed = minutes_summed - 60
        hours_summed = hours_summed + 1

    while hours_summed > 11:
        hours_summed = hours_summed - 12
        twelve_hours_summed = twelve_hours_summed + 1

    # while twelve_hours_summed > 1:
    #     twelve_hours_summed = twelve_hours_summed - 2
    #     total_days_summed = total_days_summed + 1

    # -------- crating the result --------

    result[0] = hours_summed

    if minutes_summed < 10:
        result[1] = f"0{minutes_summed}"
    else:
        result[1] = minutes_summed

    result[2], result[3] = return_day_am_or_pm(start[2], twelve_hours_summed)

    result[3] = get_day(result[3], day)

    return f"{result[0]}:{result[1]} {result[2]}{result[3]}"


class DaysOfTheWeek(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7
