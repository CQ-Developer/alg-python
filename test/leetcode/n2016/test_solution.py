from unittest import TestCase, SkipTest

from src.leetcode.n2016.solution import Solution, SolutionA


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(4, self.solution.maximum_difference([7, 1, 5, 4]))

    def test_2(self):
        self.assertEqual(-1, self.solution.maximum_difference([9, 4, 3, 2]))

    def test_3(self):
        self.assertEqual(9, self.solution.maximum_difference([1, 5, 2, 10]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
