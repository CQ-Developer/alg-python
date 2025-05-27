from src.leetcode.n2528.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.maxPower([1, 2, 4, 5, 0], 1, 2))

    def test_2(self):
        self.assertEqual(4, self.solution.maxPower([4, 4, 4, 4], 0, 3))
