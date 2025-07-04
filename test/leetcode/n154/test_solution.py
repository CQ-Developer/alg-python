from src.leetcode.n154.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls) -> None:
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    def test_1(self):
        self.assertEqual(1, self.solution.find_min([1, 3, 5]))

    def test_2(self):
        self.assertEqual(0, self.solution.find_min([2, 2, 2, 0, 1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
