#
# Solution to Project Euler problem 14
# Longest Collatz sequence
#
# The following iterative sequence is defined for the set of
# positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the
# following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and
# finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.

# Which starting number, under one million, produces the
# longest chain?

# NOTE: Once the chain starts the terms are allowed to go
# above one million.
#

def collatz_genr(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n //= 2
            yield n
        else:
            n = (3 * n) + 1
            yield n


def collatz_len(n):
    c_len = 0
    for i in collatz_genr(n):
        c_len += 1
    return c_len


def solve():
    longest_chain_len = 0
    longest_chain_index = 0

    for i in range(1_000_000):
        cl = collatz_len(i)
        if cl > longest_chain_len:
            longest_chain_len = cl
            longest_chain_index = i
    return longest_chain_index


if __name__ == "__main__":
    print(solve())
