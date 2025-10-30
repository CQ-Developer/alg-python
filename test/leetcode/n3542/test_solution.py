from src.leetcode.n3542.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(1, self.solution.min_operations([0, 2]))

    def test_b(self):
        self.assertEqual(3, self.solution.min_operations([3, 1, 2, 1]))

    def test_c(self):
        self.assertEqual(4, self.solution.min_operations([1, 2, 1, 2, 1, 2]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
