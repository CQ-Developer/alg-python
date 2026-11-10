import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n496 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    a: list[int]
    b: list[int]
    expected: list[int]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_next_greater_element(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.next_greater_element(case["a"], case["b"]) == case["expected"]
