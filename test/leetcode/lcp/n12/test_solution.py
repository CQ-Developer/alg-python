from src.leetcode.lcp.n12.solution import Solution, SolutionA, SolutionB
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.minTime([1, 2, 3, 3], 2))

    def test_2(self):
        self.assertEqual(0, self.solution.minTime([999, 999, 999], 4))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()


class SolutionBTest(SolutionTest):

    def setUp(self):
        self.solution = SolutionB()
