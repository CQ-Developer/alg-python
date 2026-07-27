from pytest import fixture

from src.solution_n853 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])


def test_2(solution: Solution):
    assert 1 == solution.car_fleet(10, [3], [3])


def test_3(solution: Solution):
    assert 1 == solution.car_fleet(100, [0, 2, 4], [4, 2, 1])
