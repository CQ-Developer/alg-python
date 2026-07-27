from pytest import fixture

from src.solution_n378 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 13 == solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)


def test_2(solution: Solution):
    assert -5 == solution.kthSmallest([[-5]], 1)
