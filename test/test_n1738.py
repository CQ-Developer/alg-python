import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1738 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    matrix: list[list[int]]
    k: int
    expected: int


def _load_test_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "test_n1738.json"
    with open(file_path, "r") as f:
        return json.load(f)


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("test_case", _load_test_cases())
def test_kth_largest_value(solution: Solution, test_case: TestCase):
    matrix = test_case["matrix"]
    k = test_case["k"]
    expected = test_case["expected"]
    assert solution.kth_largest_value(matrix, k) == expected
