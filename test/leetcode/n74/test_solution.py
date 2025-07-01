from src.leetcode.n74.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertTrue(self.solution.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

    def test_2(self):
        self.assertFalse(self.solution.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
