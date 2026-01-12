from src.leetcode.n447.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.number_of_boomerangs([[0, 0], [1, 0], [2, 0]]))

    def test_b(self):
        self.assertEqual(2, self.solution.number_of_boomerangs([[1, 1], [2, 2], [3, 3]]))

    def test_c(self):
        self.assertEqual(0, self.solution.number_of_boomerangs([[1, 1]]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
