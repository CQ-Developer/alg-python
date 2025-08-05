from unittest import TestCase, SkipTest
from src.leetcode.n121.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(5, self.solution.max_profit([7, 1, 5, 3, 6, 4]))

    def test_2(self):
        self.assertEqual(0, self.solution.max_profit([7, 6, 4, 3, 1]))
