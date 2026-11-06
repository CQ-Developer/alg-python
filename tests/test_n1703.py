import pytest

from src.n1703 import Solution, SolutionA, SolutionB


@pytest.fixture(scope="module", params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    ["nums", "k", "expected"],
    [([1, 0, 0, 1, 0, 1], 2, 1), ([1, 0, 0, 0, 0, 0, 1, 1], 3, 5), ([1, 1, 0, 1], 2, 0)],
)
def test_min_moves(
    solution: Solution,
    nums: list[int],
    k: int,
    expected: int,
):
    assert solution.min_moves(nums, k) == expected
