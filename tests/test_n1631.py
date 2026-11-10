import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1631 import Solution, SolutionA, SolutionB, SolutionC


class Case(TypedDict):
    heights: list[list[int]]
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_minimum_effort_path(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.minimumEffortPath(case["heights"]) == case["expected"]
