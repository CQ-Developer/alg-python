from pytest import fixture

from src.n316 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 'abc' == solution.remove_duplicate_letters('bcabc')


def test_b(solution: Solution):
    assert 'acdb' == solution.remove_duplicate_letters('cbacdcbc')
