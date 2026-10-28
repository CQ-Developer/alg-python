import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n304 import NumMatrix, NumMatrixA, NumMatrixB


@pytest.fixture(params=[NumMatrixA, NumMatrixB])
def num_matrix_cls(request: pytest.FixtureRequest) -> type[NumMatrix]:
    return request.param


class TestCase(TypedDict):
    matrix: list[list[int]]
    queries: list[list[int]]
    expected: list[int]


def load_cases() -> list[TestCase]:
    file_path = Path(__file__).parent / "test_n304.json"
    with open(file_path, "r") as f:
        return json.load(f)


@pytest.mark.parametrize("test_case", load_cases())
def test_sum_region(num_matrix_cls: type[NumMatrix], test_case: TestCase):
    num_matrix = num_matrix_cls(test_case["matrix"])
    for q, exp in zip(test_case["queries"], test_case["expected"]):
        assert num_matrix.sum_region(*q) == exp
