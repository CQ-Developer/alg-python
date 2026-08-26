from pytest import fixture

from src.n1128 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 1 == solution.num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]])


def test_2(solution: Solution):
    assert 3 == solution.num_equiv_domino_pairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]])
