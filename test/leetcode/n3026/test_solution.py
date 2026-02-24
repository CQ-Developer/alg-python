from src.leetcode.n3026.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(11, self.solution.maximum_subarray_sum([1, 2, 3, 4, 5, 6], 1))

    def test_b(self):
        self.assertEqual(11, self.solution.maximum_subarray_sum([-1, 3, 2, 4, 5], 3))

    def test_c(self):
        self.assertEqual(-6, self.solution.maximum_subarray_sum([-1, -2, -3, -4], 2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
