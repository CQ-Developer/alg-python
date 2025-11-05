from src.leetcode.n221.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract call')

    def test_a(self):
        self.assertEqual(4, self.solution.maximal_square([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))

    def test_b(self):
        self.assertEqual(1, self.solution.maximal_square([['0', '1'], ['1', '0']]))

    def test_c(self):
        self.assertEqual(0, self.solution.maximal_square([['0']]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
