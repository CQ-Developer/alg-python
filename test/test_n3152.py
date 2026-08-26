from pytest import fixture

from src.n3152 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [False] == solution.is_array_special([3, 4, 1, 2, 6], [[0, 4]])


def test_b(solution: Solution):
    assert [False, True] == solution.is_array_special([4, 3, 1, 6], [[0, 2], [2, 3]])


def test_c(solution: Solution):
    assert [True] == solution.is_array_special([2, 1], [[0, 1]])
