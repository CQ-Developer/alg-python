import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2055 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    s: str
    queries: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_plates_between_candles(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.plates_between_candles(case["s"], case["queries"]) == case["expected"]
