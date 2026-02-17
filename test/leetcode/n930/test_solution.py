from src.leetcode.n930.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.num_subarrays_with_sum([1, 0, 1, 0, 1], 2))

    def test_b(self):
        self.assertEqual(15, self.solution.num_subarrays_with_sum([0, 0, 0, 0, 0], 0))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
