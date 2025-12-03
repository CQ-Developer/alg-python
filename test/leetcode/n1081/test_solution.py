from src.leetcode.n1081.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual('abc', self.solution.smallest_subsequence('bcabc'))

    def test_b(self):
        self.assertEqual('acdb', self.solution.smallest_subsequence('cbacdcbc'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
