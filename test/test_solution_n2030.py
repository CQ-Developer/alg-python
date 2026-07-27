from pytest import fixture

from src.solution_n2030 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 'eet' == solution.smallest_subsequence('leet', 3, 'e', 1)


def test_b(solution: Solution):
    assert 'ecde' == solution.smallest_subsequence('leetcode', 4, 'e', 2)
