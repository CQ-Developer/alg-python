import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n853 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    target: int
    position: list[int]
    speed: list[int]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n853.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_car_fleet(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.car_fleet(case["target"], case["position"], case["speed"]) == case["expected"]
