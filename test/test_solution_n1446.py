from pytest import fixture

from src.solution_n1446 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.max_power('leetcode')


def test_b(solution: Solution):
    assert 5 == solution.max_power('abbcccddddeeeeedcba')
