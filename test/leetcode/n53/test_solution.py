from src.leetcode.n53.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(6, self.solution.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_b(self):
        self.assertEqual(1, self.solution.max_subarray([1]))

    def test_c(self):
        self.assertEqual(23, self.solution.max_subarray([5, 4, -1, 7, 8]))

    def test_d(self):
        self.assertEqual(-1, self.solution.max_subarray([-1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
