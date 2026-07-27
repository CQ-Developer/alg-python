from pytest import fixture

from src.solution_n3713 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.longest_balanced('abbac')


def test_b(solution: Solution):
    assert 4 == solution.longest_balanced('zzabccy')


def test_c(solution: Solution):
    assert 2 == solution.longest_balanced('aba')
