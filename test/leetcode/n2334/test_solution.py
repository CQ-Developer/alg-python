from src.leetcode.n2334.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertIn(self.solution.valid_subarray_size([1, 3, 4, 3, 1], 6), {3})

    def test_b(self):
        self.assertIn(self.solution.valid_subarray_size([6, 5, 6, 5, 8], 7), {1, 2, 3, 4, 5})


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
