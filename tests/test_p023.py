"""Unit tests for p023.py"""

import unittest

from problems.p023 import compute_abundants, solve


class TestNonAbundantSums(unittest.TestCase):

    def test_compute_abundants(self):
        abundants = compute_abundants(28123)
        self.assertEqual(abundants[0], 12)

    def test_solve(self):
        self.assertEqual(solve(), 4179871)
