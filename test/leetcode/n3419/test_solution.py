from unittest import TestCase
from src.leetcode.n3419.solution import Solution, SolutionA


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(1, self.solution.minMaxWeight(5, [[1, 0, 1], [2, 0, 2], [3, 0, 1], [4, 3, 1], [2, 1, 1]], 2))

    def test_2(self):
        self.assertEqual(-1, self.solution.minMaxWeight(5, [[0, 1, 1], [0, 2, 2], [0, 3, 1], [0, 4, 1], [1, 2, 1], [1, 4, 1]], 1))

    def test_3(self):
        self.assertEqual(2, self.solution.minMaxWeight(5, [[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [3, 4, 2], [4, 0, 1]], 1))

    def test_4(self):
        self.assertEqual(-1, self.solution.minMaxWeight(5, [[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [4, 0, 1]], 1))


class SolutionATest(SolutionTest):

    def setUp(self):
        self.solution = SolutionA()
