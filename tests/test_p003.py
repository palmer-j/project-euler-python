"""Unit tests for p003.py."""

import unittest

from problems.p003 import prime_factors


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factor_generation(self):
        self.assertListEqual(prime_factors(13_195), [5, 7, 13, 29])
        self.assertEqual(max(prime_factors(600_851_475_143)), 6857)
