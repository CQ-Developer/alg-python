import pytest

from src.n2055 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
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
            "**|**|***|",
            [[2, 5], [5, 9]],
            [2, 3],
        ),
        pytest.param(
            "***|**|*****|**||**|*",
            [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]],
            [9, 0, 0, 0, 0],
        ),
    ],
)
def test_plates_between_candles(solution: Solution, s: str, queries: list[list[int]], expected: list[int]):
    assert solution.plates_between_candles(s, queries) == expected
