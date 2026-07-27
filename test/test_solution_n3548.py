from pytest import fixture

from src.solution_n3548 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert solution.can_partition_grid([[1, 4], [2, 3]])


def test_b(solution: Solution):
    assert solution.can_partition_grid([[1, 2], [3, 4]])


def test_c(solution: Solution):
    assert not solution.can_partition_grid([[1, 2, 4], [2, 3, 5]])


def test_d(solution: Solution):
    assert not solution.can_partition_grid([[4, 1, 8], [3, 2, 6]])
