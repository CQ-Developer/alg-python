import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n4 import Solution, SolutionA, SolutionB, SolutionC


class Case(TypedDict):
    nums1: list[int]
    nums2: list[int]
    expected: float


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_find_median_sorted_arrays(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.find_median_sorted_arrays(case["nums1"], case["nums2"]) == case["expected"]
