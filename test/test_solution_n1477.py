from pytest import fixture

from src.solution_n1477 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 2 == solution.min_sum_of_lengths([3, 2, 2, 4, 3], 3)


def test_b(solution: Solution):
    assert 2 == solution.min_sum_of_lengths([7, 3, 4, 7], 7)


def test_c(solution: Solution):
    assert -1 == solution.min_sum_of_lengths([4, 3, 2, 6, 2, 3, 4], 6)
