#
# Solution to Project Euler problem 28
# https://projecteuler.net/problem=28
# Number Spiral Diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def spiral_diagonal_count(size):
    # firstly ensure size is odd
    assert size % 2 == 1

    counter = 1
    spiral_sum = 1
    for r in range(2, size, 2):
        for _ in range(4):
            counter += r
            spiral_sum += counter
    return spiral_sum


def solve():
    return spiral_diagonal_count(1001)


if __name__ == "__main__":
    print(solve())
