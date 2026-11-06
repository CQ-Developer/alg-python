import pytest

from src.n2245 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param(
            [
                [23, 17, 15, 3, 20],
                [8, 1, 20, 27, 11],
                [9, 4, 6, 2, 21],
                [40, 9, 1, 10, 6],
                [22, 7, 4, 5, 3],
            ],
            3,
        ),
        pytest.param(
            [
                [4, 3, 2],
                [7, 6, 1],
                [8, 8, 8],
            ],
            0,
        ),
    ],
)
def test_max_trailing_zeros(
    solution: Solution,
    grid: list[list[int]],
    expected: int,
):
    assert solution.max_trailing_zeros(grid) == expected
