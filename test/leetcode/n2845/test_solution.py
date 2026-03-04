from src.leetcode.n2845.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(3, self.solution.count_interesting_subarrays([3, 2, 4], 2, 1))

    def test_b(self):
        self.assertEqual(2, self.solution.count_interesting_subarrays([3, 1, 9, 6], 3, 0))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
