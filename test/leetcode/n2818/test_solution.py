from src.leetcode.n2818.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(81, self.solution.maximum_score([8, 3, 9, 3, 8], 2))

    def test_b(self):
        self.assertEqual(4788, self.solution.maximum_score([19, 12, 14, 6, 10, 18], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
