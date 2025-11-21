from src.leetcode.n2281.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(44, self.solution.total_strength([1, 3, 1, 2]))

    def test_b(self):
        self.assertEqual(213, self.solution.total_strength([5, 4, 6]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
