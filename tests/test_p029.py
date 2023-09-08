"""Unit tests for p029.py"""

import unittest

from problems.p029 import distrinct_powers_terms, solve


class TestDistinctPowers(unittest.TestCase):

    def test_distrinct_powers_terms(self):
        self.assertEqual(distrinct_powers_terms(5, 5), 15)
        self.assertEqual(distrinct_powers_terms(100, 100), 9183)

    def test_solve(self):
        self.assertEqual(solve(), 9183)
