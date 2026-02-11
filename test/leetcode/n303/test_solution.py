from src.leetcode.n303.solution import NumArray
from unittest import TestCase


class TestNumArray(TestCase):

    def test_a(self):
        code = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, code.sum_range(0, 2))
        self.assertEqual(-1, code.sum_range(2, 5))
        self.assertEqual(-3, code.sum_range(0, 5))
