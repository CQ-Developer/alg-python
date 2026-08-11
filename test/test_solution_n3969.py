from pytest import fixture

from src.solution_n3969 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 4 == solution.count_valid_subarrays([1, 100, 1], 1)


def test_2(solution: Solution):
    assert 0 == solution.count_valid_subarrays([1], 2)
