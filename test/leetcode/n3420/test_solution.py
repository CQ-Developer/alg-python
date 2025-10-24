from src.leetcode.n3420.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(17, self.solution.count_non_decreasing_subarrays([6, 3, 1, 2, 4, 4], 7))

    def test_b(self):
        self.assertEqual(12, self.solution.count_non_decreasing_subarrays([6, 3, 1, 3, 6], 4))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
