import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1744 import Solution, SolutionA


class Case(TypedDict):
    candies_count: list[int]
    queries: list[list[int]]
    expected: list[bool]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1744.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_can_eat(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.can_eat(case["candies_count"], case["queries"]) == case["expected"]
