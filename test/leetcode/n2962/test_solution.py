from src.leetcode.n2962.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(6, self.solution.count_subarrays([1, 3, 2, 3, 3], 2))

    def test_b(self):
        self.assertEqual(0, self.solution.count_subarrays([1, 4, 2, 1], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
