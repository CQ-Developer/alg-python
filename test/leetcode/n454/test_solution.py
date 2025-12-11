from src.leetcode.n454.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(2, self.solution.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))

    def test_b(self):
        self.assertEqual(1, self.solution.four_sum_count([0], [0], [0], [0]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
