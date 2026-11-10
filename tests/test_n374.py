import copy
import json
from pathlib import Path
from typing import TypedDict
from unittest.mock import patch

import pytest

from src.n374 import Solution, SolutionA


class Case(TypedDict):
    n: int
    pick: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n374.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_guess_number(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    pick = case["pick"]

    def guess(num: int) -> int:
        if num > pick:
            return -1
        if num < pick:
            return 1
        return 0

    with patch("src.n374.guess", side_effect=guess):
        assert solution.guess_number(case["n"]) == case["expected"]
