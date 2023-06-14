"""Unit tests for p021.py"""

import unittest

from problems.p021 import pre_compute_divisor_sums, sum_amicable


class TestSumAmicable(unittest.TestCase):

    def test_pre_compute_divisor_sums(self):
        d_sums = pre_compute_divisor_sums(10_000)
        self.assertEqual(d_sums[220], 284)
        self.assertEqual(d_sums[284], 220)

    def test_sum_amicable(self):
        self.assertEqual(sum_amicable(10_000), 31626)
