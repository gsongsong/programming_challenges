# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

if __name__ == "__main__":
    WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    mm, dd, yyyy = map(int, input().strip().split(' '))
    print(WEEKDAYS[calendar.weekday(yyyy, mm, dd)].upper())
