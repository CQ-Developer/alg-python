from src.leetcode.n848.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest("abc")

    def test_a(self):
        self.assertEqual("wqqwlcjnkphhsyvrkdod", self.solution.shifting_letters("mkgfzkkuxownxvfvxasy", [505870226, 437526072, 266740649, 224336793, 532917782, 311122363, 567754492, 595798950, 81520022, 684110326, 137742843, 275267355, 856903962, 148291585, 919054234, 467541837, 622939912, 116899933, 983296461, 536563513]))

    def test_b(self):
        self.assertEqual("rpl", self.solution.shifting_letters("abc", [3, 5, 9]))

    def test_c(self):
        self.assertEqual("gfd", self.solution.shifting_letters("aaa", [1, 2, 3]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
