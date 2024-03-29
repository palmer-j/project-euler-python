#
# Solution to Project Euler problem 1
# Multiples of 3 or 5
#

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples_3_or_5(num):
    return sum([x for x in range(num) if x % 3 == 0 or x % 5 == 0])


def solve():
    return str(sum_of_multiples_3_or_5(1000))


if __name__ == "__main__":
    print(solve())
