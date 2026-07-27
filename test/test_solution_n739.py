from pytest import fixture

from src.solution_n739 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [1, 1, 4, 2, 1, 1, 0, 0] == solution.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])


def test_2(solution: Solution):
    assert [1, 1, 0] == solution.daily_temperatures([30, 60, 90])


def test_3(solution: Solution):
    assert [1, 1, 1, 0] == solution.daily_temperatures([30, 40, 50, 60])
