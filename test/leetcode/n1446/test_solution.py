from src.leetcode.n1446.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(2, self.solution.max_power('leetcode'))

    def test_b(self):
        self.assertEqual(5, self.solution.max_power('abbcccddddeeeeedcba'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
