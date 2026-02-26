from src.leetcode.n1546.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.max_non_overlapping([1, 1, 1, 1, 1], 2))

    def test_b(self):
        self.assertEqual(2, self.solution.max_non_overlapping([-1, 3, 5, 1, 4, 2, -9], 6))

    def test_c(self):
        self.assertEqual(2, self.solution.max_non_overlapping([-5, 5, -4, 5, 4], 5))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
