from src.leetcode.n2711.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([[1, 1, 0], [1, 0, 1], [0, 1, 1]], self.solution.difference_of_distinct_values([[1, 2, 3], [3, 1, 5], [3, 2, 1]]))

    def test_b(self):
        self.assertListEqual([[0]], self.solution.difference_of_distinct_values([[1]]))

    def test_c(self):
        self.assertListEqual([[3, 3, 3, 3, 3, 3, 2, 1, 0], [2, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 2], [0, 1, 2, 3, 3, 3, 3, 3, 3]], self.solution.difference_of_distinct_values([[6, 28, 37, 34, 12, 30, 43, 35, 6], [21, 47, 38, 14, 31, 49, 11, 14, 49], [6, 12, 35, 17, 17, 2, 45, 27, 43], [34, 41, 30, 28, 45, 24, 50, 20, 4]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
