from src.leetcode.n50.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertAlmostEqual(1024.0, self.solution.my_pow(2.0, 10), 5)

    def test_b(self):
        self.assertAlmostEqual(9.261, self.solution.my_pow(2.1, 3), 5)

    def test_c(self):
        self.assertAlmostEqual(0.25, self.solution.my_pow(2.0, -2), 5)


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
