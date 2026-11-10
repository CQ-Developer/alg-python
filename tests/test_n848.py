import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n848 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    s: str
    shifts: list[int]
    expected: str


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n848.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_shifting_letters(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.shifting_letters(case["s"], case["shifts"]) == case["expected"]
