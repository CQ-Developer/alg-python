import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1329 import Solution, SolutionA


class Case(TypedDict):
    mat: list[list[int]]
    expected: list[list[int]]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1329.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_diagonal_sort(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.diagonal_sort(case["mat"]) == case["expected"]
