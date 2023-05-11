#
# Solution to Project Euler problem 15
# https://projecteuler.net/problem=15
# Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being
# able to move to the right and down, there are exactly 6 routes
# to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#


import math


def memoize(func):
    memo = {}

    def helper(*x):
        if x not in memo:
            memo[x] = func(*x)
        return memo[x]
    return helper


def solve(i_target, j_target):
    @memoize
    def search(i, j):
        if i > i_target or j > j_target:
            return 0
        if i == i_target and j == j_target:
            return 1
        return search(i + 1, j) + search(i, j + 1)
    return search(0, 0)

# This problem can also be solved using combinatorics:
# If we have m items of one kind (right move) and n items of
# another (down move) then there are (m+n)!/m!*n! ways to arrange them
# in this case we need to make exactly 20 left and right moves so this
# simplifies to (2n)!/(n!)^2


def solve_analytically(grid_size):
    return math.factorial(2 * grid_size) // math.factorial(grid_size) ** 2


if __name__ == "__main__":
    print(solve(20, 20))
    print(solve_analytically(20))
