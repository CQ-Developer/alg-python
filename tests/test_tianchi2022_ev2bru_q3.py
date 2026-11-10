import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.tianchi2022_ev2bru_q3 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    order: list[int]
    limit: int
    expected: list[int]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_arrange_bookshelf(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    assert solution.arrange_bookshelf(case["order"], case["limit"]) == case["expected"]
