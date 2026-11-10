import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.interview_n16_n24 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    target: int
    expected: list[list[int]]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "interview_n16_n24.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_pair_sums(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.pair_sums(case["nums"], case["target"]) == case["expected"]
