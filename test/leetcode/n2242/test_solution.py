from src.leetcode.n2242.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(24, self.solution.maximum_score([5, 2, 9, 8, 4], [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))

    def test_b(self):
        self.assertEqual(-1, self.solution.maximum_score([9, 20, 6, 4, 11, 12], [[0, 3], [5, 3], [2, 4], [1, 3]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
