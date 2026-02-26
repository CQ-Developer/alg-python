from src.leetcode.n1477.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls) -> None:
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(2, self.solution.min_sum_of_lengths([3, 2, 2, 4, 3], 3))

    def test_b(self):
        self.assertEqual(2, self.solution.min_sum_of_lengths([7, 3, 4, 7], 7))

    def test_c(self):
        self.assertEqual(-1, self.solution.min_sum_of_lengths([4, 3, 2, 6, 2, 3, 4], 6))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
