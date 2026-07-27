from pytest import fixture

from src.solution_n3419 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.minMaxWeight(5, [[1, 0, 1], [2, 0, 2], [3, 0, 1], [4, 3, 1], [2, 1, 1]], 2)


def test_2(solution: Solution):
    assert -1 == solution.minMaxWeight(5, [[0, 1, 1], [0, 2, 2], [0, 3, 1], [0, 4, 1], [1, 2, 1], [1, 4, 1]], 1)


def test_3(solution: Solution):
    assert 2 == solution.minMaxWeight(5, [[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [3, 4, 2], [4, 0, 1]], 1)


def test_4(solution: Solution):
    assert -1 == solution.minMaxWeight(5, [[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [4, 0, 1]], 1)
