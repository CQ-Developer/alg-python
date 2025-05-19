from unittest import TestCase
from src.leetcode.n778.solution import Solution


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.swinInWater([[0, 2], [1, 3]]))

    def test_2(self):
        self.assertEqual(16, self.solution.swinInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))

    def test_3(self):
        self.assertEqual(11, self.solution.swinInWater([[11, 15, 3, 2], [6, 4, 0, 13], [5, 8, 9, 10], [1, 14, 12, 7]]))
