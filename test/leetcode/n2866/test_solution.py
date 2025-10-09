from src.leetcode.n2866.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_1(self):
        self.assertEqual(13, self.solution.maximum_sum_of_heights([5, 3, 4, 1, 1]))

    def test_2(self):
        self.assertEqual(22, self.solution.maximum_sum_of_heights([6, 5, 3, 9, 2, 7]))

    def test_3(self):
        self.assertEqual(18, self.solution.maximum_sum_of_heights([3, 2, 5, 5, 2, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
