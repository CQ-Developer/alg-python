from src.leetcode.n2874.solution import Solution, SolutionA, SolutionB
from unittest.case import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(77, self.solution.maximum_triple_value([12, 6, 1, 2, 7]))

    def test_2(self):
        self.assertEqual(133, self.solution.maximum_triple_value([1, 10, 3, 4, 19]))

    def test_3(self):
        self.assertEqual(0, self.solution.maximum_triple_value([1, 2, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
