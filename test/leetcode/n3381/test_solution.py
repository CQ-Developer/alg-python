from src.leetcode.n3381.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.max_subarray_sum([-5, 1, 2, -3, 4], 2))

    def test_b(self):
        self.assertEqual(-10, self.solution.max_subarray_sum([-1, -2, -3, -4, -5], 4))

    def test_c(self):
        self.assertEqual(3, self.solution.max_subarray_sum([1, 2], 1))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
