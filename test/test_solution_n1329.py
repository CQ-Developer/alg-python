from pytest import fixture

from src.solution_n1329 import Solution, SolutionA


@fixture(scope='module', params=[SolutionA])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]] == solution.diagonal_sort(
        [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    )


def test_b(solution: Solution):
    assert [
        [5, 17, 4, 1, 52, 7],
        [11, 11, 25, 45, 8, 69],
        [14, 23, 25, 44, 58, 15],
        [22, 27, 31, 36, 50, 66],
        [84, 28, 75, 33, 55, 68],
    ] == solution.diagonal_sort(
        [
            [11, 25, 66, 1, 69, 7],
            [23, 55, 17, 45, 15, 52],
            [75, 31, 36, 44, 58, 8],
            [22, 27, 33, 25, 68, 4],
            [84, 28, 14, 11, 5, 50],
        ]
    )
