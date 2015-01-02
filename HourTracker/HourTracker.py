__author__ = 'anthonymace'

import datetime

def get_hours_from_each_day():
    hours_list = []
    for week in range(1, 3):
        number_of_days = int(input("How many days did you work week {}? ".format(week)))
        week_hours = []
        for day in range(1, number_of_days + 1):
            hours = input("Enter your hours from day #{}: ".format(day))
            week_hours.append(hours)
        hours_list.append(week_hours)
    return hours_list

def get_hours_from_week():
    week_one_hours = input("Enter your hours from week 1: ")
    week_two_hours = input("Enter your hours from week 2: ")
    return week_one_hours, week_two_hours

def split_hours_and_add(hours_list):
    hours_total = 0
    minutes_total = 0
    for weeks in hours_list:
        for day_hours in weeks:
            hours_total += add_hours_from_list(day_hours)
            minutes_total += add_minutes_from_list(day_hours)
    minutes_total = convert_minutes(minutes_total)
    hours_total += minutes_total[0]
    minutes_total = minutes_total[1]
    return hours_total, minutes_total

def add_hours_from_list(hour_string):
    hour = int(hour_string[0])
    return hour

def add_minutes_from_list(hour_string):
    minutes = int(hour_string[2:])
    return minutes

def convert_minutes(mins):
    additional_hours = 0
    if mins >= 60:
        while mins >= 60:
            mins -= 60
            additional_hours += 1
    else:
        return mins
    return additional_hours, mins

def hours_to_decimal(hours, minutes):
    total = hours + (minutes / 60.0)
    return total

def write_hours_to_file(hours, minutes, total_hours):
    today = datetime.date.today()
    file = open('hourLog.txt', 'a')
    file.write(str(today) + "\n")
    if minutes >= 10:
        file.write("Your time for 2 weeks is {}:{}\n".format(hours, minutes))
    else:
        file.write("Your time for 2 weeks is {}:{}\n".format(hours, minutes))
    file.write("Your hours in decimal: {:.2f}\n\n".format(total_hours))


def main():
    hours_list = get_hours_from_each_day()
    print(hours_list)
    final_total = split_hours_and_add(hours_list)
    total_hours = hours_to_decimal(int(final_total[0]), int(final_total[1]))
    write_hours_to_file(int(final_total[0]), int(final_total[1]), total_hours)
    print("Wrote hours to file")

main()