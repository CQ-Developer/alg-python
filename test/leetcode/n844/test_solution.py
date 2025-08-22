from src.leetcode.n844.solution import Solution, SolutionA, SolutionB
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertTrue(self.solution.backspace_compare('ab#c', 'ad#c'))

    def test_2(self):
        self.assertTrue(self.solution.backspace_compare('ab##', 'c#d#'))

    def test_3(self):
        self.assertFalse(self.solution.backspace_compare('a#c', 'b'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()


class TestSolutionB(TestSolution):

    def setUp(self):
        self.solution = SolutionB()
