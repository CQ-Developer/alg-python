from src.leetcode.n1930.solution import Solution, SolutionA, SolutionB, SolutionC
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(3, self.solution.count_palindromic_subsequence("aabca"))

    def test_b(self):
        self.assertEqual(0, self.solution.count_palindromic_subsequence("adc"))

    def test_c(self):
        self.assertEqual(4, self.solution.count_palindromic_subsequence("bbcbaba"))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()


class TestSolutionC(TestSolution):

    def setUp(self):
        self.solution = SolutionC()
