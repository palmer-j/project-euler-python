"""Unit tests for p014.py"""

import unittest

from problems.p014 import collatz_genr, collatz_len, solve


class TestCollatz(unittest.TestCase):

    def test_genr(self):
        self.assertEqual(list(collatz_genr(13)), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_len(self):
        self.assertEqual(collatz_len(13), 10)

    def test_solve(self):
        self.assertEqual(solve(), 837799)
