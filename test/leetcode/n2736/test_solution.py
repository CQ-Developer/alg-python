from src.leetcode.n2736.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertListEqual([6, 10, 7], self.solution.maximum_sum_queries([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]))

    def test_b(self):
        self.assertListEqual([9, 9, 9], self.solution.maximum_sum_queries([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]))

    def test_c(self):
        self.assertListEqual([-1], self.solution.maximum_sum_queries([2, 1], [2, 3], [[3, 3]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
