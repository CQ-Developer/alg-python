from pytest import fixture

from src.n454 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])


def test_b(solution: Solution):
    assert 1 == solution.four_sum_count([0], [0], [0], [0])
