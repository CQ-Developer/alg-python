import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n2476 import Solution, SolutionA, TreeNode


class Case(TypedDict):
    root: list[int | None]
    queries: list[int]
    expected: list[list[int]]


def _load_test_cases() -> list[Case]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


def _build_tree(values: list[int | None] | None) -> TreeNode | None:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    index = 1
    while index < len(values):
        node = queue.pop(0)
        left = values[index]
        index += 1
        if left is not None:
            node.left = TreeNode(left)
            queue.append(node.left)

        if index < len(values):
            right = values[index]
            index += 1
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)

    return root


@pytest.fixture(params=[SolutionA])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_closest_nodes(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    root = _build_tree(case["root"])
    assert solution.closest_nodes(root, case["queries"]) == case["expected"]
