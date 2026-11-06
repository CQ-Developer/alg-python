import pytest

from src.n2983 import Solution, SolutionA


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest):
    return request.param()


@pytest.mark.parametrize(
    "s, queries, expected",
    [
        pytest.param(
            "abcabc",
            [[1, 1, 3, 5], [0, 2, 5, 5]],
            [True, True],
        ),
        pytest.param(
            "abbcdecbba",
            [[0, 2, 7, 9]],
            [False],
        ),
        pytest.param(
            "acbcab",
            [[1, 2, 4, 5]],
            [True],
        ),
    ],
)
def test_can_make_palindrome_queries(
    solution: Solution,
    s: str,
    queries: list[list[int]],
    expected: list[bool],
):
    assert solution.can_make_palindrome_queries(s, queries) == expected
