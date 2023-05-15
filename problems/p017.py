#
# Solution to Project Euler problem 17
# https://projecteuler.net/problem=17
# Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage
#

key = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety',
}


def parse_word(n):
    word_list = []

    if n >= 1_000_000:
        raise NotImplementedError("Can't handle numbers above 1,000,000")

    if n >= 1000:
        thousands, thousands_remainder = divmod(n, 1000)
        word_list.append(parse_word(thousands))
        word_list.append('Thousand')
        n = thousands_remainder
    if n >= 100:
        hundreds, hundreds_remainder = divmod(n, 100)
        word_list.append(parse_word(hundreds))
        word_list.append('Hundred')
        n = hundreds_remainder
        if n:
            word_list.append('and')
    if n in key:
        word_list.append(key[n])
    elif n > 0:
        tens, tens_remainder = divmod(n, 10)
        word_list.append(key[tens * 10])
        word_list.append(key[tens_remainder])
    return word_list


def join_nested_list(nl, sep=' '):
    for idx, val in enumerate(nl):
        if isinstance(val, list):
            nl[idx] = join_nested_list(val, sep)
    return sep.join(nl)


def number2words(n, sep=' '):
    return join_nested_list(parse_word(n), sep)


def solve():
    return sum([len(number2words(i, '')) for i in range(1, 1001)])


if __name__ == "__main__":
    print(solve())
