from pytest import fixture

from src.n2905 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert [0, 3] == solution.find_indices([5, 1, 4, 1], 2, 4)


def test_2(solution: Solution):
    assert [0, 0] == solution.find_indices([2, 1], 0, 0)


def test_3(solution: Solution):
    assert [-1, -1] == solution.find_indices([1, 2, 3], 2, 4)
