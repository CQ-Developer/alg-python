from src.leetcode.n1095.solution import Solution, SolutionA
from unittest import TestCase, SkipTest
from unittest.mock import patch, MagicMock


class TestSolution(TestCase):
    solution: Solution

    @classmethod
    def setUpClass(cls):
        if cls is TestSolution:
            raise SkipTest('skip')
        return super().setUpClass()

    @patch('src.leetcode.n1095.solution.MountainArray', spec=True)
    def test_1(self, MockMountainArray: MagicMock):
        arr = [1, 2, 3, 4, 5, 3, 1]
        mountain_arr = MockMountainArray.return_value
        mountain_arr.length.return_value = len(arr)
        mountain_arr.get.side_effect = lambda i: arr[i]
        self.assertEqual(2, self.solution.find_in_mountain_array(3, mountain_arr))

    @patch('src.leetcode.n1095.solution.MountainArray', spec=True)
    def test_2(self, MockMountainArray: MagicMock):
        arr = [0, 1, 2, 4, 2, 1]
        mountain_arr = MockMountainArray.return_value
        mountain_arr.length.return_value = len(arr)
        mountain_arr.get.side_effect = lambda i: arr[i]
        self.assertEqual(-1, self.solution.find_in_mountain_array(3, mountain_arr))


class TestSolutionA(TestSolution):

    def setUp(self):
        self.solution = SolutionA()
