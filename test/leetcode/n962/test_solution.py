from src.leetcode.n962.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(4, self.solution.max_width_ramp([6, 0, 8, 2, 1, 5]))

    def test_b(self):
        self.assertEqual(7, self.solution.max_width_ramp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
