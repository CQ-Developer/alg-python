from src.leetcode.n1.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertListEqual([0, 1], self.solution.two_sum([2, 7, 11, 15], 9))

    def test_2(self):
        self.assertListEqual([1, 2], self.solution.two_sum([3, 2, 4], 6))

    def test_3(self):
        self.assertListEqual([0, 1], self.solution.two_sum([3, 3], 6))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
