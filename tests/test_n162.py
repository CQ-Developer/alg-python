import copy
import json
from pathlib import Path
from typing import NotRequired, TypedDict

import pytest

from src.n162 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    nums: list[int]
    expected: NotRequired[int]
    expected_any: NotRequired[list[int]]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_find_peak_element(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    result = solution.find_peak_element(case["nums"])
    if "expected_any" in case:
        assert result in case["expected_any"]
    else:
        assert result == case["expected"]
