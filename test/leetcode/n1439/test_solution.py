from src.leetcode.n1439.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(7, self.solution.kth_smallest([[1, 3, 11], [2, 4, 6]], 5))

    def test_2(self):
        self.assertEqual(17, self.solution.kth_smallest([[1, 3, 11], [2, 4, 6]], 9))

    def test_3(self):
        self.assertEqual(9, self.solution.kth_smallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 7))

    def test_4(self):
        self.assertEqual(12, self.solution.kth_smallest([[1, 1, 10], [2, 2, 9]], 7))
