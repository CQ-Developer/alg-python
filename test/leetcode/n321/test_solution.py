from src.leetcode.n321.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([9, 8, 6, 5, 3], self.solution.max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))

    def test_b(self):
        self.assertListEqual([6, 7, 6, 0, 4], self.solution.max_number([6, 7], [6, 0, 4], 5))

    def test_c(self):
        self.assertListEqual([9, 8, 9], self.solution.max_number([3, 9], [8, 9], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
