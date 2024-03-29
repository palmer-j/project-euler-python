#
# Solution to Project Euler problem 6
# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
#


def sum_square_difference(lower_bound, upper_bound):

    sum_of_squares = sum([i * i for i in range(lower_bound, upper_bound + 1)])
    square_of_sum = sum([i for i in range(lower_bound, upper_bound + 1)]) ** 2

    return square_of_sum - sum_of_squares


def solve():
    return sum_square_difference(1, 100)


if __name__ == "__main__":
    print(solve())
