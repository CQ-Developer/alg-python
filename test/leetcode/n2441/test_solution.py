from unittest import TestCase, SkipTest
from src.leetcode.n2441.solution import Solution, SolutionA


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(3, self.solution.find_max_k([-1, 2, -3, 3]))

    def test_2(self):
        self.assertEqual(7, self.solution.find_max_k([-1, 10, 6, 7, -7, 1]))

    def test_3(self):
        self.assertEqual(-1, self.solution.find_max_k([-10, 8, 6, 7, -2, -3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
