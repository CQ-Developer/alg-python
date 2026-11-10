import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3257 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    board: list[list[int]]
    expected: int


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_maximum_value_sum(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.maximum_value_sum(case["board"]) == case["expected"]
