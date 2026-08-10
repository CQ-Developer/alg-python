from pytest import fixture

from src.solution_n3729 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 3 == solution.num_good_subarrays([1, 2, 3], 3)


def test_2(solution: Solution):
    assert 2 == solution.num_good_subarrays([2, 2, 2, 2, 2, 2], 6)
