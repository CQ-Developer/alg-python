from src.leetcode.n719.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(0, self.solution.smallestDistancePair([1, 3, 1], 1))

    def test_2(self):
        self.assertEqual(0, self.solution.smallestDistancePair([1, 1, 1], 2))

    def test_3(self):
        self.assertEqual(5, self.solution.smallestDistancePair([1, 6, 1], 3))
