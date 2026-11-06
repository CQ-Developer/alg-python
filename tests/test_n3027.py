from pytest import fixture

from src.n3027 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 0 == solution.number_of_pairs([[1, 1], [2, 2], [3, 3]])


def test_b(solution: Solution):
    assert 2 == solution.number_of_pairs([[6, 2], [4, 4], [2, 6]])


def test_c(solution: Solution):
    assert 2 == solution.number_of_pairs([[3, 1], [1, 3], [1, 1]])
