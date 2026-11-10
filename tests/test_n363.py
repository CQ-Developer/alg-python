import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n363 import Solution, SolutionA


class Case(TypedDict):
    matrix: list[list[int]]
    k: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n363.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_max_sum_submatrix(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.max_sum_submatrix(case["matrix"], case["k"]) == case["expected"]
