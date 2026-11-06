from pytest import fixture

from src.n496 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [-1, 3, -1] == solution.next_greater_element([4, 1, 2], [1, 3, 4, 2])


def test_2(solution: Solution):
    assert [3, -1] == solution.next_greater_element([2, 4], [1, 2, 3, 4])
