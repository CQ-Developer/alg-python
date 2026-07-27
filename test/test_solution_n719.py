from pytest import fixture

from src.solution_n719 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 0 == solution.smallestDistancePair([1, 3, 1], 1)


def test_2(solution: Solution):
    assert 0 == solution.smallestDistancePair([1, 1, 1], 2)


def test_3(solution: Solution):
    assert 5 == solution.smallestDistancePair([1, 6, 1], 3)
