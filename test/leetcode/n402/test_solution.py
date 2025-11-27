from src.leetcode.n402.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual('1219', self.solution.remove_k_digits('1432219', 3))

    def test_b(self):
        self.assertEqual('200', self.solution.remove_k_digits('10200', 1))

    def test_c(self):
        self.assertEqual('0', self.solution.remove_k_digits('10', 2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
