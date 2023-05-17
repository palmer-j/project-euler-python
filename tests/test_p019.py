"""Unit tests for p019.py"""

import unittest

from problems.p019 import solve, built_in_solve


class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(), 171)
        self.assertEqual(built_in_solve(), 171)
