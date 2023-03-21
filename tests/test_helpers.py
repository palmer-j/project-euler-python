"""Unit tests for p006.py."""

import unittest

from problems.euler_helpers import is_prime

class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

        self.assertTrue(is_prime(5555567))
        self.assertTrue(is_prime(34656788743))

        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

        self.assertFalse(is_prime(2343477711))
        self.assertFalse(is_prime(34656788430))
        

