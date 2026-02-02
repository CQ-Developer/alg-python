from src.leetcode.n3257.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.maximum_value_sum([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]))

    def test_b(self):
        self.assertEqual(15, self.solution.maximum_value_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_c(self):
        self.assertEqual(3, self.solution.maximum_value_sum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
