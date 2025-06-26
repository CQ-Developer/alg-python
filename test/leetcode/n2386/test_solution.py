from src.leetcode.n2386.solution import Solution, SolutionA, SolutionB
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.k_sum([2, 4, -2], 5))

    def test_2(self):
        self.assertEqual(10, self.solution.k_sum([1, -2, 3, 4, -10, 12], 16))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()


class SolutionBTest(SolutionTest):

    def setUp(self):
        self.solution = SolutionB()
