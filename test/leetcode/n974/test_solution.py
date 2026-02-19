from src.leetcode.n974.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(7, self.solution.subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))

    def test_b(self):
        self.assertEqual(0, self.solution.subarrays_div_by_k([5], 9))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
