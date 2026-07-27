from pytest import fixture

from src.solution_n1814 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.count_nice_pairs([42, 11, 1, 97])


def test_2(solution: Solution):
    assert 4 == solution.count_nice_pairs([13, 10, 35, 24, 76])
