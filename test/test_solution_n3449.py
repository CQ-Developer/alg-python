from pytest import fixture

from src.solution_n3449 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.maxScore([2, 4], 3)


def test_2(solution: Solution):
    assert 2 == solution.maxScore([1, 2, 3], 5)
