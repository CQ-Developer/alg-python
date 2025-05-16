from unittest import TestCase
from src.leetcode.n2560.solution import Solution, SolutionA


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.minCapability([2, 3, 5, 9], 2))

    def test_2(self):
        self.assertEqual(2, self.solution.minCapability([2, 7, 9, 3, 1], 2))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
