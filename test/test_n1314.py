import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1314 import Solution, SolutionA


class TestCase(TypedDict):
    mat: list[list[int]]
    k: int
    expected: list[list[int]]


def load_test_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "test_n1314.json"
    with open(file_path, "r") as f:
        return json.load(f)


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("test_case", load_test_cases())
def test_matrix_block_sum(solution: Solution, test_case: TestCase):
    mat = test_case["mat"]
    k = test_case["k"]
    expected = test_case["expected"]
    print(mat)
    assert solution.matrix_block_sum(mat, k) == expected
