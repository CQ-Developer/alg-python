from pytest import fixture

from src.n1523 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 3 == solution.count_odds(3, 7)


def test_b(solution: Solution):
    assert 1 == solution.count_odds(8, 10)
