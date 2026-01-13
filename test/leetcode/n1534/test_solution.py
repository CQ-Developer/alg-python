from src.leetcode.n1534.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(4, self.solution.count_good_triplets([3, 0, 1, 1, 9, 7], 7, 2, 3))

    def test_b(self):
        self.assertEqual(0, self.solution.count_good_triplets([1, 1, 2, 2, 3], 0, 0, 1))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
