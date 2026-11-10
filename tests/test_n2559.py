import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2559 import Solution, SolutionA, SolutionB


class Case(TypedDict):
    words: list[str]
    queries: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_vowel_strings(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    assert solution.vowel_strings(case["words"], case["queries"]) == case["expected"]
