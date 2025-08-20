from src.leetcode.n3480.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(9, self.solution.max_subarrays(4, [[2, 3], [1, 4]]))

    def test_2(self):
        self.assertEqual(12, self.solution.max_subarrays(5, [[1, 2], [2, 5], [3, 5]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
