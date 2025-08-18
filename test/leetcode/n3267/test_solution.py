from src.leetcode.n3267.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.count_pair([1023, 2310, 2130, 213]))

    def test_2(self):
        self.assertEqual(3, self.solution.count_pair([1, 10, 100]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
