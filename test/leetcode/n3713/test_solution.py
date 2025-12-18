from src.leetcode.n3713.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(4, self.solution.longest_balanced('abbac'))

    def test_b(self):
        self.assertEqual(4, self.solution.longest_balanced('zzabccy'))

    def test_c(self):
        self.assertEqual(2, self.solution.longest_balanced('aba'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
