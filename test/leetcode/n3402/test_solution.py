from src.leetcode.n3402.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(15, self.solution.minimum_operations([[3, 2], [1, 3], [3, 4], [0, 1]]))

    def test_b(self):
        self.assertEqual(12, self.solution.minimum_operations([[3, 2, 1], [2, 1, 0], [1, 2, 3]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
