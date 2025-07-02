from src.leetcode.n852.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    def test_1(self):
        self.assertEqual(1, self.solution.peak_index_in_mountain_array([0, 1, 0]))

    def test_2(self):
        self.assertEqual(1, self.solution.peak_index_in_mountain_array([0, 2, 1, 0]))

    def test_3(self):
        self.assertEqual(1, self.solution.peak_index_in_mountain_array([0, 10, 5, 2]))
