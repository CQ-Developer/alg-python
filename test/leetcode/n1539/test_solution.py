from src.leetcode.n1539.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(9, self.solution.find_kth_positive([2, 3, 4, 7, 11], 5))

    def test_2(self):
        self.assertEqual(6, self.solution.find_kth_positive([1, 2, 3, 4], 2))
