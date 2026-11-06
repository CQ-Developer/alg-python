import pytest

from src.n1862 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([2, 5, 9], 10),
        pytest.param([7, 7, 7, 7, 7, 7, 7], 49),
    ],
)
def test_sum_of_floored_pairs(
    solution: Solution,
    nums: list[int],
    expected: int,
):
    assert solution.sum_of_floored_pairs(nums) == expected
