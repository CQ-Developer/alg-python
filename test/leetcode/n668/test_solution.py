from src.leetcode.n668.solution import Solution, SolutionA
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.findKthNumber(3, 3, 5))

    def test_2(self):
        self.assertEqual(6, self.solution.findKthNumber(2, 3, 6))

    def test_3(self):
        self.assertEqual(31666344, self.solution.findKthNumber(9895, 28405, 100787757))

    def test_4(self):
        self.assertEqual(23437314, self.solution.findKthNumber(17452, 29185, 95573422))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
