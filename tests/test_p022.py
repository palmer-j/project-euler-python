"""Unit tests for p022.py"""

import unittest

from problems.p022 import name_score, sorted_names_from_file, solve


class TestNameSocore(unittest.TestCase):

    def test_name_score(self):
        names = sorted_names_from_file('./data/0022_names.txt')
        self.assertEqual(names[937], 'COLIN')
        self.assertEqual(name_score('COLIN'), 53)

    def test_solve(self):
        self.assertEqual(solve(), 871198282)
