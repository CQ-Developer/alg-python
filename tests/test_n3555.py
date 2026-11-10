import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3555 import Solution, SolutionA


class Case(TypedDict):
    nums: list[int]
    k: int
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3555.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_min_subarray_sort(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.min_subarray_sort(case["nums"], case["k"]) == case["expected"]
