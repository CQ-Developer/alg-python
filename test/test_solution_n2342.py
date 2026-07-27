from pytest import fixture

from src.solution_n2342 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 54 == solution.maximum_sum([18, 43, 36, 13, 7])


def test_2(solution: Solution):
    assert -1 == solution.maximum_sum([10, 12, 19, 14])
