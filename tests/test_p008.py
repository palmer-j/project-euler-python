"""Unit tests for p008.py"""

import unittest

from problems.p008 import largest_product

class TestLargestProduct(unittest.TestCase):

    def test_largest_product(self):
        self.assertEqual(largest_product(4), 5832)
        self.assertEqual(largest_product(13), 23514624000)
