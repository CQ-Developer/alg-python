import pytest

from src.n1712 import Solution, SolutionA, SolutionB


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([1, 1, 1], 1),
        pytest.param([1, 2, 2, 2, 5, 0], 3),
        pytest.param([3, 2, 1], 0),
    ],
)
def test_ways_to_split(
    solution: Solution,
    nums: list[int],
    expected: int,
):
    assert solution.ways_to_split(nums) == expected
