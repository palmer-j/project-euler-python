"""Unit tests for p024.py"""

import unittest

from problems.p024 import nth_permutation, solve


class TestNthPermutation(unittest.TestCase):

    def test_nth_permutation(self):
        self.assertEqual(nth_permutation(list(range(3)), 6), "210")

    def test_solve(self):
        self.assertEqual(solve(), "2783915460")
