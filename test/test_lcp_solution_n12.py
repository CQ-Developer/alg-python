from pytest import fixture

from src.solution_lcp_n12 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.minTime([1, 2, 3, 3], 2)


def test_2(solution: Solution):
    assert 0 == solution.minTime([999, 999, 999], 4)
