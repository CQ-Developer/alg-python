from src.leetcode.n2506.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(2, self.solution.similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))

    def test_2(self):
        self.assertEqual(3, self.solution.similar_pairs(["aabb", "ab", "ba"]))

    def test_3(self):
        self.assertEqual(0, self.solution.similar_pairs(["nba", "cba", "dba"]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
