from src.leetcode.interview.n17.n05.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7"], self.solution.find_longest_subarray(["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))

    def test_b(self):
        self.assertEqual([], self.solution.find_longest_subarray(["A", "A"]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
