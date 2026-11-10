import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1760 import Solution


class Case(TypedDict):
    nums: list[int]
    maxOperations: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1760.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[Solution])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_minimum_size(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.minimumSize(case["nums"], case["maxOperations"]) == case["expected"]
