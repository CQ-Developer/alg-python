import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n303 import NumArray


class Case(TypedDict):
    init: list[list[int]]
    operations: list[str]
    arguments: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", _load_test_cases())
def test_num_array(case: Case):
    case = copy.deepcopy(case)
    num_array = NumArray(*case["init"])
    actual = [
        getattr(num_array, operation)(*arguments) for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
