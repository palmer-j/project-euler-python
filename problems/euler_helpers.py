import math


def is_prime(x):
    if x <= 1:  # by definition negative numbers are not prime
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    else:
        # given that any prime can be expressed in the form  (6k ± 1)
        # we can optimise the trial division method
        lim = int(math.sqrt(x))
        for i in range(5, lim + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True


def list_primality(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    res = [True for i in range(n + 1)]
    res[0], res[1] = False, False
    for i in range(math.floor(math.sqrt(n)) + 1):
        if res[i]:
            for j in range(i ** 2, n + 1, i):
                res[j] = False
    return res


def list_primes(n):
    return [i for i, isprime in enumerate(list_primality(n)) if isprime]


def prime_generator(limit):
    raise NotImplementedError
