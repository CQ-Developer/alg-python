from unittest import TestCase, SkipTest

from src.leetcode.n3623.solution import Solution, SolutionA


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.count_trapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))

    def test_2(self):
        self.assertEqual(1, self.solution.count_trapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
