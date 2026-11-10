import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2506 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    words: list[str]
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n2506.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_similar_pairs(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.similar_pairs(case["words"]) == case["expected"]
