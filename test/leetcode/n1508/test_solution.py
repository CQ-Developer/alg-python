from src.leetcode.n1508.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(13, self.solution.range_sum([1, 2, 3, 4], 4, 1, 5))

    def test_2(self):
        self.assertEqual(6, self.solution.range_sum([1, 2, 3, 4], 4, 3, 4))

    def test_3(self):
        self.assertEqual(50, self.solution.range_sum([1, 2, 3, 4], 4, 1, 10))
