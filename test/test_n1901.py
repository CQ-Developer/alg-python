from pytest import fixture

from src.n1901 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [0, 1] == solution.find_peak_grid([[1, 4], [3, 2]])


def test_2(solution: Solution):
    assert [1, 1] == solution.find_peak_grid([[10, 20, 15], [21, 30, 14], [7, 16, 32]])
