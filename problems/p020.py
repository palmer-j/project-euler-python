#
# Solution to Project Euler problem 20
# https://projecteuler.net/problem=20
# Factorial digit sum
#
# # n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

# Find the sum of the digits in the number 100!
#

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def digit_sum(n):
    digit_sum = 0
    while n >= 1:
        n, sum_inc = divmod(n, 10)
        digit_sum += sum_inc
    return digit_sum


def factorial_digit_sum(n):
    return digit_sum(factorial(n))


def solve():
    return factorial_digit_sum(100)


if __name__ == "__main__":
    print(solve())
