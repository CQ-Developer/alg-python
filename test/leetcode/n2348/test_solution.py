from src.leetcode.n2348.solution import Solution, SolutionA, SolutionB, SolutionC, SolutionD, SolutionE
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(6, self.solution.zero_filled_subarray([1, 3, 0, 0, 2, 0, 0, 4]))

    def test_b(self):
        self.assertEqual(9, self.solution.zero_filled_subarray([0, 0, 0, 2, 0, 0]))

    def test_c(self):
        self.assertEqual(0, self.solution.zero_filled_subarray([2, 10, 2019]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()


class TestSolutionD(TestSolution):

    def setUp(self):
        self.solution = SolutionD()


class TestSolutionE(TestSolution):

    def setUp(self):
        self.solution = SolutionE()
