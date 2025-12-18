from src.leetcode.n2760.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(3, self.solution.longest_alternating_subarray([3, 2, 5, 4], 5))

    def test_b(self):
        self.assertEqual(1, self.solution.longest_alternating_subarray([1, 2], 2))

    def test_c(self):
        self.assertEqual(3, self.solution.longest_alternating_subarray([2, 3, 4, 5], 4))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
