from pytest import fixture

from src.solution_n2560 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.minCapability([2, 3, 5, 9], 2)


def test_2(solution: Solution):
    assert 2 == solution.minCapability([2, 7, 9, 3, 1], 2)
