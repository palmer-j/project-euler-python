# 
# Solution to Project Euler problem 4
# Largest palindrome product
# 
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def is_palindromic(numb):
    return str(numb) == str(numb)[ : : -1]

def solve():

    res = max((i * j for i in range(100, 1000) for j in range(100, 1000) if is_palindromic(i * j)))

    return str(res)

if __name__ == "__main__":
	print(solve())