from pytest import fixture

from src.solution_n1552 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.maxDistance([1, 2, 3, 4, 7], 3)


def test_2(solution: Solution):
    assert 999999999 == solution.maxDistance([5, 4, 3, 2, 1, 1000000000], 2)
