from src.leetcode.n1901.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    def test_1(self):
        self.assertListEqual([0, 1], self.solution.find_peak_grid([[1, 4], [3, 2]]))

    def test_2(self):
        self.assertListEqual([1, 1], self.solution.find_peak_grid([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
