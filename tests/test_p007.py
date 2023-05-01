"""Unit tests for p007.py"""

import unittest

from problems.p007 import nth_prime


class TestNthPrime(unittest.TestCase):

    def test_nth_prime(self):
        self.assertEqual(nth_prime(6), 13)
        self.assertEqual(nth_prime(10_001), 104743)
