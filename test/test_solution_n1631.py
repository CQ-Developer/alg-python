from pytest import fixture

from src.solution_n1631 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]])


def test_2(solution: Solution):
    assert 1 == solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]])


def test_3(solution: Solution):
    assert 0 == solution.minimumEffortPath(
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    )
