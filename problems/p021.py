#
# Solution to Project Euler problem 21
# https://projecteuler.net/problem=21
# Amicable Numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55, 110 ; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000
#

# To solve this we will compute a table of proper divisor sums and then search
# through this for amicable pairs

def pre_compute_divisor_sums(max_n):

    pre_compute_divisor_sums = [0 for i in range(max_n)]
    for i in range(1, max_n):
        for j in range(i * 2, max_n, i):
            pre_compute_divisor_sums[j] += i
    return pre_compute_divisor_sums


def sum_amicable(max_n):
    ans = 0
    d_sums = pre_compute_divisor_sums(max_n)

    for idx, val in enumerate(d_sums):
        if idx != val and val <= max_n and d_sums[val] == idx:
            ans += idx
    return ans


if __name__ == "__main__":
    print(sum_amicable(10_000))
