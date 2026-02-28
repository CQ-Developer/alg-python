from src.leetcode.n2488.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(3, self.solution.count_subarrays([3, 2, 1, 4, 5], 4))

    def test_b(self):
        self.assertEqual(1, self.solution.count_subarrays([2, 3, 1], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
