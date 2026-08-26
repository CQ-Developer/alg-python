from pytest import fixture

from src.n28 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 0 == solution.str_str('sadbutsad', 'sad')


def test_b(solution: Solution):
    assert -1 == solution.str_str('leetcode', 'leeto')
