from pytest import fixture

from src.n2260 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.minimum_card_pickup([3, 4, 2, 3, 4, 7])


def test_2(solution: Solution):
    assert -1 == solution.minimum_card_pickup([1, 0, 5, 3])
