from unittest import TestCase, SkipTest

from src.leetcode.n1128.solution import Solution


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        super().setUpClass()

    def test_1(self):
        self.assertEqual(1, self.solution.num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]]))

    def test_2(self):
        self.assertEqual(3, self.solution.num_equiv_domino_pairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
