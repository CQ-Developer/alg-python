from pytest import fixture

from src.solution_n878 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.nthMagicalNumber(1, 2, 3)


def test_2(solution: Solution):
    assert 6 == solution.nthMagicalNumber(4, 2, 3)
