from src.leetcode.n1504.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(13, self.solution.num_submat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))

    def test_b(self):
        self.assertEqual(24, self.solution.num_submat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
