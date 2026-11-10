import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2909 import Solution, SolutionA


class Case(TypedDict):
    nums: list[int]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2909.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_minimum_sum(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.minimum_sum(case["nums"]) == case["expected"]
