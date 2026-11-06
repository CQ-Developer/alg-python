from pytest import fixture

from src.n793 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.preimageSizeFZF(0)


def test_2(solution: Solution):
    assert 0 == solution.preimageSizeFZF(5)


def test_3(solution: Solution):
    assert 5 == solution.preimageSizeFZF(3)
