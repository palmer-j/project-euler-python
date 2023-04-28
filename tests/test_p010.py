"""Unit tests for p010.py"""

import unittest

from problems.p010 import sum_summation


class TestPrimeSummation(unittest.TestCase):

    def test_prime_summation(self):
        self.assertEqual(sum_summation(10), 17)
        self.assertEqual(sum_summation(2_000_000), 142913828922)
