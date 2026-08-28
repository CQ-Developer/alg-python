import pytest

from src.n1895 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    [
        "grid",
        "expected",
    ],
    [
        pytest.param(
            [
                [7, 1, 4, 5, 6],
                [2, 5, 1, 6, 4],
                [1, 5, 4, 3, 2],
                [1, 2, 7, 3, 4],
            ],
            3,
        ),
        pytest.param(
            [
                [5, 1, 3, 1],
                [9, 3, 3, 1],
                [1, 3, 3, 8],
            ],
            2,
        ),
    ],
)
def test_largest_magic_square(solution: Solution, grid: list[list[int]], expected: int):
    assert solution.largest_magic_square(grid) == expected
