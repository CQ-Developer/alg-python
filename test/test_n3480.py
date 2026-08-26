from pytest import fixture

from src.n3480 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 9 == solution.max_subarrays(4, [[2, 3], [1, 4]])


def test_2(solution: Solution):
    assert 12 == solution.max_subarrays(5, [[1, 2], [2, 5], [3, 5]])
