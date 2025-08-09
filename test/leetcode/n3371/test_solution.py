from src.leetcode.n3371.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(10, self.solution.get_largest_outlier([2, 3, 5, 10]))

    def test_2(self):
        self.assertEqual(4, self.solution.get_largest_outlier([-2, -1, -3, -6, 4]))

    def test_3(self):
        self.assertEqual(5, self.solution.get_largest_outlier([1, 1, 1, 1, 1, 5, 5]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
