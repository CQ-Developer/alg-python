import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2949 import Solution, SolutionA, SolutionB, SolutionC, SolutionD


class Case(TypedDict):
    s: str
    k: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC, SolutionD])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_beautiful_substrings(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.beautiful_substrings(case["s"], case["k"]) == case["expected"]
