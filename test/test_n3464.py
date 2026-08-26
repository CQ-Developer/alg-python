from pytest import fixture

from src.n3464 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.maxDistance(2, [[0, 2], [2, 0], [2, 2], [0, 0]], 4)


def test_2(solution: Solution):
    assert 1 == solution.maxDistance(2, [[0, 0], [1, 2], [2, 0], [2, 2], [2, 1]], 4)


def test_3(solution: Solution):
    assert 1 == solution.maxDistance(2, [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 2], [2, 1]], 5)
