from pytest import fixture

from src.solution_n3900 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution):
    assert solution.longest_balanced('100001') == 4


def test_b(solution):
    assert solution.longest_balanced('111') == 0
