import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n50 import Solution, SolutionA


class Case(TypedDict):
    x: float
    n: int
    expected: float


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n50.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_my_pow(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    result = solution.my_pow(case["x"], case["n"])
    assert result == pytest.approx(case["expected"], abs=1e-5)
