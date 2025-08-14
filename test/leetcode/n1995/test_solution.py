from src.leetcode.n1995.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(1, self.solution.count_quadruplets([1, 2, 3, 6]))

    def test_2(self):
        self.assertEqual(0, self.solution.count_quadruplets([3, 3, 6, 4, 5]))

    def test_3(self):
        self.assertEqual(4, self.solution.count_quadruplets([1, 1, 1, 3, 5]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
