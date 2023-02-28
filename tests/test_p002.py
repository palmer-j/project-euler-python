"""Unit tests for p1.py."""

import unittest

from problems.p002 import even_fib_sum


class TestSumOfMultiples(unittest.TestCase):

    def test_sum_of_multiples(self):
        self.assertEqual(even_fib_sum(4_000_000), 4613732)