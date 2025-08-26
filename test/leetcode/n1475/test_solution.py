from src.leetcode.n1475.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertListEqual([4, 2, 4, 2, 3], self.solution.final_prices([8, 4, 6, 2, 3]))

    def test_2(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.solution.final_prices([1, 2, 3, 4, 5]))

    def test_3(self):
        self.assertListEqual([9, 0, 1, 6], self.solution.final_prices([10, 1, 1, 6]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
