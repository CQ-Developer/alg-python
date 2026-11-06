import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3212 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    grid: list[list[str]]
    expected: int


def _load_test_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "cases" / "test_n3212.json"
    with open(file_path, "r") as f:
        return json.load(f)


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("test_case", _load_test_cases())
def test_number_of_submatrices(solution: Solution, test_case: TestCase):
    grid = test_case["grid"]
    expected = test_case["expected"]
    assert solution.number_of_submatrices(grid) == expected
