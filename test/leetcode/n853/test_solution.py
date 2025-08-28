from src.leetcode.n853.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(3, self.solution.car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

    def test_2(self):
        self.assertEqual(1, self.solution.car_fleet(10, [3], [3]))

    def test_3(self):
        self.assertEqual(1, self.solution.car_fleet(100, [0, 2, 4], [4, 2, 1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
