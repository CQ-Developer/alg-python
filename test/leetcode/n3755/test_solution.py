from src.leetcode.n3755.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.max_balanced_subarray([3, 1, 3, 2, 0]))

    def test_b(self):
        self.assertEqual(8, self.solution.max_balanced_subarray([3, 2, 8, 5, 4, 14, 9, 15]))

    def test_c(self):
        self.assertEqual(0, self.solution.max_balanced_subarray([4, 1, 2, 3, 2, 2, 0, 4, 2, 3, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
