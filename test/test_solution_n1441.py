from pytest import fixture

from src.solution_n1441 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert ['Push', 'Push', 'Pop', 'Push'] == solution.build_array([1, 3], 3)


def test_2(solution: Solution):
    assert ['Push', 'Push', 'Push'] == solution.build_array([1, 2, 3], 3)


def test_3(solution: Solution):
    assert ['Push', 'Push'] == solution.build_array([1, 2], 4)
