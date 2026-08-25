import pytest

from src.solution_n1177 import Solution, SolutionA, SolutionB, SolutionC


@pytest.fixture(scope="module", params=[SolutionA, SolutionB, SolutionC])
def solution(request) -> Solution:
    return request.param()


def test_1(solution: Solution):
    assert solution.can_make_pali_queries(
        "abcda",
        [
            [3, 3, 0],
            [1, 2, 0],
            [0, 3, 1],
            [0, 3, 2],
            [0, 4, 1],
        ],
    ) == [
        True,
        False,
        False,
        True,
        True,
    ]


def test_2(solution: Solution):
    assert solution.can_make_pali_queries(
        "lyb",
        [
            [0, 1, 0],
            [2, 2, 1],
        ],
    ) == [
        False,
        True,
    ]
