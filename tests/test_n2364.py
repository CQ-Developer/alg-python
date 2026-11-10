import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2364 import Solution, SolutionA


class Case(TypedDict):
    nums: list[int]
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_count_bad_pairs(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.count_bad_pairs(case["nums"]) == case["expected"]
