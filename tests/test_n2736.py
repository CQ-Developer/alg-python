import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2736 import Solution, SolutionA


class Case(TypedDict):
    nums1: list[int]
    nums2: list[int]
    queries: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2736.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_maximum_sum_queries(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.maximum_sum_queries(case["nums1"], case["nums2"], case["queries"]) == case["expected"]
