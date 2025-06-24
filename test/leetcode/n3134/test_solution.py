from src.leetcode.n3134.solution import Solution
from unittest import TestCase


class SolutionTest(TestCase):
    solution: Solution

    def setUp(self):
        self.skipTest('skip')

    def test_1(self):
        self.assertEqual(1, self.solution.median_of_uniqueness_array([1, 2, 3]))

    def test_2(self):
        self.assertEqual(2, self.solution.median_of_uniqueness_array([3, 4, 3, 4, 5]))

    def test_3(self):
        self.assertEqual(2, self.solution.median_of_uniqueness_array([4, 3, 5, 4]))
