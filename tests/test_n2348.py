import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2348 import Solution, SolutionA, SolutionB, SolutionC, SolutionD, SolutionE


class Case(TypedDict):
    nums: list[int]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2348.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC, SolutionD, SolutionE])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_zero_filled_subarray(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.zero_filled_subarray(case["nums"]) == case["expected"]
