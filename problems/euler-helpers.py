import math

def is_prime(x):
    if x <= 1: # by definition negative numbers are not prime
        return False
    elif x <= 3:
        return True
    else:
        # given that any prime can be expressed in the form  (6k ± 1)
        # we can optimise the trial division method
        lim = int(math.sqrt(x))
        for i in range(5, lim + 1, 6):
            if x % i == 0 or n % (i + 2) == 0:
                return False
        return True

def list_primes(n):
    pass

def prime_generator(limit):
    pass

