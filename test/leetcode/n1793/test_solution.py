from src.leetcode.n1793.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract call')

    def test_a(self):
        self.assertEqual(15, self.solution.maximum_score([1, 4, 3, 7, 4, 5], 3))

    def test_b(self):
        self.assertEqual(20, self.solution.maximum_score([5, 5, 4, 5, 4, 1, 1, 1], 0))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
