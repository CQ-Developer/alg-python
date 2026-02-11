from src.leetcode.n1310.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([2, 7, 14, 8], self.solution.xor_queries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))

    def test_b(self):
        self.assertListEqual([8, 0, 4, 4], self.solution.xor_queries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
