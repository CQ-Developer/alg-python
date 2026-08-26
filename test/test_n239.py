from pytest import fixture

from src.n239 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [3, 3, 5, 5, 6, 7] == solution.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)


def test_b(solution: Solution):
    assert [1] == solution.max_sliding_window([1], 1)
