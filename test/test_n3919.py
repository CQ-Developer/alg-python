import pytest

from src.n3919 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        pytest.param(
            [-5, -2, 3],
            [[0, 2], [2, 0], [1, 2]],
            [6, 2, 5],
        ),
        pytest.param(
            [0, 2, 3, 9],
            [[3, 0], [1, 2], [2, 0]],
            [4, 1, 3],
        ),
    ],
)
def test_min_cost(
    solution: Solution,
    nums: list[int],
    queries: list[list[int]],
    expected: list[int],
):
    assert solution.min_cost(nums, queries) == expected
