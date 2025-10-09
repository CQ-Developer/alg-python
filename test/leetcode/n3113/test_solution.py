from src.leetcode.n3113.solution import Solution, SolutionA
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('abstract')

    def test_1(self):
        self.assertEqual(6, self.solution.numberOfSubarrays([1, 4, 3, 3, 2]))

    def test_2(self):
        self.assertEqual(6, self.solution.numberOfSubarrays([3, 3, 3]))

    def test_3(self):
        self.assertEqual(1, self.solution.numberOfSubarrays([1]))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
