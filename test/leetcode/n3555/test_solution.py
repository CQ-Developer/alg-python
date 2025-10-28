from src.leetcode.n3555.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertListEqual([2, 2, 0], self.solution.min_subarray_sort([1, 3, 2, 4, 5], 3))

    def test_b(self):
        self.assertListEqual([4, 4], self.solution.min_subarray_sort([5, 4, 3, 2, 1], 4))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
