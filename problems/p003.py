# 
# Solution to Project Euler problem 3
# Largest prime factor
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#

import math

def prime_factors(n):
	
	factors = []

	# find even prime factors
	while n % 2 == 0:
		factors.append(2)
		n = n / 2

	max_prime = int(math.sqrt(n))

	# find odd prime factors
	for i in range(3, max_prime + 1, 2):
		while n % i == 0:
			factors.append(i)
			n = n / i

	# checks for condition that n is itself prime
	if n > 2:
		factors.append(n)

	return factors

def solve():
	return str(max(prime_factors(600_851_475_143)))

if __name__ == "__main__":
	#print(solve())

	print(prime_factors(13195))