from pytest import fixture

from src.n2815 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert -1 == solution.max_sum([112, 131, 411])


def test_2(solution: Solution):
    assert 5902 == solution.max_sum([2536, 1613, 3366, 162])


def test_3(solution: Solution):
    assert 88 == solution.max_sum([51, 71, 17, 24, 42])
