"""Unit tests for p009.py"""

import unittest

from problems.p009 import pythag_trip_with_target


class TestLargestProduct(unittest.TestCase):

    def test_largest_product(self):
        a, b, c = pythag_trip_with_target(12)
        prod = a * b * c
        self.assertEqual(prod, 60)

        a, b, c = pythag_trip_with_target(1000)
        prod = a * b * c
        self.assertEqual(prod, 31875000)
