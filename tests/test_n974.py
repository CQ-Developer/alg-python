import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n974 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    k: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n974.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_subarrays_div_by_k(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.subarrays_div_by_k(case["nums"], case["k"]) == case["expected"]
