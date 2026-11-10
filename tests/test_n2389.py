import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2389 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    nums: list[int]
    queries: list[int]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2389.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_answer_queries(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.answer_queries(case["nums"], case["queries"]) == case["expected"]
