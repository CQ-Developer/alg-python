import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3548 import Solution, SolutionA


class Case(TypedDict):
    grid: list[list[int]]
    expected: bool


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3548.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_can_partition_grid(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.can_partition_grid(case["grid"]) == case["expected"]
