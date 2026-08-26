from pytest import fixture

from src.n1074 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.num_submatrix_sum_target([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0)


def test_b(solution: Solution):
    assert 5 == solution.num_submatrix_sum_target([[1, -1], [-1, 1]], 0)


def test_c(solution: Solution):
    assert 0 == solution.num_submatrix_sum_target([[904]], 0)
