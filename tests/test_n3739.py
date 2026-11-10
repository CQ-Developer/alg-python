import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3739 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    target: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3739.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_count_majority_subarrays(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.count_majority_subarrays(case["nums"], case["target"]) == case["expected"]
