from pytest import fixture

from src.n930 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.num_subarrays_with_sum([1, 0, 1, 0, 1], 2)


def test_b(solution: Solution):
    assert 15 == solution.num_subarrays_with_sum([0, 0, 0, 0, 0], 0)
