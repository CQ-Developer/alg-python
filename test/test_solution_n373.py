from pytest import fixture

from src.solution_n373 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [[1, 2], [1, 4], [1, 6]] == solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)


def test_2(solution: Solution):
    assert [[1, 1], [1, 1]] == solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2)
