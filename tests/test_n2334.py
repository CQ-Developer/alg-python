import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2334 import Solution, SolutionA


class Case(TypedDict):
    nums: list[int]
    threshold: int
    expected_any: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2334.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_valid_subarray_size(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    result = solution.valid_subarray_size(case["nums"], case["threshold"])
    assert result in case["expected_any"]
