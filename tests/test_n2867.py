from pytest import fixture

from src.n2867 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.count_paths(5, [[1, 2], [1, 3], [2, 4], [2, 5]])


def test_b(solution: Solution):
    assert 6 == solution.count_paths(6, [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]])
