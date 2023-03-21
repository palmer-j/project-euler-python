# 
# Solution to Project Euler problem 7
# 10001st prime
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
# 

from problems.euler_helpers import is_prime

def nth_prime(n):
    test_int = 1
    prime_counter = 0
    while prime_counter < n:
        test_int += 1
        if is_prime(test_int):
              prime_counter += 1
    return test_int

def solve():
    return nth_prime(10_001)

if __name__ == "__main__":
	print(solve())