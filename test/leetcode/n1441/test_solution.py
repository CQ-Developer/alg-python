from src.leetcode.n1441.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(['Push', 'Push', 'Pop', 'Push'], self.solution.build_array([1, 3], 3))

    def test_2(self):
        self.assertEqual(['Push', 'Push', 'Push'], self.solution.build_array([1, 2, 3], 3))

    def test_3(self):
        self.assertEqual(['Push', 'Push'], self.solution.build_array([1, 2], 4))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
