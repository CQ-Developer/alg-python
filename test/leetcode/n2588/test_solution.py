from src.leetcode.n2588.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.beautiful_subarrays([4, 3, 1, 2, 4]))

    def test_b(self):
        self.assertEqual(0, self.solution.beautiful_subarrays([1, 10, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
