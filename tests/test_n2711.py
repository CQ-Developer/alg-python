import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2711 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    grid: list[list[int]]
    expected: list[list[int]]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2711.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_difference_of_distinct_values(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.difference_of_distinct_values(case["grid"]) == case["expected"]
