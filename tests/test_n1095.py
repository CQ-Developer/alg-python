import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1095 import MountainArray, Solution, SolutionA


class FakeMountainArray(MountainArray):
    def __init__(self, arr: list[int]) -> None:
        self._arr = arr

    def get(self, index: int) -> int:
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)


class Case(TypedDict):
    arr: list[int]
    target: int
    expected: int


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_find_in_mountain_array(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    mountain_array = FakeMountainArray(case["arr"])
    assert solution.find_in_mountain_array(case["target"], mountain_array) == case["expected"]
