import pytest

from src.n3756 import Solution, SolutionA, SolutionB


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    [
        "s",
        "queries",
        "expected",
    ],
    [
        pytest.param(
            "10203004",
            [[0, 7], [1, 3], [4, 6]],
            [12340, 4, 9],
        ),
        pytest.param(
            "1000",
            [[0, 3], [1, 1]],
            [1, 0],
        ),
        pytest.param(
            "9876543210",
            [[0, 9]],
            [444444137],
        ),
    ],
)
def test_sum_and_multiply(
    solution: Solution,
    s: str,
    queries: list[list[int]],
    expected: list[int],
):
    assert solution.sum_and_multiply(s, queries) == expected
