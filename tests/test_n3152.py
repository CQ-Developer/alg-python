import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3152 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    queries: list[list[int]]
    expected: list[bool]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_is_array_special(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.is_array_special(case["nums"], case["queries"]) == case["expected"]
