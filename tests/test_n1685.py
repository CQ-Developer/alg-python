import pytest

from src.n1685 import Solution, SolutionA, SolutionB


@pytest.fixture(
    scope="module",
    params=[
        SolutionA,
        SolutionB,
    ],
)
def solution(request) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    [
        "nums",
        "expected",
    ],
    [
        ([2, 3, 5], [4, 3, 5]),
        ([1, 4, 6, 8, 10], [24, 15, 13, 15, 21]),
    ],
)
def test_get_sum_absolute_differences(solution: Solution, nums: list[int], expected: list[int]):
    assert solution.get_sum_absolute_differences(nums) == expected
