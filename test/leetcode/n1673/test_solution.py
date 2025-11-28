from src.leetcode.n1673.solution import Solution, SolutonA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):

    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_a(self):
        self.assertListEqual([2, 6], self.solution.most_competitive([3, 5, 2, 6], 2))

    def test_b(self):
        self.assertListEqual([2, 3, 3, 4], self.solution.most_competitive([2, 4, 3, 3, 5, 4, 9, 6], 4))


class TestSolutionA(TestSolution):

    def setUp(self) -> None:
        self.solution = SolutonA()
