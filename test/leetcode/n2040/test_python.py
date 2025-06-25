from src.leetcode.n2040.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(8, self.solution.kth_smallest_product([2, 5], [3, 4], 2))

    def test_2(self):
        self.assertEqual(0, self.solution.kth_smallest_product([-4, -2, 0, 3], [2, 4], 6))

    def test_3(self):
        self.assertEqual(-6, self.solution.kth_smallest_product([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
