from unittest import TestCase, SkipTest
from src.leetcode.n2905.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([0, 3], self.solution.find_indices([5, 1, 4, 1], 2, 4))

    def test_2(self):
        self.assertListEqual([0, 0], self.solution.find_indices([2, 1], 0, 0))

    def test_3(self):
        self.assertListEqual([-1, -1], self.solution.find_indices([1, 2, 3], 2, 4))
