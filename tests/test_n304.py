import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n304 import NumMatrix, NumMatrixA, NumMatrixB


class Case(TypedDict):
    init: list[list[list[int]]]
    operations: list[str]
    arguments: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[NumMatrixA, NumMatrixB])
def num_matrix_cls(request: pytest.FixtureRequest) -> type[NumMatrix]:
    return request.param


@pytest.mark.parametrize("case", _load_test_cases())
def test_sum_region(num_matrix_cls: type[NumMatrix], case: Case):
    case = copy.deepcopy(case)
    num_matrix = num_matrix_cls(*case["init"])
    actual = [
        getattr(num_matrix, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
