from src.leetcode.n3221.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(16, self.solution.max_score([1, 5, 8]))

    def test_b(self):
        self.assertEqual(42, self.solution.max_score([4, 5, 2, 8, 9, 1, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
