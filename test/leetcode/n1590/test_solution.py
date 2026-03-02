from src.leetcode.n1590.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(1, self.solution.min_subarray([3, 1, 4, 2], 6))

    def test_b(self):
        self.assertEqual(2, self.solution.min_subarray([6, 3, 5, 2], 9))

    def test_c(self):
        self.assertEqual(-1, self.solution.min_subarray([1, 2, 3], 7))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
