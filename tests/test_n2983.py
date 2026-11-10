import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2983 import Solution, SolutionA


class Case(TypedDict):
    s: str
    queries: list[list[int]]
    expected: list[bool]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2983.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_can_make_palindrome_queries(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.can_make_palindrome_queries(case["s"], case["queries"]) == case["expected"]
