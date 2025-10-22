from src.leetcode.n239.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertListEqual([3, 3, 5, 5, 6, 7], self.solution.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

    def test_b(self):
        self.assertListEqual([1], self.solution.max_sliding_window([1], 1))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
