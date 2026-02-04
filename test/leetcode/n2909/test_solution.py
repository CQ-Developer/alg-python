from src.leetcode.n2909.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(9, self.solution.minimum_sum([8, 6, 1, 5, 3]))

    def test_b(self):
        self.assertEqual(13, self.solution.minimum_sum([5, 4, 8, 7, 10, 2]))

    def test_c(self):
        self.assertEqual(-1, self.solution.minimum_sum([6, 5, 4, 3, 4, 5]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
