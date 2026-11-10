import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1523 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    low: int
    high: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1523.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_count_odds(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.count_odds(case["low"], case["high"]) == case["expected"]
