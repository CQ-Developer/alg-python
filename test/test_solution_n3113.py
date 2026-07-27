from pytest import fixture

from src.solution_n3113 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert 6 == solution.numberOfSubarrays([1, 4, 3, 3, 2])


def test_2(solution: Solution):
    assert 6 == solution.numberOfSubarrays([3, 3, 3])


def test_3(solution: Solution):
    assert 1 == solution.numberOfSubarrays([1])
