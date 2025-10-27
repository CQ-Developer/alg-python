from src.leetcode.n2832.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertListEqual([1, 4, 2, 1, 5], self.solution.maximum_length_of_ranges([1, 5, 4, 3, 6]))

    def test_b(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.solution.maximum_length_of_ranges([1, 2, 3, 4, 5]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
