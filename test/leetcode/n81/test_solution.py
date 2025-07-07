from src.leetcode.n81.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls) -> None:
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertTrue(self.solution.search([2, 5, 6, 0, 0, 1, 2], 0))

    def test_2(self):
        self.assertFalse(self.solution.search([2, 5, 6, 0, 0, 1, 2], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
