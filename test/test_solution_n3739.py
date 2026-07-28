from pytest import fixture

from src.solution_n3739 import Solution, SolutionA, SolutionB, SolutionC


@fixture(scope='module', params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 5 == solution.count_majority_subarrays([1, 2, 2, 3], 2)


def test_b(solution: Solution):
    assert 10 == solution.count_majority_subarrays([1, 1, 1, 1], 1)


def test_c(solution: Solution):
    assert 0 == solution.count_majority_subarrays([1, 2, 3], 4)
