import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1019 import ListNode, Solution, SolutionA


class Case(TypedDict):
    head: list[int]
    expected: list[int]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


def _build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_next_larger_nodes(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    head = _build_list(case["head"])
    assert solution.next_larger_nodes(head) == case["expected"]
