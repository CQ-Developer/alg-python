from pytest import fixture

from src.n3714 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.longest_balanced('abbac')


def test_b(solution: Solution):
    assert 3 == solution.longest_balanced('aabcc')


def test_c(solution: Solution):
    assert 2 == solution.longest_balanced('aba')
