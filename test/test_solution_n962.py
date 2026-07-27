from pytest import fixture

from src.solution_n962 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 4 == solution.max_width_ramp([6, 0, 8, 2, 1, 5])


def test_b(solution: Solution):
    assert 7 == solution.max_width_ramp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
