from src.leetcode.n3446.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([[8, 2, 3], [9, 6, 7], [4, 5, 1]], self.solution.sort_matrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))

    def test_b(self):
        self.assertListEqual([[2, 1], [1, 0]], self.solution.sort_matrix([[0, 1], [1, 2]]))

    def test_c(self):
        self.assertListEqual([[1]], self.solution.sort_matrix([[1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
