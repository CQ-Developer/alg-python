from pytest import fixture

from src.solution_n540 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 2 == solution.single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])


def test_2(solution: Solution):
    assert 10 == solution.single_non_duplicate([3, 3, 7, 7, 10, 11, 11])
