import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1504 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    mat: list[list[int]]
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_num_submat(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.num_submat(case["mat"]) == case["expected"]
