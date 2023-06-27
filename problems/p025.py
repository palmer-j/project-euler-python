#
# Solution to Project Euler problem 25
# https://projecteuler.net/problem=25
# 1000-digit Fibonacci Number
#
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn-1 + Fn-2 where F1=1 and F2=1
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 32
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to
# contain 1000 digits?
#

def memo(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


@memo
def fib(x):
    if x in [1, 2]:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def numb_len(x):
    res = 0
    while x > 0:
        x //= 10
        res += 1
    return res


def solve():
    x = 1
    while True:
        if numb_len(fib(x)) >= 1000:
            return x
        x += 1


if __name__ == "__main__":
    print(solve())
