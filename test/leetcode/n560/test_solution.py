from src.leetcode.n560.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.subarray_sum([1, 1, 1], 2))

    def test_b(self):
        self.assertEqual(2, self.solution.subarray_sum([1, 2, 3], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
