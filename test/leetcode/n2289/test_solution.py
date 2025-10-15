from src.leetcode.n2289.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(3, self.solution.total_steps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))

    def test_b(self):
        self.assertEqual(0, self.solution.total_steps([4, 5, 7, 7, 13]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
