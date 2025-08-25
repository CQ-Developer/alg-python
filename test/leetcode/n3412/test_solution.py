from src.leetcode.n3412.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(5, self.solution.calculate_score('aczzx'))

    def test_2(self):
        self.assertEqual(0, self.solution.calculate_score('abcdef'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
