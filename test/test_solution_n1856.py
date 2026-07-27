from pytest import fixture

from src.solution_n1856 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 14 == solution.max_sum_min_product([1, 2, 3, 2])


def test_b(solution: Solution):
    assert 18 == solution.max_sum_min_product([2, 3, 3, 1, 2])


def test_c(solution: Solution):
    assert 60 == solution.max_sum_min_product([3, 1, 5, 6, 4, 2])
