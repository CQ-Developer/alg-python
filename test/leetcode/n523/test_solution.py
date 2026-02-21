from src.leetcode.n523.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertTrue(self.solution.check_subarray_sum([23, 2, 4, 6, 7], 6))

    def test_b(self):
        self.assertTrue(self.solution.check_subarray_sum([23, 2, 6, 4, 7], 6))

    def test_c(self):
        self.assertFalse(self.solution.check_subarray_sum([23, 2, 6, 4, 7], 13))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
