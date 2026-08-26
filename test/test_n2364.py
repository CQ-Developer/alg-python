from pytest import fixture

from src.n2364 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test1(solution: Solution):
    assert 5 == solution.count_bad_pairs([4, 1, 3, 3])


def test2(solution: Solution):
    assert 0 == solution.count_bad_pairs([1, 2, 3, 4, 5])
