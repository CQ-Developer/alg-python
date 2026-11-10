import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.tianchi2022_ev2bru_q3 import Solution, SolutionA


class Case(TypedDict):
    order: list[int]
    limit: int
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "tianchi2022_ev2bru_q3.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_arrange_bookshelf(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.arrange_bookshelf(case["order"], case["limit"]) == case["expected"]
