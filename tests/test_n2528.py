from pytest import fixture

from src.n2528 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.maxPower([1, 2, 4, 5, 0], 1, 2)


def test_2(solution: Solution):
    assert 4 == solution.maxPower([4, 4, 4, 4], 0, 3)
