import pytest

from src.n1744 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    [
        "candies_count",
        "queries",
        "expected",
    ],
    [
        pytest.param(
            [7, 4, 5, 3, 8],
            [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]],
            [True, False, True],
        ),
        pytest.param(
            [5, 2, 6, 4, 1],
            [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]],
            [False, True, True, False, False],
        ),
    ],
)
def test_can_eat(
    solution: Solution,
    candies_count: list[int],
    queries: list[list[int]],
    expected: list[bool],
):
    assert solution.can_eat(candies_count, queries) == expected
