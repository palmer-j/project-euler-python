#
# Solution to Project Euler problem 5
# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
#

import math

# The smallest number evenly divisible by all numbers in a set is also
# known as the lowest common multiple (LCM) of the set of numbers
#
# https://en.wikipedia.org/wiki/Least_common_multiple#Calculation
#
# The least common multiple can be computed from the greatest common
# divisor (gcd) with the formula:
# lcm(a, b) = |ab| / gcd(a, b)
#
# You can compute the LCM of more than two numbers by iteratively
# computing the LCM of two numbers, i.e.
# lcm(a,b,c) = lcm(a,lcm(b,c))


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def solve():
    res = 1
    for i in range(1, 21):
        res = lcm(res, i)
    return res


if __name__ == "__main__":
    print(solve())
