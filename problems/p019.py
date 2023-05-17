#
# Solution to Project Euler problem 19
# https://projecteuler.net/problem=19
# Counting Sundays
#
# You are given the following information, but you may prefer to do some
# research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#

import datetime

month_len = {0: 31,
             1: 28,
             2: 31,
             3: 30,
             4: 31,
             5: 30,
             6: 31,
             7: 31,
             8: 30,
             9: 31,
             10: 30,
             11: 31,
             }


def first_of_month_genr(start=(0, 1901), end=(11, 2000)):

    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0 and not year % 400 == 0:
                return False
            else:
                return True
        return False

    month = 0
    year = 1900
    day = 0
    while year < end[1] or (year <= end[1] and month <= end[0]):
        if year > start[1] or (year >= start[1] and month >= start[0]):
            yield day
        day += month_len[month]
        if month == 1 and is_leap(year):
            day += 1
        day %= 7
        year_inc, month = divmod(month + 1, 12)
        year += year_inc
    pass


def solve():
    return sum([1 for day in first_of_month_genr() if day == 6])


def built_in_solve():
    for year in range(1901, 2001):
        for month in range(0, 12):
            pass

    return sum(1
               for month in range(1, 13)
               for year in range(1901, 2001)
               if datetime.date(year, month, 1).weekday() == 6)


if __name__ == "__main__":
    print(solve())
    print(built_in_solve())
