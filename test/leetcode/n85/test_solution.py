from src.leetcode.n85.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract call')

    def test_a(self):
        self.assertEqual(6, self.solution.maximal_rectangle([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))

    def test_b(self):
        self.assertEqual(0, self.solution.maximal_rectangle([['0']]))

    def test_c(self):
        self.assertEqual(1, self.solution.maximal_rectangle([['1']]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
