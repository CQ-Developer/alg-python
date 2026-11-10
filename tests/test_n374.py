import copy
import json
from pathlib import Path
from typing import TypedDict
from unittest.mock import patch

import pytest

from src.n374 import Solution, SolutionA


class TestCase(TypedDict):
    __test__ = False
    n: int
    pick: int
    expected: int


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_guess_number(solution: Solution, case: TestCase):
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
