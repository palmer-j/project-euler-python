#
# Solution to Project Euler problem 27
# https://projecteuler.net/problem=27
# Quadratic Primes
#
# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However, when n = 40:
# 40^2 + 40 + 41 = 40(40 + 1) + 41  is divisible by 41, and certainly when:
# n = 41: 41^2 + 41 + 41  is clearly divisible by 41.
#
# The incredible formula m^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0<= n <= 79. The product of the
# coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
#
# Find the product of the coefficients, a  and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.


import itertools
from problems.euler_helpers import is_prime


def count_consecutive_primes(a, b):
    for n in itertools.count():
        if not is_prime(n ** 2 + a * n + b):
            return n


def solve():
    max_consec, max_a, max_b = -1, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            consec = count_consecutive_primes(a, b)
            if consec > max_consec:
                max_consec = consec
                max_a = a
                max_b = b
    return max_a * max_b


if __name__ == "__main__":
    print(solve())
