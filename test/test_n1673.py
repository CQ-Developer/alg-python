from pytest import fixture

from src.n1673 import Solution, SolutonA


@fixture(scope='module', params=[SolutonA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [2, 6] == solution.most_competitive([3, 5, 2, 6], 2)


def test_b(solution: Solution):
    assert [2, 3, 3, 4] == solution.most_competitive([2, 4, 3, 3, 5, 4, 9, 6], 4)
