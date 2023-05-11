"""Unit tests for p015.py"""

import unittest

from problems.p015 import solve, solve_analytically


class TestCollatz(unittest.TestCase):

    def test_dynmaic(self):
        self.assertEqual(solve(2, 2), 6)
        self.assertEqual(solve(20, 20), 137846528820)

    def test_analytic(self):
        self.assertEqual(solve_analytically(2, 2), 6)
        self.assertEqual(solve_analytically(20, 20), 137846528820)
