from pytest import fixture

from src.solution_n3420 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 17 == solution.count_non_decreasing_subarrays([6, 3, 1, 2, 4, 4], 7)


def test_b(solution: Solution):
    assert 12 == solution.count_non_decreasing_subarrays([6, 3, 1, 3, 6], 4)
