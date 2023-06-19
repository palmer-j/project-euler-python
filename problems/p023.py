#
# Solution to Project Euler problem 23
# https://projecteuler.net/problem=23
# Non-Abundant Sums
#
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
#


def compute_abundants(limit=28123):
    # using same method used in p021
    d_sums = [0 for i in range(limit)]
    for i in range(1, limit):
        for j in range(i * 2, limit, i):
            d_sums[j] += i
    abundants = [idx for idx, val in enumerate(d_sums) if val > idx]
    return abundants


def compute_abundant_sums(limit=28123):
    abundants = compute_abundants(limit)
    expressible = [False for i in range(limit)]
    for i in abundants:
        for j in abundants:
            if i + j < limit:
                expressible[i + j] = True
    return [idx for idx, val in enumerate(expressible) if not val]


def solve():
    return sum(compute_abundant_sums(28123))


if __name__ == "__main__":
    print(solve())
