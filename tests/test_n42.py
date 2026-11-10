import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n42 import Solution, SolutionA, SolutionB, SolutionC


class TestCase(TypedDict):
    __test__ = False
    height: list[int]
    expected: int


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_trap(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.trap(case["height"]) == case["expected"]
