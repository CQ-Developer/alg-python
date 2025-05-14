from unittest import TestCase
from src.leetcode.n1631.solution import SolutionA


class TestSolution:

    def test_1(self):
        self.assertEqual(2, self.solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))

    def test_2(self):
        self.assertEqual(1, self.solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))

    def test_3(self):
        self.assertEqual(0, self.solution.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))


class TestSolutionA(TestCase, TestSolution):

    def setUp(self):
        self.solution = SolutionA()
