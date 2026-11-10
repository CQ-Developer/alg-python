import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n654 import Solution, SolutionA, SolutionB, TreeNode


class Case(TypedDict):
    nums: list[int]
    expected: list[int | None]


def _load_test_cases() -> list[Case]:
    case_file = Path(__file__).parent / "cases" / "n654.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


def _tree_to_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        index += 1
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()
    return result


@pytest.fixture(params=[SolutionA, SolutionB])
def solution(request: pytest.FixtureRequest) -> Solution:
    return request.param()


@pytest.mark.parametrize("case", _load_test_cases())
def test_construct_maximum_binary_tree(solution: Solution, case: Case):
    case = copy.deepcopy(case)
    result = solution.construct_maximum_binary_tree(case["nums"])
    assert _tree_to_list(result) == case["expected"]
