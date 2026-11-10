import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n946 import Solution, SolutionA


class Case(TypedDict):
    pushed: list[int]
    popped: list[int]
    expected: bool


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n946.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_validate_stack_sequences(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.validate_stack_sequences(case["pushed"], case["popped"]) == case["expected"]
