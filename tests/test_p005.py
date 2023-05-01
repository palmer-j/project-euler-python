"""Unit tests for p005.py."""

import unittest

from problems.p005 import lcm


class TestLCM(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
