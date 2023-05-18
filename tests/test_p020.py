"""Unit tests for p020.py"""

import unittest

from problems.p020 import factorial_digit_sum


class TestFactorialDigitSum(unittest.TestCase):

    def test_factorial_digit_sum(self):
        self.assertEqual(factorial_digit_sum(10), 27)
        self.assertEqual(factorial_digit_sum(100), 648)
