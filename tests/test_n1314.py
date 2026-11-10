import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1314 import Solution, SolutionA


class Case(TypedDict):
    mat: list[list[int]]
    k: int
    expected: list[list[int]]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1314.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_matrix_block_sum(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.matrix_block_sum(case["mat"], case["k"]) == case["expected"]
