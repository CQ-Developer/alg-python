import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1310 import Solution, SolutionA


class Case(TypedDict):
    arr: list[int]
    queries: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_xor_queries(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.xor_queries(case["arr"], case["queries"]) == case["expected"]
