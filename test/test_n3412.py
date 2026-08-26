from pytest import fixture

from src.n3412 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 5 == solution.calculate_score('aczzx')


def test_2(solution: Solution):
    assert 0 == solution.calculate_score('abcdef')
