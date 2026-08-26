from pytest import fixture

from src.n624 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.max_distance([[1, 2, 3], [4, 5], [1, 2, 3]])


def test_2(solution: Solution):
    assert 0 == solution.max_distance([[1], [1]])
