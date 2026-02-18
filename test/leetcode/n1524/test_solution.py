from src.leetcode.n1524.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.num_of_subarrays([1, 3, 5]))

    def test_b(self):
        self.assertEqual(0, self.solution.num_of_subarrays([2, 4, 6]))

    def test_c(self):
        self.assertEqual(16, self.solution.num_of_subarrays([1, 2, 3, 4, 5, 6, 7]))

    def test_d(self):
        self.assertEqual(4, self.solution.num_of_subarrays([100, 100, 99, 99]))

    def test_e(self):
        self.assertEqual(1, self.solution.num_of_subarrays([7]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
