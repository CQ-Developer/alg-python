from pytest import fixture

from src.n2812 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 0 == solution.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]])


def test_2(solution: Solution):
    assert 2 == solution.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]])


def test_3(solution: Solution):
    assert 2 == solution.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]])
