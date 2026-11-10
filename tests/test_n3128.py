import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3128 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    grid: list[list[int]]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3128.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_number_of_right_trianles(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.number_of_right_trianles(case["grid"]) == case["expected"]
