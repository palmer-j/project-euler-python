"""Unit tests for p025.py"""

import unittest

from problems.p025 import fib, solve


class TestFib(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(12), 144)

    def test_solve(self):
        self.assertEqual(solve(), 4782)
