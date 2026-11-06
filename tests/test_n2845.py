from pytest import fixture

from src.n2845 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert solution.count_interesting_subarrays([3, 2, 4], 2, 1) == 3


def test_b(solution: Solution):
    assert solution.count_interesting_subarrays([3, 1, 9, 6], 3, 0) == 2
