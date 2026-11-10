import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3412 import Solution, SolutionA


class Case(TypedDict):
    s: str
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3412.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_calculate_score(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.calculate_score(case["s"]) == case["expected"]
