from pytest import fixture

from src.n3446 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [[8, 2, 3], [9, 6, 7], [4, 5, 1]] == solution.sort_matrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]])


def test_b(solution: Solution):
    assert [[2, 1], [1, 0]] == solution.sort_matrix([[0, 1], [1, 2]])


def test_c(solution: Solution):
    assert [[1]] == solution.sort_matrix([[1]])
