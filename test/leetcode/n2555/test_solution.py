from src.leetcode.n2555.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(7, self.solution.maximize_win([1, 1, 2, 2, 3, 3, 5], 2))

    def test_2(self):
        self.assertEqual(2, self.solution.maximize_win([1, 2, 3, 4], 0))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
