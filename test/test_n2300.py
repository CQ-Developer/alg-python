import pytest

from src.n2300 import Solution, SolutionA, SolutionB, SolutionC


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "spells, potions, success, expected",
    [
        pytest.param(
            [5, 1, 3],
            [1, 2, 3, 4, 5],
            7,
            [4, 0, 3],
        ),
        pytest.param(
            [3, 1, 2],
            [8, 5, 8],
            16,
            [2, 0, 2],
        ),
    ],
)
def test_successful_pairs(
    solution: Solution,
    spells: list[int],
    potions: list[int],
    success: int,
    expected: list[int],
):
    assert solution.successful_pairs(spells, potions, success) == expected
