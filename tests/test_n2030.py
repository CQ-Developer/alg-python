import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2030 import Solution, SolutionA


class Case(TypedDict):
    s: str
    k: int
    letter: str
    repetition: int
    expected: str


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2030.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_smallest_subsequence(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.smallest_subsequence(case["s"], case["k"], case["letter"], case["repetition"]) == case["expected"]
