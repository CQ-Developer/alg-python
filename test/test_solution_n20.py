from pytest import fixture

from src.solution_n20 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert True == solution.is_valid('()')


def test_2(solution: Solution):
    assert True == solution.is_valid('()[]{}')


def test_3(solution: Solution):
    assert False == solution.is_valid('(]')


def test_4(solution: Solution):
    assert True == solution.is_valid('([])')


def test_5(solution: Solution):
    assert False == solution.is_valid('([)]')


def test_6(solution: Solution):
    assert False == solution.is_valid('({[)')


def test_7(solution: Solution):
    assert False == solution.is_valid(']')
