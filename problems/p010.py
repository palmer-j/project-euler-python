#
# Solution to Project Euler problem 10
# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

from problems.euler_helpers import list_primes


def sum_summation(n):
    return sum(list_primes(n))


def solve():
    return sum_summation(2_000_000)


if __name__ == "__main__":
    print(solve())
