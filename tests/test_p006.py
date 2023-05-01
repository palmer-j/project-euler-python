"""Unit tests for p006.py."""

import unittest

from problems.p006 import sum_square_difference


class TestSumSquareDifference(unittest.TestCase):

    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference(1, 10), 2640)
        self.assertEqual(sum_square_difference(1, 100), 25164150)
