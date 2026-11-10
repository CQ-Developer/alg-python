import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1944 import Solution, SolutionA


class Case(TypedDict):
    heights: list[int]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1944.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_can_see_persons_count(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.can_see_persons_count(case["heights"]) == case["expected"]
