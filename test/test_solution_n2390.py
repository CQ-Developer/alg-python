from pytest import fixture

from src.solution_n2390 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 'lecoe' == solution.remove_stars('leet**cod*e')


def test_2(solution: Solution):
    assert '' == solution.remove_stars('erase*****')
