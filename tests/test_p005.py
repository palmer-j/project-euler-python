"""Unit tests for p005.py."""

import unittest

from problems.p005 import lcm


class TestIsPalindromic(unittest.TestCase):

    def test_prime_factor_generation(self):
        self.assertEqual(lcm(4, 6), 12)