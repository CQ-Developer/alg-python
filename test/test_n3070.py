import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3070 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    grid: list[list[int]]
    k: int
    expected: int


def load_test_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "cases" / "test_n3070.json"
    with open(file_path, "r") as f:
        return json.load(f)


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("test_case", load_test_cases())
def test_count_submatrices(solution: Solution, test_case: TestCase):
    grid = test_case["grid"]
    k = test_case["k"]
    expected = test_case["expected"]
    assert solution.count_submatrices(grid, k) == expected
