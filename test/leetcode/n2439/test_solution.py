from src.leetcode.n2439.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(5, self.solution.minimizeArrayValue([3, 7, 1, 6]))

    def test_2(self):
        self.assertEqual(10, self.solution.minimizeArrayValue([10, 1]))
