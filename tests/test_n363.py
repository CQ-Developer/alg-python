from pytest import fixture

from src.n363 import Solution, SolutionA


@fixture(scope="module", params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    matrix = [[1, 0, 1], [0, -2, 3]]
    assert 2 == solution.max_sum_submatrix(matrix, 2)


def test_2(solution: Solution):
    matrix = [[2, 2, -1]]
    assert 3 == solution.max_sum_submatrix(matrix, 3)
