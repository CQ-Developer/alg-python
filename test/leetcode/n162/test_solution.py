from src.leetcode.n162.solution import Solution
from unittest import TestCase, SkipTest


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    def test_1(self):
        self.assertEqual(2, self.solution.find_peak_element([1, 2, 3, 1]))

    def test_2(self):
        self.assertIn(self.solution.find_peak_element([1, 2, 1, 3, 5, 6, 4]), [1, 5])
