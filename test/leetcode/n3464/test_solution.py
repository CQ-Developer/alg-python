from src.leetcode.n3464.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.maxDistance(2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4))

    def test_2(self):
        self.assertEqual(1, self.solution.maxDistance(2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4))

    def test_3(self):
        self.assertEqual(1, self.solution.maxDistance(2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5))
