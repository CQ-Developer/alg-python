import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1793 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    k: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1793.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_maximum_score(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.maximum_score(case["nums"], case["k"]) == case["expected"]
