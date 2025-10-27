from src.leetcode.n1966.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abc')

    def test_a(self):
        self.assertEqual(1, self.solution.binary_searchable_numbers([7]))

    def test_b(self):
        self.assertEqual(1, self.solution.binary_searchable_numbers([-1, 5, 2]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
