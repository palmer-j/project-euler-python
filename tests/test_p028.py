"""Unit tests for p028.py"""

import unittest

from problems.p028 import spiral_diagonal_count, solve


class TestSpiralDiagonals(unittest.TestCase):

    def test_spiral_diagonals(self):
        self.assertEqual(spiral_diagonal_count(5), 101)
        self.assertEqual(spiral_diagonal_count(1001), 669171001)

    def test_solve(self):
        self.assertEqual(solve(), 669171001)
