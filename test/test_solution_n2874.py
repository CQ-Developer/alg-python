from pytest import fixture

from src.solution_n2874 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 77 == solution.maximum_triple_value([12, 6, 1, 2, 7])


def test_2(solution: Solution):
    assert 133 == solution.maximum_triple_value([1, 10, 3, 4, 19])


def test_3(solution: Solution):
    assert 0 == solution.maximum_triple_value([1, 2, 3])
