from src.leetcode.n71.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual('/home', self.solution.simplify_path('/home/'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
