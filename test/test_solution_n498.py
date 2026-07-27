from pytest import fixture

from src.solution_n498 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [1, 2, 4, 7, 5, 3, 6, 8, 9] == solution.find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def test_b(solution: Solution):
    assert [1, 2, 3, 4] == solution.find_diagonal_order([[1, 2], [3, 4]])
