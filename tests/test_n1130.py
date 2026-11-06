from pytest import fixture

from src.n1130 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 32 == solution.mct_from_leaf_values([6, 2, 4])


def test_b(solution: Solution):
    assert 44 == solution.mct_from_leaf_values([4, 11])
