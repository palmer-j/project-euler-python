"""Unit tests for p026.py"""

import unittest

from problems.p026 import reciprocal_cycle_len, solve


class TestReciprocalCycleLen(unittest.TestCase):

    def test_reciprocal_cycle_len(self):
        self.assertEqual(reciprocal_cycle_len(7), 6)

    def test_solve(self):
        self.assertEqual(solve(), 983)
