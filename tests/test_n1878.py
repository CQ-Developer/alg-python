import pytest

from src.n1878 import Solution, SolutionA


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
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ],
            [228, 216, 211],
        ),
        pytest.param(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [20, 9, 8],
        ),
        pytest.param(
            [
                [7, 7, 7],
            ],
            [7],
        ),
    ],
)
def test_get_biggest_three(
    solution: Solution,
    grid: list[list[int]],
    expected: list[int],
):
    assert solution.get_biggest_three(grid) == expected
