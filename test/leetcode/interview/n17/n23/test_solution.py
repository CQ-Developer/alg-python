from src.leetcode.interview.n17.n23.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertListEqual([1, 0, 2], self.solution.find_square([[1, 0, 1], [0, 0, 1], [0, 0, 1]]))

    def test_b(self):
        self.assertListEqual([0, 0, 1], self.solution.find_square([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
