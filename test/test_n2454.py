from pytest import fixture

from src.n2454 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [9, 6, 6, -1, -1] == solution.second_greater_element([2, 4, 0, 9, 6])


def test_b(solution: Solution):
    assert [-1, -1] == solution.second_greater_element([3, 3])
