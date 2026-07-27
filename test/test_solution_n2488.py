from pytest import fixture

from src.solution_n2488 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 3 == solution.count_subarrays([3, 2, 1, 4, 5], 4)


def test_b(solution: Solution):
    assert 1 == solution.count_subarrays([2, 3, 1], 3)
