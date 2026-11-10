import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1776 import Solution, SolutionA


class Case(TypedDict):
    cars: list[list[int]]
    expected: list[float]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1776.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_get_collision_times(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.get_collision_times(case["cars"]) == case["expected"]
