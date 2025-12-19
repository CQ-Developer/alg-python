from src.leetcode.n525.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(2, self.solution.find_max_length([0, 1]))

    def test_b(self):
        self.assertEqual(2, self.solution.find_max_length([0, 1, 0]))

    def test_c(self):
        self.assertEqual(6, self.solution.find_max_length([0, 1, 1, 1, 1, 1, 0, 0, 0]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
