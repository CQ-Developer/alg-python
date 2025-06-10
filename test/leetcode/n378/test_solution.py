from src.leetcode.n378.solution import Solution, SolutionA, SolutionB
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(13, self.solution.kthSmallest(
            [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))

    def test_2(self):
        self.assertEqual(-5, self.solution.kthSmallest([[-5]], 1))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()


class SolutionBTest(SolutionTest):

    def setUp(self):
        self.solution = SolutionB()
