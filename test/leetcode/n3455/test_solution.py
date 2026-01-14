from src.leetcode.n3455.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual(8, self.solution.shortest_matching_substring("abaacbaecebce", "ba*c*ce"))

    def test_b(self):
        self.assertEqual(-1, self.solution.shortest_matching_substring("baccbaadbc", "cc*baa*adb"))

    def test_c(self):
        self.assertEqual(0, self.solution.shortest_matching_substring("a", "**"))

    def test_d(self):
        self.assertEqual(6, self.solution.shortest_matching_substring("madlogic", "*adlogi*"))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
