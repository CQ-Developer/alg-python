import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1475 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    prices: list[int]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1475.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_final_prices(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.final_prices(case["prices"]) == case["expected"]
