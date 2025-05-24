from unittest import TestCase
from src.leetcode.n2517.solution import Solution, SolutionA


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest("skip")

    def test_1(self):
        self.assertEqual(8, self.solution.maximumTastiness([13, 5, 1, 8, 21, 2], 3))

    def test_2(self):
        self.assertEqual(2, self.solution.maximumTastiness([1, 3, 1], 2))

    def test_3(self):
        self.assertEqual(0, self.solution.maximumTastiness([7, 7, 7, 7], 2))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
