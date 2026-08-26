from pytest import fixture

from src.n852 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.peak_index_in_mountain_array([0, 1, 0])


def test_2(solution: Solution):
    assert 1 == solution.peak_index_in_mountain_array([0, 2, 1, 0])


def test_3(solution: Solution):
    assert 1 == solution.peak_index_in_mountain_array([0, 10, 5, 2])
