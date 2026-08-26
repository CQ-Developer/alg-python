from pytest import fixture

from src.n1310 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [2, 7, 14, 8] == solution.xor_queries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])


def test_b(solution: Solution):
    assert [8, 0, 4, 4] == solution.xor_queries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]])
