from src.leetcode.n1749.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(5, self.solution.max_absolute_sum([1, -3, 2, 3, -4]))

    def test_b(self):
        self.assertEqual(8, self.solution.max_absolute_sum([2, -5, 1, -4, 3, -2]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
