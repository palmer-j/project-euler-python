"""Unit tests for p016.py"""

import unittest

from problems.p016 import power_digit_sum


class TestPowerDigitSum(unittest.TestCase):

    def test_power_digit_sum(self):
        self.assertEqual(power_digit_sum(2, 15), 26)
        self.assertEqual(power_digit_sum(2, 1000), 1366)
