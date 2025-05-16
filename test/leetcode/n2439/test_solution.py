from src.leetcode.n2439.solution import Solution, SolutionA, SolutionB
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.minimizeArrayValue([3, 7, 1, 6]))

    def test_2(self):
        self.assertEqual(10, self.solution.minimizeArrayValue([10, 1]))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()


class SolutionBTest(SolutionTest):

    def setUp(self):
        self.solution = SolutionB()
