import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n321 import Solution, SolutionA


class Case(TypedDict):
    nums1: list[int]
    nums2: list[int]
    k: int
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n321.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_max_number(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.max_number(case["nums1"], case["nums2"], case["k"]) == case["expected"]
