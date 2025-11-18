from src.leetcode.n1856.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(14, self.solution.max_sum_min_product([1, 2, 3, 2]))

    def test_b(self):
        self.assertEqual(18, self.solution.max_sum_min_product([2, 3, 3, 1, 2]))

    def test_c(self):
        self.assertEqual(60, self.solution.max_sum_min_product([3, 1, 5, 6, 4, 2]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
