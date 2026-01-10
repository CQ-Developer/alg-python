from src.leetcode.n3128.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.number_of_right_trianles([[0, 1, 0], [0, 1, 1], [0, 1, 0]]))

    def test_b(self):
        self.assertEqual(0, self.solution.number_of_right_trianles([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))

    def test_c(self):
        self.assertEqual(2, self.solution.number_of_right_trianles([[1, 0, 1], [1, 0, 0], [1, 0, 0]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
