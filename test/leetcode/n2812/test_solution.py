from src.leetcode.n2812.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(0, self.solution.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))

    def test_2(self):
        self.assertEqual(2, self.solution.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))

    def test_3(self):
        self.assertEqual(2, self.solution.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
