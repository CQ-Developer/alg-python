from src.leetcode.n1277.solution import Solution, SolutionA, SolutionB, SolutionC, SolutionD
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(15, self.solution.count_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))

    def test_b(self):
        self.assertEqual(7, self.solution.count_squares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))


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
