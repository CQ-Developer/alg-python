from pytest import fixture

from src.n844 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.backspace_compare('ab#c', 'ad#c')


def test_2(solution: Solution):
    assert solution.backspace_compare('ab##', 'c#d#')


def test_3(solution: Solution):
    assert not solution.backspace_compare('a#c', 'b')
