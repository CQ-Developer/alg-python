from src.leetcode.n3449.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.maxScore([2, 4], 3))

    def test_2(self):
        self.assertEqual(2, self.solution.maxScore([1, 2, 3], 5))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
