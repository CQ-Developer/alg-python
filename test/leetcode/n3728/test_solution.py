from src.leetcode.n3728.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.count_stable_subarrays([9, 3, 3, 3, 9]))

    def test_b(self):
        self.assertEqual(0, self.solution.count_stable_subarrays([1, 2, 3, 4, 5]))

    def test_c(self):
        self.assertEqual(1, self.solution.count_stable_subarrays([-4, 4, 0, 0, -8, -4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
