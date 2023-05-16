"""Unit tests for p017.py"""

import unittest

from problems.p017 import number2words, solve


class TestPowerDigitSum(unittest.TestCase):

    def test_power_digit_sum(self):
        self.assertEqual(number2words(999999), 'Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')

    def test_solve(self):
        self.assertEqual(solve(), 21124)
