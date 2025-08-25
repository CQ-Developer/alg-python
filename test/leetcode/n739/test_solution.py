from src.leetcode.n739.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([1, 1, 4, 2, 1, 1, 0, 0], self.solution.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    def test_2(self):
        self.assertListEqual([1, 1, 0], self.solution.daily_temperatures([30, 60, 90]))

    def test_3(self):
        self.assertListEqual([1, 1, 1, 0], self.solution.daily_temperatures([30, 40, 50, 60]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
