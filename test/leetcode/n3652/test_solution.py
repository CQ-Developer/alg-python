from src.leetcode.n3652.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(10, self.solution.max_profit([4, 2, 8], [-1, 0, 1], 2))

    def test_b(self):
        self.assertEqual(9, self.solution.max_profit([5, 4, 3], [1, 1, 0], 2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
