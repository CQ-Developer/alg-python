import pytest

from src.n2281 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "strength, expected",
    [
        pytest.param([1, 3, 1, 2], 44),
        pytest.param([5, 4, 6], 213),
    ],
)
def test_total_strength(
    solution: Solution,
    strength: list[int],
    expected: int,
):
    assert solution.total_strength(strength) == expected
