"""Unit tests for p027.py"""

import unittest

from problems.p027 import solve


class TestQuadraticPrimes(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(), -59231)
