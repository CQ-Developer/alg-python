import pytest

from src.n3748 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        pytest.param(
            [3, 1, 2],
            [[0, 1], [1, 2], [0, 2]],
            [2, 3, 4],
        ),
        pytest.param(
            [2, 2],
            [[0, 1], [0, 0]],
            [3, 1],
        ),
    ],
)
def test_count_stable_subarrays(
    solution: Solution,
    nums: list[int],
    queries: list[list[int]],
    expected: list[int],
):
    assert solution.count_stable_subarrays(nums, queries) == expected
