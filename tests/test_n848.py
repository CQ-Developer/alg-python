import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n848 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    __test__ = False
    s: str
    shifts: list[int]
    expected: str


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_shifting_letters(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.shifting_letters(case["s"], case["shifts"]) == case["expected"]
