import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n3067 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    edges: list[list[int]]
    signalSpeed: int
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n3067.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_count_pairs_of_connectable_servers(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.count_pairs_of_connectable_servers(case["edges"], case["signalSpeed"]) == case["expected"]
