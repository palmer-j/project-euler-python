#
# Solution to Project Euler problem 22
# https://projecteuler.net/problem=22
# Names Scores
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?


def sorted_names_from_file(filepath):
    with open(filepath, 'r') as f:
        file_txt = f.read()
        names = [n[1:-1] for n in file_txt.split(',')]
        return sorted(names)


def name_score(name):
    return sum([ord(char) - ord('A') + 1 for char in name])


def sum_name_scores(names):
    ans = 0
    for idx, name in enumerate(names):
        ans += name_score(name) * (idx + 1)
    return ans


def solve():
    names = sorted_names_from_file('./data/0022_names.txt')
    score = sum_name_scores(names)
    return score


if __name__ == "__main__":
    print(solve())
