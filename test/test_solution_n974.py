from pytest import fixture

from src.solution_n974 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 7 == solution.subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5)


def test_b(solution: Solution):
    assert 0 == solution.subarrays_div_by_k([5], 9)
