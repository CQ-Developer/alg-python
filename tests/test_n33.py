from pytest import fixture

from src.n33 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.search([4, 5, 6, 7, 0, 1, 2], 0)


def test_11(solution: Solution):
    assert 6 == solution.search([4, 5, 6, 7, 0, 1, 2], 2)


def test_2(solution: Solution):
    assert -1 == solution.search([4, 5, 6, 7, 0, 1, 2], 3)


def test_3(solution: Solution):
    assert -1 == solution.search([1], 0)
