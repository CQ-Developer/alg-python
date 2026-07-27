from pytest import fixture

from src.solution_n2962 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 6 == solution.count_subarrays([1, 3, 2, 3, 3], 2)


def test_b(solution: Solution):
    assert 0 == solution.count_subarrays([1, 4, 2, 1], 3)
