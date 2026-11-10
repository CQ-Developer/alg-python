import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n402 import Solution, SolutionA


class Case(TypedDict):
    num: str
    k: int
    expected: str


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n402.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_remove_k_digits(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.remove_k_digits(case["num"], case["k"]) == case["expected"]
