"""Unit tests for p012.py"""

import unittest

from problems.p012 import count_divisors, first_natural_with_n_divisors


class TestDivisors(unittest.TestCase):

    def test_count_divisors(self):
        self.assertEqual(count_divisors(28), 6)
        self.assertEqual(count_divisors(21), 4)

    def test_first_natural(self):
        self.assertEqual(first_natural_with_n_divisors(5), 28)
        self.assertEqual(first_natural_with_n_divisors(500), 76576500)
