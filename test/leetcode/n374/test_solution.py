from src.leetcode.n374.solution import Solution, SolutionA
from unittest import TestCase, SkipTest
from unittest.mock import patch, MagicMock


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    @patch('src.leetcode.n374.solution.guess')
    def test_1(self, mock: MagicMock):
        pick = 6
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        self.assertEqual(6, self.solution.guess_number(10))

    @patch('src.leetcode.n374.solution.guess')
    def test_2(self, mock: MagicMock):
        pick = 1
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        self.assertEqual(1, self.solution.guess_number(1))

    @patch('src.leetcode.n374.solution.guess')
    def test_3(self, mock: MagicMock):
        pick = 1
        mock.side_effect = lambda num: -1 if num > pick else 1 if num < pick else 0
        self.assertEqual(1, self.solution.guess_number(2))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
