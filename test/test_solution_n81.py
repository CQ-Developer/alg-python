from pytest import fixture

from src.solution_n81 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.search([2, 5, 6, 0, 0, 1, 2], 0)


def test_2(solution: Solution):
    assert not solution.search([2, 5, 6, 0, 0, 1, 2], 3)
