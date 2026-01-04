from src.leetcode.n3583.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(1, self.solution.special_triplets([6, 3, 6]))

    def test_b(self):
        self.assertEqual(1, self.solution.special_triplets([0, 1, 0, 0]))

    def test_c(self):
        self.assertEqual(2, self.solution.special_triplets([8, 4, 2, 8, 4]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
