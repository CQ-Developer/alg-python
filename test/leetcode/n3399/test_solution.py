from unittest import TestCase
from src.leetcode.n3399.solution import Solution, SolutionA


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.minLength('000001', 1))

    def test_2(self):
        self.assertEqual(1, self.solution.minLength('0000', 2))

    def test_3(self):
        self.assertEqual(1, self.solution.minLength('0101', 0))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
