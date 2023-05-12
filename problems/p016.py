#
# Solution to Project Euler problem 16
# https://projecteuler.net/problem=16
# Power digit sum
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?
#


def power_digit_sum(base, exponent):
    return sum([int(i) for i in str(base ** exponent)])


def solve():
    return power_digit_sum(2, 1000)


if __name__ == "__main__":
    print(solve())
