#
# Solution to Project Euler problem 9
# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

def is_pythag_trip(a, b, c):
    return (a < b < c) and (a ** 2 + b ** 2 == c ** 2)


def pythag_trip_with_target(target=1000):
    upper_lim = target // 2
    for a in range(upper_lim + 1):
        for b in range(a, upper_lim + 1):
            c = target - (a + b)
            if is_pythag_trip(a, b, c):
                return a, b, c
    raise Exception("No triple found")


def solve():
    a, b, c = pythag_trip_with_target(1000)
    return a * b * c


if __name__ == "__main__":
    print(solve())
