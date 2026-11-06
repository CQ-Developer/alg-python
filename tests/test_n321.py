from pytest import fixture

from src.n321 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [9, 8, 6, 5, 3] == solution.max_number([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)


def test_b(solution: Solution):
    assert [6, 7, 6, 0, 4] == solution.max_number([6, 7], [6, 0, 4], 5)


def test_c(solution: Solution):
    assert [9, 8, 9] == solution.max_number([3, 9], [8, 9], 3)
