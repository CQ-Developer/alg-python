from src.leetcode.n3739.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(5, self.solution.count_majority_subarrays([1, 2, 2, 3], 2))

    def test_b(self):
        self.assertEqual(10, self.solution.count_majority_subarrays([1, 1, 1, 1], 1))

    def test_c(self):
        self.assertEqual(0, self.solution.count_majority_subarrays([1, 2, 3], 4))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
