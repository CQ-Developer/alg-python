from src.leetcode.n316.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual('abc', self.solution.remove_duplicate_letters('bcabc'))

    def test_b(self):
        self.assertEqual('acdb', self.solution.remove_duplicate_letters('cbacdcbc'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
