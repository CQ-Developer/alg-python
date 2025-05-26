from src.leetcode.n1552.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.maxDistance([1, 2, 3, 4, 7], 3))

    def test_2(self):
        self.assertEqual(999999999, self.solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
