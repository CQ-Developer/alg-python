from src.leetcode.n3116.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):

    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(9, self.solution.find_kth_smallest([3, 6, 9], 3))

    def test_2(self):
        self.assertEqual(12, self.solution.find_kth_smallest([5, 2], 7))

    def test_3(self):
        self.assertEqual(35, self.solution.find_kth_smallest([5], 7))
