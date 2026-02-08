from src.leetcode.n498.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([1, 2, 4, 7, 5, 3, 6, 8, 9], self.solution.find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_b(self):
        self.assertListEqual([1, 2, 3, 4], self.solution.find_diagonal_order([[1, 2], [3, 4]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
