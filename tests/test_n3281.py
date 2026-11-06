from pytest import fixture

from src.n3281 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.maxPossibleScore([6, 0, 3], 2)


def test_2(solution: Solution):
    assert 5 == solution.maxPossibleScore([2, 6, 13, 13], 5)
