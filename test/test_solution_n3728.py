from pytest import fixture

from src.solution_n3728 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.count_stable_subarrays([9, 3, 3, 3, 9])


def test_b(solution: Solution):
    assert 0 == solution.count_stable_subarrays([1, 2, 3, 4, 5])


def test_c(solution: Solution):
    assert 1 == solution.count_stable_subarrays([-4, 4, 0, 0, -8, -4])
