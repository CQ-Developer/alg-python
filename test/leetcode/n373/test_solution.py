from src.leetcode.n373.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertListEqual([[1, 2], [1, 4], [1, 6]], self.solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))

    def test_2(self):
        self.assertListEqual([[1, 1], [1, 1]], self.solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
