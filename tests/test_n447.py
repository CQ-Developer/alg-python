from pytest import fixture

from src.n447 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.number_of_boomerangs([[0, 0], [1, 0], [2, 0]])


def test_b(solution: Solution):
    assert 2 == solution.number_of_boomerangs([[1, 1], [2, 2], [3, 3]])


def test_c(solution: Solution):
    assert 0 == solution.number_of_boomerangs([[1, 1]])
