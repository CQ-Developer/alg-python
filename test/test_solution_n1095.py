from unittest.mock import MagicMock, patch

from pytest import fixture

from src.solution_n1095 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    with patch('src.solution_n1095.MountainArray', spec=True) as MockMountainArray:
        arr = [1, 2, 3, 4, 5, 3, 1]
        mountain_arr = MockMountainArray.return_value
        mountain_arr.length.return_value = len(arr)
        mountain_arr.get.side_effect = lambda i: arr[i]
        assert 2 == solution.find_in_mountain_array(3, mountain_arr)


def test_2(solution: Solution):
    with patch('src.solution_n1095.MountainArray', spec=True) as MockMountainArray:
        arr = [0, 1, 2, 4, 2, 1]
        mountain_arr = MockMountainArray.return_value
        mountain_arr.length.return_value = len(arr)
        mountain_arr.get.side_effect = lambda i: arr[i]
        assert -1 == solution.find_in_mountain_array(3, mountain_arr)
