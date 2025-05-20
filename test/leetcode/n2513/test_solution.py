from unittest import TestCase
from src.leetcode.n2513.solution import Solution, SolutionA


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.minimizeSet(2, 7, 1, 3))

    def test_2(self):
        self.assertEqual(3, self.solution.minimizeSet(3, 5, 2, 1))

    def test_3(self):
        self.assertEqual(15, self.solution.minimizeSet(2, 4, 8, 2))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
