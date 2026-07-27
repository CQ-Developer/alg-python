from pytest import fixture

from src.solution_n2711 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert [[1, 1, 0], [1, 0, 1], [0, 1, 1]] == solution.difference_of_distinct_values(
        [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
    )


def test_b(solution: Solution):
    assert [[0]] == solution.difference_of_distinct_values([[1]])


def test_c(solution: Solution):
    assert [
        [3, 3, 3, 3, 3, 3, 2, 1, 0],
        [2, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 2],
        [0, 1, 2, 3, 3, 3, 3, 3, 3],
    ] == solution.difference_of_distinct_values(
        [
            [6, 28, 37, 34, 12, 30, 43, 35, 6],
            [21, 47, 38, 14, 31, 49, 11, 14, 49],
            [6, 12, 35, 17, 17, 2, 45, 27, 43],
            [34, 41, 30, 28, 45, 24, 50, 20, 4],
        ]
    )
