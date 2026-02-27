from src.leetcode.n1124.solution import Solution, SolutionA, SolutionB, SolutionC, SolutionD
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(3, self.solution.longest_WPI([9, 9, 6, 0, 6, 6, 9]))

    def test_b(self):
        self.assertEqual(0, self.solution.longest_WPI([6, 6, 6]))


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
