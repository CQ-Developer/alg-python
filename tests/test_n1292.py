import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1292 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    mat: list[list[int]]
    threshold: int
    expected: int


def _load_test_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "cases" / "test_n1292.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("test_case", _load_test_cases())
def test_max_side_length(solution: Solution, test_case: TestCase):
    mat = test_case["mat"]
    threshold = test_case["threshold"]
    expected = test_case["expected"]
    assert solution.max_side_length(mat, threshold) == expected
