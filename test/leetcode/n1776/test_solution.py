from src.leetcode.n1776.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([1.0, -1.0, 3.0, -1.0], self.solution.get_collision_times([[1, 2], [2, 1], [4, 3], [7, 2]]))

    def test_b(self):
        self.assertListEqual([2.0, 1.0, 1.5, -1.0], self.solution.get_collision_times([[3, 4], [5, 4], [6, 3], [9, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
