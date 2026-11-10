import copy
import json
from pathlib import Path
from typing import TypedDict
from unittest.mock import patch

import pytest

from src.n278 import Solution, SolutionA, SolutionB


class TestCase(TypedDict):
    __test__ = False
    n: int
    bad: int
    expected: int


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_first_bad_version(solution: Solution, case: TestCase):
    case = copy.deepcopy(case)
    with patch("src.n278.is_bad_version", side_effect=lambda version: version >= case["bad"]):
        assert solution.first_bad_version(case["n"]) == case["expected"]
