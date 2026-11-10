import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1442 import Solution, SolutionA, SolutionB, SolutionC


class Case(TypedDict):
    arr: list[int]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n1442.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB, SolutionC])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_count_triplets(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.count_triplets(case["arr"]) == case["expected"]
