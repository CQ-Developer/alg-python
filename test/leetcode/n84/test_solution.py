from src.leetcode.n84.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(10, self.solution.largest_rectangle_area([2, 1, 5, 6, 2, 3]))

    def test_b(self):
        self.assertEqual(4, self.solution.largest_rectangle_area([2, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TesSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
