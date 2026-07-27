from pytest import fixture

from src.solution_n1081 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 'abc' == solution.smallest_subsequence('bcabc')


def test_b(solution: Solution):
    assert 'acdb' == solution.smallest_subsequence('cbacdcbc')
