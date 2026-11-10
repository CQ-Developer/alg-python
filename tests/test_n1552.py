import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1552 import Solution, SolutionA


class Case(TypedDict):
    position: list[int]
    m: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1552.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_max_distance(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.maxDistance(case["position"], case["m"]) == case["expected"]
