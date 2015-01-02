__author__ = 'anthonymace'

def get_hours_from_week():
    week_one_hours = input("Enter your hours from week 1: ")
    week_two_hours = input("Enter your hours from week 2: ")
    return week_one_hours, week_two_hours

def split_hours_and_add(hours_list):
    week_one_hours = hours_list[0]
    week_two_hours = hours_list[1]
    week_one_hours_split = week_one_hours.split(':')
    week_two_hours_split = week_two_hours.split(':')
    added_hours = int(week_one_hours_split[0]) + int(week_two_hours_split[0])
    added_minutes = int(week_one_hours_split[1]) + int(week_two_hours_split[1])
    converted_time = convert_minutes(added_minutes)
    added_hours += converted_time[0]
    added_minutes = converted_time[1]
    return added_hours, added_minutes

def convert_minutes(mins):
    if (mins >= 60):
        mins -= 60
        hours = 1
    else:
        return mins
    return hours, mins


def main():
    hours_list = get_hours_from_week()
    print(hours_list)
    final_total = split_hours_and_add(hours_list)
    if (final_total[1] >= 10):
        print("Your time for 2 weeks is {}:{}".format(final_total[0], final_total[1]))
    else:
        print("Your time for 2 weeks is {}:0{}".format(final_total[0], final_total[1]))


main()