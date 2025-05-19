from unittest import TestCase
from src.leetcode.n2616.solution import Solution, SolutionA


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_a(self):
        self.assertEqual(1, self.solution.minimizeMax([10, 1, 2, 7, 1, 3], 2))

    def test_b(self):
        self.assertEqual(0, self.solution.minimizeMax([4, 2, 1, 2], 1))

    def test_c(self):
        self.assertEqual(1, self.solution.minimizeMax([3, 4, 2, 3, 2, 1, 2], 3))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
