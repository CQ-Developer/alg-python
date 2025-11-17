from src.leetcode.n2104.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertEqual(4, self.solution.sub_array_ranges([1, 2, 3]))

    def test_b(self):
        self.assertEqual(4, self.solution.sub_array_ranges([1, 3, 3]))

    def test_c(self):
        self.assertEqual(59, self.solution.sub_array_ranges([4, -2, -3, 4, 1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
