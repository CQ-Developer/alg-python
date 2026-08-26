from pytest import fixture

from src.n3185 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.count_complete_day_pairs([12, 12, 30, 24, 24])


def test_2(solution: Solution):
    assert 3 == solution.count_complete_day_pairs([72, 48, 24, 3])
