__author__ = 'anthonymace'

def get_hours_from_week():
    week_one_hours = input("Enter your hours from week 1: ")
    week_two_hours = input("Enter your hours from week 2: ")
    return week_one_hours, week_two_hours

def split_hours(hours_list):
    week_one_hours = hours_list[0]
    week_two_hours = hours_list[1]
    week_one_hours_split = week_one_hours.split(':')
    week_two_hours_split = week_two_hours.split(':')
    added_hours = int(week_one_hours_split[0]) + int(week_two_hours_split[0])
    added_minutes = int(week_one_hours_split[1]) + int(week_two_hours_split[1])
    print(added_hours)
    print(added_minutes)

def main():
    hours_list = get_hours_from_week()
    print(hours_list)
    split_hours(hours_list)


main()