import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1074 import Solution, SolutionA


class Case(TypedDict):
    matrix: list[list[int]]
    target: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_num_submatrix_sum_target(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.num_submatrix_sum_target(case["matrix"], case["target"]) == case["expected"]
