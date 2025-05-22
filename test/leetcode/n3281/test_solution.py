from src.leetcode.n3281.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.maxPossibleScore([6, 0, 3], 2))

    def test_2(self):
        self.assertEqual(5, self.solution.maxPossibleScore([2, 6, 13, 13], 5))
