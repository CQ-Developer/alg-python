from src.leetcode.n1074.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.num_submatrix_sum_target([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))

    def test_b(self):
        self.assertEqual(5, self.solution.num_submatrix_sum_target([[1, -1], [-1, 1]], 0))

    def test_c(self):
        self.assertEqual(0, self.solution.num_submatrix_sum_target([[904]], 0))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
