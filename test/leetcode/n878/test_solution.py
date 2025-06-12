from src.leetcode.n878.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.nthMagicalNumber(1, 2, 3))

    def test_2(self):
        self.assertEqual(6, self.solution.nthMagicalNumber(4, 2, 3))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
