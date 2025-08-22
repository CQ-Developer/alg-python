from src.leetcode.n2390.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual('lecoe', self.solution.remove_stars('leet**cod*e'))

    def test_2(self):
        self.assertEqual('', self.solution.remove_stars('erase*****'))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
