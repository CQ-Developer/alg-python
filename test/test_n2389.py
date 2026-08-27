import pytest

from src.n2389 import Solution, SolutionA, SolutionB


@pytest.fixture(
    params=[
        SolutionA,
        SolutionB,
    ],
)
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    ["nums", "queries", "expected"],
    [
        ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
        ([2, 3, 4, 5], [1], [0]),
    ],
)
def test_answer_queries(solution: Solution, nums: list[int], queries: list[int], expected: list[int]):
    assert solution.answer_queries(nums, queries) == expected
