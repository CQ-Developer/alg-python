from src.leetcode.n153.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    def test_1(self):
        self.assertEqual(1, self.solution.find_min([3, 4, 5, 1, 2]))

    def test_2(self):
        self.assertEqual(0, self.solution.find_min([4, 5, 6, 7, 0, 1, 2]))

    def test_3(self):
        self.assertEqual(11, self.solution.find_min([11, 13, 15, 17]))
