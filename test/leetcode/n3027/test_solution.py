from src.leetcode.n3027.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(0, self.solution.number_of_pairs([[1, 1], [2, 2], [3, 3]]))

    def test_b(self):
        self.assertEqual(2, self.solution.number_of_pairs([[6, 2], [4, 4], [2, 6]]))

    def test_c(self):
        self.assertEqual(2, self.solution.number_of_pairs([[3, 1], [1, 3], [1, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
