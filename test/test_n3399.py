from pytest import fixture

from src.n3399 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.minLength('000001', 1)


def test_2(solution: Solution):
    assert 1 == solution.minLength('0000', 2)


def test_3(solution: Solution):
    assert 1 == solution.minLength('0101', 0)
