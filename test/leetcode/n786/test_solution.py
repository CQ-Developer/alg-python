from src.leetcode.n786.solution import Solution, SolutionA, SolutionB
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertListEqual([2, 5], self.solution.kth_smallest_prime_fraction([1, 2, 3, 5], 3))

    def test_2(self):
        self.assertListEqual([1, 7], self.solution.kth_smallest_prime_fraction([1, 7], 1))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()


class SolutionBTest(SolutionTest):

    def setUp(self):
        self.solution = SolutionB()
