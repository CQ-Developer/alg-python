import pytest

from src.n3445 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize(
    "s, k, expected",
    [
        pytest.param("12233", 4, -1),
        pytest.param("1122211", 3, 1),
        pytest.param("110", 3, -1),
    ],
)
def test_max_difference(
    solution: Solution,
    s: str,
    k: int,
    expected: int,
):
    assert solution.max_difference(s, k) == expected
