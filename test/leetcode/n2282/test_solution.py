from src.leetcode.n2282.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertListEqual([[2, 1, 2, 1, 0]], self.solution.see_people([[3, 1, 4, 2, 5]]))

    def test_b(self):
        self.assertListEqual([[3, 1], [2, 1], [1, 0]], self.solution.see_people([[5, 1], [3, 1], [4, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
