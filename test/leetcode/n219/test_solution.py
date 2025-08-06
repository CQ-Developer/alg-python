from unittest import TestCase, SkipTest

from src.leetcode.n219.solution import Solution, SolutionA


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')

    def test_1(self):
        self.assertTrue(self.solution.contains_nearby_duplicate([1, 2, 3, 1], 3))

    def test_2(self):
        self.assertTrue(self.solution.contains_nearby_duplicate([1, 0, 1, 1], 1))

    def test_3(self):
        self.assertFalse(self.solution.contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

    def test_4(self):
        self.assertFalse(self.solution.contains_nearby_duplicate([1], 1))

    def test_5(self):
        self.assertFalse(self.solution.contains_nearby_duplicate([1, 2, 1], 0))

    def test_6(self):
        self.assertTrue(self.solution.contains_nearby_duplicate([0, 1, 2, 3, 2, 5], 3))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
